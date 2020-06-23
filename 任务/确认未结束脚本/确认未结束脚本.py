#coding=utf8
import requests,json,threading
from datetime import datetime, timedelta
lock = threading.Lock()

number=0

"""环境配置"""
config = 'pre' #开发环境dev  测试环境test 演示环境pre

def APP_token(username, password='888888'):
    """作用：根提供的账号密码获取APP-token"""
    """请求方式:POST"""
    app_token_url = 'https://{}-ms.xgjk.info/cms-auth/auth/app/login'.format(config)
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
    return token
class over():
    def find_not_over(self,user):
        # url = 'https://pre-ms.xgjk.info/cms-cost-service/cost/apply/lastYearWaitingBill/findWaitingBillPageResult?pageNumber=1&pageSize=10000&billType=ACTION_TASK'
        url = 'https://{}-ms.xgjk.info/cms-cost-service/cost/apply/lastYearWaitingBill/findWaitingBillPageResult?pageNumber=1&pageSize=10000&billType=ACTION_TASK'.format(config)

        """指定查询的日期"""
        # url = 'http://192.168.8.112:18003/cost/apply/lastYearWaitingBill/findWaitingBillPageResult?pageSize=10000&pageNumber=1&billType=ACTION_TASK&month=2020-04'
        self.request_headers = {'Accept': 'application/json, text/plain, */*',
                           'Content-Type': 'application/json;charset=UTF-8',
                           'Authorization': APP_token(user)
                           }
        req_list = requests.get(url=url,headers=self.request_headers).json()['result']
        return req_list

    def sure_not_over(self,id_list):
        global number
        not_over_url = 'https://{}-ms.xgjk.info/cms-cost-service/cost/apply/lastYearWaitingBill/saveAndSubmit'.format(config)
        for data in id_list:
            date = datetime.now()
            sure_date = date.strftime("%Y-%m-%d %H:%M:%S")
            parameters = {"billType":data['billType'],
                      "budgetMonth":data['budgetMonth'],
                      "memo":"接口确认未结束,确认时间为："+sure_date,
                      "sourceId":data['sourceId'],
                      "title":data['title']
                        }
            req = requests.post(url=not_over_url,headers=self.request_headers,data=json.dumps(parameters)).json()
            lock.acquire()  # 加锁
            number += 1
            print(number,req)
            lock.release()  # 释放锁

if __name__=='__main__':
    tt = over()
    all_is_list = tt.find_not_over('ua0000000416')   #输入需要确认未结束的账号
    step = 1
    new_id_list = [all_is_list[i:i+step] for i in range(0,len(all_is_list),step)]

    for id_list in new_id_list:
        t = threading.Thread(target=tt.sure_not_over,args=(id_list,))
        t.start()


