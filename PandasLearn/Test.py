# coding=utf-8
import numpy as np
import pandas as pd
import pickle as pk


# frame = pd.DataFrame(np.random.random((4,4)),
#                    index=['exp1','exp2','exp3','exp4'],
#                   columns =['jan2015','fab2015','mar2015','apr2005'])
# pd.read_excel
# frame.to_excel
def t_json():
    frame = pd.DataFrame(np.arange(16).reshape(4,4),
                         index=['white','black','red','blue'],
                         columns=['up','down','right','left'])
    frame.to_json('frame.json')

def r_json():
    frame2 = pd.read_json("frame.json")
    print(frame2)

def mege():
    data = {'id':['ball','pencil','pen','mug','ashtray'],
            'price':[12.33,11.44,22.21,12.34,33.64]}
    data2 = {'id':['pencil','pencil','ball','pen'],
            'price':['white','red','red','black']}
    frame1 = pd.DataFrame(data)
    frame2 = pd.DataFrame(data2)
    pd.merge(frame1,frame2)   # join 通过id列

def test():
    L = [1,2,4,8,16,32,64]
    i=0
    while 2 **5 != L[i] and i<len(L):
        i = i+1
    else:
        print(L[i])
test()


