import pymysql,copy
from datetime import datetime

doctor_list = [
    {"doctorId":"201709444226","openId":"da6a695008a14600bf1f44b3312ea9fe"},
    {"doctorId":"201709173403","openId":"8447c97d8838442fb007e868e84caab6"},
    {"doctorId":"201503290066","openId":"f62c34538e3149e58db115d63163ffd0"},
    {"doctorId":"201709443545","openId":"7dc325494af04fb7ad0ccf68499253c0"}
               ]
action = pymysql.connect(host="192.168.8.122",user="xgjk_w",password="xgjk@2019",database="cms_action",charset="utf8")
action_cursor = action.cursor()

sql_1 = "select id as a from cms_action.contract_browse_doctor order by id desc limit 1;"  #查询医生浏览表中最大的id
action_cursor.execute(sql_1)
max_id = action_cursor.fetchall()[0][0]
com_id = copy.copy(max_id)

meetid = input("请输入会议id：")
sql_2 = "select bizId,bizType,contractId from contract_dachen_relate where valid=1 and meetId={};".format(meetid)#同步大辰内容表
action_cursor.execute(sql_2)
dachen_detail = action_cursor.fetchall()[0]
for doctor in doctor_list:
    max_id +=1
    sql_3 = "INSERT into cms_action.contract_browse_doctor " \
            "(id,version,meetId,contractId,doctorId,openId,longTime,firstTime,bizId,bizType,updateTime,createTime) " \
            "VALUES({}, 0, {},{},{}, '{}', 25,now(),'{}',{},now(),now());"\
        .format(max_id,meetid,dachen_detail[2],doctor["doctorId"],doctor["openId"],dachen_detail[0],dachen_detail[1])
    action_cursor.execute(sql_3)
action.commit()  # 事务提交
sql_1 = "select id as a from cms_action.contract_browse_doctor order by id desc limit 1;"
action_cursor.execute(sql_1)
max_id = action_cursor.fetchall()[0][0]

if max_id==com_id+4:
    print("插入成功！")
else:
    raise Exception('print("插入失败！")')  #Exception('print("插入失败！")')注意这两个的区别，这个带字符串，直接打印字符串里的内容，python把字符串的内容一字不差解析成了异常并打印出来


action_cursor.close()  # 关闭连接

