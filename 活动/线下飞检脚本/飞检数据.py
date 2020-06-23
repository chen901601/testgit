# coding=utf8
import requests, json, random, urllib.request
from datetime import datetime, timedelta
from time import sleep


activity_name = "飞检区域活动王娜接口造数据"

date = datetime.now()
date_datetime = date+timedelta(hours=2)
date_str=datetime.strftime(date_datetime,"%Y-%m-%d %H:%M:%S")
time_int = int(date_str[14:16])
if time_int%5!=0:
    if time_int<55:
        date_datetime = date_datetime+timedelta(minutes=(5-(time_int%5)))
        # print(date_datetime)
    else:
        date_datetime = date_datetime - timedelta(minutes=(time_int % 5))
        # print(date_datetime)

"""第一段议程开始时间"""
meet_time_one= date_datetime
meet_time1= datetime.strftime(meet_time_one,"%Y-%m-%d %H:%M:%S")
meet_time1 = meet_time1[11:16]
print("第一段议程的时间："+meet_time1)
"""第二段议程开始时间"""
meet_time_two= date_datetime+timedelta(minutes=30)
meet_time2= datetime.strftime(meet_time_two,"%Y-%m-%d %H:%M:%S")
meet_time2 = meet_time2[11:16]
print("第二段议程的时间："+meet_time2)
"""第三段议程开始时间"""
meet_time_three= date_datetime+timedelta(minutes=60)
meet_time3= datetime.strftime(meet_time_three,"%Y-%m-%d %H:%M:%S")
meet_time3 = meet_time3[11:16]
print("第三段议程的时间："+meet_time3)
"""第西段议程开始时间"""
meet_time_four= date_datetime+timedelta(minutes=90)
meet_time4= datetime.strftime(meet_time_four,"%Y-%m-%d %H:%M:%S")
meet_time4 = meet_time4[11:16]
print("第四段议程的时间："+meet_time4)
"""第五段议程开始时间"""
meet_time_five= date_datetime+timedelta(minutes=120)
meet_time5= datetime.strftime(meet_time_five,"%Y-%m-%d %H:%M:%S")
meet_time5 = meet_time5[11:16]
print("第五段议程的时间："+meet_time5)

"""把datetime转成字符串 :statrtime.strftime("%Y-%m-%d %H:%M:%S")"""
date = date.strftime("%Y-%m-%d %H:%M:%S")
print("当前日期为："+date)

plandate = date[0:10]
print("创建的活动开会日为："+plandate)

"""下列代表用例来判断最后一段议程的时间超过当前天的，因为每段议程的时间是上一段议程的时间+30分钟，有可能到最后一段议程就超一天了"""
plan_date = datetime.now()+timedelta(days=1)
plan_date = datetime.strftime(plan_date, "%Y-%m-%d %H:%M:%S")[0:10]
plan_date = plan_date+" 00:00:00"
plan_date = datetime.strptime(plan_date,"%Y-%m-%d %H:%M:%S")
print(plan_date)
if meet_time_five>plan_date:
    print("最后一段议程的日期已经超过当前天了，请手动添加")
    exit()



def APP_token(username, password='888888'):
    """作用：根提供的账号密码获取APP-token"""
    """请求方式:POST"""
    app_token_url = 'https://test-ms.xgjk.info/cms-auth/auth/app/login'
    request_headers = {'Accept': 'application/json, text/plain, */*',
                       'Content-Type': 'application/json;charset=UTF-8',
                       }
    param_fram = {"username": username,
                  "password": password,
                  "isBind": "NO"}
    request = requests.post(url=app_token_url, headers=request_headers, data=json.dumps(param_fram)).text
    response = json.loads(request)
    value = response.get('value')
    token = value.get('token')
    # print(token)
    return token

def creat_action(username):#ua0000000416
    if username[9:]!="416":
        print('使用造数据账号不是王娜，请修改"headEmployeeId"和"headEmployeeName"字段值后，再屏蔽该提示语判断条件后再执行脚本！')
        exit()
    action_type_url = "https://test-ms.xgjk.info/cms-act-service/act/basic/activityClass/getById?activityClassId=375"
    action_url = 'https://test-ms.xgjk.info/cms-act-service/act/area/app/save'
    token = APP_token(username)
    headers = {"Accept": "application/json,text/plain, */*",
                     "Content-Type": "application/json;charset=UTF-8",
                     "Authorization": token
                     }

    type_req = requests.get(url=action_type_url, headers=headers).json()
    needSponsor = type_req["needSponsor"]  # True 需要
    projectPeopleChooseType = type_req["projectPeopleChooseType"]  # NO_CHOOSE 不需要选择  GEN_CHOOSE 可选 MUST_CHOOSE 必选

    """承办方、主办方"""
    if needSponsor:
        print("主办方、承办方必填")
        sponsorIds = [61]  # 主办方
        contractorIds = [61]  # 承办方
    else:
        print("主办方、承办方不需要填写")
        sponsorIds = []
        contractorIds = []

    """项目执行人、项目发起人"""
    if projectPeopleChooseType == "MUST_CHOOSE":  # 项目发起人、执行人必填的
        print("项目发起人、项目执行人必填")
        projectSponsor = 7024  # 项目发起人
        projectExecutor = 201709785111  # 项目执行人
    elif projectPeopleChooseType == "GEN_CHOOSE":  # 项目发起人、执行人选填的
        print("项目发起人、项目执行人选填")
        projectSponsor = 7024  # 项目发起人
        projectExecutor = ""  # 项目执行人
    else:  # 项目发起人、执行人不需要的
        print("项目发起人、项目执行人不出现")
        projectSponsor = ""
        projectExecutor = ""
    fram_data = {
    "activitySignType":"NeedSign",
    "backgroundDesc":"背景介绍",
    "breedGroupList":[
        {
            "breedGroupId":6,
            "companyId":1
        }
    ],
    "content":"活动内容",
    "departmentList":[
        {
            "applyMoney":1100,
            "breedGroupId":6,
            "budgetTypeId":1,
            "companyId":1,
            "departmentId":72
        }
    ],
    "headEmployeeId":416,
    "headEmployeeName":"王娜",
    "isSubmit":False,
    "laborCostPlanMeetCount":5,
    "latitude":"22.554847",
    "longitude":"113.949025",
    "meetAddr":"深圳市南山区朗山路11号",
    "province":"广东省",
    "city":"深圳市",
    "district":"南山区",
    "meetClassId":375,
    "meetClassSubId":"",
    "name":activity_name+str(date),
    "planEndTime":plandate+" "+meet_time5,
    "planStartTime":plandate+" "+meet_time1,
    "planMeetCount":100,
    "purposeList":[
        {
            "id":24,
            "name":"心好累",
            "memo":"大",
            "doctorMedicineGradeIds":"1",
            "doctorMedicineGradeText":"A++级",
            "doctorAcademicGradeIds":"1",
            "doctorAcademicGradeText":"学术1级"
        }
    ],
    "relateManList":[
        {
            "manId":415,
            "manName":"徐鹏"
        }
    ],
    "scope":"SINGLE_CITY",
    "strategyList":[
        # """这是APP端区域活动的传值方式"""
        {
            "academicId": 9061,
            "academicName": "阿牛专用黛力新学术方向",
            "breedGroupId": 6,
            "breedGroupName": "黛力新",
            "hospitalGradeIds": None,
            "id": 292,
            "memo": None,
            "name": "区域策略-深康黛力新2020年",
            "popularizeKeyWords": "区域深康黛力新阿牛推广关键002",
            "popularizeKeyWordsId": "526",
            "sectionOfficeIds": None,
            "type": "区域"
        }
        # """这是PC端区域活动的传值方式"""
        # {
        #     "id": 292,
        #     "name": "区域策略-深康黛力新2020年",
        #     "popularizeKeyWords": "区域深康黛力新阿牛推广关键001",
        #     "popularizeKeyWordsId": 525,
        #     "academicName": "阿牛专用黛力新学术方向",
        #     "academicId": 9061
        # }
    ],
    "subjectList":[
        {
            "subjectId":33,
            "remark":"",
            "subjectName":"劳务费",
            "applyMoney":800,
            "typeId":12,
            "totalMoney":""
        },
        {
            "subjectId":34,
            "remark":"",
            "subjectName":"餐费",
            "applyMoney":100,
            "typeId":12,
            "totalMoney":""
        },
        {
            "subjectId":35,
            "remark":"",
            "subjectName":"小食",
            "applyMoney":50,
            "typeId":12,
            "totalMoney":""
        },
        {
            "subjectId":36,
            "remark":"",
            "subjectName":"住宿费",
            "applyMoney":150,
            "typeId":12,
            "totalMoney":""
        }
    ],
    "specialAuditReason":"",
    "innerPlan":False,
    "expensePlanList":[],
    "subjectCompanyId":1,
    "doctorList":[],
    "empViewerList":[],
    "hospitalId":"",
    "pics":["https://default.test.file.dachentech.com.cn/image/app/201912251116548130.jpg"],
    "sectionGuestList":[],
    "sectionViewerList":[],
    "agenda":{
        "activityClassId":375,
        "activityName":activity_name+str(date),
        "sessionList":[
            {
                "time":plandate,
                "sessionDetailList":[
                    {
                        "agendaSettingId":1,
                        "meetRoleId":1,
                        "theme":"开幕致辞",
                        "startTime":meet_time1,
                        "endTime":meet_time2,
                        "relatedList":[
                            {
                                "companyName":"",
                                "relateId":201503290066,
                                "lecturerLevel":"CITY",
                                "lecturerLevelText":"城市级讲者",
                                "relateName":"黄小乐",
                                "relateType":"DOCTOR",
                                "hospitalName":"宁波大学医学院附属医院（宁波三院）",
                                "openId":"0377c96ea54743ab961b4165a85f7d12",
                                "title":"Resident",
                                "titleText":"住院医师",
                                "canPaid":True,
                                "contractCountDTO":{
                                    "yearCount":61,
                                    "monthCount":11,
                                    "weekCount":5
                                }
                            }
                        ]
                    },
                    {
                        "agendaSettingId":2,
                        "meetRoleId":1,
                        "theme":"这是讲题的主题",
                        "startTime":meet_time2,
                        "endTime":meet_time3,
                        "relatedList":[
                            {
                                "companyName":"",
                                "relateId":201709070836,
                                "lecturerLevel":"CENTRE",
                                "lecturerLevelText":"中央级讲者",
                                "relateName":"黄小可",
                                "relateType":"DOCTOR",
                                "hospitalName":"深圳大学医院",
                                "openId":"6da3de8ff1294ffb90b45941209ab0ee",
                                "title":"Resident",
                                "titleText":"住院医师",
                                "canPaid":True,
                                "contractCountDTO":{
                                    "yearCount":22,
                                    "monthCount":6,
                                    "weekCount":2
                                }
                            }
                        ]
                    },
                    {
                        "agendaSettingId":4,
                        "meetRoleId":4,
                        "theme":"这是点评的主题",
                        "startTime":meet_time3,
                        "endTime":meet_time4,
                        "relatedList":[
                            {
                                "companyName":"",
                                "relateId":201709147871,
                                "lecturerLevel":"CITY",
                                "lecturerLevelText":"城市级讲者",
                                "relateName":"凌小小",
                                "relateType":"DOCTOR",
                                "hospitalName":"安阳市人民医院",
                                "openId":"ba4639b2d65b4466884fcf4ebb1ebf08",
                                "title":"Resident",
                                "titleText":"住院医师",
                                "canPaid":True,
                                "contractCountDTO":{
                                    "yearCount":20,
                                    "monthCount":1,
                                    "weekCount":1
                                }
                            },
                            {
                                "companyName":"",
                                "relateId":201709173403,
                                "lecturerLevel":"AREA",
                                "lecturerLevelText":"区域级讲者",
                                "relateName":"凌素芬",
                                "relateType":"DOCTOR",
                                "hospitalName":"福建省三明市第二医院",
                                "openId":"db9f8748130e4afd849e6f4c70396d20",
                                "title":"Resident",
                                "titleText":"住院医师",
                                "canPaid":True,
                                "contractCountDTO":{
                                    "yearCount":29,
                                    "monthCount":1,
                                    "weekCount":None
                                }
                            },
                            {
                                "companyName": "",
                                "relateId": 201709089366,
                                "lecturerLevel": "AREA",
                                "lecturerLevelText": "区域级讲者",
                                "relateName": "黄小花",
                                "relateType": "DOCTOR",
                                "hospitalName": "哈尔滨医科大学附属第二医院",
                                "openId": "29ffa20193a0494d880fef0f69694e09",
                                "title": "Resident",
                                "titleText": "住院医师",
                                "canPaid": True,
                                "contractCountDTO": {
                                    "yearCount": 0,
                                    "monthCount": 0,
                                    "weekCount": 0
                                                     }
                            }
                        ]
                    },
                    {
                        "agendaSettingId":5,
                        "meetRoleId":-1,
                        "theme":"闭幕致辞",
                        "startTime":meet_time4,
                        "endTime":meet_time5,
                        "relatedList":[
                            {
                                "companyName":"深圳市康哲药业有限公司",
                                "relateId":417,
                                "lecturerLevel":"",
                                "lecturerLevelText":"",
                                "relateName":"田惠芳",
                                "relateType":"COLLEAGUE",
                                "hospitalName":"",
                                "openId":"",
                                "title":"",
                                "titleText":"",
                                "canPaid":False
                            }
                        ]
                    }
                ]
            }
        ]
    },
    "sponsorIds":sponsorIds,
    "contractorIds":contractorIds,
    "academicPlatformId":"62",
    "projectSponsor":projectSponsor,
    "projectExecutor":projectExecutor
        }

    if type_req['needUnion']==True: #需要联合举办，当需要联合举办时，我们赋值联合举办字段的值为False
        print("需要联合举办，并赋默认值为“否”！")
        fram_data["needUnion"]="False"
    elif type_req['needUnion'] == False: #不要联合举办时，在传参集合里就不会出现needUnion字段
        print("不需要联合举办！")

    req = requests.post(url=action_url,headers=headers,data=json.dumps(fram_data)).text
    resp = json.loads(req)
    print(resp)



if __name__=='__main__':
    creat_action('UA0000000416')


