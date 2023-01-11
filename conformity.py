import pandas
import pandas as pd

final_list = []
for i in range(1,13): #循环读取12个csv文件，也就是每个月份的数据
    if i < 10:
        s = './json/20210'+str(i)+'.csv'
    else:
        s = './json/2021'+str(i)+'.csv'
    print(s)
    date = pandas.read_csv(s, sep=',', encoding='gb18030') #读取数据
    final_list.append(date) #将数据赋给列表
dataset = pd.concat(final_list,ignore_index = False) #合并处理,在这里作用为转换，因为final_list是列表调不了.to_csv功能
dataset.to_csv("newWeather360.csv",index=None) #写到csv文件中