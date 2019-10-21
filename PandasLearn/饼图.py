# coding=utf-8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''绘制饼图'''
def bt():
    labels = ['Nokia','Samsung','Apple','Lumia']
    values = [10,30,45.5,14.5]
    colors = ['yellow','green','red','blue']
    explode =[0.1,0,0,0]  #代表每个点的偏离位置
    plt.title('a pie chart!')
    plt.pie(values,labels=labels,colors=colors,explode=explode,startangle=0,
            shadow=True,autopct='%1.1f%%') #shadow 显示阴影 autopct显示百分比1.1表示保留一位小数
    plt.axis('equal')
    plt.show()

'''dataFrame 数据源饼图'''
def df_bt():
    data = {'series1':[1,2,3,4,5],
            'series2': [2,4,5,2,5],
            'series3': [3,2,3,1,3]}
    df = pd.DataFrame(data)
    df['series2'].plot(kind='pie',figsize=(8,8))  #figsize指figure大小
    plt.show()

'''等值线图'''
def dzxt():
    dx = 0.01;dy =0.01
    x = np.arange(-2.0,2.0,dx)
    y = np.arange(-2.0,2.0,dy)
    X,Y = np.meshgrid(x,y)
    def f(x,y):
        return (1 - y**5 +x**5)*np.exp(-x**2-y**2)
    C = plt.contour(X,Y,f(X,Y),8,colors='black')
    plt.contourf(X,Y,f(X,Y),8,cmap=plt.cm.hot)
    plt.clabel(C,inline = 1, fontsize=10)
    plt.colorbar()
    plt.show()
'''极区图 使用bar()函数'''
def jqt():
    N = 8
    theta = np.arange(0.,2 *np.pi,2 *np.pi /N)
    radii = np.array([4,7,5,3,1,5,6,7])
    plt.axes([0.025,0.025,0.95,0.95], polar=True)
    colors = np.array(['#4bb2c5','#c5b47f','#EAA228','#579557','#839557',
                       '#958c12','#953589','#4b5de4'])
    bars = plt.bar(theta,radii,width=(2 *np.pi/N),bottom=0,color=colors,
                   align='edge')
    plt.title(-2,'这是极区图',loc='left')
    plt.show()
jqt()