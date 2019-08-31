import threading
import time
def coding():
    for x in range(3):
        print("正在打印 %s " % x)
        time.sleep(2)
def wrodir():
    for y in range(3):
        print("正在加载 %s "% y)
        time.sleep(2)
def main():
    t1 = threading.Thread(target=coding)    #  创建线程，注意后面的coding不加括号，加括号相当于添加返回值
    t2 = threading.Thread(target=wrodir)
    t1.start()   # 启动线程
    t2.start()
if __name__ == '__main__':
    main()









