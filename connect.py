import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def reciever():
    
    s.bind((userIp,userPort))
    while True:
        x = s.recvfrom(1024)
        senderIp = x[1][0]
        senderMessage = x[0].decode()
        print("\t"+senderIp+"  :  "+senderMessage)
        #print(x)
        
def sender():
    if(len(senderIp)==0):
        senderIP = input("Enter the IP address of the reciever\t -->  ")
    
    message = input("\t message ->\t")
    s.sendto(message.encode(),(senderIp,1234))
        
def findIp():   
    hostname = socket.gethostname()    
    hostIp = socket.gethostbyname(hostname)    
    #print("Your Computer Name is:" + hostname)    
    return(hostIp)


def startChat():
    userIp = findIp()
    userPort = 1234
    print("Your Computer IP is:\t" + userIp)
    
    send = threading.Thread(target = sender)
    recieve = threading.Thread(target = reciever)
    send.start()
    recieve.start()
    #sender()
    
startChat()
