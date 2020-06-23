# coding=utf8
import requests, json, random, urllib.request
from datetime import datetime, timedelta
from time import sleep

employeeName = '阿牛'

date = datetime.now()

date = date.strftime("%Y-%m-%d %H:%M:%S")
print("当前日期为："+date)
month = date[0:7]
# print(month)
"""把datetime转成字符串 :statrtime.strftime("%Y-%m-%d %H:%M:%S")"""
date=datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
"""将指定日加一天"""
plandate = date + timedelta(days=30)
plandate = plandate.strftime("%Y-%m-%d %H:%M:%S")[0:10]
print("创建的活动开会日为："+plandate)

"""议程参数"""
sessionDetailList = [
{"agendaSettingId":1,"meetRoleId":1,"theme":"开幕致辞","startTime":"00:00","endTime":"00:10","relatedList":[{"companyName":"","relateId":201709785484,"lecturerLevel":"AREA","lecturerLevelText":"区域级讲者","relateName":"庄董二","relateType":"DOCTOR","hospitalName":"卫生部中日友好医院","openId":"5fd4d26be2e44788b9a9ae0daee9bbba","title":"Resident","titleText":"住院医师","canPaid":True}]},
{"agendaSettingId":1,"meetRoleId":1,"theme":"开幕致辞","startTime":"00:10","endTime":"01:20","relatedList":[{"companyName":"","relateId":201709785484,"lecturerLevel":"AREA","lecturerLevelText":"区域级讲者", "relateName":"庄董二","relateType":"DOCTOR","hospitalName":"卫生部中日友好医院","openId":"5fd4d26be2e44788b9a9ae0daee9bbba","title":"Resident","titleText":"住院医师","canPaid": False}]},
{"agendaSettingId":1,"meetRoleId":1,"theme":"开幕致辞","startTime":"00:10","endTime":"01:20","relatedList":[{"companyName":"","relateId":201709785484,"lecturerLevel":"AREA","lecturerLevelText":"区域级讲者", "relateName":"庄董二","relateType":"DOCTOR","hospitalName":"卫生部中日友好医院","openId":"5fd4d26be2e44788b9a9ae0daee9bbba","title":"Resident","titleText":"住院医师","canPaid": False}]},
{"agendaSettingId":1,"meetRoleId":1,"theme":"开幕致辞","startTime":"00:10","endTime":"01:20","relatedList":[{"companyName":"","relateId":201709785484,"lecturerLevel":"AREA","lecturerLevelText":"区域级讲者", "relateName":"庄董二","relateType":"DOCTOR","hospitalName":"卫生部中日友好医院","openId":"5fd4d26be2e44788b9a9ae0daee9bbba","title":"Resident","titleText":"住院医师","canPaid": False}]},
{"agendaSettingId":1,"meetRoleId":1,"theme":"开幕致辞","startTime":"00:10","endTime":"01:20","relatedList":[{"companyName":"","relateId":201709785484,"lecturerLevel":"AREA","lecturerLevelText":"区域级讲者", "relateName":"庄董二","relateType":"DOCTOR","hospitalName":"卫生部中日友好医院","openId":"5fd4d26be2e44788b9a9ae0daee9bbba","title":"Resident","titleText":"住院医师","canPaid": False}]},
{"agendaSettingId":1,"meetRoleId":1,"theme":"开幕致辞","startTime":"00:10","endTime":"01:20","relatedList":[{"companyName":"","relateId":201709785484,"lecturerLevel":"AREA","lecturerLevelText":"区域级讲者", "relateName":"庄董二","relateType":"DOCTOR","hospitalName":"卫生部中日友好医院","openId":"5fd4d26be2e44788b9a9ae0daee9bbba","title":"Resident","titleText":"住院医师","canPaid": False}]},
{"agendaSettingId":1,"meetRoleId":1,"theme":"开幕致辞","startTime":"00:10","endTime":"01:20","relatedList":[{"companyName":"","relateId":201709785484,"lecturerLevel":"AREA","lecturerLevelText":"区域级讲者", "relateName":"庄董二","relateType":"DOCTOR","hospitalName":"卫生部中日友好医院","openId":"5fd4d26be2e44788b9a9ae0daee9bbba","title":"Resident","titleText":"住院医师","canPaid": False}]},
{"agendaSettingId":1,"meetRoleId":1,"theme":"开幕致辞","startTime":"00:10","endTime":"01:20","relatedList":[{"companyName":"","relateId":201709785484,"lecturerLevel":"AREA","lecturerLevelText":"区域级讲者", "relateName":"庄董二","relateType":"DOCTOR","hospitalName":"卫生部中日友好医院","openId":"5fd4d26be2e44788b9a9ae0daee9bbba","title":"Resident","titleText":"住院医师","canPaid": False}]},
{"agendaSettingId":1,"meetRoleId":1,"theme":"开幕致辞","startTime":"00:10","endTime":"01:20","relatedList":[{"companyName":"","relateId":201709785484,"lecturerLevel":"AREA","lecturerLevelText":"区域级讲者", "relateName":"庄董二","relateType":"DOCTOR","hospitalName":"卫生部中日友好医院","openId":"5fd4d26be2e44788b9a9ae0daee9bbba","title":"Resident","titleText":"住院医师","canPaid": False}]},
{"agendaSettingId":1,"meetRoleId":1,"theme":"开幕致辞","startTime":"00:10","endTime":"01:20","relatedList":[{"companyName":"","relateId":201709785484,"lecturerLevel":"AREA","lecturerLevelText":"区域级讲者", "relateName":"庄董二","relateType":"DOCTOR","hospitalName":"卫生部中日友好医院","openId":"5fd4d26be2e44788b9a9ae0daee9bbba","title":"Resident","titleText":"住院医师","canPaid": False}]},
{"agendaSettingId":1,"meetRoleId":1,"theme":"开幕致辞","startTime":"00:10","endTime":"01:20","relatedList":[{"companyName":"","relateId":201709785484,"lecturerLevel":"AREA","lecturerLevelText":"区域级讲者", "relateName":"庄董二","relateType":"DOCTOR","hospitalName":"卫生部中日友好医院","openId":"5fd4d26be2e44788b9a9ae0daee9bbba","title":"Resident","titleText":"住院医师","canPaid": False}]},
{"agendaSettingId":1,"meetRoleId":1,"theme":"开幕致辞","startTime":"00:10","endTime":"01:20","relatedList":[{"companyName":"","relateId":201709785484,"lecturerLevel":"AREA","lecturerLevelText":"区域级讲者", "relateName":"庄董二","relateType":"DOCTOR","hospitalName":"卫生部中日友好医院","openId":"5fd4d26be2e44788b9a9ae0daee9bbba","title":"Resident","titleText":"住院医师","canPaid": False}]},
{"agendaSettingId":1,"meetRoleId":1,"theme":"开幕致辞","startTime":"00:10","endTime":"01:20","relatedList":[{"companyName":"","relateId":201709785484,"lecturerLevel":"AREA","lecturerLevelText":"区域级讲者", "relateName":"庄董二","relateType":"DOCTOR","hospitalName":"卫生部中日友好医院","openId":"5fd4d26be2e44788b9a9ae0daee9bbba","title":"Resident","titleText":"住院医师","canPaid": False}]},
{"agendaSettingId":1,"meetRoleId":1,"theme":"开幕致辞","startTime":"00:10","endTime":"01:20","relatedList":[{"companyName":"","relateId":201709785484,"lecturerLevel":"AREA","lecturerLevelText":"区域级讲者", "relateName":"庄董二","relateType":"DOCTOR","hospitalName":"卫生部中日友好医院","openId":"5fd4d26be2e44788b9a9ae0daee9bbba","title":"Resident","titleText":"住院医师","canPaid": False}]},
{"agendaSettingId":1,"meetRoleId":1,"theme":"开幕致辞","startTime":"00:10","endTime":"01:20","relatedList":[{"companyName":"","relateId":201709785484,"lecturerLevel":"AREA","lecturerLevelText":"区域级讲者", "relateName":"庄董二","relateType":"DOCTOR","hospitalName":"卫生部中日友好医院","openId":"5fd4d26be2e44788b9a9ae0daee9bbba","title":"Resident","titleText":"住院医师","canPaid": False}]},
{"agendaSettingId":1,"meetRoleId":1,"theme":"开幕致辞","startTime":"00:10","endTime":"01:20","relatedList":[{"companyName":"","relateId":201709785484,"lecturerLevel":"AREA","lecturerLevelText":"区域级讲者", "relateName":"庄董二","relateType":"DOCTOR","hospitalName":"卫生部中日友好医院","openId":"5fd4d26be2e44788b9a9ae0daee9bbba","title":"Resident","titleText":"住院医师","canPaid": False}]},
{"agendaSettingId":1,"meetRoleId":1,"theme":"开幕致辞","startTime":"00:10","endTime":"01:20","relatedList":[{"companyName":"","relateId":201709785484,"lecturerLevel":"AREA","lecturerLevelText":"区域级讲者", "relateName":"庄董二","relateType":"DOCTOR","hospitalName":"卫生部中日友好医院","openId":"5fd4d26be2e44788b9a9ae0daee9bbba","title":"Resident","titleText":"住院医师","canPaid": False}]},
{"agendaSettingId":1,"meetRoleId":1,"theme":"开幕致辞","startTime":"00:10","endTime":"01:20","relatedList":[{"companyName":"","relateId":201709785484,"lecturerLevel":"AREA","lecturerLevelText":"区域级讲者", "relateName":"庄董二","relateType":"DOCTOR","hospitalName":"卫生部中日友好医院","openId":"5fd4d26be2e44788b9a9ae0daee9bbba","title":"Resident","titleText":"住院医师","canPaid": False}]},
{"agendaSettingId":1,"meetRoleId":1,"theme":"开幕致辞","startTime":"00:10","endTime":"01:20","relatedList":[{"companyName":"","relateId":201709785484,"lecturerLevel":"AREA","lecturerLevelText":"区域级讲者", "relateName":"庄董二","relateType":"DOCTOR","hospitalName":"卫生部中日友好医院","openId":"5fd4d26be2e44788b9a9ae0daee9bbba","title":"Resident","titleText":"住院医师","canPaid": False}]},
{"agendaSettingId":1,"meetRoleId":1,"theme":"开幕致辞","startTime":"00:10","endTime":"01:20","relatedList":[{"companyName":"","relateId":201709785484,"lecturerLevel":"AREA","lecturerLevelText":"区域级讲者", "relateName":"庄董二","relateType":"DOCTOR","hospitalName":"卫生部中日友好医院","openId":"5fd4d26be2e44788b9a9ae0daee9bbba","title":"Resident","titleText":"住院医师","canPaid": False}]},
{"agendaSettingId":1,"meetRoleId":1,"theme":"开幕致辞","startTime":"00:10","endTime":"01:20","relatedList":[{"companyName":"","relateId":201709785484,"lecturerLevel":"AREA","lecturerLevelText":"区域级讲者", "relateName":"庄董二","relateType":"DOCTOR","hospitalName":"卫生部中日友好医院","openId":"5fd4d26be2e44788b9a9ae0daee9bbba","title":"Resident","titleText":"住院医师","canPaid": False}]},
{"agendaSettingId":1,"meetRoleId":1,"theme":"开幕致辞","startTime":"00:10","endTime":"01:20","relatedList":[{"companyName":"","relateId":201709785484,"lecturerLevel":"AREA","lecturerLevelText":"区域级讲者", "relateName":"庄董二","relateType":"DOCTOR","hospitalName":"卫生部中日友好医院","openId":"5fd4d26be2e44788b9a9ae0daee9bbba","title":"Resident","titleText":"住院医师","canPaid": False}]},
{"agendaSettingId":1,"meetRoleId":1,"theme":"开幕致辞","startTime":"00:10","endTime":"01:20","relatedList":[{"companyName":"","relateId":201709785484,"lecturerLevel":"AREA","lecturerLevelText":"区域级讲者", "relateName":"庄董二","relateType":"DOCTOR","hospitalName":"卫生部中日友好医院","openId":"5fd4d26be2e44788b9a9ae0daee9bbba","title":"Resident","titleText":"住院医师","canPaid": False}]},
{"agendaSettingId":1,"meetRoleId":1,"theme":"开幕致辞","startTime":"00:10","endTime":"01:20","relatedList":[{"companyName":"","relateId":201709785484,"lecturerLevel":"AREA","lecturerLevelText":"区域级讲者", "relateName":"庄董二","relateType":"DOCTOR","hospitalName":"卫生部中日友好医院","openId":"5fd4d26be2e44788b9a9ae0daee9bbba","title":"Resident","titleText":"住院医师","canPaid": False}]},
{"agendaSettingId":1,"meetRoleId":1,"theme":"开幕致辞","startTime":"00:10","endTime":"01:20","relatedList":[{"companyName":"","relateId":201709785484,"lecturerLevel":"AREA","lecturerLevelText":"区域级讲者", "relateName":"庄董二","relateType":"DOCTOR","hospitalName":"卫生部中日友好医院","openId":"5fd4d26be2e44788b9a9ae0daee9bbba","title":"Resident","titleText":"住院医师","canPaid": False}]},
{"agendaSettingId":1,"meetRoleId":1,"theme":"开幕致辞","startTime":"00:10","endTime":"01:20","relatedList":[{"companyName":"","relateId":201709785484,"lecturerLevel":"AREA","lecturerLevelText":"区域级讲者", "relateName":"庄董二","relateType":"DOCTOR","hospitalName":"卫生部中日友好医院","openId":"5fd4d26be2e44788b9a9ae0daee9bbba","title":"Resident","titleText":"住院医师","canPaid": False}]},
{"agendaSettingId":1,"meetRoleId":1,"theme":"开幕致辞","startTime":"00:10","endTime":"01:20","relatedList":[{"companyName":"","relateId":201709785484,"lecturerLevel":"AREA","lecturerLevelText":"区域级讲者", "relateName":"庄董二","relateType":"DOCTOR","hospitalName":"卫生部中日友好医院","openId":"5fd4d26be2e44788b9a9ae0daee9bbba","title":"Resident","titleText":"住院医师","canPaid": False}]},
{"agendaSettingId":1,"meetRoleId":1,"theme":"开幕致辞","startTime":"00:10","endTime":"01:20","relatedList":[{"companyName":"","relateId":201709785484,"lecturerLevel":"AREA","lecturerLevelText":"区域级讲者", "relateName":"庄董二","relateType":"DOCTOR","hospitalName":"卫生部中日友好医院","openId":"5fd4d26be2e44788b9a9ae0daee9bbba","title":"Resident","titleText":"住院医师","canPaid": False}]},
{"agendaSettingId":1,"meetRoleId":1,"theme":"开幕致辞","startTime":"00:10","endTime":"01:20","relatedList":[{"companyName":"","relateId":201709785484,"lecturerLevel":"AREA","lecturerLevelText":"区域级讲者", "relateName":"庄董二","relateType":"DOCTOR","hospitalName":"卫生部中日友好医院","openId":"5fd4d26be2e44788b9a9ae0daee9bbba","title":"Resident","titleText":"住院医师","canPaid": False}]},
{"agendaSettingId":1,"meetRoleId":1,"theme":"开幕致辞","startTime":"00:10","endTime":"01:20","relatedList":[{"companyName":"","relateId":201709785484,"lecturerLevel":"AREA","lecturerLevelText":"区域级讲者", "relateName":"庄董二","relateType":"DOCTOR","hospitalName":"卫生部中日友好医院","openId":"5fd4d26be2e44788b9a9ae0daee9bbba","title":"Resident","titleText":"住院医师","canPaid": False}]},
]

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
    action_url = 'https://test-ms.xgjk.info/cms-act-service/act/area/app/save'
    token = APP_token(username)
    headers = {"Accept": "application/json,text/plain, */*",
                     "Content-Type": "application/json;charset=UTF-8",
                     "Authorization": token
                     }
    fram_data = {"activitySignType":"NeedSign",
                 "backgroundDesc":"背景介绍",
                 "breedGroupList":[
                     {"breedGroupId":13,"companyId":2}],
                 "content":"这是活动内容",
                 "departmentList":[
                     {"applyMoney":800,
                      "breedGroupId":13,
                      "budgetTypeId":1,
                      "companyId":2,
                      "departmentId":579}],
                 "headEmployeeId":416,
                 "headEmployeeName":"王娜",
                 "isSubmit":True,
                 "laborCostPlanMeetCount":2,
                 "latitude":"",
                 "longitude":"",
                 "meetAddr":"",
                 "meetClassId":375,
                 "meetClassSubId":"",
                 "name":"西康-新活素-接口造数据-创建时间="+str(date),
                "planEndTime":plandate+" 02:00",
                 "planStartTime":plandate+" 00:00",
                 "planMeetCount":10,
                 "purposeList":[
                     {"purposeId":24,
                      "purposeName":"心好累",
                      "doctorMedicineGradeIds":"1",
                      "doctorMedicineGradeText":None,
                      "doctorAcademicGradeIds":"1",
                      "doctorAcademicGradeText":None,
                      "memo":None,
                      "id":24,
                      "name":"心好累"}],
                 "relateManList":[],
                 "scope":"SINGLE_CITY",
                 "strategyList":[
                     {"id":259,
                      "name":"西康-新活素战略",
                      "memo":"打赏",
                      "hospitalGradeIds":"27",
                      "sectionOfficeIds":"1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,65,66,89,17,76,77,78,18,19",
                      "type":"区域"}],
                 "subjectList":[
                     {"subjectId":33,"remark":"","subjectName":"劳务费","applyMoney":600,"typeId":12,"totalMoney":""},
                     {"subjectId":34,"remark":"","subjectName":"餐费","applyMoney":100,"typeId":12,"totalMoney":""},
                     {"subjectId":35,"remark":"","subjectName":"小食","applyMoney":50,"typeId":12,"totalMoney":""},
                     {"subjectId":36,"remark":"","subjectName":"住宿费","applyMoney":50,"typeId":12,"totalMoney":""}],
                 "specialAuditReason":"",
                 "innerPlan":False,
                 "expensePlanList":[],
                 "subjectCompanyId":2,
                 "doctorList":[],
                 "empViewerList":[],
                 "hospitalId":"",
                 "pics":[],
                 "sectionGuestList":[],
                 "sectionViewerList":[],
                 "agenda":{
                     "activityClassId":375,
                     "activityName":"西康-新活素-接口造数据-创建时间="+str(date),
                     "sessionList":[
                         {
                             "time":plandate,
                             "sessionDetailList":[
                                 {
                                     "agendaSettingId":1,
                                     "meetRoleId":1,
                                     "theme":"开幕致辞",
                                     "startTime":"00:00",
                                     "endTime":"01:00",
                                     "relatedList":[
                                         {
                                             "id":1930,
                                             "sessionDetailId":1568,
                                             "sessionId":856,
                                             "agendaId":561,
                                             "relateId":201709785484,
                                             "relateType":"DOCTOR",
                                             "relateTypeText":"医生",
                                             "relateName":"庄董二",
                                             "companyName":"",
                                             "title":"Resident",
                                             "titleText":"住院医师",
                                             "hospitalName":"卫生部中日友好医院",
                                             "lecturerLevel":"AREA",
                                             "lecturerLevelText":"区域级讲者",
                                             "sendContract":False,
                                             "canPaid":True,
                                             "openId":"5fd4d26be2e44788b9a9ae0daee9bbba"}]},
                                 {
                                     "agendaSettingId":1,
                                     "meetRoleId":1,
                                     "theme":"开幕致辞",
                                     "startTime":"01:00",
                                     "endTime":"02:00",
                                     "relatedList":[
                                         {
                                             "id":1931,
                                             "sessionDetailId":1569,
                                             "sessionId":856,
                                             "agendaId":561,
                                             "relateId":201709785484,
                                             "relateType":"DOCTOR",
                                             "relateTypeText":"医生",
                                             "relateName":"庄董二",
                                             "companyName":"",
                                             "title":"Resident",
                                             "titleText":"住院医师",
                                             "hospitalName":"卫生部中日友好医院",
                                             "lecturerLevel":"AREA",
                                             "lecturerLevelText":"区域级讲者",
                                             "sendContract":False,
                                             "canPaid":True,
                                             "openId":"5fd4d26be2e44788b9a9ae0daee9bbba"}]}]}]},
                 "sponsorIds":[],
                 "contractorIds":[],
                 "id":17262}
    req = requests.post(url=action_url,headers=headers,data=json.dumps(fram_data)).text
    resp = json.loads(req)
    print("新增"+resp['message'])
def findActPlan(username):
    token = APP_token(username)
    headers = {"Accept": "application/json,text/plain, */*",
               "Content-Type": "application/json;charset=UTF-8",
               "Authorization": token
               }
    """查询待审核的单据"""
    url = 'https://test-ms.xgjk.info/cms-act-service/act/area/app/findActPlanList?pageNumber=1&pageSize=8&budgetDate={}&statusList%5B0%5D=DRAFT&statusList%5B1%5D=AUDIT_START&statusList%5B2%5D=AUDIT_BACK&statusList%5B3%5D=AUDIT_WAIT&headEmployeeName=&departmentName=&breedGroupName='.format(month)
    req = requests.get(url=url,headers=headers).text
    resp = json.loads(req)
    # print(resp)
    result = resp['result']
    id_list = []
    for action in result:

        if '西康-新活素-接口造数据-创建时间=' in action['name'] and action['headEmployeeName']=='王娜' and action['status']=='AUDIT_WAIT':
            # print(action)
            id_list.append(action['id'])
    # print(id_list)

    for id in id_list:
        """查询待审单据详情"""
        action_detail_url = 'https://test-ms.xgjk.info/cms-act-service/act/area/app/getDetail?id={}'.format(id)
        req = requests.get(url=action_detail_url,headers=headers).text
        resp = json.loads(req)
        # print(resp)
        planStartTime = resp['planStartTime']
        planEndTime = resp['planEndTime']
        activityid_dict = {}
        for activityid in resp['subjectList']:
            activityid_dict[activityid['subjectId']] = (activityid['id'])
        subjectList1 = {
            "id":activityid_dict[33] ,
            "activityId": id,
            "typeId": 12,
            "typeName": "学术会议费",
            "subjectId": 33,
            "subjectName": "劳务费",
            "initMoney": 600,
            "realMoney": 600, "remark": None,
            "costCompanyId": None,
            "applyMoney": 600}
        subjectList2 = {
                           "id":activityid_dict[34],
                           "activityId":id,
                           "typeId":12,
                           "typeName":"学术会议费",
                           "subjectId":34,
                           "subjectName":"餐费",
                           "initMoney":100,
                           "realMoney":100,
                           "remark":None,
                           "costCompanyId":None,
                           "applyMoney":100}
        subjectList3 = {      "id":activityid_dict[35],
                              "activityId":id,
                              "typeId":12,
                              "typeName":"学术会议费",
                              "subjectId":35,
                              "subjectName":"小食",
                              "initMoney":50,
                              "realMoney":50,
                              "remark":None,
                              "costCompanyId":None,
                              "applyMoney":50}
        subjectList4 = {"id":activityid_dict[36],
                           "activityId":id,
                           "typeId":12,
                           "typeName":"学术会议费",
                           "subjectId":36,
                           "subjectName":"住宿费",
                           "initMoney":50,
                           "realMoney":50,
                           "remark":None,
                           "costCompanyId":None,
                           "applyMoney":50}

        """审核单据"""
        audit_url = 'https://test-ms.xgjk.info/cms-act-service/act/area/app/audit'
        frame_data = {"backgroundDesc":"背景介绍",
                      "content":"这是活动内容",
                      "costCompanyList":[2],
                      "departmentList":[
                          {
                              "applyMoney":800,
                              "breedGroupId":13,
                              "budgetTypeId":1,
                              "companyId":2,
                              "departmentId":579,
                              "hospitalId":None}],
                      "description":"接口自动化审核通过！",
                      "headEmployeeId":416,
                      "headEmployeeName":"王娜",
                      "id":id,
                      "laborCostPlanMeetCount":2,
                      "latitude":"",
                      "longitude":"",
                      "meetAddr":"",
                      "planEndTime":planEndTime,
                      "planMeetCount":10,
                      "planStartTime":planStartTime,
                      "relateManList":[],
                      "subjectList":[subjectList1,subjectList2,subjectList3,subjectList4],
                      "auditStatus":"YES"}
        aa = 'subjectList'
        req = requests.post(url=audit_url,headers=headers,data=json.dumps(frame_data)).text
        resp = json.loads(req)
        print("审核"+resp['message'])


if __name__=='__main__':
    creat_action('ua0000000416')
    findActPlan('ua0000000415')