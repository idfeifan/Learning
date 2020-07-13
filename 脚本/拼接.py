import pandas as pd
import os
import re
#demo
def roll():
    df= pd.read_excel(r'C:\Users\35807\Desktop\南通市社会治理现代化指挥中心数据资源库建设_技术规则.xlsx',sheet_name='技术规则')
    print(df.loc[0,'指标分类*'])
    for idx in df.index:
        if df.loc[idx,'指标分类*']=='有效性':
            df.loc[idx,'全量文本错误条件'] = '更新这条内容'
            print(df.loc[idx,'全量文本错误条件'])
    file_name= "test.xls"
    if os.path.exists(file_name):
        os.remove(file_name)
    df.to_excel(file_name,sheet_name='技术规则',index=False,header=True)
def temp(file_name):
    '''
    字符串中存在，两处，要求替换最后一次出现的情况
    :param file_name:
    :return: 生成新的excle
    '''
    path = r"C:\Users\35807\Desktop\result-0712.xlsx"
    df= pd.read_excel(path,sheet_name='Sheet1')
    print(df.loc[0,'Index_class'])
    for idx in df.index:
        if df.loc[idx,'Index_class']=='有效性':
            a = df.loc[idx,'Fault_condition']
            result = a[::-1]
            strinfo = re.compile(r"\)'MMYYYY',\)\(pmatsemit_xinu\(emitxinu_morf")

            b = strinfo.sub('99',result,1)
            result = b[::-1]
            df.loc[idx,'Fault_condition'] = result
            #df.loc[idx,'All_sql'] = '更新这条内容'

            #修改Fault_sql
            a = df.loc[idx,'Fault_sql']
            result = a[::-1]
            strinfo = re.compile(r"\)'MMYYYY',\)\(pmatsemit_xinu\(emitxinu_morf")
            b = strinfo.sub('99',result,1)
            result = b[::-1]
            df.loc[idx,'Fault_sql'] = result
    if os.path.exists(file_name):
        os.remove(file_name)
    df.to_excel(file_name,sheet_name='技术规则',index=False,header=True)
#电话sql修改，正则匹配错误脚本，并进行替换
def PhoneSubstr(path):
    df= pd.read_excel(path,sheet_name='技术规则')
    l = list()
    print(df.loc[0,'Index_class'])
    for idx in df.index:
        if df.loc[idx,'Index_class']=='有效性':
            a = df.loc[idx,'Fault_condition']
            b = df.loc[idx,'Fault_sql']
            #a= r'''case when nvl(PHONENUM,'') REGEXP  "^((\d{2,3})-)(\d{7,8})(-(\d{3,4}))?$" =false'''
            #print(r'''case when nvl((.*?),'') REGEXP  "^((\d{2,3})-)(\d{7,8})(-(\d{3,4}))?$" =false''')
            strinfo = re.compile(r'''case when (.*?) REGEXP  "\^\(\(\\d\{2,3}\)-\)\(\\d\{7,8\}\)\(-\(\\d\{3,4}\)\)\?\$" =false''')
            zd= strinfo.findall(a)
            strinfo2 = re.compile(r'''case when ''' + zd[0] + r''' REGEXP  "\^\(\(\\d\{2,3}\)-\)\(\\d\{7,8\}\)\(-\(\\d\{3,4}\)\)\?\$" =false''')
            source = r'''case when''' + zd[0] + r''' REGEXP  "^((\d{2,3})-)(\d{7,8\})(-(\d{3,4}))?$" =false'''
            target = "case when translate(nvl("+str(zd[0])+r",''),'0123456789-','') <>''"

            a_1 = strinfo2.sub(target,a,1)
            #print(type(source))
            df.loc[idx,'Fault_condition'] = a_1
            strinfo_b = re.compile(r'''case when ''' + zd[0] + r''' REGEXP  "\^\(\(0\\d\{2,3}\)-\)\(\\d\{7,8\}\)\(-\(\\d\{3,4}\)\)\?\$" =false''')

            b_1 = strinfo_b.sub(target,b,1)
            df.loc[idx,'Fault_sql'] = b_1

    if os.path.exists('result-0713.xlsx'):
        os.remove('result-0713.xlsx')
    df.to_excel('result-0713.xlsx',sheet_name='技术规则',index=False,header=True)
#电话sql修改，正则匹配错误脚本，并进行替换
def PhoneSubstr2(path):
    df= pd.read_excel(path,sheet_name='技术规则')
    for idx in df.index:
        if df.loc[idx,'Index_class']=='有效性':
            Fault_condition = df.loc[idx,'Fault_condition']
            Fault_sql = df.loc[idx,'Fault_sql']
            task_id = df.loc[idx,'task_id']
            strinfo = re.compile(r'''case when (.*?) REGEXP "\^\(\(13\[0-9]\)\|\(147\)\|\(15\[0-9]\)\|\(166\)\|\(173\)\|\(17\[5-8]\)\|\(18\[0-9\]\|\(19\[0-9\]\)\)\)\\d\{8\}\$" =FALSE''')
            columns= strinfo.findall(Fault_condition)
            print(columns)
            if list(columns)==0:
                print("task_id:" + task_id + ", 此任务脚本有问题，字段未提取出来")
            else:
                source = r'case when ' + columns[0] + r''' REGEXP "\^\(\(13\[0-9]\)\|\(147\)\|\(15\[0-9]\)\|\(166\)\|\(173\)\|\(17\[5-8]\)\|\(18\[0-9]|\(19\[0-9]\)\)\)\\d\{8}$" =FALSE'''
                target = 'case when translate(nvl(' + columns[0] + ",''),'0123456789','') <>''"
                pat = re.search(source,Fault_condition)
                print(pat)
                if pat == None:
                    print('task_id:'+str(task_id)+'，没有匹配到' )
                result_Fault_condition = strinfo.sub(target,Fault_condition)
                df.loc[idx,'Fault_condition'] = result_Fault_condition


                strinfo2 = re.compile(r'''case when (.*?) REGEXP "\^\(\(13\[0-9\]\)\|\(147\)\|\(15\[0-9\]\)\|\(166\)\|\(173\)\|\(17\[5-8\]\)\|\(18\[0-9]\)\|\(19\[0-9\]\)\)\\d\{8\}\$" =FALSE''')
                target = 'case when translate(nvl(' + columns[0] + ",''),'0123456789','') <>''"
                b_1 = strinfo2.sub(target,Fault_sql)
                df.loc[idx,'Fault_sql'] = b_1

    if os.path.exists('result-0713-1.xlsx'):
        os.remove('result-0713-1.xlsx')
    df.to_excel('result-0713-1.xlsx',sheet_name='技术规则',index=False,header=True)
def pk_check():
    df= pd.read_excel(r'C:\Users\35807\Desktop\南通市社会治理现代化指挥中心数据资源库建设_技术规则1.xlsx',sheet_name='主键校验')
    print(df.loc[0,'指标分类*'])
    for idx in df.index:
        db = df.loc[idx,'数据库名*']
        table = df.loc[idx,'表名*']
        column = df.loc[idx,'字段名称*']
        if df.loc[idx,'指标分类*']=='唯一性':
            df.loc[idx,'文本错误条件'] = '''SELECT aa.*
                                                from ''' + db + '''.''' + table + ''' aa ,
                                                (
                                                    select MAX(etl_time_field) etl_time_field,''' + column + '''
                                                from ''' + db + '''.''' + table + '''
                                                group by ''' + column + ''' having count(1)>1
                                                ) bb
                                                where aa.''' + column + '''=bb.''' + column + ''' and aa.etl_time_field=bb.etl_time_field'''
            df.loc[idx,'全量SQL'] = 'select count(1) from  '+db+'.'+table
            df.loc[idx,'错误SQL'] ='''SELECT count(1)
                                                from ''' + db + '''.''' + table + ''' aa ,
                                                (
                                                    select MAX(etl_time_field) etl_time_field,''' + column + '''
                                                from ''' + db + '''.''' + table + '''
                                                group by ''' + column + ''' having count(1)>1
                                                ) bb
                                                where aa.''' + column + '''=bb.''' + column + ''' and aa.etl_time_field=bb.etl_time_field'''
    file_name= "南通市社会治理现代化指挥中心数据资源库建设_技术规则_liuhu.xlsx"
    if os.path.exists(file_name):
        os.remove(file_name)
    df.to_excel(file_name,sheet_name='技术规则',index=False,header=True)
def time_check(path):
    df= pd.read_excel(path,sheet_name='时间格式检测')
    print(df.loc[0,'指标分类*'])
    for idx in df.index:
        db = df.loc[idx,'数据库名*']
        table = df.loc[idx,'表名*']
        column = df.loc[idx,'字段名称*']
        if df.loc[idx,'指标分类*']=='有效检查性':
            df.loc[idx,'文本错误条件'] = r'select * from '+r'('+ r"select *,REPORT_TIME regexp "+"""'([\d]{4}(((0[13578]|1[02])((0[1-9])|([12][0-9])|(3[01])))|(((0[469])|11)((0[1-9])|([12][1-9])|30))|(02((0[1-9])|(1[0-9])|(2[1-8])))))|((((([02468][048])|([13579][26]))00)|([0-9]{2}(([02468][048])|([13579][26]))))(((0[13578]|1[02])((0[1-9])|([12][0-9])|(3[01])))|(((0[469])|11)((0[1-9])|([12][1-9])|30))|(02((0[1-9])|(1[0-9])|(2[1-9])))))'  """ + column+ ' from ' + str(db) + '.' + str(table) + ') a  where a.' + str(column) + '=false'
            df.loc[idx,'全量SQL'] = 'select count(1) from '+db+'.'+table
            df.loc[idx,'错误SQL'] =r'select count(1) from '+r'('+ r"select *,REPORT_TIME regexp "+"""'([\d]{4}(((0[13578]|1[02])((0[1-9])|([12][0-9])|(3[01])))|(((0[469])|11)((0[1-9])|([12][1-9])|30))|(02((0[1-9])|(1[0-9])|(2[1-8])))))|((((([02468][048])|([13579][26]))00)|([0-9]{2}(([02468][048])|([13579][26]))))(((0[13578]|1[02])((0[1-9])|([12][0-9])|(3[01])))|(((0[469])|11)((0[1-9])|([12][1-9])|30))|(02((0[1-9])|(1[0-9])|(2[1-9])))))'  """ + column+ ' from ' + str(db) + '.' + str(table) + ') a  where a.' + str(column) + '=false'
    file_name= "南通市社会治理现代化指挥中心数据资源库建设_技术规则_ljb.xlsx"
    if os.path.exists(file_name):
        os.remove(file_name)
    df.to_excel(file_name,sheet_name='时间格式检测',index=False,header=True)
def lat_lng_check(path):
    df= pd.read_excel(path,sheet_name='经纬度')
    print(df.loc[0,'指标分类*'])
    for idx in df.index:
        db = df.loc[idx,'数据库名*']
        table = df.loc[idx,'表名*']
        column = df.loc[idx,'字段名称*']
        if df.loc[idx,'指标分类*']=='有效检查性':
            df.loc[idx,'文本错误条件'] = r'''select * from (select *,translate(JD,"\.",'') regexp '^[0-9]*$' ''' + column+ ''' from ''' + db + '''.''' + table + ''') a where a.''' + column+ '''=false'''
            df.loc[idx,'全量SQL'] = 'select count(1) from '+db+'.'+table
            df.loc[idx,'错误SQL'] =r'''select * from (select *,translate(JD,"\.",'') regexp '^[0-9]*$' ''' + column+ ''' from ''' + db + '''.''' + table + ''') a where a.''' + column+ '''=false'''
    file_name= "南通市社会治理现代化指挥中心数据资源库建设_技术规则_ljb_经纬度.xlsx"
    if os.path.exists(file_name):
        os.remove(file_name)
    df.to_excel(file_name,sheet_name='时间格式检测',index=False,header=True)

if __name__ == '__main__':
    path = r"C:\Users\35807\Desktop"
    file ='技术规则jb(1).xlsx'
    pathfile = os.path.join(path,file)
    print(pathfile)
    lat_lng_check(pathfile)


