#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2019/12/2 11:22
# @Author : way
# @Site :
# @Describe: 检查 脚本文件 转换格式为 LF , utf-8

import sys
import os
import chardet

def turn(file):
    with open(file, 'rb') as f:
        data = f.read()
        encoding = chardet.detect(data)['encoding']
        data_str = data.decode(encoding)
        tp = 'LF'
        if '\r' in data_str:
            tp = 'Macintosh(CR)'
            data_str = data_str.replace('\r', '\n')
        if encoding not in ['utf-8', 'ascii'] or tp == 'Macintosh(CR)':
            with open(file, 'w', newline='\n', encoding='utf-8') as f:
                f.write(data_str)
            print(f"{file}: ({tp},{encoding}) trun to (LF,utf-8) success!")
if __name__ == "__main__":
    dr = r'D:\SVN\产品线\数据治理\南通市社会治理现代化指挥中心数据资源库建设项目\项目实施资料\hive开发\20200702MySql迁移\市政园林局\wu'
    for path in os.listdir(dr):
        file = os.path.join(dr, path)
        turn(file)