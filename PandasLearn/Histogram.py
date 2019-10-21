# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
'''垂直条状图'''
def cztzt():
    index = np.arange(5)
    value = [5, 7, 3, 4, 6]
    std1 = [0.8, 1.0, 0.4, 0.9, 1.3]
    plt.rcParams['font.sans-serif'] = 'NSimSun,Times New Roman'  # 设置字体的类型
    plt.title('A Bar Chart', loc='center', fontsize=22)
    plt.bar(index, value, yerr=std1, error_kw={'ecolor': '0.1',
                                               'capsize': 6},
            alpha=0.2, label='First')  # alpha  控制图表透明度
    # 使用刻度表名x轴类别，并定义标签位置
    plt.xticks(index, ['A', 'B', 'C', 'D', 'E'])
    plt.legend(loc=2)
    plt.show()
'''水平条状图'''
def sptzt():
    ind = np.arange(5)
    value2 = [5,7,3,4,6]
    std2 = [0.5,2,0.6,1.2,0.3]
    plt.title('a horizontal bar chart')
    plt.barh(ind, value2,xerr= std2,error_kw ={'ecolor': '0.1',
                                               'capsize': 6},
            alpha=0.2, label='First')
    plt.yticks(ind,['A', 'B', 'C', 'D', 'E'])
    plt.legend(loc=4)
    plt.show()

'''多序列条状图'''
def dxltzt():
    index2 = np.arange(5)
    data = [5, 7, 3, 4, 6]
    data2 = [5, 5, 4, 3, 7]
    data3 = [4, 7, 2, 6, 6]
    bw =0.3
    plt.axis([0,5,0,8])
    plt.title('A multiseries bar chart',fontsize = 20)
    plt.bar(index2+0.1,data,bw,color='b',label ='blue')
    plt.bar(index2+0.1+bw, data2, bw, color='g',label ='greem')
    plt.bar(index2 + 0.1 + 2*bw, data3, bw, color='r',label ='red')
    plt.xticks(index2+0.1+bw , ['A', 'B', 'C', 'D', 'E'])
    plt.legend(loc = 2)
    plt.show()

'''为pandas DataFrame生成多序列条状图'''
def pd_dataframe_dxltzt():
    data = {'series1':[1, 3, 4, 3, 5],
            'series2': [2, 4, 5, 2, 4],
            'series3': [3, 2, 3, 1, 3]}
    df = pd.DataFrame(data,
                      index=['a','b','c','d','e'])
    #df.plot(kind ='bar')
    df.plot.bar()
    plt.show()
'''堆积图'''
def djt():
    index = np.arange(4)
    series1 =np.array([3,4,5,2])
    series2 = np.array([1, 2, 2, 5])
    series3 = np.array([2, 3, 3, 4])
    plt.axis([0,15,0,4])
    plt.title('a multiseries horizontal stacked bar chart')
    plt.barh(index,series1,color='w',hatch='xx')
    plt.barh(index, series2, color='w', hatch='///', left=series1)
    plt.barh(index, series3, color='w', hatch='\\\\\\',left =(series1+series2))
    plt.yticks(index+0.4,['Jab15','Feb15','Mar15','Apr15'])
    plt.show()

'''为pandas DataFrame绘制堆积条状图'''
def df_djt():
    data = {'series1': [1, 3, 4, 3, 5],
            'series2': [2, 4, 5, 2, 4],
            'series3': [3, 2, 3, 1, 3]}
    df = pd.DataFrame(data)
    df.plot(kind= 'bar',stacked = True)  #设置stacked参数为true绘制堆积图
    plt.show()


'''其他条状图
# 修改条状图的边框和条状图内部区域的颜色，只要用另外两个关键字参数
#facecolor和edgecolor设置两种不同的颜色即可，末端显示y值标签
#标签位置用ha和va关键字参数来调整'''
def qtt():
    x0 = np.arange(8)
    y1 = np.array([1,3,4,6,4,3,2,1])
    y2 = np.array([1,2,5,4,3,3,2,1])
    plt.ylim(-7,7) #限制纵坐标高度
    plt.bar(x0,y1,0.9,facecolor = 'r', edgecolor ='w')
    plt.bar(x0,-y2, 0.9, facecolor='b', edgecolor='w')
    plt.xticks(())
    plt.grid(True) #设置网格
    for x, y in zip(x0,y1):
        plt.text(x , y + 0.05, '%d' % y, ha='center', va ='bottom')
    for x, y in zip(x0,y2):
        plt.text(x , -y - 0.05, '%d' % y, ha='center', va ='top')
    plt.show()
qtt()