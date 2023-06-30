def outer(func):
    def inner():
        print("我睡觉了")
        func()
        print("我起床了！")
    return inner

@outer
def sleep():
    import random
    import time
    print("睡觉中。。。。。。。。。。。。。。。。。。。。。。。。。")
    x = random.randint(1,20)
    time.sleep(x)
    print(f"睡了{x}小时")


sleep()

# fn1 = outer(sleep)
# fn1()