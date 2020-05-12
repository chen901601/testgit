# -*- coding:utf-8 -*-
import pytest
# def test_passing():
#     assert (1, 2, 3) == (1, 2, 3)
#
#
# def test_failing():
#     assert (1, 2, 3) == (3, 2, 1)

import requests,json,os
curpath = os.path.dirname(os.path.realpath(__file__))

def send_param(name):
    print(name)
    def inner(fun):
        filename = os.path.join(curpath,'data.txt')
        with open(filename,'r+') as f:
            filedetail = f.read()
            file_list = filedetail.split(',')

            print(file_list)
        def warp(agrs=file_list, **kwagrs):
            fun(*agrs, **kwagrs)
        return warp
    return inner


@send_param(1)
def test_main(param1=1,param2=2):
    print(param1)
    print(param2)
