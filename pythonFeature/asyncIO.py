# @Time : 2021/4/29 16:12
# @Author : LiuBin
# @File : asyncIO.py
# @Description : 
# @Software: PyCharm
"""python异步编程-协程
* 与多线程不同，协程的特点在于是一个线程执行，避免了切换线程的开销；不需要多线程的锁机制。
* 搭配多进程+协程可以获得极高的执行效率
* Python对协程的支持是通过generator实现的。
* 类比python程序级别的函数中断（协程原理）<==>操作系统的CPU中断（多线程原理）
* 用Donald Knuth的一句话总结协程的特点：“子程序就是协程的一种特例。”

* 涉及包 asyncio
>> 参考廖雪峰博客
"""

import threading


# 1.先看一个 生产者-消费者模型，了解协程的本质就是利用generator中断程序。
def consumer():
    r = ''
    while True:
        n = yield r
        # if not n:
        #     return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


def produce(c):
    c.send(None)  # 等价于next(c),第一次用于启动生成器，c第一次执行到yield就中止
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()


c = consumer()
produce(c)

print("\n********************************************\n")

# 2. python3.4之后的内置异步IO库处理协程 / python3.5之后的异步IO语法处理协程
import asyncio


@asyncio.coroutine
def hello(no):
    print("A:Hello {}! {}".format(no, threading.current_thread()))
    # 异步调用asyncio.sleep():
    r = yield from asyncio.sleep(3)
    print("A:Hello {} again! {}".format(no, threading.current_thread()))


async def hello2(no):
    print("B:Hello {}! {}".format(no, threading.current_thread()))
    # 异步调用asyncio.sleep():
    await asyncio.sleep(5)
    print("B:Hello {} again! {}".format(no, threading.current_thread()))


# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(asyncio.wait([hello(no) for no in range(3)] + [hello2(no) for no in range(2)]))
loop.close()

print("\n********************************************\n")
