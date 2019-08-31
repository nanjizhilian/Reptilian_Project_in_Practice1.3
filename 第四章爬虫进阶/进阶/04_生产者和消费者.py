import random
import threading
import time


gmoney = 1000
glock = threading.Lock()    # 创建一把全局变量锁
class Preoducr(threading.Thread):
    def run(self):
        global gmoney   # 生明，要使用外部全局变量
        while True:
            miney = random.randint(100,1000)    #  randint 必须传入两个参数，一个是起始值，一个是结束值
            glock.acquire() # 上锁
            miney += 1
            print("%s生产了%d钱，剩余%d钱"%(threading.current_thread,miney,gmoney))

            glock.release() #  解锁
            time.sleep(2)


class Consumer(threading.Thread):
    def run(self):
        global gmoney
        while True:
            monkey = random.randint(100,1000)
            glock.acquire() # 上锁
            if gmoney >= monkey:
                gmoney -= monkey
                print("%s消费了%d元钱，剩余%d元钱",(threading.current_thread,monkey,gmoney))
            else:
                print("钱不够了")
            glock.release()


def main():
    for i in range(3):
        t1 = Preoducr()
        t1.start()
    for i in range(5):
        t2 = Consumer()
        t2.start()

if __name__ == '__main__':
    main()




