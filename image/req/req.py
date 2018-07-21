#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
#

import zmq
import cv2
import numpy as np
import zmqnparray as zmqa

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

#  Do 10 requests, waiting each time for a response
for request in range(10):
    A=cv2.imread('concombre.png',1)
    print("Sending request %s … " % (request) )
    cv2.imshow('request',A)
    zmqa.send(socket,A)

    #  Get the reply.
    B= zmqa.recv(socket)
    print("Received reply %s " % (request))
    cv2.imshow('reply',B)
    cv2.waitKey(0)

cv2.destroyAllWindows()
