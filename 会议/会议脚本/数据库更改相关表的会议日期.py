#coding=utf-8
#说明：根据会议id去更改任务表action_task的planStartTime,planEndTime字段日期为当前日期，
# 但是不会更改时间，比如计划开始时间是2020-03-06 10:20:00，只会更改2020-03-06为当前天
#还会根据action_task的sourceId,taskSourceType值，来判断是去改总部还是区域表的planStartTime,planEndTime字段日期为当前日期
#并且也根据action_task的sourceId,taskSourceType值，去更改议程表time字段日期
#(265680,265681,265682,265683,265684,265685)
import pymysql
from datetime import datetime
now_date = datetime.now()
now_date_str = now_date.strftime("%Y-%m-%d %H:%M:%S")[:10] #要改成的日期
py_action = pymysql.connect(host="192.168.8.122",user="xgjk_w",password="xgjk@2019",database="cms_action",charset="utf8")
py_act = pymysql.connect(host="192.168.8.122",user="xgjk_w",password="xgjk@2019",database="cms_act",charset="utf8")

action_table = py_action.cursor()
act_table = py_act.cursor()

meetId = input("请输入会议id：")
sql_1 = "select planStartTime,planEndTime,sourceId,taskSourceType from cms_action.action_task where id=(select taskId from cms_action.action_meet where id={});".format(int(meetId))

action_table.execute(sql_1)
action_task_data = action_table.fetchall()[0]
planStartTime,planEndTime = action_task_data[0].strftime("%Y-%m-%d %H:%M:%S")[10:],action_task_data[1].strftime("%Y-%m-%d %H:%M:%S")[10:] #获取任务表的计划开始时间和计划结束时间
planStartTime_1 = now_date_str + planStartTime
planEndTime_1 = now_date_str + planEndTime
sourceId = action_task_data[2]
taskSourceType = action_task_data[3] #HQ_ACT 总部活动
print("修改后计划开始时间：{}；修改后计划结束时间：{}".format(planStartTime_1,planEndTime_1))

sql_2 = 'update action_task set planStartTime="{}",planEndTime="{}" where id=(select taskId from action_meet where id={});'.format(planStartTime_1,planEndTime_1,int(meetId))
action_table.execute(sql_2)
if taskSourceType=="HQ_ACT":
    """修改活动表的时间"""
    hq_sql_l = 'update act_hq set planStartTime="{}",planEndTime="{}" where id={};'.format(planStartTime_1,planEndTime_1,sourceId)
    act_table.execute(hq_sql_l)
    """修改议程表的时间"""
    hq_sql_2 = 'update act_agenda_session set time="{}" where agendaId=(select id from cms_act.act_agenda where activityType="HEADQUARTERS" and sourceId={});'.format(now_date_str,sourceId)
    act_table.execute(hq_sql_2)

elif taskSourceType=="AREA_ACT": #AREA_ACT区域活动
    """修改活动表的时间"""
    hq_sql_l = 'update act_area set planStartTime="{}",planEndTime="{}" where id={};'.format(planStartTime_1,planEndTime_1, sourceId)
    act_table.execute(hq_sql_l)
    """修改议程表的时间"""
    hq_sql_2 = 'update act_agenda_session set time="{}" where agendaId=(select id from cms_act.act_agenda where activityType="AREA" and sourceId={});'.format(now_date_str, sourceId)
    act_table.execute(hq_sql_2)
else:
    print("不存在此种taskSourceType！")

py_action.commit() #事务提交
py_act.commit()
action_table.close() #关闭连接
act_table.close()
