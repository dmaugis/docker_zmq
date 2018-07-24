#include <string>
#include <iostream>
#include <unistd.h>
#include <zmq_addon.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui.hpp>
//using namespace cv;
#include <nlohmann/json.hpp>
using json = nlohmann::json;


int main () {
 
    zmq::context_t context (1);
    zmq::socket_t socket (context, ZMQ_REP);
    socket.bind ("tcp://*:5555");

    cv::Mat  img_req;
    cv::Mat  img_rep;
    std::string extra;
    while (true) {

        {
        bool ok=false;
        zmq::multipart_t req;

        ok = req.recv(socket);
        std::cout << "Received " <<  req.size() << " parts" << std::endl;
        std::string  reqhead=req.popstr();
        std::cout << "head '" <<  reqhead << "'" << std::endl;
        auto j = json::parse(reqhead);
	//std::cout << "extra: "<< j["extra"] << std::endl;
        extra=j["extra"].dump();

        std::cout << "type:  "<< j["dtype"] << std::endl;
	std::cout << "shape: "<< j["shape"] << std::endl;

	std::vector<int> shape=j["shape"];
	std::cout << "shape[0]: "<< shape[0] << std::endl;
	std::cout << "shape[1]: "<< shape[1] << std::endl;
	std::cout << "shape[2]: "<< shape[2] << std::endl;
        int _rows=shape[0];
        int _cols=shape[1];
        int _type=shape[2];

        zmq::message_t msg=req.pop();
        
        img_req=cv::Mat(_rows,_cols, CV_8UC3,msg.data<char>());
 
        std::cout << "Done Receiving" << std::endl; 

        cv::Canny(img_req, img_rep, 100, 200, 3);
        }
	//cv::imshow("Requested",img_req);
        //cv::waitKey(0);
        {
        bool ok=false;
        zmq::multipart_t rep;

        json j;
        j["dtype"]="uint8";

	std::vector<int> shape;
	shape.push_back(img_rep.rows);
        shape.push_back(img_rep.cols);
        shape.push_back(1);
        j["shape"]=shape;
        
        j["extra"]=extra;
        rep.addstr(j.dump());
        
        rep.addmem(img_rep.data,img_rep.total() * img_rep.elemSize());
        ok = rep.send(socket);
        }
    }
    return 0;
}

