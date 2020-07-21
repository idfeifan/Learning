
import os
import chardet
'''
@Time : 2020/7/18 14:28
# @Author : liufeifan
# @Describe: 检查 脚本文件 转换格式为 LF , utf-8
'''
def turn(file):
    #打开文件
    with open(file, 'rb') as f:
        data = f.read()
        encoding = chardet.detect(data)['encoding']
        data_str = data.decode(encoding)
        tp = 'LF'
        if '\r' in data_str:
            tp = 'Macintosh(CR)'
            data_str = data_str.replace('\r', '\n') #替换为unix 格式
        if encoding not in ['utf-8', 'ascii'] or tp == 'Macintosh(CR)':
            with open(file, 'w', newline='\n', encoding='utf-8') as f:
                f.write(data_str)  #替换为unix 格式，并且转换格式为utf-8
            print(f"{file}: ({tp},{encoding}) trun to (LF,utf-8) success!")
if __name__ == "__main__":
    dr = r'C:\Users\35807\Desktop\bak'
    #root 表示上级目录， dirs，files内在文件和目录的列表，如果目录下文件为空，则files为空列表
    for root,dirs,files in os.walk(dr):
        #遍历文件
        for file in files:
            #切割文件名称和类型
            f=os.path.splitext(file)
            filename,type = f
            #判断文件是为.sh结尾文件
            if type == '.sh':
                #拼接文件
                file_name = os.path.join(root,file)
                turn(file_name)