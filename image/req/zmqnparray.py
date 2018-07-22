
import zmq
import numpy as np


def send(socket, array, flags=0, copy=True, track=False):
    A = np.ascontiguousarray(array)
    md = dict(
         dtype = str(A.dtype),
         shape = A.shape,
    )
    socket.send_json(md, flags|zmq.SNDMORE)
    return socket.send(A, flags, copy=copy, track=track)

def recv(socket, flags=0, copy=True, track=False):
    md = socket.recv_json(flags=flags)
    msg = socket.recv(flags=flags, copy=copy, track=track)
    A = np.frombuffer(msg, dtype=md['dtype'])
    return A.reshape(md['shape'])

