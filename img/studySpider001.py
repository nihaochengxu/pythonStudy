import os
import threading

import requests
import re
from Crypto.Cipher import AES

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}
# url = "https://kanmeitu1.cc/p/59348.html"
# res = requests.get(url,headers=headers)
# html = res.text
# urls = re.findall(r'src="https.+?.jpg"',html)
# print(urls)
# urls = ['src="https://kanmeitu.ojbkcdn.com/t32/2022112004/2022112004p3vz2vzlgdp.jpg"', 'src="https://kanmeitu.ojbkcdn.com/t32/2022112004/2022112004gmkss2k55tq.jpg"', 'src="https://kanmeitu.ojbkcdn.com/t32/2022112004/2022112004wu0efqd4oft.jpg"', 'src="https://kanmeitu.ojbkcdn.com/t32/2022112004/2022112004vmdlmlx42sc.jpg"', 'src="https://kanmeitu.ojbkcdn.com/t32/2022112004/20221120041wcuij0f2cc.jpg"', 'src="https://kanmeitu.ojbkcdn.com/t32/2022112004/2022112004xv1wu5yotck.jpg"', 'src="https://kanmeitu.ojbkcdn.com/t32/2022112004/20221120042c5m40xx5lc.jpg"', 'src="https://kanmeitu.ojbkcdn.com/t32/2022112004/20221120040ebtfs25uu2.jpg"', 'src="https://kanmeitu.ojbkcdn.com/t32/2022112004/2022112004rm5ii5k1kau.jpg"', 'src="https://kanmeitu.ojbkcdn.com/t32/2022112004/2022112004ffbatkumiyg.jpg"', 'src="https://kanmeitu.ojbkcdn.com/t32/2022112004/2022112004nb21jbfeinn.jpg"', 'src="https://kanmeitu.ojbkcdn.com/t32/2022112004/2022112004vazuipmv33l.jpg"', 'src="https://kanmeitu.ojbkcdn.com/t32/2022112004/2022112004d2isi1b0hlb.jpg"', 'src="https://kanmeitu.ojbkcdn.com/t32/2022112004/2022112004sa325bwgyrt.jpg"', 'src="https://kanmeitu.ojbkcdn.com/t32/2022112004/2022112004vlygenblp4d.jpg"', 'src="https://kanmeitu.ojbkcdn.com/t32/2022112004/2022112004nw33grb0ixa.jpg"', 'src="https://kanmeitu.ojbkcdn.com/t32/2022112004/2022112004hcisxiqdq5y.jpg"', 'src="https://kanmeitu.ojbkcdn.com/t32/2022112004/2022112004dggy254lsa5.jpg"', 'src="https://kanmeitu.ojbkcdn.com/t32/2022112004/2022112004oyvkiotrhe2.jpg"', 'src="https://kanmeitu.ojbkcdn.com/t32/2022112004/2022112004golj0oaaia2.jpg"', 'src="https://kanmeitu.ojbkcdn.com/t32/2022112004/2022112004pkvhq32i3fa.jpg"', 'src="https://kanmeitu.ojbkcdn.com/t32/2022112004/20221120045alsy2wc3m2.jpg"', 'src="https://kanmeitu.ojbkcdn.com/t32/2022112004/2022112004qgqhn2webof.jpg"', 'src="https://kanmeitu.ojbkcdn.com/t32/2022112004/20221120043qv2ws1ov3p.jpg"', 'src="https://kanmeitu.ojbkcdn.com/t32/2022112004/2022112004eoiyd5twbeg.jpg"', 'src="https://kanmeitu.ojbkcdn.com/t32/2022112004/2022112004wibwcdp4umy.jpg"']
# for url in urls:
#      # s = url.split("\"")
#     s = url[url.index("\"")+1:-1]
#     print(s)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',}

###下载ts文件
def download(url,name,key):
    r = requests.get(url, headers=headers).content
    cryptor = AES.new(key, AES.MODE_CBC,key)
    with open(name+"", "wb") as code:
        code.write(cryptor.decrypt(r))
        code.close()
def download1(url,name):
    url = "https://m3u8.woikanp.com/hls/contents/videos/102000/102695/102695.mp4/"+name
    r = requests.get(url, headers=headers)
    with open(name+"", "wb") as code:
        code.write(r.content)
        # code.close()
    # code.write(r.content)

def getTsList(key):
    global count
    count = 1
    root = "F:/Pic/test/"  # 保存的路径
    if not os.path.exists(root):  # 判断是否存在文件并下载img
        os.mkdir(root)

    threads = []
    for i in ts_url_list:
        if "#" not in i:
            i = i.replace("\n", "")
            # print(i)
            # n = i[-7:]
            t = threading.Thread(target=download, args=(i, root + str(count),key,))
            t.start()
            threads.append(t)
    for t in threads:
        t.join()
            # download(urlheader+""+i,"cdzj2/"+str(count)+".ts")


# res_ts = requests.get(ts_url).content
# urlheader="https://xigua-cdn.haima-zuida.com/20210219/19948_fcbc225a/1000k/hls/"
# key_url = 'https://9dzh34ee91.motorjn.com/20221125/OpI2NFdB/2500kb/hls/key.key'
#
with open("studyindex.m3u8","r") as f:
    ts_list = f.readlines()

#去掉前面没用的信息
ts_url_list = ts_list[17:]
# ts_key_str = ts_list[5]
key_url_list = re.findall("https.*.key",ts_list[5])
# 这要判断none
key_url = None
key = None
if key_url != None:
    key = requests.get(key_url,headers=headers).content
if key != None:
    print(key)
    getTsList(key)
else:
    print("sb吴权初")
    root = "F:/Pic/test/"  # 保存的路径
    if not os.path.exists(root):  # 判断是否存在文件并下载img
        os.mkdir(root)

    threads = []
    for i in ts_url_list:
        if "#" not in i:
            i = i.replace("\n", "")
            # print(i)
            # n = i[-7:]
            t = threading.Thread(target=download1, args=(i, root + str(i),))
            t.start()
            threads.append(t)
    for t in threads:
        t.join()
