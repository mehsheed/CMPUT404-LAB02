#!/usr/bin/env python3
import socket, sys




BUFFER = 4096


#create a tcp socket
def create_tcp_socket():
    print('Creating socket')
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    print('Socket created successfully')
    return s

#get host information
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

    request = b"GET / HTTP/1.1\nHost: " + host.encode('utf-8') + b"\n\n"
    
    s = create_tcp_socket()
    remote_ip = get_ip(host)
    print (f'Socket Connected to {host} on ip {remote_ip}')

    s.connect((host,port))
    s.send(request)
    s.shutdown(socket.SHUT_WR)
    result = s.recv(BUFFER)
    while (len(result) > 0):
        print(result)
        result = s.recv(BUFFER)
        
        
    s.close()
    

def main():
    
        host = "localhost"
        port = 8080
        get(host,port)

        


        

        
        
if __name__ == "__main__":
    main()

