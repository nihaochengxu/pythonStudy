# num = [1,2,3]
# def sout(i):
#     print(i)
#     return i;
# task =[sout(i) for i in num]
# print(task)
# import requests
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
#     "cookie":"_zap=0b6ec58a-f475-4de6-9cc4-d9c66dbb911d; _xsrf=9fde8f05-8d5b-4f12-b14f-e3eda07faf3f; d_c0=AFDXOFIHIhaPTjMc_nTczeL887IpXv68VJc=|1673020742; arialoadData=false; SESSIONID=BkAp9vZQCg6hcGT2OTKOlQXYAFujy8YmW7PA8w2MUhw; JOID=VFgcAEku3DAccOEhNytu7x_GED0sar57bU2RcmxpvQ9-EqJzDI2Xg3py7iI8633-jvF_8-0ss6wNA2b8bV969qA=; osd=V18RA0st2z0fcuImOihs7BjLEz8vbbN4b06Wf29rvghzEaBwC4CUgXl14yE-6HrzjfN89OAvsa8KDmX-blh39aI=; __snaker__id=ou2GTYot3GchU0bT; gdxidpyhxdE=6D52wb+sg9\pJPONm1Kplr9o0aAVdEuA6mPZGY7uMe\IqWds4C5rBki8Hlanh0jwaUndERs5LHVwMwl\W4EZ+J1Ga+OpAxhabMMxKDzoVZkPLNm65B2cvnodzXtYQso77CSL0tr4mlS8gp9QG16fPaMUwOETzzXMP/llYGurqhlGySsB:1673022513215; YD00517437729195:WM_NI=nr8nJ/dFjr4AjjsuC4lzworzgUmOCIQRRAsnJYUIsLIuN3SW1A4+ZEzhnnzqBVmuil6+GekCfyHzmUGqm7fv4sLgvg7tgCgjzqjqw7pNpeM8uZZOdbiGSvBokLVipodSRmc=; YD00517437729195:WM_NIKE=9ca17ae2e6ffcda170e2e6eeb9cb65f4a9969af143aaef8aa2d54e938a8b87c170ad9ae194bc3eb4bea2b7e82af0fea7c3b92aaeaef88fc925a89aa693b74baab6bd96c240b0a6b990f172a58ba3b0c243938e9ea2f2668a879baaf2488bab82d4d25df39ffcccd94fbab8a28ff97b828aa396ec68f6f58986ea49a6a7889bf05f85afa3d8e57ef8ad8488f56df5aca9a4e662baafa692f63db492c086d034b78696b0e76aab999d97c165a9949a8af365a88d9e8ee237e2a3; YD00517437729195:WM_TID=ovDYAQmW16NFUBVAFFNr527LkSUjmQn5; captcha_session_v2=2|1:0|10:1673021791|18:captcha_session_v2|88:bFhkcllmWGJZaEIxcUZmRGkvZVFjSkdidzJUSS9XMzBVVlRabzBvYldNcHN4dE9qQm9zUG8wdkFrM1ZNb3dhVw==|d4995b662781b22914c0888191c6e187d4e2eaeab045d23d15b78e5c00584257; z_c0=2|1:0|10:1673021879|4:z_c0|92:Mi4xc1E4cE13QUFBQUFBVU5jNFVnY2lGaVlBQUFCZ0FsVk5kSmVsWkFDbXFMU2hIS19GY3VlLTZGaHhfUm1nOVdOZk1n|c65cf2c80702b7af88ac98a0ce4c52baf64e8447898592faef313da9ad8f9d8c; KLBRSID=fb3eda1aa35a9ed9f88f346a7a3ebe83|1673021881|1673020747"
#     # "cookie":"_zap=0b6ec58a-f475-4de6-9cc4-d9c66dbb911d; _xsrf=9fde8f05-8d5b-4f12-b14f-e3eda07faf3f; d_c0=AFDXOFIHIhaPTjMc_nTczeL887IpXv68VJc=|1673020742; arialoadData=false; YD00517437729195:WM_NI=wKPxRbsSo4tiJZIx1cElSijIPgPOWY/r4C7InD07xtK1idS+am/rRpvKfOWjhX4H6pd7Nx6VKLE0eRAapfTVj6w+bsj01EQSgWmoPZk38FHhgOLHopoKUlkAZyxVtFY4QUE=; YD00517437729195:WM_NIKE=9ca17ae2e6ffcda170e2e6ee92f67dabac8f93cf68ad928ea2c55e878a8fb1c143b89fe5d5cf63f189b782eb2af0fea7c3b92ab595a099d16ab18da1d5f7638a868799b46987b49d8ae94394b9a0b0d653edaefca4b643ae9c00d8fb8089efa785d221a3b3e193d17cb695aab0d662ac88fca9b57ca8e98299b55e89948bd1e85a83bfc087d75eaaeab9cce179aaf0ffa6d459a589a390d352a9edf8a7cb64a59184a9ee7cad959b8dea4b9aa7b8b7f74e9bec9fb6c837e2a3; YD00517437729195:WM_TID=DxJf1FJGi7REUFARVRdu4tTXhfwT2s+q; gdxidpyhxdE=A+egdy41d+9+XtOPBPt6/dMOnIzsUW3AOQPm0VMebz/JCygrEPjQUCoMmSTHevDOxTNguy8+a+WWWoMoS3X40Lxf/YSDpDU4rUdks4WNq5P7O4vaOo/u8rlDhM7XTMKHLdCysmkrYf8CdZyGVR0QBLoUVcCSwL5YoPH9zfcJEbWCCq0e:1673022495154; captcha_session_v2=2|1:0|10:1673021791|18:captcha_session_v2|88:bFhkcllmWGJZaEIxcUZmRGkvZVFjSkdidzJUSS9XMzBVVlRabzBvYldNcHN4dE9qQm9zUG8wdkFrM1ZNb3dhVw==|d4995b662781b22914c0888191c6e187d4e2eaeab045d23d15b78e5c00584257; KLBRSID=975d56862ba86eb589d21e89c8d1e74e|1673022100|1673020742"
# }
# url = "https://www.zhihu.com/api/v4/me?include=visits_count%2Cdraft_count"
# read = requests.get(url,headers = headers)  #获取url
# print(read.text)


# 协程参考链接：https://zhuanlan.zhihu.com/p/59621713
import asyncio


async def a():
    print('Suspending a')
    await asyncio.sleep(0)
    print('Resuming a')
    return 'sba'

async def b():
    print('In b')
    return 'sbb'

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [loop.create_task(a()), loop.create_task(b())]
    wait_task = asyncio.wait(tasks)
    loop.run_until_complete(wait_task)
    for i in tasks:
        try:
            print('返回值：', i.result())
        except asyncio.InvalidStateError:
            print('task状态未完成，捕获了 InvalidStateError 异常')
    loop.close()