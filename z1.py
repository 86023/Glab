# -*- coding: utf-8 -*-
#-*- by:Lee -*-
#-*- date:2017-02-16 -*-
import requests
import json
import time
import re

print("input-username:")					#�����˺�
user =input()
print("input-password:")					#��������
passwd =input()
print("input-your want search:")			#��������				
search=input()
print("input-your result filename:")		#���������ļ�
result=input()
print("input-your search pages")			#������ҳ������
page=input()
data = {'username': user,'password': passwd}
data_encoded = json.dumps(data)				#json����
url='https://api.zoomeye.org/user/login'	
a=requests.post(url,data_encoded)
JWT=a.text
token="JWT"+" "+JWT[18:-2]					#��ȡtoken����д
print(token)
txt=open(result,"a+")
r='\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
reg=re.compile(r)

header={"Authorization":token}
for i in range(1,int(page)):
	url='https://api.zoomeye.org/host/search?query='+search+'&page='+str(i)		
	X=requests.get(url,headers=header)
	html=X.text
	a=re.findall(reg,html)
	for i in a:
		txt.write(i+'\n')
		print (i)
	time.sleep(2)

	