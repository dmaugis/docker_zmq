#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#

import time
import zmq
import cv2
import numpy as np
import zmqnparray as zmqa

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    #  Wait for next request from client
    A,extra = zmqa.recv(socket)
    if 'fname' in extra:
        print("Received request %s" % str(extra['fname']))
    else:
        print("Received request %s" % str(extra))

    #  Do some 'work'
    #time.sleep(1)
    B = cv2.Canny(A,100,200)
    nonzero = cv2.countNonZero(B)
    #  Send reply back to client
    zmqa.send(socket,B,extra=nonzero)

