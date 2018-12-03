import socket

while(1): #infinite loop until valid input
    print("Port: ", end = '')

    try: #try to get valid port data
        port = int(input())
    
    except:
        print("Invalid port.\n")
        continue
    
    servername = "localhost" #default name as localhost, only runs on private address range
    
    print("Port: " + str(port) + '\n', end = '')
    print("Is this correct? [y/n]  ")
    
    if(input().lower()[0]=='n'):
        continue
    break

addr = (servername, port) # sets address as a tuple, servername as string, port as int
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create socket using IPv4 and TCP
sock.bind(addr) #bind a socket to localhost
sock.listen(1) #listen for 1 connection

while(1): #infinite loop to listen for connections
    print("Trying to connect")
    conSock, cliAddr = sock.accept() #accept connection, return socket object to conSock, and client's IP address to cliAddr
    message = "" #string
    current = "" #char buffer 
    
    while(current!='\n'): #while current character isn't newline, used to be able to accept any size input 
        message += current # add buffer to string
        current = conSock.recv(1).decode() #receive one character from the client, and decode it into the native character set
    
    print(message)
    
    conSock.close() #close socket when done translating message, and then start over again
