#!/usr/bin/python
# coding=utf-8
import string
from Crypto.PublicKey import RSA

# 读取公钥参数
with open('pubkey.pem', 'r') as f:
    key = RSA.importKey(f)
    N = key.n
    e = key.e

p = 275127860351348928173285174381581152299
q = 319576316814478949870590164193048041239
with open('flag.enc', 'r') as f:
    cipher = f.read().encode('hex')
    cipher = string.atoi(cipher, base=16)
    # print cipher

# 计算yp和yq
yp = gmpy.invert(p,q)
yq = gmpy.invert(q,p)

# 计算mp和mq
mp = pow(cipher, (p + 1) / 4, p)
mq = pow(cipher, (q + 1) / 4, q)

# 计算a,b,c,d
a = (yp * p * mq + yq * q * mp) % N
b = N - int(a)
c = (yp * p * mq - yq * q * mp) % N
d = N - int(c)

for i in (a,b,c,d):
    s = '%x' % i
    if len(s) % 2 != 0:
        s = '0' + s
    print(s.decode('hex'))
