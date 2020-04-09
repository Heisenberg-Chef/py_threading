import time
import threading

def test_thread(para = 'hi',sleep = 5):
    """线程运行函数"""
    time.sleep(sleep)
    print(para)
    print('----------')

def main():
    # 创建线程
    thread_hi = threading.Thread(target=test_thread)
    thread_hello = threading.Thread(target=test_thread,args=('hello',1))

    # 启动线程
    thread_hi.start()
    thread_hello.start()

    print("开始执行join方法".center(50,"*"))

    #   执行join方法会阻塞调用线程(主线程)，直到调用join方法的线程(thread_hi)结束
    thread_hi.join()
    print('线程thread_hi结束')
    #   这里不会阻塞主线程因为运行到这里的时候，线程thread_hello已经结束
    thread_hello.join()
    print('Main thread has ended.')

if __name__=='__main__':
    main()
