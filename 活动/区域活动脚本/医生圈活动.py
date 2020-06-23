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
    type_dict = {22:'直播',23:'视频',24:'微学堂',26:'大讲堂',358:'常出现',379:'外部线上-阿牛专用'}
    token = APP_token(username)
    type_url = 'https://test-ms.xgjk.info/cms-act-service/act/area/app/findActivityType'
    headers = {"Accept": "application/json,text/plain, */*",
               "Content-Type": "application/json;charset=UTF-8",
               "Authorization": token
               }
    action_url = 'https://test-ms.xgjk.info/cms-act-service/act/area/app/update'
    for type_id in type_dict.items(): #type_dict.items  items字典循环打印key和value  type_dict.key  打印key  type_dict.value打印value
        type_req = requests.get(url=type_url,headers=headers).text
        type_resp = json.loads(type_req)
        lenth = len(type_resp)
        times = 0
        for ty in type_resp:
            times+=1
            # print(ty['id'],type(ty['id']))
            if ty['id']==type_id[0]:#判断写死的活动类型id在系统中存在否
                if ty['name']==type_id[1]:#判断写死的活动类型名称在系统中存在否
                    """活动目的获取"""
                    class_url = 'https://test-ms.xgjk.info/cms-act-service/act/purpose/findListByMeetClass?meetClassId={}'.format(ty['id'])
                    calss_req = requests.get(url=class_url, headers=headers).text
                    calss_resp = json.loads(calss_req)
                    if calss_resp!= None:
                        purposeList = calss_resp[-1]
                        action_url = 'https://test-ms.xgjk.info/cms-act-service/act/area/app/save'
                        fram_data = {"activitySignType": "NeedSign",
                                     "backgroundDesc": "背景介绍",
                                     "breedGroupList": [
                                         {"breedGroupId": 6, "companyId": 1}],
                                     "content": "这是活动内容",
                                     "departmentList": [
                                         {"applyMoney": 800,
                                          "breedGroupId": 6,
                                          "budgetTypeId": 1,
                                          "companyId": 1,
                                          "departmentId": 72}],
                                     "headEmployeeId": 416,
                                     "headEmployeeName": "王娜",
                                     "isSubmit": True,
                                     "laborCostPlanMeetCount": 1,
                                     "latitude": "",
                                     "longitude": "",
                                     "meetAddr": "",
                                     "meetClassId": ty['id'],
                                     "meetClassSubId": "",
                                     "name": ty['name']+"活动，接口造数据-创建时间=" + str(date),
                                     "planEndTime": plandate + " 02:00",
                                     "planStartTime": plandate + " 00:00",
                                     "planMeetCount": 9,
                                     "purposeList": [purposeList],
                                     "relateManList": [],
                                     "scope": "SINGLE_CITY",
                                     "strategyList": [
                                         {"id": 186, "name": "辽宁区域黛力新123", "memo": "战略说明456", "hospitalGradeIds": "27",
                                          "sectionOfficeIds": "1,6,7,8,9,10,11,12,13,14,15,16,65,66,89", "type": "区域"}],
                                     "subjectList": [
                                         {"subjectId": 33, "remark": None, "subjectName": "劳务费", "applyMoney": 600,
                                          "typeId": 12},
                                         {"subjectId": 34, "remark": None, "subjectName": "餐费", "applyMoney": 100,
                                          "typeId": 12},
                                         {"subjectId": 35, "remark": None, "subjectName": "小食", "applyMoney": 50,
                                          "typeId": 12},
                                         {"subjectId": 36, "remark": None, "subjectName": "住宿费", "applyMoney": 50,
                                          "typeId": 12}],
                                     "specialAuditReason": "",
                                     "innerPlan": False,
                                     "expensePlanList": [],
                                     "subjectCompanyId": 1,
                                     "doctorList": [],
                                     "empViewerList": [],
                                     "hospitalId": "",
                                     "pics": [],
                                     "sectionGuestList": [],
                                     "sectionViewerList": [],
                                     "agenda": {
                                         "activityClassId": ty['id'],
                                         "activityName": ty['name']+"活动，接口造数据-创建时间=" + str(date),
                                         "sessionList": [
                                             {"time": plandate,
                                              "sessionDetailList": [
                                                  {"agendaSettingId": 1, "meetRoleId": 1, "theme": "开幕致辞",
                                                   "startTime": "00:00", "endTime": "01:00", "relatedList": [
                                                      {"companyName": "", "relateId": 201503290066,
                                                       "lecturerLevel": "CITY", "lecturerLevelText": "城市级讲者",
                                                       "relateName": "黄小乐", "relateType": "DOCTOR",
                                                       "hospitalName": "宁波大学医学院附属医院（宁波三院）",
                                                       "openId": "0377c96ea54743ab961b4165a85f7d12",
                                                       "title": "Resident", "titleText": "住院医师", "canPaid": True}]},
                                                  {"agendaSettingId": 1, "meetRoleId": 1, "theme": "开幕致辞",
                                                   "startTime": "01:00", "endTime": "02:00", "relatedList": [
                                                      {"companyName": "", "relateId": 201503290066,
                                                       "lecturerLevel": "CITY", "lecturerLevelText": "城市级讲者",
                                                       "relateName": "黄小乐", "relateType": "DOCTOR",
                                                       "hospitalName": "宁波大学医学院附属医院（宁波三院）",
                                                       "openId": "0377c96ea54743ab961b4165a85f7d12",
                                                       "title": "Resident", "titleText": "住院医师", "canPaid": False}]}

                                              ]}]},
                                     "sponsorIds": [],
                                     "contractorIds": [],
                                     "id": 17237}
                        req = requests.post(url=action_url,headers=headers,data=json.dumps(fram_data)).text
                        resp = json.loads(req)
                        print("新增"+ty['name']+"活动"+resp['message'])
                    else:
                        print("选择的"+str(ty['name'])+'没有活动目的！')
                else:
                    if times <= lenth:  #将写死的活动类型名称与系统中存在的名称循环对比，直到对比全部了仍不存在时抛出错误提示
                        continue
                    else:
                        print("活动类型id=" + str(type_id[0]) + "对应的类型名称不是"+str(type_id[1]))
            else:
                if times<=lenth:#将写死的活动类型id与系统中存在的id循环对比，直到对比全部了仍不存在时抛出错误提示
                    continue
                else:
                    print("活动类型id:"+str(type_id[0])+"不存在！")




if __name__=='__main__':
    creat_action('ua0000000416')