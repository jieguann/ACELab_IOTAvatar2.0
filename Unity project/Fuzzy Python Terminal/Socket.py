# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 16:26:16 2019

@author: acelabuser
"""

import FuzzyControl as fc
import socket
import sys
emotionN = None
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print(server_address)
sock.bind(server_address)
sock.listen(1)

while True:
    # Wait for a connection
    
    connection, client_address = sock.accept()
    
    try:
        
        # Receive the data in small chunks and retransmit it
        while True:
            print("connect")
            
            emotion,brightness,soilmoisture,count,valence,arousal,valenceN,arousalN = fc.Fuzzy()
           
                
            connection.sendall({"emotion":emotion,})
           
            
    finally:
        # Clean up the connection
        connection.close()