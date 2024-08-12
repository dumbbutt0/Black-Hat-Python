import socket

target_host = input("Enter Your Target IP 🗡: ")
host = target_host.encode()
port = 9997

#create a UDP sock object 
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Send specified data to a server 
client.sendto(b"dummywashere",(host,port))

#recieve some data
data, addr = client.recvfrom(4096)

#decode bytes to strings and close socket
print(data.decode())
client.close()