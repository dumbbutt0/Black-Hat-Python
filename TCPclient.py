import socket

target_host = input("Ping test for who?: ")       #specify the website 
host = target_host.encode(encoding="utf-8")
target_port = 80                   #specify the port

#create a TCP socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect to client 
client.connect((target_host, target_port))

#send a request
client.send(b"GET / HTTP/1.1\r\nHost: "+host+b"\r\n\r\n")

#recieve data from server
response = client.recv(4096)

print(response.decode())
client.close
