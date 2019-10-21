# coding=utf-8
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
'''绘制z = f(x,y)三维曲面 plot_surface'''
def surface():
    fig = plt.figure()
    ax =Axes3D(fig)
    X= np.arange(-2,2,0.05)
    Y =np.arange(-2,2,0.05)
    X,Y =np.meshgrid(X,Y)
    def f(x,y):
        return (1 - y**5 + x**5)*np.exp(-x**2 -y**2)
    ax.plot_surface(X,Y,f(X,Y),rstride=1,cstride=1,
                    cmap=plt.cm.winter)
    ax.view_init(elev=30, azim=125) #初始视角设置
    plt.show()

'''3D散点图'''
def D_sdt():
    xs = np.random.randint(30,40,100)
    ys = np.random.randint(20, 30, 100)
    zs = np.random.randint(10, 20, 100)
    xs2 = np.random.randint(50, 60, 100)
    ys2 = np.random.randint(30, 40, 100)
    zs2 = np.random.randint(50, 70, 100)
    xs3 = np.random.randint(10, 30, 100)
    ys3 = np.random.randint(40, 50, 100)
    zs3 = np.random.randint(40, 50, 100)
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.scatter(xs,ys,zs)
    ax.scatter(xs2, ys2, zs2,marker='^')
    ax.scatter(xs3, ys3, zs3,marker='*')
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    plt.show()
D_sdt()