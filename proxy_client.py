import socket, sys




BUFFER = 4096


def create_tcp_socket():
    print('Creating socket')
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    print('Socket created successfully')
    return s

def get_ip(host):
    print(f'Getting IP for {host}')
    try:
        remote_ip = socket.gethostbyname( host )
    except socket.error (e):
        print (e)
        sys.exit()

    print (f'Ip address of {host} is {remote_ip}')
    return remote_ip



def get (host,port):

    request = b"GET / HTTP/1.1\nHost: www.google.com\n\n" + host.encode('utf-8') + b"\n\n"

    s = create_tcp_socket()

    s.connect((host,port))

    ip_addr = get_ip(host)
    print (f'Socket Connected to {host} on ip {ip_addr}')

    s.send(request)

    s.shutdown(socket.SHUT_WR)

    result = b'' 

    while True:
        chunk = s.recv(BUFFER)
        if not chunk:
            break
        result += chunk
    

    s.close()
    
    return result


def main():
    
        host = "127.0.0.1"
        port = 8080
        print(get(host,port))

        


        

        
        
if __name__ == "__main__":
    main()







