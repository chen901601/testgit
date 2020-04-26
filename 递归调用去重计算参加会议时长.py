#coding=utf-8
import pymysql,copy
from datetime import datetime,timedelta

py_action = pymysql.connect(host="192.168.8.122",user="xgjk_w",password="xgjk@2019",database="cms_action",charset="utf8")
action_table = py_action.cursor()
sql = "select joinTime,unJoinTime,id from action_meet_telecon_detail where memberOpenId='9db038256a8e4115b455c23e1d201566';"
action_table.execute(sql)
result = action_table.fetchall()
time_list = []

for i in result:
    singel_list = (i[0],i[1])
    time_list.append(singel_list)

def cacult_time(time_list):
    start_time_number = 0
    interval_time_list = []
    time_number = len(time_list)
    time_list_1 = sorted(time_list,reverse = False)
    time_list_1.append((time_list_1[-1][1]+timedelta(minutes=1),time_list_1[-1][1]+timedelta(minutes=2)))
    for index in range(0,time_number):
        if time_list_1[index][1]<time_list_1[index+1][0]: #判断所有时间段中有开始时间>结束的时间的
            every_time_list = []
            for num in range(start_time_number,index+1):
                every_time_list.append(time_list_1[num])
            every_time_list = sorted(every_time_list,key=lambda x:x[1],reverse=True)
            interval_time_list.append((time_list_1[start_time_number][0],every_time_list[-1][1]))
            start_time_number = index+1

    """下行代码是因为time_list_1也增加了一段最面的时间，为了能使最终两个时间列表一致，所以interval_time_list也要加上"""
    # time_list_2 = copy.deepcopy(interval_time_list)
    interval_time_list.append((interval_time_list[-1][1]+timedelta(minutes=1),interval_time_list[-1][1]+timedelta(minutes=2)))
    if time_list_1!=interval_time_list:  #一直排到没有交叉的时间段
        del (interval_time_list[-1])  # 去掉列表最后一个元素，保留原生数据，因为为了便于if判断，上面将interval_time_list手动添加了一个元素
        interval_time_list = cacult_time(interval_time_list)
    return interval_time_list

finall_list = cacult_time(time_list)
del(finall_list[-1]) #去掉列表最后一个元素，还原原生数据，因为定义函数cacult_time是递归调用，但是要是没有递归调用cacult_time，就不会还原原生数据，所以在这里要还原一次
totle_time = datetime.now()-datetime.now() #赋值一个为0的时间变量
for date in finall_list:
    totle_time +=date[1]-date[0]

totle_time = str(totle_time)
nn = totle_time.find(":")
mm = totle_time.rfind(":")
h = totle_time[0:nn]
min = totle_time[nn+1:mm]
s = totle_time[mm+1:]
print(totle_time)
print(int(h)*60+int(min)+int(s)/60)