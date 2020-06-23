# -*- coding: utf-8 -*
#@Time:2020/6/9 18:56
#@Auther:chenyr

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
    #每新增编写一个活动类型，都需要赋值给到相应的activityClassId
    action_type_url = "https://test-ms.xgjk.info/cms-act-service/act/basic/activityClass/getById?activityClassId=413"
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
    "academicPlatformId":"",
    "activitySignType":"NeedSign",
    "meetClassSubId":None,
    "subjectList":[
        {
            "applyMoney":1100,
            "subjectId":33,
            "typeId":12
        },
        {
            "applyMoney":100,
            "subjectId":35,
            "typeId":12
        },
        {
            "applyMoney":300,
            "subjectId":36,
            "typeId":12
        },
        {
            "applyMoney":400,
            "subjectId":37,
            "typeId":12
        }
    ],
    "agenda":{
        "activityClassId":413,
        "activityName":"国内会-线上，区域" + str(date),
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
                                "id":23593,
                                "agendaSessionDetailRelatedId":23593,
                                "sessionDetailId":17098,
                                "sessionId":5667,
                                "agendaId":3178,
                                "relateId":201503290066,
                                "relateType":"DOCTOR",
                                "relateTypeText":"医生",
                                "relateName":"黄小乐",
                                "companyName":"",
                                "title":"Resident",
                                "titleText":"住院医师",
                                "hospitalName":"宁波大学医学院附属医院（宁波三院）",
                                "lecturerLevel":"CITY",
                                "lecturerLevelText":"城市级讲者",
                                "sendContract":False,
                                "canPaid":True,
                                "openId":"0377c96ea54743ab961b4165a85f7d12",
                                "contractCountDTO":{
                                    "yearCount":0,
                                    "monthCount":0,
                                    "weekCount":0
                                }
                            }
                        ]
                    },
                    {
                        "agendaSettingId":2,
                        "meetRoleId":1,
                        "theme":"这是讲题的主题",
                        "startTime":"07:00",
                        "endTime":"08:00",
                        "relatedList":[
                            {
                                "id":23594,
                                "agendaSessionDetailRelatedId":23594,
                                "sessionDetailId":17099,
                                "sessionId":5667,
                                "agendaId":3178,
                                "relateId":201709070836,
                                "relateType":"DOCTOR",
                                "relateTypeText":"医生",
                                "relateName":"黄小可",
                                "companyName":"",
                                "title":"Resident",
                                "titleText":"住院医师",
                                "hospitalName":"深圳大学医院",
                                "lecturerLevel":"CENTRE",
                                "lecturerLevelText":"中央级讲者",
                                "sendContract":False,
                                "canPaid":True,
                                "openId":"6da3de8ff1294ffb90b45941209ab0ee",
                                "contractCountDTO":{
                                    "yearCount":0,
                                    "monthCount":0,
                                    "weekCount":0
                                }
                            }
                        ]
                    },
                    {
                        "agendaSettingId":4,
                        "meetRoleId":4,
                        "theme":"这是点评的主题",
                        "startTime":"08:00",
                        "endTime":"10:00",
                        "relatedList":[
                            {
                                "id":23595,
                                "agendaSessionDetailRelatedId":23595,
                                "sessionDetailId":17100,
                                "sessionId":5667,
                                "agendaId":3178,
                                "relateId":201709173403,
                                "relateType":"DOCTOR",
                                "relateTypeText":"医生",
                                "relateName":"凌素芬",
                                "companyName":"",
                                "title":"Resident",
                                "titleText":"住院医师",
                                "hospitalName":"福建省三明市第二医院",
                                "lecturerLevel":"AREA",
                                "lecturerLevelText":"区域级讲者",
                                "sendContract":False,
                                "canPaid":True,
                                "openId":"db9f8748130e4afd849e6f4c70396d20",
                                "contractCountDTO":{
                                    "yearCount":0,
                                    "monthCount":0,
                                    "weekCount":0
                                }
                            },
                            {
                                "id":23596,
                                "agendaSessionDetailRelatedId":23596,
                                "sessionDetailId":17100,
                                "sessionId":5667,
                                "agendaId":3178,
                                "relateId":201709147871,
                                "relateType":"DOCTOR",
                                "relateTypeText":"医生",
                                "relateName":"凌小小",
                                "companyName":"",
                                "title":"Resident",
                                "titleText":"住院医师",
                                "hospitalName":"安阳市人民的医院",
                                "lecturerLevel":"CITY",
                                "lecturerLevelText":"城市级讲者",
                                "sendContract":False,
                                "canPaid":True,
                                "openId":"ba4639b2d65b4466884fcf4ebb1ebf08",
                                "contractCountDTO":{
                                    "yearCount":0,
                                    "monthCount":0,
                                    "weekCount":0
                                }
                            },
                            {
                                "id":23597,
                                "agendaSessionDetailRelatedId":23597,
                                "sessionDetailId":17100,
                                "sessionId":5667,
                                "agendaId":3178,
                                "relateId":201709446654,
                                "relateType":"DOCTOR",
                                "relateTypeText":"医生",
                                "relateName":"黄小七",
                                "companyName":"",
                                "title":"Resident",
                                "titleText":"住院医师",
                                "hospitalName":"深圳大学医院",
                                "lecturerLevel":"AREA",
                                "lecturerLevelText":"区域级讲者",
                                "sendContract":False,
                                "canPaid":False,
                                "openId":"41947c4487c5433a8e9c6f97574e3db2",
                                "contractCountDTO":{
                                    "yearCount":0,
                                    "monthCount":0,
                                    "weekCount":0
                                }
                            },
                            {
                                "id":23598,
                                "agendaSessionDetailRelatedId":23598,
                                "sessionDetailId":17100,
                                "sessionId":5667,
                                "agendaId":3178,
                                "relateId":201709446653,
                                "relateType":"DOCTOR",
                                "relateTypeText":"医生",
                                "relateName":"黄小六",
                                "companyName":"",
                                "title":"Resident",
                                "titleText":"住院医师",
                                "hospitalName":"深圳大学医院",
                                "lecturerLevel":"AREA",
                                "lecturerLevelText":"区域级讲者",
                                "sendContract":False,
                                "canPaid":False,
                                "openId":"b2f787aeeb6a416182ac6851bd5b8b35",
                                "contractCountDTO":{
                                    "yearCount":0,
                                    "monthCount":0,
                                    "weekCount":0
                                }
                            },
                            {
                                "id":23599,
                                "agendaSessionDetailRelatedId":23599,
                                "sessionDetailId":17100,
                                "sessionId":5667,
                                "agendaId":3178,
                                "relateId":201709446652,
                                "relateType":"DOCTOR",
                                "relateTypeText":"医生",
                                "relateName":"黄小五",
                                "companyName":"",
                                "title":"Resident",
                                "titleText":"住院医师",
                                "hospitalName":"深圳大学医院",
                                "lecturerLevel":"AREA",
                                "lecturerLevelText":"区域级讲者",
                                "sendContract":False,
                                "canPaid":False,
                                "openId":"b426c7e8817b4b06a819e23aff1cd4a0",
                                "contractCountDTO":{
                                    "yearCount":0,
                                    "monthCount":0,
                                    "weekCount":0
                                }
                            },
                            {
                                "id":23600,
                                "agendaSessionDetailRelatedId":23600,
                                "sessionDetailId":17100,
                                "sessionId":5667,
                                "agendaId":3178,
                                "relateId":201709444205,
                                "relateType":"DOCTOR",
                                "relateTypeText":"医生",
                                "relateName":"黄小鹏",
                                "companyName":"",
                                "title":"Resident",
                                "titleText":"住院医师",
                                "hospitalName":"百色市皮肤病防治院",
                                "lecturerLevel":"AREA",
                                "lecturerLevelText":"区域级讲者",
                                "sendContract":False,
                                "canPaid":False,
                                "openId":"a41a60a9db7849c5a6142dc72b707909",
                                "contractCountDTO":{
                                    "yearCount":0,
                                    "monthCount":0,
                                    "weekCount":0
                                }
                            },
                            {
                                "id":23601,
                                "agendaSessionDetailRelatedId":23601,
                                "sessionDetailId":17100,
                                "sessionId":5667,
                                "agendaId":3178,
                                "relateId":201709443548,
                                "relateType":"DOCTOR",
                                "relateTypeText":"医生",
                                "relateName":"黄小红",
                                "companyName":"",
                                "title":"Resident",
                                "titleText":"住院医师",
                                "hospitalName":"深圳大学医院",
                                "lecturerLevel":"CENTRE",
                                "lecturerLevelText":"中央级讲者",
                                "sendContract":False,
                                "canPaid":False,
                                "openId":"79aae49babeb44f69c3c99a4f8b39bdf",
                                "contractCountDTO":{
                                    "yearCount":0,
                                    "monthCount":0,
                                    "weekCount":0
                                }
                            }
                        ]
                    },
                    {
                        "agendaSettingId":5,
                        "meetRoleId":-1,
                        "theme":"闭幕致辞",
                        "startTime":"10:00",
                        "endTime":"12:00",
                        "relatedList":[
                            {
                                "id":23602,
                                "agendaSessionDetailRelatedId":23602,
                                "sessionDetailId":17101,
                                "sessionId":5667,
                                "agendaId":3178,
                                "relateId":417,
                                "relateType":"COLLEAGUE",
                                "relateTypeText":"同事",
                                "relateName":"田惠芳",
                                "companyName":"深圳市康哲药业有限公司",
                                "title":None,
                                "titleText":None,
                                "hospitalName":"",
                                "lecturerLevel":None,
                                "lecturerLevelText":None,
                                "sendContract":False,
                                "canPaid":False,
                                "openId":None,
                                "contractCountDTO":None
                            }
                        ]
                    },
                    {
                        "agendaSettingId":3,
                        "meetRoleId":None,
                        "theme":"会中休息",
                        "startTime":"12:00",
                        "endTime":"14:00",
                        "relatedList":[

                        ]
                    },
                    {
                        "agendaSettingId":5,
                        "meetRoleId":1,
                        "theme":"闭幕致辞",
                        "startTime":"14:00",
                        "endTime":"16:00",
                        "relatedList":[
                            {
                                "id":23603,
                                "agendaSessionDetailRelatedId":23603,
                                "sessionDetailId":17103,
                                "sessionId":5667,
                                "agendaId":3178,
                                "relateId":201709089366,
                                "relateType":"DOCTOR",
                                "relateTypeText":"医生",
                                "relateName":"黄小花",
                                "companyName":"",
                                "title":"Resident",
                                "titleText":"住院医师",
                                "hospitalName":"哈尔滨医科大学附属第二医院",
                                "lecturerLevel":"AREA",
                                "lecturerLevelText":"区域级讲者",
                                "sendContract":False,
                                "canPaid":True,
                                "openId":"29ffa20193a0494d880fef0f69694e09",
                                "contractCountDTO":{
                                    "yearCount":0,
                                    "monthCount":0,
                                    "weekCount":0
                                }
                            }
                        ]
                    }
                ]
            }
        ]
    },
    "laborCostPlanMeetCount":5,
    "backgroundDesc":"背景介绍",
    "content":"活动内容",
    "sponsorIds":sponsorIds,
    "contractorIds":contractorIds,
    "breedGroupList":[
        {
            "breedGroupId":13,
            "companyId":2
        },
        {
            "breedGroupId":6,
            "companyId":1
        }
    ],
    "departmentList":[
        {
            "applyMoney":"900",
            "breedGroupId":13,
            "budgetTypeId":6,
            "companyId":2,
            "departmentId":662,
            "hospitalId":None
        },
        {
            "applyMoney":"1000",
            "breedGroupId":6,
            "budgetTypeId":6,
            "companyId":1,
            "departmentId":254,
            "hospitalId":None
        }
    ],
    "doctorList":[

    ],
    "empViewerList":[

    ],
    "sectionGuestList":[

    ],
    "sectionViewerList":[

    ],
    "hasRecord":True,
    "expensePlanList":[

    ],
    "echoExpensePlanIds":[

    ],
    "headEmployeeId":416,
    "headEmployeeName":"王娜",
    "hospitalId":"",
    "innerPlan":False,
    "latitude":22.550198,
    "longitude":113.94036,
    "meetAddr":"广东省深圳市南山区粤海街道深圳高新区生物孵化器",
    "province":"广东省",
    "city":"深圳市",
    "district":"南山区",
    "meetClassId":413,
    "name":"国内会-线上，区域" + str(date),
    "pics":[
        "https://default.test.file.dachentech.com.cn/undefinedxg-cms-web-img202006091853325400.jpg",
        "https://default.test.file.dachentech.com.cn/undefinedxg-cms-web-img202006091853370860.png",
        "https://default.test.file.dachentech.com.cn/undefinedxg-cms-web-img202006091853486160.png"
    ],
    "planStartTime":plandate+" 06:00",
    "planEndTime":plandate+" 16:00",
    "planMeetCount":10,
    "projectSponsor":projectSponsor,
    "projectExecutor":projectExecutor,
    "purposeList":[
        {
            "id":51,
            "name":"测试用"
        }
    ],
    "relateManList":[

    ],
    "scope":"SINGLE_CITY",
    "strategyList":[
        {
            "id":290,
            "name":"总部活动策略-黛力新2020年深康",
            "popularizeKeyWords":"阿牛黛力新总部推广关键词004",
            "popularizeKeyWordsId":520,
            "academicName":"阿牛专用黛力新学术方向",
            "academicId":9061
        },
        {
            "id":307,
            "name":"新活素策略-阿牛",
            "popularizeKeyWords":"新活素策略005",
            "popularizeKeyWordsId":566,
            "academicName":"阿牛专用新活素学术方向",
            "academicId":9072
        }
    ],
    "subjectCompanyId":1,
    "externalActivity":{

    },
    "isSubmit":False,
    "id":19312
}

    if type_req['needUnion'] == True:  # 需要联合举办，当需要联合举办时，我们赋值联合举办字段的值为False
        print("需要联合举办，并赋默认值为“否”！")
        fram_data["needUnion"] = "False"
    elif type_req['needUnion'] == False:  # 不要联合举办时，在传参集合里就不会出现needUnion字段
        print("不需要联合举办！")

    req = requests.post(url=action_url, headers=headers, data=json.dumps(fram_data)).text
    resp = json.loads(req)
    print(resp)


if __name__ == '__main__':
    creat_action('ua0000000416')

