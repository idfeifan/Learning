# coding=UTF-8
import os
import shutil
import pandas as pd
def copyFile(dr = r'C:\Users\35807\Desktop\脚本'):
    df = pd.read_excel('C:\\Users\\35807\\Desktop\\dwd.xlsx',sheet_name='Sheet1',header=None)
    p_col=['table']
    df.columns=p_col
    list = []
    for root,dirs,files in os.walk(dr):
        #遍历文件
        for file in files:
            #切割文件名称和类型
            f=os.path.splitext(file)
            filename,type = f
            if type == '.sh':
                list.append(filename)
    for idx in df.index:
        res = df.loc[idx,'table'].strip() in list
        if res == True:
            source = os.path.join(r"C:\Users\35807\Desktop\脚本",df.loc[idx,'table'].strip() + type)
            shutil.copy(source, r'C:\Users\35807\Desktop\bak')

def modifyfile(dr= r'C:\Users\35807\Desktop\bak'):
    list = []
    for root,dirs,files in os.walk(dr):
        #遍历文件
        for file in files:
            #切割文件名称和类型
            pathfile = os.path.join(dr,file)
            with open(pathfile, 'rb') as f:
                lines = f.read().decode('utf-8')
            new_lines = lines.replace('date_time=$(date -d "yesterday" +%Y%m%d)','date_time=$(date +%Y%m%d)')
            with open(pathfile,'w') as f2:
                    f2.write(new_lines)
if __name__ == '__main__':
    copyFile()
    modifyfile()