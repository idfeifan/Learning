# coding=utf-8
from sklearn import datasets
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from sklearn.decomposition import PCA  #降低维度
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from matplotlib.colors import ListedColormap
'''鸾尾花数据绘制图'''
def iris():
    iris = datasets.load_iris()
    x = iris.data[:,2] #加载第一列数据
    y = iris.data[:,3]
    species = iris.target #显示花色种类

    x_min ,x_max = x.min() -0.5,x.max() +0.5
    y_min, y_max = y.min() - 0.5, y.max() + 0.5

    plt.figure()
    plt.title('Iris Dataset - Classification By Sepal Sizes',size=16)
    plt.scatter(x,y,c=species)
    plt.xlabel('Sepal length')
    plt.ylabel('Sepal width')
    plt.xlim(x_min,x_max)
    plt.ylim(y_min,y_max)
    plt.xticks(())
    plt.yticks(())
    plt.show()
'''主成分分解，降维'''
def zcffj():
    iris = datasets.load_iris()
    x = iris.data[:,1]
    y = iris.data[:,2]
    species = iris.target
    #PCA参数n_components降低维度到多少fit_tran
    x_reduced = PCA(n_components=3).fit_transform(iris.data)
    print(x_reduced)
    print(iris)
    #绘制3D图
    fig =plt.figure()
    ax =Axes3D(fig)
    ax.set_title('Iris Dataset by PAC',size = 14)
    ax.scatter(x_reduced[:,0],x_reduced[:,1],x_reduced[:,2],c=species)
    ax.set_xlabel('First eigenvector')
    ax.set_ylabel('Second eigenvector')
    ax.set_zlabel('Third eigenvector')
    ax.w_xaxis.set_ticklabels(())
    ax.w_yaxis.set_ticklabels(())
    ax.w_zaxis.set_ticklabels(())
    plt.show()
'''K-邻近分类 KNN算法
导入KneighborsClassifier
    打乱数据集，使用前149条用作训练集，剩余10条用作测试'''
def KNN():
    np.random.seed(0)
    iris = datasets.load_iris()
    x = iris.data
    y = iris.target
    i = np.random.permutation(len(iris.data)) #打乱数据，i中存储的记录数据的位置

    x_train = x[i[:-10]] #取140条数据
    y_train = y[i[:-10]]
    x_test = x[i[-10:]]
    y_test = y[i[-10:]]

    knn = KNeighborsClassifier()
    knn.fit(x_train,y_train) #对140调数据进行knn分类器训练，得到预测模型
    #使用predict()函数进行预测结果与y_test中的实际值进行比较
    y_predict = knn.predict(x_test)
    #将y_predict 于y_test数据进行比较
'''决策边界'''
def jcbj():
    iris = datasets.load_iris()
    x = iris.data[:,:2]
    y = iris.target

    x_min, x_max = x[:,0].min() -.5 ,x[:,0].max() +.5
    y_min, y_max = x[:,1].min() -.5 ,x[:,1].max() +.5

    cmap_light = ListedColormap(['#AAAAFF','#AAFFAA','#FFAAAA'])
    h = 0.02
    #获取两个坐标点
    xx,yy=np.meshgrid(np.arange(x_min,x_max,h),np.arange(y_min,y_max,h))
    knn = KNeighborsClassifier()
    knn.fit(x,y) #进行训练的函数

    Z = knn.predict(np.c_[xx.ravel(),yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.figure()
    plt.pcolormesh(xx,yy,Z,cmap = cmap_light)

    plt.scatter(x[:,0],x[:,1],c=y)
    plt.xlim(xx.min(),xx.max())
    plt.ylim(yy.min(),yy.max())
    plt.show()







jcbj()