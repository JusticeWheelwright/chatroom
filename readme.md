# Overview

This program was written in order to expirement with networking functions and specifically the socket class. It utilizes a chat system for two computers to communicate and also a system by which the most recent conversation can be recalled for the two computers. By doing so, I hope to gain a greater knowledge of this topic and expand my programming repetoire.

[Software Demo Video](http://youtube.link.goes.here)

# Network Communication

This program utilizes a client to server relationship to create a chatroom where two computers can communicate and exchange messages with eachother. this program uses tcp and utilizes port 8080. Messages sent between these two objects include session information and the actual messages which can be in whatever format the user desires. The program operates using a seperate server and client file which communicate with eachother on seperate environments to operate the program.

# Development Environment

This program was developed using Visual studio code and python. The only required import for this program is the socket library.

# Useful Websites

* [socket documentation](https://docs.python.org/3.6/library/socket.html)
* [socket send guide](https://pythontic.com/modules/socket/send)
* [python string decoding](https://www.geeksforgeeks.org/python-strings-decode-method/)
* [python socket programming tutorial](https://www.geeksforgeeks.org/python-strings-decode-method/)
* [socket server client example](https://www.digitalocean.com/community/tutorials/python-socket-programming-server-client)

# Future Work

* fix the interaction with recalling previous conversations so that the client side can move onto the the conversation portion of the program
* implement more complex functions and program flow to enable more versatile tasks