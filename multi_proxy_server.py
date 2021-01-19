import socket, time, sys
from multiprocessing import Process

HOST = "localhost"
PORT = 8001
BUFFER_SIZE = 1024

def get_remote_ip(host):
    print(f'Getting IP for {host}')
    try:
        remote_ip = socket.gethostbyname(host)
    except socket.gaierror:
        print('Hostname could not be resolved. Exiting')
        sys.exit()

    print(f'Ip address of {host} is {remote_ip}')
    return remote_ip

def communicate(addr, conn):
    print(f"connection from {addr}")
    host = 'www.google.com'
    port = 80
    buffer_size = 4096
    #google
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_end:
        print("Connecting to Google")
        remote_ip = get_remote_ip(host)

        proxy_end.connect((remote_ip, port))

        send_full_data = conn.recv(BUFFER_SIZE)
        print(f"Sending received data {send_full_data} to google")
        proxy_end.sendall(send_full_data)

        proxy_end.shutdown(socket.SHUT_WR)

        #continue accepting data until no more left
        full_data = b""
        
        while True:
            data = proxy_end.recv(buffer_size)
            # print("recv: " + str(data))
            if not data:
                break
            full_data += data
        # print(full_data)
        conn.sendall(full_data)

        conn.close()
        proxy_end.close()

def main():
    

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_start:
        print("Starting proxy server")
        proxy_start.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        proxy_start.bind((HOST, PORT))
        proxy_start.listen(2)       

        while True:
            # client
            conn, addr = proxy_start.accept()
            print("Connected by", addr)

            p = Process(target=communicate, args=(addr, conn))
            p.daemon = True
            p.start()
            print("started process ", p)

            


if __name__ == "__main__":
    main()