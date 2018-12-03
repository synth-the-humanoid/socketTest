import socket

while(1): #infinite loop for taking input, broken when given valid input
    print("Server to connect to: ", end = '')
    servername = input()

    print("Port to connect to: ", end = '')
    
    try: #try to get valid port input
        port = int(input())
    
    except:
        print("Invalid port number.\n")
        continue
    
    try: #try to get DNS of host name
        servername = socket.gethostbyname(servername)
    
    except:
        print("Invalid server name.\n")
        continue
    
    print('\n', end = '')
    print("Server: " + servername + "\nPort: " + str(port))
    print('\n')
    print("Is this correct? [y/n]  ", end = '')
    
    if (input().lower()[0] == 'n'):
        print('\n')
        continue
    
    break

print("Message to send to server: ", end = '')
message = input() #gets message from STDIN, and appends a newline to it. The server program reads data sent to it until a newline is reached, for extensibility.
message += '\n'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creates a socket object using IPv4(AF_INET) and TCP(SOCK_STREAM)
sock.connect((servername, port)) #connect to server(as string) and port(as int) in a tuple

print("Connected to " + servername)

sock.sendall(message.encode()) #sends the message, which has to be encoded into binary using the .encode() method

print("Sent message")

sock.close() #closes socket for cleanup

print("Socket closed")
