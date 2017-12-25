from socket import *  #引入了套接字模块
def portScanner(host,port):  #函数参数地址和端口
    try:                     #异常处理
        s = socket(AF_INET,SOCK_STREAM)
#创建对象s,属性ipv4地址  tcp流的方式
        s.connect((host,port)) #连接地址和端口
        print('[+] %d open' % port)  #输出端口开放
        s.close()   #套接字关闭
    except:            #跟try对应
        print('[_] %d closed'% port) #输出端口关闭
def main():
    setdefaulttimeout(1) #时间改成1秒
    for p in range(80,1024):   #for循环
        portScanner('192.168.2.1',p)  #运用上面定义好的函数
if __name__ == '__main__':
    main()



from socket import *    #引入套接字
import threading        #多线程模块
lock = threading.Lock() #创建了一个多线程信号
openNum = 0             #变量值0
threads = []            #变量值[]
def portScanner(host,port):   #函数名，带上地址和端口参数
    global openNum            #global全局变量
    try:                      #异常处理
        s = socket(AF_INET,SOCK_STREAM)   #创建名为s对象，ipv4,tcp流
        s.connect((host,port))   #连接地址和端口
        lock.acquire()           #信号抓取
        openNum+=1               #变量加一
        print('[+] %d open' % port)  #输出端口开放
        lock.release()           #释放信号
        s.close()                #关闭s
    except :                      #以上try产生异常就pass
        pass
def main():
    setdefaulttimeout(1)    #默认值1
    for p in range(1,65535):    #生成1~1023
        t = threading.Thread(target=portScanner,args=('192.168.2.216',p))
        #创建多线程对象
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print('[*] The scan is complete!')
    print('[*] A total of %d open port ' % (openNum))
if __name__ == '__main__':
    main()
