"""
 多行注释
"""
"""
123
"""

"""
print("123456789")
# 单行注释
print("123456678985231466")
money = 50
print("钱包：",money)
money = money-10
print("钱包更新：",money)
print(type(money))
num = 100
str_num = str(num)
print(type(str_num))
asd=123
print(asd)
_floyd = '董配军'


print(_floyd)
print("指数运算", 2**50);
message = 'floydw'
print("这个字符为：%s" %message)

"""
"""
input的返回值为字符型
num = input()
int_num=int(num)
if int_num>10:
    print("你输入的值太小了")
    print(f"你输入的值为{int_num}")
else:
    int_num=int_num+10
    print("现在的值为：%d"%int_num)
"""


# name = input("请输入你的姓名：")
# if name == 'floyd':
#     print("你是董配军，我认识你！")
# elif name == 'lyy':
#     print("你是王运，我认识你！")
# else:
#     print("不好意思我不认识你！")

# import random
# num = random.randint(1,10)
# if int(input("请输入你猜想的第一次数据：")) == num:
#     print("你猜对啦！")
# elif int(input("请输入你猜想的第二次是值：")) == num:
#     print("你猜对啦！")
# elif int(input("请输入你猜想的第三次的值为：")) == num:
#     print("你猜对啦！")
# else:
#     print(f"你三次都猜错了，我的值为{num}")

# i = 0
# sum = 0
# while i <= 100000:
#     print("向小美表白第%d次："%i)
#     i = i+1
#     sum =sum+i
# print(sum)

# import random
# num = random.randint(1,100)
# i = 0
# while i <= 100:
#     if i!=num:
#         i=i+1
#     else:
#         print("你猜对了：%d"%i)
#         break

#九九乘法表
j = 1
while j < 10:
    i = 1
    while i <= j:
        k = i*j
        print(f"{i}*{j}={k}",end='  ')
        i=i+1
    print()
    j=j+1

# i = 123456789
# for sum in i:
#     j = 1
#     while j <= i:
#         sum = j*i
#         print(sum,end='   ')
#     print()

