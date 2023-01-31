# ！/usr/bin/python3
# -*- coding: utf-8 -*-
import re
# from lxml import etree
import requests
import time
from tqdm import tqdm
import os
from urllib.request import urlopen

def download_from_url(url, dst):
    """
    @param: url to download file
    @param: dst place to put the file
    :return: bool
    """
    # 获取文件长度
    try:
        file_size = int(urlopen(url).info().get('Content-Length', -1))
    except Exception as e:
        print(e)
        print("错误，访问url: %s 异常" % url)
        return False

    # print("file_size",file_size)
    # 判断本地文件存在时
    if os.path.exists(dst):
        # 获取文件大小
        first_byte = os.path.getsize(dst)
    else:
        # 初始大小为0
        first_byte = 0

    # 判断大小一致，表示本地文件存在
    if first_byte >= file_size:
        print("文件已经存在,无需下载")
        return file_size


    header = {"Range": "bytes=%s-%s" % (first_byte, file_size)}

    pbar = tqdm(
        total=file_size, initial=first_byte,
        unit='B', unit_scale=True, desc=url.split('/')[-1])

    # 访问url进行下载
    req = requests.get(url, headers=header, stream=True)
    try:
        with(open(dst, 'ab')) as f:
            for chunk in req.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    pbar.update(1024)
    except Exception as e:
        print(e)
        return False

    pbar.close()
    return True

def DownloadFile(url, name):
    """
    下载文件
    :param url:
    :param name:
    :return:
    """
    try:
        resp = requests.get(url=url, stream=True)
        content_size = int(resp.headers['Content-Length']) / 1024
        with open(name, "wb") as f:
            print("package total size is:", content_size, 'k,start...')
            for data in tqdm(iterable=resp.iter_content(1024), total=content_size, unit='k', desc=name):
                f.write(data)

        print("%s 下载成功"%url)
        return True
    except Exception as e:
        print(e)
        print("%s 下载失败" % url)
        return False

# 头部
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
}

# 访问页面
# response = requests.get('https://www.ku6.com/detail/371', headers=headers)
# data = response.text
#
# #构造了一个XPath解析对象并对HTML文本进行自动修正
# html = etree.HTML(data)
# # 获取视频播放链接
# html_data = html.xpath('//div[@class="r_box"]/ul/li//a/@href')
# # print("html_data", html_data, type(html_data))

# 遍历url
# for i in html_data:
#     url = "https://www.ku6.com%s" % i
#     print(url)
#
#     # 访问url
#     response_1 = requests.get(url, headers=headers)
#     data_1 = response_1.text
#     # 正则匹配视频地址
#     video = re.findall('type: "video/mp4", src: "(.*?)"',data_1)
#     video_1 = video[0]
if __name__ == '__main__':
    video_1 = 'https://7fe143wa08.motorjn.com/20221125/OpI2NFdB/index.m3u8'
    video_1 = 'https://m3u8.woikanp.com/hls/contents/videos/102000/102695/102695.mp4/index.m3u8'
    x = "study"+video_1.split('/')[-1]

    # 本地保存视频文件名
    name = x
    print("name", name)

    # 下载视频
    download_from_url(video_1, name)
    # 这里只演示第一个视频，直接break

