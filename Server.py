import socket
#import numpy as np
#import cv2
import time
import threading

#_______________________________________________________________________________________________

c1_send_s = socket.socket()
c1_send_s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

c2_send_s = socket.socket()
c2_send_s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

c1_recv_s = socket.socket()
c1_recv_s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

c2_recv_s = socket.socket()
c2_recv_s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#_______________________________________________________________________________________________

c1_send_port=2024 #send to client 1
c1_recv_port=2025 #recieve from client1
c2_send_port=2026 #send to clent2
c2_recv_port=2027 #recieve from client2

#_____________________________________________________________
ip=""

c1_send_s.bind(("",c1_send_port))
c1_recv_s.bind(("",c1_recv_port))
c2_send_s.bind(("",c2_send_port))
c2_recv_s.bind(("",c2_recv_port))

#______________________________________________________________
c1_send_s.listen()
c1_recv_s.listen()
c2_recv_s.listen()
c2_send_s.listen()

#______________________________________________________________

c1_recv_session , c1_recv_addr = c1_recv_s.accept()
c2_recv_session , c2_recv_addr = c2_recv_s.accept()
c1_send_session , c1_send_addr = c1_send_s.accept()
c2_send_session , c2_send_addr = c2_send_s.accept()

#_________________________________________________________________

print(c1_recv_addr)
print(c2_recv_addr)
print(c1_send_addr)
print(c1_send_addr)


#_________________________________________________________________

def c1_recieve():
    while True:
        c1_message = c1_recv_session.recv.recv(10000000000)
        time.sleep(0.1)
        c2_send_session.send(c1_message)
        
def c2_recieve():
    while True:
        c2_message = c2_recv_session.recv.recv(10000000000)
        time.sleep(0.1)
        c1_send_session.send(c2_message)
        
#___________________________________________________________________

c1_recv_thread = threading.Thread(target=c1_recieve)
c2_recv_thread = threading.Thread(target=c2_recieve)

c1_recv_thread.start()
c2_recv_thread.start()

#___________________________________________________________________

