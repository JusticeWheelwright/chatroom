import time, socket, sys
 
new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)
 
port = 8080
 
new_socket.bind((host_name, port))
print("Binding successful!")
print("This is your IP: ", s_ip)
 
name = input('Enter name: ')
 
new_socket.listen(1) 
 
 
conn, add = new_socket.accept()
 
print("Received connection from ", add[0])
print('Connection Established. Connected From: ',add[0])
 
client = (conn.recv(1024)).decode()
print(client + ' has connected.')

message = conn.recv(1024)
message = message.decode()
f = open("log.txt")
if message == "y":
    for line in f:
        message = f.readline()
        if message == '':
            conn.send(False)
        else:
            print(message)
            conn.send(message.encode())
    f = open("log.txt", "a")
else:
    f = open("log.txt", "w")
 


conn.send(name.encode())
while True:
    message = input(host_name, ':')
    f.write(message)
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    f.write(message)
    print(client, ':', message)