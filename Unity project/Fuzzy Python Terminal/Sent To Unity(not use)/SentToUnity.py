
import socket 
import FuzzyControl as fc

#s = socket.socket()  
#host = "localhost" 
#port = 1234  
#s.bind((host, port))  
#
#s.listen(1)  


#while True:
#    c, addr = s.accept()  
#    print('host ', addr)
#    data = fc.Fuzzy()
#    #c.send(bytes(str(data[0]) + str(data[1])))
#    c.send(bytearray(str(data[0]), 'utf8'))
#    print(data)



  
    
#while True:
#
#    c, addr = s.accept()
#    print('host ', addr)
#    data = fc.Fuzzy()
#    print(data)
#        #c.send(bytes(str(data[0]) + str(data[1])))
#    c.send(bytearray(str(data[0]), 'utf8'))
#    print(data)
#    c.close()


# Create a TCP/IP socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



# Bind the socket to the port

server_address = ('localhost', 1234)

print('Starting up on {} port {}'.format(*server_address))

sock.bind(server_address)



# Listen for incoming connections

sock.listen(1)



while True:

    # Wait for a connection

    print('waiting for a connection')

    connection, client_address = sock.accept()

    try:

        print('connection from', client_address)



        # Receive the data in small chunks and retransmit it

        while True:

            data = fc.Fuzzy()
#    #c.send(bytes(str(data[0]) + str(data[1])))
#    c.send(bytearray(str(data[0]), 'utf8'))

            print('received {!r}'.format(data))

            if data:

                print('sending data back to the client')

                connection.sendall(bytearray(str(data), 'utf8'))

            else:

                print('no data from', client_address)

                break



    finally:

        # Clean up the connection

        print("Closing current connection")

        connection.close()
 


#import socket
#TCP_IP = '127.0.0.1'
#TCP_PORT = 5005
#BUFFER_SIZE = 1024 
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.bind((TCP_IP, TCP_PORT))
#s.listen(1)
#conn, addr = s.accept()
#print('Connection address:', addr)
#while 1:
#    data = conn.recv(BUFFER_SIZE)
#    if not data: break
#    print( "received data:", data)
#    conn.send(data)  
#conn.close()