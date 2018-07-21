#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#

import time
import zmq
import numpy as np
import zmqnparray as zmqa

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    #  Wait for next request from client
    A = zmqa.recv(socket)
    print("Received request: %s" % str(A) )

    #  Do some 'work'
    time.sleep(1)
    B = A[:] + 1
    #  Send reply back to client
    zmqa.send(socket,B)

