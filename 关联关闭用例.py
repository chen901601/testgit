#coding=utf8
import json, requests,re,jira,time


"""下列为获取cookie"""

class test_case():
    """初始化jira页面，获取token"""
    def __init__(self):
        self.user = input('请输入Jira账号:')
        self.password = input('请输入Jira密码:')
        login_url = 'http://120.78.205.250:18080/login.jsp'
        payload = {"os_username": self.user,
                   "os_password": self.password,
                   "os_cookie": True,
                   "os_destination": "",
                   "user_role": "",
                   "atl_token": "",
                   "login": "登录"}

        # '''allow_redirects=False表示重定向<Response [302]>，allow_redirects=True表示成功，<Response [200]>'''
        resp = requests.post(login_url, data=payload, allow_redirects=False)
        cookieJsessionId = resp.headers["Set-Cookie"].split(";")[0]
        resp = requests.get(login_url)
        cookie1 = resp.headers["Set-Cookie"].split(";")  # 重定向后后再次发送请求时，去获取请求头的信息 headers
        self.cookieToken = cookie1[0].replace("lout", "lin")
        atl_token_number = self.cookieToken.find("=") #寻找cookieToken字符串中的=号，方便切割字符串
        self.atl_token = self.cookieToken[atl_token_number+1:]  #切除atl_token，为关闭用例做准备

        # 查询接口的cookie的JSESSIONID是由login.jsp这个接口返回，atlassian.xsrf.token是由jira / 这个接口返回
        self.cookie = "jira.editor.user.mode=wysiwyg;" + cookieJsessionId + ";" + self.cookieToken
        self.headers = {'Cookie': self.cookie,
                   'X-Atlassian-Token': 'no-check',
                   'X - Requested - With': 'XMLHttpRequest',
                   'User-Agent': 'wswp'
                   }

        """将jira的Views视图修改成detail view模式，若是list view模式，则下面的部分url会有错，所以必须修改成detail view模式"""
        try:
            change_view_url = 'http://120.78.205.250:18080/rest/issueNav/latest/preferredSearchLayout'
            form_data = {'layoutKey': 'split-view'}
            req = requests.post(url=change_view_url, headers=self.headers, data=form_data)
        except:
            print("Views视图修改出错，请重试或找脚本开发人员调试代码！")


    """根据用例id查询用例的详情，主要是要查出该用例关联的主任务号 CMS001-18847"""
    def find_case_detail(self,case_id):
        try:
            detail_url = 'http://120.78.205.250:18080/secure/AjaxIssueEditAction!default.jspa?decorator=none&issueId={}&_=1535173369870'.format(case_id)
            detail_req = requests.post(url=detail_url, headers=self.headers)
            req_json = json.loads(detail_req.text)
            fields = req_json['fields']

            """下面的代码只是为了方便查找想要的内容在fields的第几个元素"""
            # j=0
            # for i in fields:
            #     print(j)
            #     print(i)
            #     j+=1

            task_key = fields[10]
            editHtml = task_key['editHtml']
            # print(editHtml)
            task_number = re.findall('(.*?)</textarea>', editHtml)[0]

            task_number_code = re.findall('CMS001-\w+', task_number)  # 拿到康哲项目主任务号  \w+贪婪匹配全数字
            if task_number_code==[]:  #如果拿不到康哲项目主任号，就是玄关项目
                task_number_code = re.findall('XG001-\w+', task_number)  # 拿到玄关主任务号

            main_vesion = fields[14]
            version_editHtml = main_vesion['editHtml']
            version_number = re.findall('value="(.*?)" />', version_editHtml)[0]

            return [task_number_code[0], version_number]  # 返回列表的第一个元素是用例要关联的主任务号，第二个元素是用例的版本号

        except Exception as e:
            print('这是错误的脚本代码:', e)
            print('It is have a error when find main task number!')


    """查找用例"""
    def find_case(self):
        self.case_version = input("请输入要操作那个版本的用例，如(2.4.0):")

        """以下的case_first_url主要是为了查找总用例数"""
        """statu是寻找（未开始）状态的用例"""
        if self.action_code=="1":#关联用例时，查的是所有状态的用例
            case_first_url = 'http://120.78.205.250:18080/issues/?jql=project%20%3D%20CS%20AND%20issuetype%20%3D%20%E6%B5%8B%E8%AF%95%E7%94%A8%E4%BE%8B%20AND%20resolution%20%3D%20Unresolved%20AND%20fixVersion%20%3D%20{}%20AND%20assignee%20in%20(currentUser())%20order%20by%20updated%20DESC'.format(self.case_version)
        else:#关闭用例时，查询的范围是用例状态=（未开始，测试环境通过）
            case_first_url = 'http://120.78.205.250:18080/issues/?jql=project%20%3D%20CS%20AND%20issuetype%20%3D%20%E6%B5%8B%E8%AF%95%E7%94%A8%E4%BE%8B%20AND%20status%20in%20(%E6%9C%AA%E5%BC%80%E5%A7%8B%2C%20%E6%B5%8B%E8%AF%95%E7%8E%AF%E5%A2%83%E9%80%9A%E8%BF%87)%20AND%20resolution%20%3D%20Unresolved%20AND%20fixVersion%20%3D%20{}%20AND%20assignee%20in%20(currentUser())%20order%20by%20updated%20DESC'.format(self.case_version)
        req_first = requests.get(url=case_first_url, headers=self.headers)
        try:
            self.total_case = re.findall('total&quot;:(.*?),&quot;', req_first.text)[0]
        except:
            if self.action_code=="1":
                text_word = "关联"
            elif self.action_code=="2":
                text_word = "关闭"
            print("未找到{}版本的测试用例，请登录Jira确认后再进行{}用例操作！".format(self.case_version,text_word))
            exit()
        case_sum_list = []
        for index in range(1, int(self.total_case), 50):
            try:
                """每次展示50条，所以startIndex都要是50的间隔"""
                if self.action_code=='1':#关联用例时寻找的是所有状态的用例。
                    case_url = 'http://120.78.205.250:18080/issues/?jql=project%20%3D%20CS%20AND%20issuetype%20%3D%20%E6%B5%8B%E8%AF%95%E7%94%A8%E4%BE%8B%20AND%20resolution%20%3D%20Unresolved%20AND%20fixVersion%20%3D%20{}%20AND%20assignee%20in%20(currentUser())%20order%20by%20updated%20DESC&startIndex={}'.format(self.case_version, index)
                else:#关闭用例时寻找的是状态=（未开始，测试环境通过）的用例。
                    case_url = 'http://120.78.205.250:18080/issues/?jql=project%20%3D%20CS%20AND%20issuetype%20%3D%20%E6%B5%8B%E8%AF%95%E7%94%A8%E4%BE%8B%20AND%20status%20in%20(%E6%9C%AA%E5%BC%80%E5%A7%8B%2C%20%E6%B5%8B%E8%AF%95%E7%8E%AF%E5%A2%83%E9%80%9A%E8%BF%87)%20AND%20resolution%20%3D%20Unresolved%20AND%20fixVersion%20%3D%20{}%20AND%20assignee%20in%20(currentUser())%20order%20by%20updated%20DESC&startIndex={}'.format(self.case_version, index)
                req = requests.get(url=case_url, headers=self.headers)
                case_sum = re.findall('<ol class="issue-list">(.*?)<div class="pagination-container aui-item">', req.text)[0]
                case_single = re.findall('<li(.*?)</li>', case_sum)
                for case in case_single:
                    data_id = re.findall('data-id="(.*?)"', case)[0]  # 获取用例的id
                    data_key = re.findall('data-key="(.*?)"', case)[0]  # 获取用例的任务号
                    title = re.findall('title="(.*?)"', case)[0]  # 获取用例的标题
                    if self.action_code=="1":  #关联主任务时，需要去查用例要关联的主任务编号，需要调用find_case_detail函数
                        test_detail = self.find_case_detail(data_id)
                        inner_case_list = [data_id, data_key, title, test_detail[0],test_detail[1]]  # 第0个元素：用例id，第1个元素：用例号。第2个元素：用例标题，第3个元素：用例要管联的主任务号，第4个元素：用例的版本号
                        case_sum_list.append(inner_case_list)
                    elif self.action_code=="2": #关闭用例时不需要查询主任务编号，不需要调用find_case_detail，提高效率
                        inner_case_list = [data_id, data_key, title]  # 第0个元素：用例id，第1个元素：用例号。第2个元素：用例标题
                        case_sum_list.append(inner_case_list)
            except:
                print('查询测试用例的url有错误')
                break
        return case_sum_list

    """将用例关联主任务"""
    def link_case(self, link_sum=0):  # CS-26887    CS-26889
        case_totle = self.find_case()
        print("当前版本需要关联用例数为{}".format(self.total_case))
        if int(self.total_case)==0:
            exit()
        print("正在关联{}版本用例，请耐心等待...".format(self.case_version))
        for inner_case_list in case_totle:
            try:
                link_url = 'http://120.78.205.250:18080/secure/LinkJiraIssue.jspa'
                form_data = {'inline': 'true',
                             'decorator': 'dialog',
                             'atl_token': self.cookieToken,
                             'id': inner_case_list[0],  #用例id
                             'jiraAppId': '',
                             'linkDesc': 'blocks',
                             'issueKeys': inner_case_list[3], #主任务编号
                             'comment': '',
                             'commentLevel': ''
                             }
                req = requests.post(url=link_url, headers=self.headers, data=form_data)
                link_sum += 1
                print("已关联第"+str(link_sum)+"条用例")

            except Exception as e:
                print('这是错误的脚本代码:', e)
                print('it have a error when link the main task!')
        return link_sum

    """关闭用例"""
    def close_case_task(self,unusual_case):
        """关闭【测试用例】任务，请求方式POST"""
        case_totle = self.find_case()
        print("当前版本需要关闭用例数为{}".format(self.total_case))
        if int(self.total_case)==0:
            exit()
        print("正在关闭{}版本用例，请耐心等待...".format(self.case_version))
        Jiras = {
            'url': "http://120.78.205.250:18080",  # jira地址
            'username': self.user,  # 登录账号
            'password': self.password,  # 登录密码
        }

        myjira = jira.JIRA(Jiras['url'], basic_auth=(Jiras['username'], Jiras['password']))  # 创建jira链接
        for inner_case_list in case_totle:
            myissues = myjira.issue(inner_case_list[1])
            status = str(myissues.fields.status)
            update_url = 'http://120.78.205.250:18080/secure/WorkflowUIDispatcher.jspa'
            if status == "未开始":
                # print("用例id={}".format(int(inner_case_list[0]))) #打印用例的id
                paramt_data = {"id": int(inner_case_list[0]),
                               "action": 11,  # 11点击测试环境通过      41点击演示环境通过
                               "atl_token": self.atl_token}
                req_1 = requests.post(url=update_url, headers=self.headers, data=paramt_data)
                myissues = myjira.issue(inner_case_list[1]) #每执行一次myjira.issue，就会获取一次数据缓存在myjira.issue中
                status = str(myissues.fields.status) #如果状态改变后，需要再次获取用例的状态，例如当前用例的状态=未开始，满足当前条件，执行该代码后状态变为=测试环境通过，此时要再次获取状态
                print(inner_case_list[1]+status)
            if status == "测试环境通过":
                paramt_data = {"id": int(inner_case_list[0]),
                               "action": 41,  # 11点击测试环境通过      41点击演示环境通过
                               "atl_token": self.atl_token}
                req_1 = requests.post(url=update_url, headers=self.headers, data=paramt_data)
                myissues = myjira.issue(inner_case_list[1])
                status = str(myissues.fields.status)
                print(inner_case_list[1] + status)
            if status == "已完成":
                pass
            else:
                unusual_case.append(inner_case_list[1])
        return unusual_case


    def main(self):
        self.action_code = input("请输入您要操作的类型，关联用例请输入1，关闭用例请输入2 ： ")
        unusual_case = []
        while 1:
            if self.action_code=="1":
                self.link_case()
                break
            elif self.action_code=="2":
                un_case_list = self.close_case_task(unusual_case)
                if len(un_case_list)>0: #判断关闭用例是否有存在异常的，若存在则打印出来
                    print(un_case_list)
                break
            else:
                self.action_code = input("您输入的类型数据没有对应的功能！\n请重新输入，关联用例请输入1，关闭用例请输入2 ：")
        print("已完成。")



if __name__=="__main__":
    act= test_case() #类的实例化
    act.main()

    # threads = []
    # step = 5
    # total_case_new = [total_case[i:i + step] for i in range(0, len(total_case), step)]
    # for total_case in total_case_new:
    #     t = Thread(target=target_def, agrs=(total_case,))
    #     threads.append(t)
    #     t.start()
    # for t in threads:
    #     t.join()