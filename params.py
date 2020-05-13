import requests,json,os

curpath = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(curpath,'data.txt')


def log(username,password):
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

def send_param(paramlist):
    try:
        paramlist[0]
    except Exception:
        print("The parameter list of 'paramlist' has a argument at least,but get 0 actual" )
        exit()
    def inner(fun):
        """读取文件"""
        with open(paramlist[0],'r+') as f:
            filedetail = f.read()
            file_list = filedetail.split(',')
        del[paramlist[0]]  # 去掉传参的第一个元素，即读取文件的元素
        def warp(*agrs, **kwagrs):
            for file_element in file_list: #根据读取的配置文件，如果有多组就多次执行目标函数
                file_element = [file_element]
                if len(paramlist) > 0:
                    for data in paramlist:
                        file_element.append(data)  # 重新组成agrs列表
                    agrs = file_element
                    fun(*agrs, **kwagrs)
        return warp
    return inner

@send_param([filename,log("ua0000000416","888888")])
def main(month,token):
    url = "https://test-ms.xgjk.info/cms-act-service/act/area/app/findActPlanList?pageNumber=1&pageSize=8&budgetDate={}&headEmployeeName=&departmentName=&breedGroupName=".format(month)
    headers = {"Accept": "application/json,text/plain, */*",
                     "Content-Type": "application/json;charset=UTF-8",
                     "Authorization": token
                     }
    req = requests.get(url=url, headers=headers).json()
    print(req)

if __name__=="__main__":
    main()

