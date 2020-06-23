import requests,json
from datetime import datetime
from time import sleep

"""
import datetime
datetime.datetime.now().year  获取当前年
datetime.datetime.now().month 获取当前月
datetime.datetime.now().day   获取当前日
"""
now_yeas = datetime.now().year
now_month = datetime.now().month
if now_month in (1,2,3):
    now_season = 1
elif now_month in (4,5,6):
    now_season = 2
elif now_month in (7,8,9):
    now_season = 3
elif now_month in (10,11,12):
    now_season = 4
date = datetime.now()

date = date.strftime("%Y-%m-%d %H:%M:%S")

"""把datetime转成字符串 :statrtime.strftime("%Y-%m-%d %H:%M:%S")"""
date=datetime.strptime(date, "%Y-%m-%d %H:%M:%S")


def PC_token(username, password='888888'):
    """作用：根提供的账号密码获取PC-token"""
    """请求方式:POST"""
    pc_token_url = 'http://test-ms.xgjk.info/cms-auth/auth/pc/login'
    request_headers = {'Accept': 'application/json, text/plain, */*',
                       'Content-Type': 'application/json;charset=UTF-8',
                       }
    param_fram = {"username": username,
                  "password": password,
                  "captchaValue": "9999",
                  "captchaKey": "yvkpYGzQYgEX7Wd4"
                  }
    request = requests.post(url=pc_token_url, headers=request_headers, data=json.dumps(param_fram)).text
    response = json.loads(request)
    value = response.get('value')
    token = value.get('token')
    # print(token)
    return token

def add_plan(user):
    """添加季度总部费用计划"""
    date = datetime.now()
    date = date.strftime("%Y-%m-%d %H:%M:%S")
    """把datetime转成字符串 :statrtime.strftime("%Y-%m-%d %H:%M:%S")"""
    date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    token = PC_token(user)
    add_url = 'http://test-ms.xgjk.info/cms-cost-service/cost/plan/costPlanSeasonHQAct/saveAndSubmit'
    headers = {'Accept': 'application/json, text/plain, */*',
               'Content-Type': 'application/json;charset=UTF-8',
               "Authorization": token
               }
    formdata = {"breedGroupId":6,
                "companyId":1,
                "departmentId":72,
                "year":"2019",
                "season":3,
                "details":[
                    {
                        "categoryId":74,
                        "hqCostPlanType":"C11",
                        "memo":"备注",
                        "planMoney":"1000",
                        "platformLevel":"false",
                        "projectName":"这是接口造数据"+str(date),
                        "strategyId":32}
                ]
                }
    req = requests.post(url=add_url,headers=headers,data=json.dumps(formdata)).text
    resp = json.loads(req)
    print("新增总部活动费用计划"+resp['message'])

def find_plan(user):
    """寻找待审的总部季度费用计划并审核通过"""
    token = PC_token(user)
    find_url = 'http://test-ms.xgjk.info/cms-cost-service/cost/plan/costPlanSeasonHQAct/findPageResult?pageNumber=1&pageSize=10&companyId=1&departmentId=&breedGroupId=&hqCostPlanType=&strategyId=&hasYearPlan=&year={}&season={}&state=&myTask=true&export=false'.format(now_yeas,now_season)
    headers = {'Accept': 'application/json, text/plain, */*',
               'Content-Type': 'application/json;charset=UTF-8',
               "Authorization": token
               }
    req = requests.get(url=find_url,headers=headers).text
    resp = json.loads(req)
    resp = resp['result']
    id_list1 = []
    id_list2 = []
    for code in resp:
        # print(code)
        if code['state']=='WAIT' and code['departmentName']=='丹东心一区':
            id_list1.append(code['id'])
        elif code['state']=='AUDIT_START' and code['departmentName']=='丹东心一区':
            id_list2.append(code['id'])
    """审核待审核的单据"""
    audit_url = 'https://test-ms.xgjk.info/cms-cost-service/cost/plan/costPlanSeasonHQAct/audit'
    for id in id_list1:
        formdata = {"auditStatus": "YES",
                    "id": id,
                    "memo": ""
                    }
        req = requests.post(url=audit_url, headers=headers, data=json.dumps(formdata)).text
        resp = json.loads(req)
        print("待审核的单据审核" + resp['message'])

    """审核待审核中的单据"""
    id_list = id_list1+id_list2
    for id in id_list:
        formdata = {"auditStatus":"YES",
                    "id":id,
                    "memo":""
                    }
        req = requests.post(url=audit_url, headers=headers, data=json.dumps(formdata)).text
        resp = json.loads(req)
        print("审核中的单据最终审核"+resp['message'])


if __name__=="__main__":
    for i in range(10):
        add_plan('ua0000003764')
        find_plan('ua0000003764')
        sleep(0.5)