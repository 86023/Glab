import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip='www.sina.com.cn'
port=80
s.connect((ip,port))
s.send(b'GET / HTTP/1.1\R\nHost: \
www.sina.com.cn\r\nConnection: close\r\n\r\n')
buffer = []
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
print(data)
