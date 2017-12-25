from base64 import b64decode

flag = #‘from exe end’太多了就不贴了
#print flag
flag =flag.replace("_","1")
flag = flag.replace("*","W")
flag = list(flag)
flag.reverse()
flag = "".join(flag)
for i in range(0,25):
       flag=b64decode(flag)

print flag
