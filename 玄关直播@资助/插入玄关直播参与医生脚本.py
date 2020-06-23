import pymysql
from datetime import datetime

dragon_py = pymysql.connect(host="192.168.8.122",user="xgjk_w",password="xgjk@2019",database="dragon_action",charset="utf8")
dragon_cursor = dragon_py.cursor()
doctor_list = [[29,'10c9b122586b4dd5906886103f491c70',10],[11,'d9e556ce4e97435b9707184f291eb5f5',8],[4,'6accd2c9b015404da2e845c3d2ee4d62',7]]


def add_meetdoctor():
    taskId = input("请输入要插入的任务id：")
    find_taskid_sql = 'select count(*) from dragon_action.action_contract_live_doctor where taskId={};'.format(taskId)
    dragon_cursor.execute(find_taskid_sql)
    result_data = dragon_cursor.fetchall()[0][0]
    if result_data!=0:
        wirte_messge = input("任务id={}的直播已经在《与会医生表》存在{}条数据，请确认是否继续插入！\n继续请输入：1，停止请直接回车。\n".format(taskId,result_data))
        if wirte_messge!='1':
            exit()
    add_id_sql = 'select id from dragon_action.action_contract_live_doctor order by id desc limit 1;'#查找玄关直播参与医生表的最大id，用来创建时id赋值
    add_messge_sql = 'select contractId,bizId,bizType from dragon_action.action_contract_dachen where taskId={};'.format(taskId)  #查出玄关直播任务的关联直播信息
    dragon_cursor.execute(add_id_sql)
    add_id = dragon_cursor.fetchall()[0][0]
    dragon_cursor.execute(add_messge_sql)
    add_messge = dragon_cursor.fetchall()[0]
    for doctor_messge in doctor_list:
        add_id += 1
        inisert_sql = "INSERT into dragon_action.action_contract_live_doctor (id,version,taskId,contractId,doctorId,openId,longTime,firstTime,bizId,bizType) " \
                  "VALUES ({},0,{},{},{},'{}',{},now(),{},{});".format(add_id,taskId,add_messge[0],doctor_messge[0],doctor_messge[1],doctor_messge[2],add_messge[1],add_messge[2])
        dragon_cursor.execute(inisert_sql)
    dragon_py.commit()  # 事务提交
    dragon_cursor.close()  # 关闭连接

"""以下是数据库存储过程"""
# delimiter  //
# drop procedure if exists add_meetdoctor;
# create procedure add_meetdoctor(in taskid int)  #字符串类型的必须指定长度
# begin
# select id into c from action_contract_live_doctor order by id desc limit 1; #将查询到的id值赋给c
# set c=c+1;  #c自增1
# select bizId,contractId into a,b from action_contract_dachen where taskId=taskid;
# INSERT into action_contract_live_doctor (id,version,taskId,contractId,doctorId,openId,longTime,firstTime,bizId,bizType)VALUES (c,0,taskid,b,29,'10c9b122586b4dd5906886103f491c70',10,now(),a,1);
# set c=c+1;
# INSERT into action_contract_live_doctor (id,version,taskId,contractId,doctorId,openId,longTime,firstTime,bizId,bizType)VALUES (c,0,taskid,b,11,'d9e556ce4e97435b9707184f291eb5f5',9,now(),a,1);
# set c=c+1;
# INSERT into action_contract_live_doctor (id,version,taskId,contractId,doctorId,openId,longTime,firstTime,bizId,bizType)VALUES (c,0,taskid,b,4,'6accd2c9b015404da2e845c3d2ee4d62',8,now(),a,1);
# end
# //
# call add_meetdoctor(378);



if __name__=="__main__":
    add_meetdoctor()

"""根据直播活动和任务，查询主任务的id和直播活动的主题，并于查看需要插入参与医生的taskId是哪个直播主题"""
"""select a.id as taskId,b.topic from action_task a inner join dragon_act.support_apply b on b.id=a.sourceId and a.id=a.rootId and a.taskType='LIVE' order by b.createTime desc;"""