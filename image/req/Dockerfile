FROM dmaugis/zmq

COPY req.py /tmp/
COPY install-req.sh /tmp/
COPY zmqnparray.py /tmp/
RUN  /tmp/install-req.sh  
RUN  rm /tmp/install-req.sh
CMD  python /tmp/req.py



