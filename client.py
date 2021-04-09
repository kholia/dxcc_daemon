#!/usr/bin/env python3

import sys
import json
import socket

HOST = '127.0.0.1'
PORT = 7373

if len(sys.argv) > 1:
    callsign = sys.argv[1]
else:
    callsign = "VU3CER"

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(callsign.encode("ascii"))
        data = s.recv(1024)
        data = json.loads(data)
        print('Received:', data)
