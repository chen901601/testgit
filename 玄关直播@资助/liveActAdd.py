# -*- coding: utf-8 -*
#@Time:2020/5/27 16:09
#@Auther:chenyr

import requests,urllib,json
from cms_ERP.xg_live.xgAppGetToken import getToken
from datetime import datetime, timedelta

date = datetime.now()
month = date.strftime("%Y-%m")
print(month)
date = date + timedelta(days=1)
date = date.strftime("%Y-%m-%d")

print(date)

#根据讲者的名字查找讲者的信息
def getSpeakerDetail(name='刘琦'):  #普通讲者：刘琦   特邀讲者：陈明
    """Request Method: GET"""

    #中文转换url编码  urllib.parse.quote(name)
    #url编码转回中文  urllib.parse.unquote("%E5%88%98%E7%90%A6")
    nameUTF8 = urllib.parse.quote(name)

    url = 'http://testdragon-ms.xgjk.info/dragon-customer/customer/doctor/findLecturerPageList?' \
          'doctorName={}&hospitalId=&pageNumber=1&pageSize=20'.format(nameUTF8)

    headers = {"Accept": "application/json,text/plain, */*",
                     "Content-Type": "application/json;charset=UTF-8",
                     "Authorization": getToken()
                     }

    result = requests.get(url = url,headers=headers).json()
    doctorDetail = result['result'][0]
    speakerId = doctorDetail['id']
    lecturerMoney = doctorDetail['lecturerMoney']
    specialLecturerMoney = doctorDetail['specialLecturerMoney']

    #如果特殊劳务费值不为None,则说明是特邀讲者，劳务费使用特邀讲者劳务费
    if specialLecturerMoney != None:
        dcctor = {"speakerId":speakerId,"serviceFee":specialLecturerMoney,"speakerType":"特邀讲者"}
    # 如果特殊劳务费值为None,则说明是普通讲者，劳务费=普通讲者基础金额+最高奖励金额
    else:
        dcctor = {"speakerId":speakerId,"serviceFee":lecturerMoney+1000,"speakerType":"普通讲者"}
    return dcctor

#添加直播活动
def addLive():
    """Request Method: POST"""

    url = "http://testdragon-ms.xgjk.info/dragon-act/act/support/app/add"
    headers = {"Accept": "application/json,text/plain, */*",
                     "Content-Type": "application/json;charset=UTF-8",
                     "Authorization": getToken()
                     }
    data = {
            "fieldComm":{
                "applyDeptId":28,
                "applyDesc":"申请说明-自动化生成",
                "budgetDeptId":28,
                "budgetTypeId":"1",
                "circleId":"",
                "isSubmit":False,
                "labelContent":"直播事由03-下级01",
                "liveMonth":month,
                "liveEndTime":date + " 20:00",
                "liveStartTime":date + " 14:00",
                "payLaborCost":True,
                "picList":[

                ],
                "productId":"3",
                "secondWorkProjectId":28,
                "speakerId":getSpeakerDetail()['speakerId'],
                "subjectList":[
                    {
                        "money":100,
                        "subjectId":90
                    },
                    {
                        "money":500,
                        "subjectId":97
                    },
                    {
                        "money":getSpeakerDetail()['serviceFee'],
                        "subjectId":98
                    }
                ],
                "topic":getSpeakerDetail()['speakerType']+datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "useBudget":True
            }
        }
    result = requests.post(url=url,headers=headers,data=json.dumps(data)).json()
    print(result)

if __name__=="__main__":
    addLive()