import socket    
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)     
ip='127.0.0.1'     
port=9999 
s.connect((ip,port))
s.send(b'word')       
d = s.recv(1024)           
print(d)
