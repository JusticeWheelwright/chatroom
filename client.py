import socket

#sets up client
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_host = socket.gethostname()
ip = socket.gethostbyname(server_host)
sport = 8080

#asks user for the server to connect to
print('your IP address: ',ip)
server_host = input('Enter host\'s IP address:')
name = input('Enter your name: ')

#connects to specified server
sock.connect((server_host, sport))

#sends and recieves server name information
sock.send(name.encode())
server_name = sock.recv(1024)
server_name = server_name.decode()

#asks the user if they want to continue the last conversation and returns the response to the server
print(server_name,' has joined...')
cont = input("continue last conversation? (y/n)")
sock.send(cont.encode())

#recieves content of last conversation from the server and prints until the file holding the conversation is empty
while cont == "y":
    message = (sock.recv(1024)).decode()
    if message == False:
        cont = "n"
        break
    else:
        print(message)

# recieves and prints messages to the server
while True:
    message = (sock.recv(1024)).decode()
    print(server_name+":"+ message)
    msg = input("Me : ")
    sock.send(msg.encode())  