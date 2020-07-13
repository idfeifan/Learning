#!/bin/bash
#DWD目标表
hive_dwd_table=DWD_STHJJ.DWD_STHJJ_KQZLZS_A
echo  $hive_dwd_table ;
#ODS源表
hive_ods_table=ODS_STHJJ.ODS_STHJJ_KQZLZS
echo $hive_ods_table;
#日志信息表
hive_log_table=DWD_DSJGLJ.DWD_ETL_TABLES_LOG
echo $hive_log_table;
#判读是否传入日期参数，如果传入则使用传入的日期，没有则使用$date_time
if [ ! -n "$1" ] ;then
    date_time=$(date -d "yesterday" +%Y%m%d)
    etl_time_field=$(date -d "$date_time 1 days ago" +%Y%m%d)

    drop_date=$(date -d "$date_time 7 days ago" +%Y%m%d)

    echo "=======================没有传入日期参数=============================="
    echo "echo $date_time "
    echo "echo $etl_time_field "
    echo "echo $drop_date"

else    date_time=$1
    etl_time_field=$(date -d "$date_time 1 days ago" +%Y%m%d)

    drop_date=$(date -d "$date_time 7 days ago" +%Y%m%d)

    echo "=======================传入日期参数=============================="
    echo "echo $date_time "
    echo "echo $etl_time_field "
    echo "echo $drop_date"
fi
#创建分区
 hive -e "alter TABLE $hive_dwd_table  add if not exists  partition(etl_time_field=$date_time)"


 #输出开始时间到日志
start_time=$(date "+%Y-%m-%d %H:%M")
#   echo $start_time>>/home/hadoop/app/sh/date_log/$hive_table$MYDATE.log;
#echo"$MYDATE" >> /home/hadoop/app/sh/date_log/fnd_flex_values$MYDATE.log;

#取历史没有变化数据与ODS最新数据合并，插入DWD表形成最新周期数据 
hive -e  "insert  overwrite table   $hive_dwd_table  partition(etl_time_field=$date_time )
  select    
a.co,
a.coa24,
a.zdbm,
a.iaqi,
a.id,
a.no2,
a.no2a24,
a.o3,
a.o3ma8,
a.pm10a24,
a.pm25a24,
a.pm25a24max,
a.rq,
a.so2,
a.so2a24,
a.zdmc,
a.data_source ,
a.insert_date ,
a.etl_flag_field

  from  (select * from   $hive_dwd_table 
where   etl_time_field=$etl_time_field )a
 LEFT JOIN 
 ( select
ID
  from       $hive_ods_table
 where dt=$date_time 
)  b
 on a.ID=b.ID where b.ID is null 
 union all  
select  
CO  CO,
COA24  COA24,
CODE  ZDBM,
IAQI  IAQI,
ID  ID,
NO2  NO2,
NO2A24  NO2A24,
O3  O3,
O3MA8  O3MA8,
PM10A24  PM10A24,
PM25A24  PM25A24,
PM25A24MAX  PM25A24MAX,
RQ  RQ,
SO2  SO2,
SO2A24  SO2A24,
STATION      ZDMC,
'ODS_STHJJ'   DATA_SOURCE,
from_unixtime(unix_timestamp(),'YYYY-MM-dd HH:mm:ss')   INSERT_DATE,
 ETL_FLAG_FIELD   ETL_FLAG_FIELD
    from       $hive_ods_table
  
where dt=$date_time ;";


#判断上面的插入操作是否成功
if [ $? -ne 0 ]; then
    status_job="执行失败"
    echo $status_job
else
    status_job="执行成功"
     echo $status_job
    hive -e "alter table $hive_dwd_table drop if exists partition(etl_time_field=$drop_date)";
fi



#输出结束时间到日志中
end_time=$(date "+%Y-%m-%d %H:%M")
 echo $end_time  
echo "====================================开始输出日志信息======================================="

echo $start_time,$end_time,$hive_dwd_table,$hive_ods_table,$status_job;


#输出日志信息到日志表中
hive -e "insert into $hive_log_table(job_name,target_table,source_table,start_time,end_time,status,expmessage,data_size)
VALUES('${hive_dwd_table}','${hive_dwd_table}','${hive_ods_table}','${start_time}','${end_time}','$status_job','null','null');";



