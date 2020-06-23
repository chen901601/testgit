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
    "laborCostPlanMeetCount":1,
    "latitude":"",
    "longitude":"",
    "meetAddr":"",
    "meetClassId":23,
    "meetClassSubId":"",
    "name":"医生圈视频会议王娜接口造数据"+str(date),
    "planEndTime":plandate+" 08:00",
    "planStartTime":plandate+" 07:00",
    "planMeetCount":100,
    "purposeList":[
        {
            "id":39,
            "name":"视频-视频",
            "memo":"短时",
            "doctorMedicineGradeIds":"1,7,6,5,3,2,4",
            "doctorMedicineGradeText":"A++级,A+级,A级,B级,C级,D级,Q级",
            "doctorAcademicGradeIds":"1,2,3,4,5,6,7,8,9,10",
            "doctorAcademicGradeText":"学术1级,学术2级,学术3级,学术4级,学术5级,学术6级,学术7级,学术8级,学术9级,境外专家"
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

    ],
    "sectionViewerList":[

    ],
    "agenda":{
        "activityClassId":23,
        "activityName":"医生圈视频会议王娜接口造数据"+str(date),  #医生圈的议程只能有一段议程
        "sessionList":[
            {
                "time":plandate,
                "sessionDetailList":[
                    {
                        "agendaSettingId":2,
                        "meetRoleId":1,
                        "theme":"这是医生圈视频会议的讲题主题",
                        "startTime":"07:00",
                        "endTime":"08:00",
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
    "sponsorIds":[

    ],
    "contractorIds":[

    ],
    "academicPlatformId":62,
    "projectSponsor":7024,
    "projectExecutor":201709785111,
    "id":18150
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

