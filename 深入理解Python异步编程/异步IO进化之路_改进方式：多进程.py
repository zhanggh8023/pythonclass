# -*- coding: utf-8 -*-
# @Time    : 2020/7/29 14:22
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : 异步IO进化之路_改进方式：多进程.py
# @Software: PyCharm

import time
import socket
from concurrent import futures
'''
1/在一个程序内，依次执行10次太耗时，那开10个一样的程序同时执行不就行了。于是我们想到了多进程编程。为什么我们会先想到多进程呢？发展脉络如此。在更早的操作系统（Linux 2.4）及其以前，进程是 OS 调度任务的实体，是面向进程设计的OS。

2/由于线程的数据结构比进程更轻量级，同一个进程可以容纳多个线程，从进程到线程的优化由此展开。后来的OS也把调度单位由进程转为线程，进程只作为线程的容器，用于管理进程所需的资源。而且OS级别的线程是可以被分配到不同的CPU核心同时运行的。
'''
def blocking_way():
    sock  = socket.socket()
    # blocking
    sock.connect(("example.com", 80))
    request = 'GET / HTTP/1.0 \r\nHost: example.com\r\n\r\n'
    sock.send(request.encode('ascii'))
    response = b''
    chunk = sock.recv(4096)
    while chunk:
        response += chunk
        # blocking
        chunk = sock.recv(4096)
    return response


def process_way():
    workers = 10
    # 开10个一样的程序同时执行 3.4s
    # with futures.ProcessPoolExecutor(workers) as executor:

    # 把调度单位由进程转为10线程 0.4s-1.4s
    with futures.ThreadPoolExecutor(workers) as executor:
        time1 = time.time()
        futs = {executor.submit(blocking_way) for i in range(10)}
        print(time.time() - time1)

    return len([fut.result() for fut in futs])

'''
1/注：总体耗时约为 0.6 秒。

改善效果立竿见影。但仍然有问题。总体耗时并没有缩减到原来的十分之一，而是九分之一左右，还有一些时间耗到哪里去了？进程切换开销。

进程切换开销不止像“CPU的时间观”所列的“上下文切换”那么低。CPU从一个进程切换到另一个进程，需要把旧进程运行时的寄存器状态、内存状态全部保存好，再将另一个进程之前保存的数据恢复。对CPU来讲，几个小时就干等着。当进程数量大于CPU核心数量时，进程切换是必然需要的。

除了切换开销，多进程还有另外的缺点。一般的服务器在能够稳定运行的前提下，可以同时处理的进程数在数十个到数百个规模。如果进程数量规模更大，系统运行将不稳定，而且可用内存资源往往也会不足。

多进程解决方案在面临每天需要成百上千万次下载任务的爬虫系统，或者需要同时搞定数万并发的电商系统来说，并不适合。

除了切换开销大，以及可支持的任务规模小之外，多进程还有其他缺点，如状态共享等问题，后文会有提及，此处不再细究。


2/注：总体运行时间约0.43秒。

结果符合我们预期，比多进程耗时要少些。从运行时间上看，多线程似乎已经解决了切换开销大的问题。而且可支持的任务数量规模，也变成了数百个到数千个。

但是，多线程仍有问题，特别是Python里的多线程。首先，Python中的多线程因为GIL的存在，它们并不能利用CPU多核优势，一个Python进程中，只允许有一个线程处于运行状态。那为什么结果还是如预期，耗时缩减到了十分之一？

因为在做阻塞的系统调用时，例如sock.connect(),sock.recv()时，当前线程会释放GIL，让别的线程有执行机会。但是单个线程内，在阻塞调用上还是阻塞的。
小提示：Python中 time.sleep 是阻塞的，都知道使用它要谨慎，但在多线程编程中，time.sleep 并不会阻塞其他线程。

除了GIL之外，所有的多线程还有通病。它们是被OS调度，调度策略是抢占式的，以保证同等优先级的线程都有均等的执行机会，那带来的问题是：并不知道下一时刻是哪个线程被运行，也不知道它正要执行的代码是什么。所以就可能存在竞态条件。

例如爬虫工作线程从任务队列拿待抓取URL的时候，如果多个爬虫线程同时来取，那这个任务到底该给谁？那就需要用到“锁”或“同步队列”来保证下载任务不会被重复执行。

而且线程支持的多任务规模，在数百到数千的数量规模。在大规模的高频网络交互系统中，仍然有些吃力。当然，多线程最主要的问题还是竞态条件。
'''

if __name__ == '__main__':
    time2 = time.time()
    process_way()
    print(time.time() - time2)