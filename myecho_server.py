import socket

# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# sock.bind(('localhost', 8001))
sock = socket.create_server(('localhost', 8001), family=socket.AF_INET)

sock.listen(1)

while True:
    print("wait for income...")
    connection, client_address = sock.accept()
    # print(str(type(client_address[0])) + str(type(client_address[1])))
    print("client address: " + client_address[0])
    print("port: " + str(client_address[1]))
    data = connection.recv(1024)
    if data:
        connection.sendall(data)
        print("content: " + data.decode("utf-8"))
        

connection.close()