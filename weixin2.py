#coding:UTF-8
import itchat, time
def lc():
    print("登入成功")
def ec():
    print("退出")

itchat.auto_login(loginCallback=lc, exitCallback=ec,enableCmdQR=2)
#enableCmdQR=2设置二维码长度、hotReload=True保存会话
#itchat.send('Hello',toUserName='filehelper')给自己文件助手发送消息
#mps = itchat.get_mps()
#mps = itchat.search_mps(name = '')
#print(mps)
#itchat.send('3',toUserName='@36571ffde0ae35965b1da49706c8595d')
#gonzhonghao = itchat.search_friends(userName='@36571ffde0ae35965b1da49706c8595d')
#print(gonzhonghao)
#users = itchat.search_friends(name='昌盛')#好友
#print(users)
#获取`UserName`,用于发送消息
#userName = users[0]['UserName']
mps = itchat.get_mps()
mps = itchat.search_mps(name='T00ls')
#print(mps)
userName = mps[0]['UserName']
for i in range(30):
    itchat.send('3',toUserName = userName)
    time.sleep(86400)
#time.sleep(86400)休眠24小时
#itchat.logout()  