from socket import *
def portScanner(host,port):
    try:
        a = socket(AF_INET,SOCK_STREAM)
        a.connect((host,port))
        print ('[+] %d open' % port)
        a.close()
    except:
        print('[-] %d close' % port)
def main():
    setdefaulttimeout(1)
    for p in range (80,1024):
        portScanner('192.168.1.1',p)
if __name__ == '__main__':
    main()
