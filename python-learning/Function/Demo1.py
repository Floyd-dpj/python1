# name = input("请输入姓名:")
# money = 5000000
# def look():
#     print(f"账户当前余额为：{money}")
#     caidan()
# def addmoney(add):
#     global money
#     money = money + add
#     caidan()
#     print(f"当前账户余额为{money}")
# def reducemoney(reduce):
#     global money
#     money = money -reduce
#     caidan()
#     print(money)
#     print(f"当前账户余额为：{money}")
# def caidan():
#     print("当前以返回主菜单！")
#
# while money :
#     print("我要存钱！")
#     add = input("存款金额为：")
#     i_add = int(add)
#     addmoney(i_add)
#     break
# try:
#     f = open("D:/test.txt", 'r', encoding='UTF-8')
# except:
#     pass
#     f = open('D:/test.txt', 'w', encoding='UTF-8')
import time
# from Function import my_module
# my_module.test(1, 2)
# from Function import *
# my_module.test(5, 6)
import json
data = [{'name': '张大山', 'age': 45}, {"name": '章顶点', 'age': 15}]
#json_str = json.dumps(data, ensure_ascii=False)
json_str = json.dumps(data)
print(type(json_str))
print(json_str)
s = json.loads(json_str)
print(s)
