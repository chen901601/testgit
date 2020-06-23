# coding=utf8
import requests, json, random, urllib.request
from datetime import datetime, timedelta
from time import sleep
date = datetime.now()

date = date.strftime("%Y-%m-%d %H:%M:%S")
print("当前日期为："+date)
budgetDate = date[:7]
print("预算日期="+budgetDate)
"""把datetime转成字符串 :statrtime.strftime("%Y-%m-%d %H:%M:%S")"""
date=datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
"""将指定日加一天"""
plandate = date + timedelta(days=0)
plandate = plandate.strftime("%Y-%m-%d %H:%M:%S")[0:10]
print("创建的活动开会日为："+plandate)


def PC_token(username,password='888888'):
    """作用：根提供的账号密码获取PC-token"""
    """请求方式:POST"""
    pc_token_url='http://test-ms.xgjk.info/cms-auth/auth/pc/login'
    request_headers={'Accept': 'application/json, text/plain, */*',
                     'Content-Type': 'application/json;charset=UTF-8',
                     }
    param_fram={"username":username,
                "password":password,
                "captchaValue":"9999",
                "captchaKey":"yvkpYGzQYgEX7Wd4"
                }
    request=requests.post(url=pc_token_url,headers=request_headers,data=json.dumps(param_fram)).text
    response=json.loads(request)
    value=response.get('value')
    token=value.get('token')
    # print(token)
    return token



def creat_action(username,meet_time1,meet_time2,meet_time3,meet_time4,meet_time5):
    action_type_url = 'http://test-ms.xgjk.info/cms-act-service/act/basic/activityClass/getById?activityClassId=378'
    action_url = 'http://test-ms.xgjk.info/cms-act-service/act/hq/save'
    token = PC_token(username)
    headers = {"Accept": "application/json,text/plain, */*",
                     "Content-Type": "application/json;charset=UTF-8",
                     "Authorization": token
                     }
    type_req = requests.get(url=action_type_url,headers=headers).json()
    needSponsor = type_req["needSponsor"]  #True 需要
    projectPeopleChooseType = type_req["projectPeopleChooseType"] #NO_CHOOSE 不需要选择  GEN_CHOOSE 可选 MUST_CHOOSE 必选


    """承办方、主办方"""
    if needSponsor:
        # print("主办方、承办方必填")
        sponsorIds = [61] #主办方
        contractorIds = [61] #承办方
    else:
        # print("主办方、承办方不需要填写")
        sponsorIds = []
        contractorIds = []

    """项目执行人、项目发起人"""
    if projectPeopleChooseType=="MUST_CHOOSE": #项目发起人、执行人必填的
        # print("项目发起人、项目执行人必填")
        projectSponsor = 7024  #项目发起人
        projectExecutor = 201709785111  #项目执行人
    elif projectPeopleChooseType=="GEN_CHOOSE": #项目发起人、执行人选填的
        # print("项目发起人、项目执行人选填")
        projectSponsor = 7024  # 项目发起人
        projectExecutor = ""  # 项目执行人
    else:  #项目发起人、执行人不需要的
        # print("项目发起人、项目执行人不出现")
        projectSponsor = ""
        projectExecutor = ""
    fram_data = {
    "actBudgetDetailList":[
        {
            "breedGroupId":6,
            "budgetSource":"HAND_DOWN",
            "budgetTypeId":3,
            "companyId":1,
            "departmentId":254,
            "firstBudgetId":79,
            "initMoney":1500,
            "secondBudgetId":568,
            "currencyId":1
        }
    ],
    "actSubjectList":[
        {
            "subjectId":33,
            "subjectName":"劳务费",
            "remark":"",
            "typeId":12,
            "totalMoney":1000
        },
        {
            "subjectId":34,
            "subjectName":"餐费",
            "remark":"",
            "typeId":12,
            "totalMoney":150
        },
        {
            "subjectId":35,
            "subjectName":"小食",
            "remark":"",
            "typeId":12,
            "totalMoney":100
        },
        {
            "subjectId":36,
            "subjectName":"住宿费",
            "remark":"",
            "typeId":12,
            "totalMoney":250
        }
    ],
    "activitySignType":"NeedSign",
    "backgroundDesc":"防守打法",
    "budgetDate":budgetDate,
    "content":"达大厦",
    "definedMeetAddr":"",
    "doctorExpertGradeIds":"",
    "doctorIecturerGradeIds":"",
    "doctorMedicineGradeIds":"",
    "headEmployeeId":416,
    "headEmployeeName":"王娜",
    "hospitalGradeIds":"27",
    "hospitalLabelIds":"",
    "hospitalTypeIds":"",
    "latitude":"",
    "longitude":"",
    "meetAddr":"",
    "meetClassId":385,
    "name":"新王娜总部线上"+plandate+" "+meet_time1,
    "planEndTime":plandate+" "+meet_time5,
    "planMeetCount":100,
    "laborCostPlanMeetCount":4,
    "planStartTime":plandate+" "+meet_time1,
    "relateList":[
        {
            "manId":415,
            "manName":"徐鹏"
        }
    ],
    "expensePlanList":[
        {
            "breedGroupId":6,
            "money":1500,
            "planId":None,
            "projectName":"项目名称",
            "projectTypeId":79,
            "strategyId":290,
            "academicName":"",
            "academicId":None,
            "popularizeKeyWordsId":517,
            "popularizeKeyWords":"阿牛黛力新总部推广关键词001"
        }
    ],
    "totalMoney":"1500.00",
    "subjectCompanyId":1,
    "doctorList":[

    ],
    "empViewerList":[

    ],
    "sectionGuestList":[

    ],
    "sectionViewerList":[

    ],
    "academicPlatformId":67,
    "projectSponsor":7024,
    "projectExecutor":201709785111,
    "pics":[
        "https://default.test.file.dachentech.com.cn/undefinedxg-cms-web-img201912241955090420.jpg"
    ],
    "specialAuditReason":"",
    "agenda":{
        "activityClassId":385,
        "activityName":"新王娜总部线上"+plandate+" "+meet_time1,
        "sessionList":[
            {
                "time":plandate,
                "sessionDetailList":[
                    {
                        "agendaSettingId":1,
                        "meetRoleId":3,
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
                                "titleText":"住院医师",
                                "title":"Resident",
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
                        "theme":"这是讲题的主题",
                        "startTime":meet_time2,
                        "endTime":meet_time3,
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
                                "titleText":"住院医师",
                                "title":"Resident",
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
                                "hospitalName":"安阳市人民的医院",
                                "openId":"ba4639b2d65b4466884fcf4ebb1ebf08",
                                "titleText":"住院医师",
                                "title":"Resident",
                                "canPaid":True,
                                "contractCountDTO":{
                                    "yearCount":None,
                                    "monthCount":None,
                                    "weekCount":None
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
                                "titleText":"住院医师",
                                "title":"Resident",
                                "canPaid":True,
                                "contractCountDTO":{
                                    "yearCount":None,
                                    "monthCount":None,
                                    "weekCount":None
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
    "contractorIds":[

    ],
    "sponsorIds":[

    ],
    "code":"CA2020-100000378",
    "id":17732,
    "isSubmit":False
}
    if type_req['needUnion']==True: #需要联合举办，当需要联合举办时，我们赋值联合举办字段的值为False
        # print("需要联合举办，并赋默认值为“否”！")
        fram_data["needUnion"]="False"
    elif type_req['needUnion'] == False: #不要联合举办时，在传参集合里就不会出现needUnion字段
        # print("不需要联合举办！")
        pass

    req = requests.post(url=action_url,headers=headers,data=json.dumps(fram_data)).text
    resp = json.loads(req)
    print(resp)

if __name__=='__main__':

    start_hour = input("请输入会议开始的时辰，（例如12点，就输入：12）：")
    while 1:
        if start_hour.isdigit()==False:
            start_hour = input("输入的会议开始时辰不是数据类型，请重新输入：")
            continue
        if int(start_hour)<6:
            start_hour = input("输入的会议开始时辰必须大于等于6，请重新输入：")
            continue
        for minth in range(0, 60, 5):
            if len(str(minth)) == 1:
                minth = "0" + str(minth)
            start_minth = str(minth)
            meet_time1 = start_hour + ":" + start_minth
            start_time = datetime.strptime(meet_time1, "%H:%M")
            meet_time2 = (start_time + timedelta(hours=1)).strftime("%Y-%m-%d %H:%M:%S")
            meet_time3 = (start_time + timedelta(hours=2)).strftime("%Y-%m-%d %H:%M:%S")
            meet_time4 = (start_time + timedelta(hours=3)).strftime("%Y-%m-%d %H:%M:%S")
            meet_time5 = (start_time + timedelta(hours=4)).strftime("%Y-%m-%d %H:%M:%S")
            if meet_time5[0:11] != start_time.strftime("%Y-%m-%d %H:%M:%S")[0:11]:
                start_hour = input("输入的会议开始时辰过大，导致会议跨天数，请重新输入会议开始时辰：")
                break
            else:
                print("议程的开始时间为{}".format(plandate+" "+meet_time1))
                creat_action('ua0000000416',meet_time1,meet_time2[11:16],meet_time3[11:16],meet_time4[11:16],meet_time5[11:16])
        if meet_time5[0:11] == start_time.strftime("%Y-%m-%d %H:%M:%S")[0:11]:
            break
