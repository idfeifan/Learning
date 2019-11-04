# coding=utf-8

import  csv
filename = r'E:\Pwork\Learning\Python从入门到实践\项目\下载数据\data\death_valley_2018_full.csv'
with open(filename) as file:
    reader = csv.reader(file)
    header_row = next(reader)

    for index,column_header in enumerate(header_row):
        print(index,column_header)
