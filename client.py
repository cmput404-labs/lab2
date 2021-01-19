import socket, sys



def create_tcp_socket():
    print("create socket")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except(socket.error, msg):
        print("error occured, exit")
        sys.exit()
    print("succeess create socket!")
    return s


def get_remote_ip(host):
    try:
        remote_ip = socket.gethostbyname( host )
    except socket.gaierror:
        print("host name cannot be resolved")
        sys.exit()
    return remote_ip


def send_data(serversocket, payload):
    print("sending payload")
    try:
        serversocket.sendall(payload.encode())
    except socket.error:
        print("send failed")
        sys.exit()
    print("Payload sent successfully")


def main():
    try:
        host = ""
        port = 8001
        payload = "GET / HTTP/1.1\r\nHost: "+host+"\r\n\r\n"
        buffer_size = 4096

        s = create_tcp_socket()

        remote_ip = get_remote_ip(host)
        s.connect((remote_ip,port))
        send_data(s,payload)
        s.shutdown(socket.SHUT_WR)
        full_data = b""
        while True:
            data = s.recv(buffer_size)
            if not data:
                break
            full_data += data
        print(full_data)
    except Exception as e:
        print(e)
    finally:
        s.close()


if __name__ == "__main__":
    main()