from socket import *   #引入socket模块
import threading       #引入多线程模块
import argparse        #引入选项参数模块
lock = threading.Lock()   #创建lock对象信号
openNum = 0             #创建变量值为0
threads = []            #创建变量值为空列表

def portScanner(host,port):   #函数作为连接
    global openNum           #全局变量
    try:                   #异常处理
        s = socket(AF_INET,SOCK_STREAM)   #s套接字对象，括号里inet代表ipv4，tcp流
        s.connect((host,port))      #连接地址和端口，括号里的是元组
        lock.acquire()              #抓取信号
        openNum+=1                  #变量加一
        print('[+] %d open' % port)    #输出端口开放
        lock.release()              #释放信号
        s.close()             #套接字关闭
    except:                      #异常处理
        pass                   #通过

def main():        #作为入口
    p = argparse.ArgumentParser(description='Port scanner!.')   
    #创建选项参数对象p，括号里的是描述
    p.add_argument('-H', dest='hosts', type=str)
    #添加选项-H，变量dest,数据类型是字符串
    args = p.parse_args()  #读取命令行赋值
    hostList = args.hosts.split(',')    #切割空格为逗号
    setdefaulttimeout(1)         #默认值为1
    for host in hostList:    #遍历列表
        print('Scanning the host:%s......' % (host)) 
        for p in range(1,65535):  #生成1~65535个端口
            t = threading.Thread(target=portScanner,args=(host,p))
            #创建多线程对象t，括号里第一个是函数，第二个是参数
            threads.append(t)   #添加进列表中
            t.start()        #线程开始

        for t in threads:    
            t.join()     #循环加入

        print('[*] The host:%s scan is complete!' % (host))   
        print('[*] A total of %d open port ' % (openNum))

if __name__ == '__main__':    #代表脚本本身运行
    main()               #运行当前脚本