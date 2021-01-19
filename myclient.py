import socket, sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    

s.connect(("www.google.com" , 80))
s.sendall(b"GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n")
print(s.recv(4096))
s.close

def create_tcp_socket():
    print('Creating scoket')
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
    except(socket.error, msg):
        

    payload = f'GET / HTTP/1.0\r\nHost: {host}\r\n\r\n'

if __name__ = 