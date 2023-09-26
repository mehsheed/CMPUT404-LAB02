import socket
from threading import Thread


BUFFER = 4096
PROXY_SERVER_HOST = "127.0.0.1"
PROXY_SERVER_HOST_PORT = 8080



def send_request (host,port,request):
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        #connect to host:port
        client_socket.connect((host,port))

        client_socket.send(request)

        client_socket.shutdown(socket.SHUT_WR)


        data = client_socket.recv(BUFFER)
        
        result = b'' + data

        while (len(data) > 0):
            data = client_socket.recv(BUFFER)
            result += data
        return result
    

def handle_connection(conn, addr):
    with conn:
        print(f"Connected by {addr}")

        request = b''

        while True:
            data = conn.recv(BUFFER)
            if not data:
                break
            request += data
        print ("Client sent : ",request.decode('utf-8'))
        response = send_request("www.google.com",80,request)
        conn.sendall(response)


def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((PROXY_SERVER_HOST, PROXY_SERVER_HOST_PORT))

        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.listen(2)
        conn,addr = server_socket.accept()
        handle_connection(conn,addr)


def start_threaded_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((PROXY_SERVER_HOST, PROXY_SERVER_HOST_PORT))

        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.listen(2)
        print(f"[LISTENING] Server is listening on {PROXY_SERVER_HOST}:{PROXY_SERVER_HOST_PORT}")

        while True:
            conn, addr = server_socket.accept()
            thread = Thread(target=handle_connection, args=(conn, addr))
            
            thread.run()





def main():
    
        
       #start_server()
    start_threaded_server()

if __name__ == "__main__":
    main()