import threading
import time
class CodingTred(threading.Thread):
    def run(self):
        for x in range(3):
            print("正在加载 %s" % threading.Thread)
            time.sleep(2)
class Wrodsdj(threading.Thread):
    def run(self):
        for y in range(3):
            print("正在画图 %s" % threading.Thread)
            time.sleep(2)
def main():
    t1 = CodingTred()
    t2 = Wrodsdj()
    t1.start()
    t2.start()
if __name__ == '__main__':
    main()




