#encoding=utf-8
import os
import csv
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False


filedir='./json/'
monthly_ave_high_temp=[]	#每月平均最高温
monthly_ave_low_temp=[]		#每月平均最低温
monthly_ave_temp=[]			#每月平均气温
monthly_ave_prec=[]			#每月平均降水概率

monthly_high_temp=[]		#每月中每天的最高温
monthly_low_temp=[]			#每月中每天的最低温
daily_temp=[]				#每月中每天的平均气温
daily_prec=[]				#每月中每天的降水概率

month_temp=[]

def ReadCSVFile(filedir):
    for root,dirs,files in os.walk(filedir): #os.walk(dirpath,dirnames,filenames)返回3个参数，这里是如果‘根目录’，‘目录名称’，以及‘文件’在os.walk返回的值（也就是‘./json/*’目录的所有文件）中,就执行下面操作
        for filename in files:
            with open(filedir+filename,'r') as f: #以读的方式打开‘./json/*’下的文件
                high_temp=[]
                low_temp=[]
                temp=[]
                prec=[]
                reader=csv.reader(f)
                headers=next(reader)
                for row in reader:
                    prec.append(int(row[9][:-1])) #降水概率，取第10列除了最后一行的所有数据
                    high_temp.append(int(row[10])) #最高温度，取第11列的所有数据
                    low_temp.append(int(row[11])) #最低温度，取第12列的所有数据
                    temp.append((int(row[10])+int(row[11]))/2) #将最高温度+最低温度的值除于2，也就是平均值
                    daily_temp.append((int(row[10])+int(row[11]))/2) #添加每月中每天的平均气温
                    daily_prec.append(int(row[9][:-1])) #添加每月中每天的降水概率
            monthly_high_temp.append(high_temp) #添加每月中每天的最高温
            monthly_low_temp.append(low_temp) #添加每月中每天的最低温
            #下面都是取平均值
            monthly_ave_high_temp.append(np.mean(high_temp))
            monthly_ave_low_temp.append(np.mean(low_temp))
            monthly_ave_temp.append((np.mean(high_temp)+np.mean(low_temp))/2)
            monthly_ave_prec.append(np.mean(prec))

            month_temp.append(temp)

        print("获取JSON数据成功!")

#读取数据
ReadCSVFile(filedir)
#绘制年平均气温变化图
#对数据进行处理，绘制每月的平均温度
plt.subplots(figsize=(30,20))
plt.xticks(range(0,13,1),rotation=30)
plt.yticks(range(0,38,1))
plt.grid()  #显示网格
x=np.arange(1, 13)
y1=monthly_ave_high_temp
y2=monthly_ave_temp
y3=monthly_ave_low_temp
y4=[np.mean(monthly_ave_temp)]*12
plt.plot(x,monthly_ave_high_temp,'*-',color='red',linewidth=0.8)
plt.plot(x,monthly_ave_temp,'o-',color='yellow',linewidth=0.8)
plt.plot(x,monthly_ave_low_temp,'o-',color='green',linewidth=0.8)
plt.plot(x,[np.mean(monthly_ave_temp)]*12,'--',color='red',linewidth=0.9)
plt.fill_between(x, monthly_ave_high_temp, monthly_ave_low_temp, facecolor='blue', alpha=0.2) # facecolor指定了区域的颜色
bar_width = 0.35
plt.plot(x,y1,label='月平均最高温',color='red')
plt.plot(x,y2,label='月平均温度',color='yellow')
plt.plot(x,y3,label='月平均最低温',color='green')
plt.plot(x,y1,label='年平均温度',color='red')
plt.legend(bbox_to_anchor=(1,1),#图例边界框起始位置
           loc="upper right",#图例的位置
           ncol=1,#列数
           mode="None",#当值设置为“expend”时，图例会水平扩展至整个坐标轴区域
           borderaxespad=0,#坐标轴和图例边界之间的间距
           title="图例",#图例标题
           shadow=False,#是否为线框添加阴影
           fancybox=True)#线框圆角处理参数
plt.title('2020年南昌市年平均气温变化情况',fontproperties='SimHei',fontsize=15)
plt.xlabel('月份',fontproperties='SimHei',fontsize=15)
plt.ylabel('温度/℃',fontproperties='SimHei',fontsize=15)
plt.savefig('2020年南昌市年平均气温变化情况',dpi=300)
# plt.show()

plt.subplots(figsize=(30,20))
#绘制各月的气温变化图
plt.xlim(0,32)
plt.subplots_adjust(wspace=0.35,hspace=0.55)
for i in range(1,13):
    plt.subplot(3,4,i)
    plt.plot(np.arange(1, len(monthly_high_temp[i-1])+1),monthly_high_temp[i-1],'*-',color='red',linewidth=0.8)
    plt.plot(np.arange(1, len(monthly_low_temp[i-1])+1),monthly_low_temp[i-1],'*-',color='blue',linewidth=0.8)
    ave_temp=(np.mean(monthly_low_temp[i-1])+np.mean(monthly_high_temp[i-1]))/2
    plt.plot(np.arange(1, len(monthly_low_temp[i-1])+1),[ave_temp]*len(monthly_low_temp[i-1]),'-',color='green',linewidth=0.8)
    plt.title('2020年南昌市'+str(i)+'月气温变化情况',fontproperties='SimHei',fontsize=15)
    plt.xlabel('日期',fontproperties='SimHei',fontsize=15)
    plt.ylabel('温度/℃',fontproperties='SimHei',fontsize=15)

plt.plot(np.arange(1, len(monthly_high_temp[i-1])+1),monthly_high_temp[i-1],label='每日最高温',color='red')
plt.plot(np.arange(1, len(monthly_high_temp[i-1])+1),monthly_low_temp[i-1],label='每日最低温',color='blue')
plt.plot(np.arange(1, len(monthly_high_temp[i-1])+1),[ave_temp]*len(monthly_low_temp[i-1]),label='当月平均温',color='green')
plt.legend(bbox_to_anchor=(1.6,2.5),#图例边界框起始位置
           loc="upper right",#图例的位置
           ncol=1,#列数
           mode="None",#当值设置为“expend”时，图例会水平扩展至整个坐标轴区域
           borderaxespad=0,#坐标轴和图例边界之间的间距
           title="图例",#图例标题
           shadow=False,#是否为线框添加阴影
           fancybox=True)#线框圆角处理参数
plt.savefig('2020年南昌市各月气温变化情况',dpi=300)
# plt.show()


x_data=np.arange(1, 13)
y_data=monthly_ave_temp
for i in range(len(y_data)):
    y_data[i]=round(y_data[i],2)

fig,ax = plt.subplots(figsize=(30,20))
plt.xlabel('月份',fontproperties='SimHei',fontsize=15)
plt.ylabel('月平均温度/℃',fontproperties='SimHei',fontsize=15)
ax.bar(x_data,y_data)
for x,y in zip(x_data,y_data):
    ax.annotate(str(y)+'℃',(x,y+0.05),fontsize=14,horizontalalignment='center')
plt.title('2020年南昌市月平均气温变化情况',fontproperties='SimHei',fontsize=15)
plt.savefig('2020年南昌市月平均气温变化情况',dpi=300)
# plt.show()

#绘制一年中各种温度的天数所占的比例
#统计温度区间  左闭右开
df=pd.Series(daily_temp)
size=[]
explode=(0.05,0.1,0.05,0.1,0.15,0.15,0.05)
labels=['[0,5)','[5,10)','[10,15)','[15,20)','[20,25)','[25,30)','[30,35)']
elements=['温度处于[0,5)℃','温度处于[5,10)℃','温度处于[10,15)℃','温度处于[15,20)℃','温度处于[20,25)℃','温度处于[25,30)℃','温度处于[30,35)℃']
for i in range(0,7):
    size.append(df[(df>=i*5) & (df<(i*5+5))].count())
#绘制圆饼图
plt.subplots(figsize=(15,10))
wedges,texts,autotexts=plt.pie(size,explode,labels=elements,autopct='%1.1f%%',startangle=90,radius=0.8)
plt.axis()
plt.legend(wedges,
           elements,
           fontsize=12,
           title="说明",
           loc="upper right",
           bbox_to_anchor=(0.91, 0, 0.3, 1))
plt.title('2020年南昌市每日气温统计情况',fontproperties='SimHei',fontsize=15)
plt.savefig('2020年南昌市每日气温统计情况',dpi=300)

#温度分布图
plt.subplots(figsize=(15,10))
data1=pd.read_csv('newWeather360.csv',encoding='utf-8')
plt.title('2020年南昌市最高气温分布概率',fontproperties='SimHei',fontsize=15)
sns.displot(data1['hmax'])
plt.xlabel('温度/℃',fontproperties='SimHei',fontsize=15)
plt.ylabel('概率',fontproperties='SimHei',fontsize=15)
plt.savefig('2020年南昌市最高气温分布概率',dpi=300)


# plt.subplots(figsize=(20,15))
data1=pd.read_csv('newWeather360.csv',encoding='utf-8')
sns.lmplot(x='date',y='hmax',data = data1,hue='nlyf',fit_reg=False,markers='*')
plt.title('2020年南昌市全年气温分布图散点图',fontproperties='SimHei',fontsize=13, y=-0.11)
plt.xlabel('日期',fontproperties='SimHei',fontsize=15)
plt.ylabel('温度/℃',fontproperties='SimHei',fontsize=15)
plt.savefig('2020年南昌市全年气温分布图散点图',dpi=300)
plt.show()
