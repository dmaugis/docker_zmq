FROM dmaugis/zmq

COPY rep.py /tmp/
COPY install-rep.sh /tmp/
RUN  /tmp/install-rep.sh  
RUN  rm /tmp/install-rep.sh
CMD  python /tmp/rep.py



