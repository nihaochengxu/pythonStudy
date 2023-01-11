# date='2021'+'{:2}'.format(12)
# date1='2021'+'{:02}'.format(1)
# print(date)
# print(date1)
# 导包,发起请求使用urllib库的request请求模块
from urllib import request
from fake_useragent import UserAgent
from urllib import parse
import requests
import re
import os

from bs4 import BeautifulSoup
# 多线程同时下载
from threading import Thread,current_thread
# 线程池+异步下载
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
}
def download(url,path):
    try:
        if not os.path.exists(path):
            read = requests.get(url,headers=headers)
            with open(path, "wb")as f:
                f.write(read.content)
                f.close()
                print("one img save success")
        else:
            print("one img is exists！")
    except:
        print("one img save failure")
        return ;
def getPic(res):
    # if len(res) == 0:
    #     print("res错误")
    #     return ;
    soup = BeautifulSoup(res, "html.parser")

    #通过分析网页内容，查找img的统一父类及属性
    all_img = soup.find_all('img')
    # all_img = soup.find_all(attrs={'alt': '[福利COS] Cosplay日奈娇 - 星空钻石/26P'})
    # print(all_img)
    imgs = all_img[1:]
    print(type(imgs[0]))
    imgList = [];

    for img in imgs:
        src = img['src']  #获取img标签里的src内容
        img_url = src
        imgList.append(img_url)
    # print(imgList)
    # root = "F:/Pic/2/azhu4/"   #保存的路径
    # if not os.path.exists(root):  #判断是否存在文件并下载img
    #     os.mkdir(root)
    #
    #
    # threads = []
    # for imgUrl in imgList:
    # #     print(img_url)
    #     path = root + imgUrl.split('/')[-1]  #获取img的文件名
    #     t = Thread(target=download, args = (imgUrl,path))
    #     t.start()
    #     threads.append(t)
    # for t in threads:
    #     t.join()
    # #     # print(path)


# 多线程下载
def getHtml(url,callback=getPic):
    read = requests.get(url,headers=headers)  #获取url
    read.raise_for_status()   #状态响应 返回200连接成功
    read.encoding = read.apparent_encoding  #从内容中分析出响应内容编码方式
    if read.status_code == 200:
        callback(read.text)
def getHtml1(url):
    read = requests.get(url,headers=headers)  #获取url
    read.raise_for_status()   #状态响应 返回200连接成功
    read.encoding = read.apparent_encoding  #从内容中分析出响应内容编码方式
    if read.status_code == 200:
        return read.text
if __name__ == '__main__':
    imgList =[]
    for i in  range(0,10):
        if i == 0:
            url = "https://www.xgmn01.com/Xgyw/Xgyw24583.html"
        else:
            url = "https://www.xgmn01.com/Xgyw/Xgyw24583_"+str(i)+".html"#需要爬取图片的网页地址
        print(url)
        imgList.append(url)
    # url1 = "https://kanmeitu1.cc/p/41609.html";
    # url1 = "https://kanmeitu1.cc/p/59117.html";
    # url1 = "https://kanmeitu1.cc/p/57484.html";
    # url1 = "https://kanmeitu1.cc/p/59348.html";
    # res = getHtml1(url1)
    # getPic(res)
    # print(imgList)
    pool=ThreadPoolExecutor(50)
    for l in imgList:
    #     # 多线程下载
    #     t = Thread(target=getHtml, args=(l,))
    #     t.start()
        pool.submit(getHtml,l).add_done_callback(getPic)
    pool.shutdown(wait=True);
