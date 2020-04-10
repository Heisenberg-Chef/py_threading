"""
使用锁实现线程同步
"""
import time
import threading

# 创建锁
lock = threading.Lock()

# 全局变量
global_resource = [None] * 5


def change_resource(para, sleep):
    # 请求锁
    lock.acquire()

    # 这段代码如果不加锁，第一个线程运行结束后global_resource中是乱的，输出为：修改全局变量为： ['hello', 'hi', 'hi', 'hello', 'hello']
    # 第二个线程运行结束后，global_resource中还是乱的，输出为：修改全局变量为： ['hello', 'hi', 'hi', 'hi', 'hi']
    global global_resource
    for i in range(len(global_resource)):
        global_resource[i] = para
        time.sleep(sleep)
    print("修改全局变量为：", global_resource)

    # 释放锁
    lock.release()


def main():
    thread_hi = threading.Thread(target=change_resource, args=('hi', 2))
    thread_hello = threading.Thread(target=change_resource, args=('hello', 1))
    thread_hi.start()
    thread_hello.start()


if __name__ == '__main__':
    main()
