# coding=utf-8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
'''线性图'''
def zxt():
    x = np.arange(-2 * np.pi, 2 * np.pi, 0.01)
    y = np.sin(3 * x) / x
    y1 = np.sin(2 * x) / x
    y2 = np.sin(1 * x) / x
    plt.plot(x, y, 'k--', linewidth=3)
    plt.plot(x, y1, 'm-.')
    plt.plot(x, y2, color='#87a3cc', linestyle='--')

    # 使用xticks()和yticks()函数分别为每个函数传入两个值
    # 第一个列表存储刻度的位置，第二个列表存储刻度的标签
    plt.xticks([-2 * np.pi, -np.pi, 0, np.pi, 2 * np.pi],
               [r'$-2\pi$', r'$-\pi$', r'$0$', r'$+\pi$', r'$+2\pi$'])

    plt.yticks([-1, 0, +1, +2, +3],
               [r'$-1$', r'$0$', r'$+1$', r'$+2$', r'$+3$'])

    # annotate()函数适用于添加注释
    plt.annotate(r'$\lim_{x\to 0}\frac{sin(x)}{x} = 1$', xy=[0, 1], xycoords='data',
                 xytext=[50, 100], fontsize=22, textcoords='offset points',
                 arrowprops=dict(arrowstyle="->",
                                 connectionstyle="arc3,rad=.2"))

    # 显示笛卡尔坐标，使用gca()函数获取axes对象，指定每条边的上下左右
    # set_color() 设置颜色
    # set_position() 移动跟x轴和y轴相符合的边框，使其穿过远点（0,0）
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))

    plt.show()

def DataFrame_plot():
    data = {'series1':[1, 2, 4, 2, 5],
            'series2': [1, 3, 3, 4, 5],
            'series3': [1, 1, 2, 2, 5]}
    df = pd.DataFrame(data)
    x = np.arange(5)
    plt.axis([0,5,0,7]) #设置轴边界
    plt.plot(x,df)
    plt.legend(data,loc=2) #设置图标签
    print(df)
    print(x)
    plt.show()
DataFrame_plot()