import time, socket, sys

# create server 
new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)
 
port = 8080
 
# bind socket and then create user name for conversations
new_socket.bind((host_name, port))
print("your IP: ", s_ip)
 
name = input('Enter name: ')
 
# listen for client
new_socket.listen(1) 
 
# accept client
conn, add = new_socket.accept()
 
print("Received connection from ", add[0])
print('Connection Established. Connected From: ',add[0])
 
# get client name
client = (conn.recv(1024)).decode()
print(client + ' connected.')

# file system - gets message from the client on whether they want to continue previous conversation or not
message = conn.recv(1024)
message = message.decode()
conn.send(name.encode())
f = open("log.txt")
# if client wants to continue conversation
if message == "y":
    # reads all the contents of the file and prints them out locally and encodes them to the client until it reaches the end of the file
    for line in f:
        message = f.readline()
        if message == '':
            conn.send(False)
        else:
            print(message)
            conn.send(message.encode())
    f = open("log.txt", "a")
# if user does not want to continue previous conversation, overwrite the file
else:
    f = open("log.txt", "w")
 

# main loop - takes input, sends it to client and also prints out messages from the client. 
# This function also prints out all messages, to file so it can be continued later
while True:
    message = input(host_name, ':')
    f.write(host_name, ':', message)
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    f.write(client, ':', message)
    print(client, ':', message)