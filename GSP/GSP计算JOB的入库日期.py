from datetime import datetime, timedelta
import time

date = datetime.now()
print("当前日期为："+date.strftime("%Y-%m-%d"))
type_code = input("1：批号有效期/30N后的当前日期，2：需要的当前时间，3：批号有效日期，4：指定日期加指定天数后的日期：\n")
if type_code=="1":
    expiryDate = input("请输入批号有效日期：")
    expiryDate = expiryDate+" 00:00:00"
    expiryDate = datetime.strptime(expiryDate, "%Y-%m-%d %H:%M:%S")
    diff_day = (expiryDate - date).days
    if diff_day>0:
        score = diff_day//30
        for i in range(score,0,-1):
            nowday = expiryDate-timedelta(days=int(i*30))
            if (expiryDate - nowday).days <= 180:
                print("满足批号有效期-当前日期=30的第{}当前时间为：{}".format((score-i),nowday))

    # for i in range(5):
    #     nowdate = date+timedelta(days=int(adddays))
    # adddate = date+timedelta(days=int(adddays))
    # print(adddate.strftime("%Y-%m-%d %H:%M:%S"))
elif type_code=="2":
    indays = input("在库时间：")#在库时间
    value = input("要整除的倍数：") #整除的倍数
    entrydate = input("入库时间：")+" 00:00:00"
    entrydate = datetime.strptime(entrydate, "%Y-%m-%d %H:%M:%S")
    remainder = 0#默认余数为0
    n_date = entrydate+timedelta(days=int(indays))
    print("满足（当前时间-入库时间=在库时间）的当前时间为：{}".format((datetime.strftime(n_date,"%Y-%m-%d"))+" 00:00:00"))
    for mul in range(1,30):
        days = int(indays)+int(value)*mul+int(remainder)
        nowdate = entrydate+timedelta(days=days)
        print("第{}个当前时间为：{}".format(mul,nowdate.strftime("%Y-%m-%d %H:%M:%S")))
elif type_code=="3":
    nowdate = input("请输入当前日期：")
    i = 1
    while 1:
        if 30*i<180:
            expdate = datetime.strptime(nowdate,"%Y-%m-%d")
            expdate = expdate+timedelta(days=int(30*i))
            print("第{}个批号的有效期为：{}".format(i,expdate))
            i +=1
        else:
            break

elif type_code=="4":
    the_days = input("请输入指定日期，格式为xxxx-xx-xx：")
    the_days = datetime.strptime(the_days,"%Y-%m-%d")
    add_days = input("请输入需要加的天数：")
    after_days = the_days + timedelta(days=int(add_days))
    print(after_days)

