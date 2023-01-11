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
import time
from bs4 import BeautifulSoup
# 多线程同时下载
from threading import Thread,current_thread
# 线程池+异步下载
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
#
#
# #构建查询字符串字典
# query_string = {
#     'ie': 'utf-8',
#     'wd': '爬虫'
# }
# #调用parse模块的urlencode()进行编码
# result = parse.urlencode(query_string)
# #使用format函数格式化字符串，拼接url地址
# url = 'http://www.baidu.com/s?{}'.format(result)
# print(url)

# http://httpbin.org/get 这个网站能测试 HTTP 请求和响应的各种信息，比如 cookie、IP、headers 和登录验证等，且支持 GET、POST 等多种方法，对 Web 开发和测试很有帮助。
# urlopen()向URL发请求,返回响应对象,注意url必须完整
# url = 'http://httpbin.org/get' #向测试网站发送请求
# #重构请求头，伪装成 Mac火狐浏览器访问，可以使用上表中任意浏览器的UA信息
# ua = UserAgent()
# headers = {
#     'User-Agent':ua.firefox}
# # 1、创建请求对象，包装ua信息
# req = request.Request(url=url,headers=headers)
# # 2、发送请求，获取响应对象
# res = request.urlopen(req)
# # 3、提取响应内容
# html = res.read().decode('utf-8')
# # 打印响应内容
# print(html)
# /html/body/section/div/div/article/p/img[1]
# for i in  range(2):
#     if i == 0:
#         continue;
#     url = "https://www.xgmn01.com/Xgyw/Xgyw19496_"+str(i)+".html"#需要爬取图片的网页地址
#     print(url)
#     # 2、发送请求，获取响应对象
#     res = request.urlopen(url)
#     # 3、提取响应内容
#     html = res.read().decode('utf-8')
#     # page = requests.get(url).text#得到网页源码
#     # page.read().decode('utf-8')
#     print(html)
#     res1 = re.compile(r'src="/+?.jpg"')#运用正则表达式过滤出图片路径地址
#     reg = re.findall(res1, html)#匹配网页进行搜索出图片地址数组
#     print(reg)
#     # #循环遍历下载图片
#     num = 0
#     for i in reg:
#         a = requests.get(i)
        # E:\ideaProject\pythonStudy\json
        # if not os.path.exists("E:\ideaProject\pythonStudy\json"): #判断如果不存在filedir（./json/）这个目录
        #     os.makedirs("E:\ideaProject\pythonStudy\json")  #创建这个目录
        # f = open("img/%s.jpg"%num, 'wb')#以二进制格式写入img文件夹中
        # f.write(a.content)
        # f.close()
        # print("第%s张图片下载完毕"%num)
        # num = num+1
    # print(page)
    # <img alt="xgyw.top_蜜桃少女是依酱呀T恤底下主题私房半脱露性感黑色缕空内衣秀完美身材诱惑写真31P" title="xgyw.top_蜜桃少女是依酱呀T恤底下主题私房半脱露性感黑色缕空内衣秀完美身材诱惑写真31P" src="/uploadfile/202109/28/8D194125636.jpg">
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
}
def getPic(res):
    # if len(res) == 0:
    #     print("res错误")
    #     return ;
    # print(res)
    res= res.result()
    soup = BeautifulSoup(res, "html.parser")
    #通过分析网页内容，查找img的统一父类及属性
    all_img = soup.find('p').find_all('img')
    root = "F:/Pic/3/"   #保存的路径
    if not os.path.exists(root):  #判断是否存在文件并下载img
        os.mkdir(root)
    # print(all_img)
        # .find_all('img') #img为图片的标签
    imgList = [];
    for img in all_img:
        src = img['src']  #获取img标签里的src内容
        img_url = "https://www.xgmn01.com"+src
        # print(img_url)
        imgList.append(img_url)
    for imgUrl in imgList:
        path = root + imgUrl.split('/')[-1]  #获取img的文件名
        # print(path)
        try:
            if not os.path.exists(path):
                read = requests.get(imgUrl)
                with open(path, "wb")as f:
                    f.write(read.content)
                    f.close()
                    print("文件保存成功！")
            else:
                print("文件已存在！")
        except:
            print("文件爬取失败！")
            continue;

# 多线程下载
def getHtml1(url,callback=getPic):
    read = requests.get(url)  #获取url
    read.raise_for_status()   #状态响应 返回200连接成功
    read.encoding = read.apparent_encoding  #从内容中分析出响应内容编码方式
    if read.status_code == 200:
        callback(read.text)
def getHtml(url):
    read = requests.get(url,headers=headers)  #获取url
    read.raise_for_status()   #状态响应 返回200连接成功
    read.encoding = read.apparent_encoding  #从内容中分析出响应内容编码方式
    if read.status_code == 200:
        return read.text
    # getPic(read.text)
if __name__ == '__main__':
    begin = time.time()
    urls = [];
    for i in  range(0,29):
        if i == 0:
            url = "https://www.xgmn01.com/Xiuren/Xiuren24077.html"
        else:
            url = "https://www.xgmn01.com/Xiuren/Xiuren24077_"+str(i)+".html"#需要爬取图片的网页地址
        # print(url)
        urls.append(url)
    print(urls)
    pool=ThreadPoolExecutor(50)
    strList=[]
    for url in urls:
        # 多线程下载
        # t = Thread(target=getHtml, args=(url,))
        # t.start()
        pool.submit(getHtml,url).add_done_callback(getPic)
    #     strList.append(future)
    #     # strList.append(future.result())
    #         # .add_done_callback(getPic)
    # for i in strList:
    #     i.add_done_callback(getPic)
    pool.shutdown(wait=True);
    times = time.time() - begin
    print(times)

