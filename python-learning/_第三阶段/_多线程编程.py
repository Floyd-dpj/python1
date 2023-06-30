import time
import threading


def sing():
    while 1:
        print("我在唱歌。。。。。。。。。。。。。。。。。。。")
        time.sleep(1)

def dance():
    while 1:
        print("我在跳舞。。。。。。。。。。。。。。。。。。。。")
        time.sleep(1)

sing_thread = threading.Thread(target=sing)
dance_thread = threading.Thread(target=dance)
sing_thread.start()
dance_thread.start()