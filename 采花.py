# coding=utf-8
import sys
import requests
from bs4 import BeautifulSoup
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0'}
base_url = 'http://www.kanmeizi.cn'
# 保存图片
index = 1
def svae_img(url):
    global index
    html = url_text(url)
    doms = html.select('li img[class="height_min"]')
    for dom in doms:
        img_url = dom.get('src')
        img = requests.get(img_url, headers=headers, stream=True)
        if img.status_code == 200:
            ext = img_url.split('.')[-1]
            open('{}.{}'.format(index, ext), 'wb').write(img.content)
        print('正在采摘第%d朵花' % index)
        index += 1
# 获取html
def url_text(url):
    return BeautifulSoup(requests.get(url, headers=headers).text, "html.parser")
# 执行程序 判断是否需要帮助
page_count = 10
url = 'http://www.kanmeizi.cn/tag_8.html'
if len(sys.argv) > 1:
    if sys.argv[1] == 'help':
        print("格式:python run.py [url page_count]")
        print("例如: python run.py [url]http://www.kanmeizi.cn[/url] 2")
        sys.exit()
    elif sys.argv[1].startswith('http://'):
        url = sys.argv[1]
        if len(sys.argv) > 2:
            page_count = int(sys.argv[2])
        print('目标采集%s,目标篮数:%s' % (url, page_count))
    else:
        print('您输入的参数有误')
else:
    print('您使用了默认配置 采集美腿花10篮...')
for i in range(0, page_count):
    svae_img(url)
    data = BeautifulSoup(requests.get(url, headers=headers).text, "html.parser")
    a_dom = data.find('center').find('li', class_='active').find_next_sibling('li').find('a')
    if a_dom == None:
        break
    url = base_url + a_dom.get('href')
print('采摘完毕，共采摘到%d朵花' % (index-1))