import requests
import json

# class invest():
# 查询产品详情
def check_invest_list():
    url = "http://internal-private-dgruop-924110274.ap-northeast-1.elb.amazonaws.com/kimpper-invest/production/query/productions"
    headers = {
        # "Content-Type": "application/x-www-form-urlencoded",
        "device-id": "1",
        "x-uuid": "86f4bcc4-bab7-47cf-a150-b402497a5cea",
            }
    res = requests.get(url=url,headers=headers)
    res_json = res.json()
    print(res_json)
    itemNo = res_json["data"]["fixProductions"]["All"][0]["itemNo"]
    return itemNo
item = check_invest_list()
print(item)

# 购买产品
# def Subscription():


# 刘威上传代码测试binance