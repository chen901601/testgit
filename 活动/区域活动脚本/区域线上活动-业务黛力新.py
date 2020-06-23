# coding=utf8
import requests, json, random, urllib.request
from datetime import datetime, timedelta
from time import sleep

employeeName = '阿牛'

date = datetime.now()

date = date.strftime("%Y-%m-%d %H:%M:%S")
print("当前日期为："+date)
"""把datetime转成字符串 :statrtime.strftime("%Y-%m-%d %H:%M:%S")"""
date=datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
"""将指定日加一天"""
plandate = date + timedelta(days=30)
plandate = plandate.strftime("%Y-%m-%d %H:%M:%S")[0:10]
print("创建的活动开会日为："+plandate)


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

def creat_action(username):
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
            "applyMoney":1900,
            "breedGroupId":6,
            "budgetTypeId":1,
            "companyId":1,
            "departmentId":72
        }
    ],
    "headEmployeeId":416,
    "headEmployeeName":"王娜",
    "isSubmit":False,
    "laborCostPlanMeetCount":6,
    "latitude":"",
    "longitude":"",
    "meetAddr":"",
    "meetClassId":379,
    "meetClassSubId":"",
    "name":"区域线上活动王娜接口造数据"+str(date),
    "planEndTime":plandate+" 11:00",
    "planStartTime":plandate+" 06:00",
    "planMeetCount":100,
    "purposeList":[
        {
            "id":32,
            "name":"好累",
            "memo":"的",
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
            "remark":None,
            "subjectName":"劳务费",
            "applyMoney":800,
            "typeId":12
        },
        {
            "subjectId":34,
            "remark":None,
            "subjectName":"餐费",
            "applyMoney":100,
            "typeId":12
        },
        {
            "subjectId":35,
            "remark":None,
            "subjectName":"小食",
            "applyMoney":50,
            "typeId":12
        },
        {
            "subjectId":36,
            "remark":None,
            "subjectName":"住宿费",
            "applyMoney":150,
            "typeId":12
        },
        {
            "applyMoney": 800,
            "subjectName": "调查费",
            "subjectId": 57,
            "typeId": 12,
            "totalMoney": ""
        }
    ],
    "specialAuditReason":"",
    "innerPlan":False,
    "expensePlanList":[

    ],
    "subjectCompanyId":1,
    "doctorList":[

    ],
    "empViewerList":[

    ],
    "hospitalId":"",
    "pics":[
        "https://default.test.file.dachentech.com.cn/image/app/201912251116548130.jpg"
    ],
    "sectionGuestList":[
        {
            "hospitalId":200108221943,
            "hospitalName":"宁波大学医学院附属医院（宁波三院）",
            "sectionId":18,
            "sectionName":"全科"
        },
        {
            "hospitalId":200507160002,
            "hospitalName":"深圳大学医院",
            "sectionId":18,
            "sectionName":"全科"
        }
    ],
    "sectionViewerList":[

    ],
    "agenda":{
        "activityClassId":379,
        "activityName":"区域线上活动王娜接口造数据"+str(date),
        "sessionList":[
            {
                "time":plandate,
                "sessionDetailList":[
                    {
                        "agendaSettingId":1,
                        "meetRoleId":3,
                        "theme":"开幕致辞",
                        "startTime":"06:00",
                        "endTime":"07:00",
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
                                    "yearCount":1,
                                    "monthCount":1,
                                    "weekCount":1
                                }
                            }
                        ]
                    },
                    {
                        "agendaSettingId":2,
                        "meetRoleId":1,
                        "theme":"这是区域线上会有的讲题主题",
                        "startTime":"07:00",
                        "endTime":"08:00",
                        "relatedList":[
                            {
                                "companyName":"",
                                "relateId":201709070836,
                                "lecturerLevel":"FOREIGN",
                                "lecturerLevelText":"外籍讲者",
                                "relateName":"黄小可",
                                "relateType":"DOCTOR",
                                "hospitalName":"深圳大学医院",
                                "openId":"6da3de8ff1294ffb90b45941209ab0ee",
                                "title":"Resident",
                                "titleText":"住院医师",
                                "canPaid":True,
                                "contractCountDTO":{
                                    "yearCount":1,
                                    "monthCount":1,
                                    "weekCount":1
                                }
                            }
                        ]
                    },
                    {
                        "agendaSettingId": 4,
                        "meetRoleId": 4,
                        "theme": "发发",
                        "startTime": "08:00",
                        "endTime": "10:00",
                        "relatedList": [
                            {
                                "id": 11608,
                                "agendaSessionDetailRelatedId": 11608,
                                "sessionDetailId": 9578,
                                "sessionId": 3717,
                                "agendaId": 2161,
                                "relateId": 201709147871,
                                "relateType": "DOCTOR",
                                "relateTypeText": "医生",
                                "relateName": "凌小小",
                                "companyName": "",
                                "title": "Resident",
                                "titleText": "住院医师",
                                "hospitalName": "安阳市人民的医院",
                                "lecturerLevel": "CITY",
                                "lecturerLevelText": "城市级讲者",
                                "sendContract": False,
                                "canPaid": True,
                                "openId": "ba4639b2d65b4466884fcf4ebb1ebf08",
                                "contractCountDTO": {
                                    "yearCount": 6,
                                    "monthCount": 0,
                                    "weekCount": 4
                                }
                            },
                            {
                                "id": 11609,
                                "agendaSessionDetailRelatedId": 11609,
                                "sessionDetailId": 9578,
                                "sessionId": 3717,
                                "agendaId": 2161,
                                "relateId": 201709173403,
                                "relateType": "DOCTOR",
                                "relateTypeText": "医生",
                                "relateName": "凌素芬",
                                "companyName": "",
                                "title": "Resident",
                                "titleText": "住院医师",
                                "hospitalName": "福建省三明市第二医院",
                                "lecturerLevel": "AREA",
                                "lecturerLevelText": "区域级讲者",
                                "sendContract": False,
                                "canPaid": True,
                                "openId": "db9f8748130e4afd849e6f4c70396d20",
                                "contractCountDTO": {
                                    "yearCount": 1,
                                    "monthCount": 0,
                                    "weekCount": 0
                                }
                            },
                            {
                                "companyName": "",
                                "relateId": 201709443548,
                                "lecturerLevel": "CENTRE",
                                "lecturerLevelText": "中央级讲者",
                                "relateName": "黄小红",
                                "relateType": "DOCTOR",
                                "hospitalName": "深圳大学医院",
                                "openId": "79aae49babeb44f69c3c99a4f8b39bdf",
                                "title": "Resident",
                                "titleText": "住院医师",
                                "canPaid": False,
                                "contractCountDTO": {
                                    "yearCount": 0,
                                    "monthCount": 0,
                                    "weekCount": 0
                                }
                            },
                            {
                                "companyName": "",
                                "relateId": 201709444205,
                                "lecturerLevel": "AREA",
                                "lecturerLevelText": "区域级讲者",
                                "relateName": "黄小鹏",
                                "relateType": "DOCTOR",
                                "hospitalName": "百色市皮肤病防治院",
                                "openId": "a41a60a9db7849c5a6142dc72b707909",
                                "title": "Resident",
                                "titleText": "住院医师",
                                "canPaid": False,
                                "contractCountDTO": {
                                    "yearCount": 1,
                                    "monthCount": 0,
                                    "weekCount": 0
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
                                "canPaid": False,
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
                        "startTime":"10:00",
                        "endTime":"11:00",
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
    "sponsorIds":[

    ],
    "contractorIds":[

    ],
    "academicPlatformId":62,
    "projectSponsor":7024,
    "projectExecutor":"",
    "id":18112
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
    creat_action('ua0000000416')

