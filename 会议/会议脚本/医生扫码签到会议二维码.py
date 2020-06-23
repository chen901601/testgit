import requests,json,sys
import pymysql,random

py = pymysql.connect(host="192.168.8.122",user="xgjk_w",password="xgjk@2019",database="cms_customer",charset="utf8")
action = pymysql.connect(host="192.168.8.122",user="xgjk_w",password="xgjk@2019",database="cms_action",charset="utf8")
py_table = py.cursor()
py_action = action.cursor()

sign_name = ["凌素芬","凌小小","黄小乐","黄小可"]  #签到人员列表
sign_name_openid = []  #签到人员的openid列表
change_sign_name =input("默认签到的医生名单为：{}；\n如需要改动，"
                 "请重新输入医生名字，医生与医生之间使用中文的“，”隔开，不需要改动签到医生名单的请回车：\n".format(sign_name))


if change_sign_name!="":
    sign_name = change_sign_name.split("，")

name_null_openid = [] #用来存放opneid为空的医生名字
for name in sign_name:
    sql = "select id,name,openId from cms_customer.basic_doctor where name='{}' and openId is not null limit 1;".format(name)
    py_table.execute(sql)
    row_value = py_table.fetchall()
    row_value = list(row_value)  #强制转换格式，因为fetchall得到的tuple类型不能做判断，且fetchone得到的值可以做判断，但是不能对返回的数据做处理，比如不能取数
    if row_value:
        sign_name_openid.append(row_value[0][2])
    else:
        name_null_openid.append(name)
py_table.close()
if name_null_openid:
    name_str = "，".join(name_null_openid)
    if len(name_null_openid)==len(sign_name):
        print("输入需要签到的医生openid都为空，请重新执行脚本！")
        sys.exit()
    sure_code = input("{}医生的openid为空，为空的将不会进行签到操作，请确认是否继续？继续请回车，退出请输入任意键后回车：\n".format(name_str))
    if sure_code:
        sys.exit()



while 1:
    meetid = input("请输入需要签到的会议id：\n")
    if meetid:
        break
meet_type_sql = "select meetType,endTime from action_meet where id={};".format(meetid)
py_action.execute(meet_type_sql)
result = py_action.fetchall()
result = list(result)
if result==[]:
    print("会议id={}的会议不存在，不能进行接口签到操作！".format(meetid))
    sys.exit()

result = result[0]
meet_type = result[0]
endTime_state = result[1]
py_action.close()

#MEET_OUT_ONLINE("外部会议线上"),
#MEET_OFF_ONLINE("外部会议线下");
#MEET_DOCTOR_ORG("医生圈会议");
if meet_type!="MEET_OUT_OFFLINE":
    print("该会议不是线下会议，不能进行接口签到操作！")
    sys.exit()
elif endTime_state:
    print("该会议已经结束，不能进行接口签到操作！")
    sys.exit()



#MedicalCircle/1.13.1/031/android/Xiaomi_MI 6  医生圈版本：1.13.1，Android系统的小米手机
"""使用小米手机签到的数据"""
phone_system_xiaomi = "DachenJsBridge/MedicalCircle/1.13.1/031/android/Xiaomi_MI 6/Xiaomi/sagit/sagit:8.0.0/OPR1.170623.027/V10.0.1.0.OCACNFH:user/release-keys/mobile/DachenApp/MedicalCircle/1.13.1/031/android/Xiaomi_MI 6/Xiaomi/sagit/sagit:8.0.0/OPR1.170623.027/V10.0.1.0.OCACNFH:user/release-keys/mobile"
signMacId_xiaomi = "WcC3QEoi1G4DAEm1E7PgAXK1"
"""使用oppo手机签到的数据"""
phone_system_oppo_R11 = "DachenJsBridge/MedicalCircle/1.13.1/031/android/OPPO_OPPO R11/R11_11_A.52_191224/mobile/DachenApp/MedicalCircle/1.13.1/031/android/OPPO_OPPO R11/R11_11_A.52_191224/mobile"
signMacId_oppo_R11 = "Wb5CQ4mPOLsDAPEl96AMCTSQ"

"""存储手机信息的字典"""
phone_data ={"xiaomi": [phone_system_xiaomi,signMacId_xiaomi], "oppo_R11": [phone_system_oppo_R11,signMacId_oppo_R11]}
"""存储手机类型列表，用来随机抽取"""
phone_list = ["xiaomi","oppo_R11"]

def sign_fun():
    """请求方式POST"""
    sign_url = "https://test-ms.xgjk.info/cms-action-service/public/meet/sign"
    for name_openid in sign_name_openid:
        phone = random.choice(phone_list)
        # print(phone_data[phone][0])
        # print(phone_data[phone][1])
        sign_headers ={
                    "Host": "test-ms.xgjk.info",
                    "Connection": "keep-alive",
                    "Content-Length": "171",
                    "Accept": "application/json, text/plain, */*",
                    "Origin": "http://test-app.xgjk.info",
                    "User-Agent": phone_data[phone][0],
                    "Content-Type": "application/json;charset=UTF-8",
                    "Referer": "http://test-app.xgjk.info/",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,en-US;q=0.9",
                    "X-Requested-With": "com.dachen.medicalcircle"
                    }

        data_xiaomi = {
                    "openId": name_openid,
                    "signMacId":phone_data[phone][1],
                    "meetId": meetid,
                    "partnerType":"DoctorOrg",
                    "userLevel":"3",
                    "latitude":0,
                    "longitude":0
                     }

        req_sign_detail = requests.post(url=sign_url,headers=sign_headers,data=json.dumps(data_xiaomi)).text
        print(req_sign_detail)

if __name__=="__main__":
    sign_fun()