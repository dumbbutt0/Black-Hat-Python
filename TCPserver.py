import socket
import threading 

ip ='0.0.0.0'
port =1234

def main():
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #start a TCP client
    server.bind((ip,port))  #starts listening on the TCP port
    server.listen(5)  #sets the max connections to 5
    print(f"[*] Listening on {ip}:{port}") 

    while True:
        client,address = server.accept()  #accepts connections on our server
        print(f"[*] Accepted a connection from {address[0]}:{address[1]}")
        client_handler = threading.Thread(target=handle_client, args=(client,))   #creates a new thread for each connection
        client_handler.start()

def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)        #recieves data from the client
        print(f"[*] recieved: {request.decode('utf-8')}")       #decodes data and prints recieved data
        sock.send(b'DUMMY WAS HERE')


if __name__ =="__main__":
    main()