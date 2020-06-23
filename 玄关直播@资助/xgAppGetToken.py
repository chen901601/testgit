# -*- coding: utf-8 -*
#@Time:2020/5/27 16:40
#@Auther:chenyr.

import requests,json


def getToken(usrname="13613079832",passwd="888888"):
    """Request Method: POST"""
    url = "http://testdragon-ms.xgjk.info/dragon-security/auth/app/login"
    headers = {
                'Accept': 'application/json, text/plain, */*',
                'Content-Type': 'application/json;charset=UTF-8',
             }
    data = {
        "username":usrname,
        "password":passwd,
        "isBind":"NO"
            }
    result = requests.post(url=url, headers=headers, data= json.dumps(data)).json()
    token = result['value']['token']

    return token
