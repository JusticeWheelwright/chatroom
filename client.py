import time, socket, sys

#sets up client
socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_host = socket.gethostname()
ip = socket.gethostbyname(server_host)
sport = 8080

#asks user for the server to connect to
print('your IP address: ',ip)
server_host = input('Enter friend\'s IP address:')
name = input('Enter your name: ')

#connects to specified server
socket_server.connect((server_host, sport))

#sends and recieves server name information
socket_server.send(name.encode())
server_name = socket_server.recv(1024)
server_name = server_name.decode()

#asks the user if they want to continue the last conversation and returns the response to the server
print(server_name,' has joined...')
cont = input("continue last conversation? (y/n)")
socket_server.send(cont.encode())

#recieves content of last conversation from the server and prints until the file holding the conversation is empty
log = "y"
while log != "":
    message = (socket_server.recv(1024)).decode()
    if message == "":
        log = ""
    else:
        print(message)

# recieves and prints messages to the server
while True:
    message = (socket_server.recv(1024)).decode()
    print(server_name, ":", message)
    message = input("Me : ")
    socket_server.send(message.encode())  