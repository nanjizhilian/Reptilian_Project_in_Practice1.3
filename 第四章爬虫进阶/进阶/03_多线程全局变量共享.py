import threading
values = 0
gloas = threading.Lock()    # 创建了一个锁
def add_values():
    global values   # g;oba;告诉函数，引用的是外面的全局变量
    gloas.acquire()  # 上锁
    for x in range(1000000):
        values += 1
    gloas.release()  # 解锁
    print("锁内加载 %d" % values)

def main():
    for i in  range(2):  # 创建2个线程
        t1 = threading.Thread(target=add_values)
        t1.start()

if __name__ == '__main__':
    main()



