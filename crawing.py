#encoding=utf-8
import csv
import time
import re
import os

import pandas
import requests
import json
import numpy as np


url='http://d1.weather.com.cn/calendar_new/2021/101210701_'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    'Referer':'http://www.weather.com.cn/',
}
filedir='./json/'
field=['alins', 'als', 'blue', 'c1', 'c2', 'cla', 'date', 'des', 'fe', 'hgl', 'hmax', 'hmin', 'hol', 'insuit', 'jq', 'max', 'maxobs', 'min', 'minobs', 'nl', 'nlyf', 'r', 'rainobs', 'suit', 't1', 't1t', 't2', 't3', 't3t', 'time', 'today', 'update', 'w1', 'wd1', 'winter', 'wk', 'wor', 'ws1', 'yl']

def getJsonData(url,headers,month):
    # print(i)
    #eg：url，一个完整的月份url请求实例：http://d1.weather.com.cn/calendar_new/2022/101210701_202207.html?_=1655478466291
    t=time.time() #返回当前时间的时间戳
    date='2021'+'{:02}'.format(month) #将month替代{:02}；是当month为1和12时，不加0（就是{:2}）会date变成‘2021 1’和‘202112’,会有空格，不符合天气请求url的格式；加了0（就是{:02}),date会变成‘202101’和‘202112’
    suffix='.html?_=' #请求后缀，具体看eg：url
    rubbing=int(round(t * 1000)) #随机数
    url=url+date+suffix+str(rubbing) #拼接url，最终结果就是类似上面的url实例
    response = requests.get(url, headers=headers) #请求url
    response.encoding="utf-8" #设置编码
    json_code=response.text.replace('var fc40 = ','') #获取相应的response的text，并将字符串的的前缀‘var fc40 = ’代替为空字符串
    json_page = json.loads(json_code) #转为json格式
    saveJsonData(json_page,date+'.csv') #调用其他方法，将json_page，'date'.csv作为参数传进去


def saveJsonData(json_page,filename):
    if not os.path.exists(filedir): #判断如果不存在filedir（./json/）这个目录
        os.makedirs(filedir)  #创建这个目录
    with open(filedir+filename,'w',newline='') as f: #打开文件，‘w’是指以写的方式（这些参数的意义可以上网找到的），
        writer=csv.DictWriter(f,fieldnames=field) #f是打开文件的对象，field是csv文件的表头
        writer.writeheader()  #将表头名称写入csv文件
        for inf in json_page:
            if filename[:-4] in inf['date']: #filename为202101.csv，filename[:-4]为202101;如果inf['date']包含‘202101’这个字符串，就执行下面的语句写入到csv文件
                writer.writerow(inf)   #r.writerow()一次写入一行
    print(filename+'保存成功!')

#获取2020年南昌市气温
for i in range(1,13):
    getJsonData(url,headers,i)



