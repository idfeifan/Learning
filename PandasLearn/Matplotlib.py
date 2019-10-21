# coding=utf-8
import datetime
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
import math
'''多个图表在一张图中'''


def dtb():
    t = np.arange(0, 2.5, 0.1)
    s1 = []
    s2 = []
    s3 = []
    y1 = map(math.sin, math.pi * t)
    y2 = map(math.sin, math.pi * t + math.pi / 2)
    y3 = map(math.sin, math.pi * t - math.pi / 2)
    for i in y1:
        s1.append(i)
    for i in y2:
        s2.append(i)
    for i in y3:
        s3.append(i)
    yy1 = np.array(s1)
    yy2 = np.array(s2)
    yy3 = np.array(s3)
    plt.plot(t, y1, 'b--', t, yy2, 'g', t, yy3, 'r-.')
    plt.show()


# plt.plot([1,2,4,2,1,0,1,2,1,4],linewidth='5.0') //linewidth控制线条宽度
# plt.show()
'''多张图在一个figure中'''


def more_figure():
    t = np.arange(0, 5, 0.1)
    q = np.sin(2*np.pi*t)
    q2 = np.sin(2*np.pi*t)
    plt.subplot(211)
    plt.plot(t,q,'b-.')

    plt.subplot(212)
    plt.plot(t,q2,'r--')
    plt.show()
'''
LaTeX功能 图表添加标签
'''
def picture_lable():
    plt.axis([0,5,0,20]) # 定义横纵坐标边界
    plt.title('My first plot' , fontsize = 20 ,fontname = 'Times New Roman')
    plt.xlabel('Counting' , color = 'gray')

'''将图片直接保存为图片'''
def save_picture():
    plt.axis([0,5,0,20]) #规定横纵坐标刻度
    plt.title("My First plot",fontsize=20,fontname='Time New Roman') #设置标题
    plt.xlabel("Counting",color='gray') #设置横坐标描述
    plt.ylabel("Square values", color='gray') #设置纵坐标描述
    plt.text(1,1.5,'First') #设置刻度描述
    plt.text(2, 4.5, 'Second')
    plt.text(3, 9.5, 'Third')
    plt.text(4, 16.5, 'Fourth')
    plt.text(1.1,12, r'$y = x^2$',bbox={'facecolor':'yellow','alpha':0.2}) #添加彩色边框公式
    plt.grid(color='g', linestyle='--', linewidth=1)  #网格化图表
    plt.plot([1,2,3,4],[1,4,9,16],'ro')
    plt.plot([1, 2, 3, 4], [0.8,3.5,8,15], 'g^')
    plt.plot([1, 2, 3, 4], [0.5, 2.5, 4, 12], 'b*')
    plt.legend(['Fryst series','Second series','Third series'],loc = 2) #设置图例说明添加到图标中
    plt.savefig('save_picture.png')
    plt.show()

def deal_time():
    months = mdates.MonthLocator()
    days =mdates.DayLocator()
    timeFmt = mdates.DateFormatter('%Y-%m')
    events = [datetime.date(2015,1,23),
              datetime.date(2015, 1, 28),
              datetime.date(2015, 2, 3),
              datetime.date(2015, 2, 21),
              datetime.date(2015, 3, 15),
              datetime.date(2015, 3, 24),
              datetime.date(2015, 4, 8),
              datetime.date(2015, 4, 24)]
    readings = [12,22,25,20,18,15,17,14]
    fig, ax =plt.subplots()
    ax.plot(events,readings)
    ax.set_title('this deal_time')
    ax.xaxis.set_major_locator(months)
    ax.xaxis.set_major_formatter(timeFmt)
    ax.xaxis.set_minor_locator(days)
    plt.show()


deal_time()