#!/usr/bin/env python3
import socket
import time
from threading import Thread

#define address & buffer size

HOST = "127.0.0.1"

PORT = 8060
BUFFER_SIZE = 4096


def handle_connection(conn, addr):
    with conn:
       print(f"[NEW CONNECTION] {addr} connected.")
       while True:
           data = conn.recv(BUFFER_SIZE)
           if not data:
               break
           print(data)
           conn.sendall(data)

def start_server():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
        
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        #bind socket to address
        s.bind((HOST, PORT))
        #set to listening mode
        s.listen()
        print(f"[LISTENING] Server is listening on {HOST}")

        conn, addr = s.accept()
        handle_connection(conn, addr)

def start_threaded_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
        s.bind((HOST, PORT))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        #bind socket to address
        
        
        #set to listening mode
        s.listen(2)
        print(f"[LISTENING] Server is listening on {HOST}")

        while True:
            conn, addr = s.accept()
            thread = Thread(target=handle_connection, args=(conn, addr))
            
            thread.run()
            

    



def main():
    
        
       #start_server()
    start_threaded_server()

if __name__ == "__main__":
    main()
