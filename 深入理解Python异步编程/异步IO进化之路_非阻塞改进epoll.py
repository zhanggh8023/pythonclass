# -*- coding: utf-8 -*-
# @Time    : 2020/7/30 10:53
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : 异步IO进化之路_非阻塞改进epoll.py
# @Software: PyCharm


import socket
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE

selector = DefaultSelector()
stopped = False
urls_todo = {'/', '/1', '/2', '/3', '/4', '/5', '/6', '/7', '/8', '/9'}


class Crawler:
    def __init__(self, url):
        self.url = url
        self.sock = None
        self.response = b''

    def fetch(self):
        self.sock = socket.socket()
        self.sock.setblocking(False)
        try:
            self.sock.connect(("example.com", 80))
        except BlockingIOError:
            pass
        selector.register(self.sock.fileno(), EVENT_WRITE, self.connected)

    def connected(self, key, mask):
        selector.unregister(key.fd)
        get = 'GET {0}/ HTTP/1.0 \r\nHost: example.com\r\n\r\n'.format(self.url)
        self.sock.send(get.encode('ascii'))
        selector.register(key.fd, EVENT_READ, self.read_response)

    def read_response(self, key, mask):
        global stopped
        # 如果响应大于4kb，下一次循环会继续读
        chunk = self.sock.recv(4096)
        if chunk:
            self.response += chunk
        else:
            selector.unregister(key.fd)
            urls_todo.remove(self.url)
            if not urls_todo:
                stopped = True


'''
此处和前面稍有不同的是，我们将下载不同的10个页面，相对URL路径存放于urls_todo集合中。现在看看改进在哪。

首先，不断尝试send() 和 recv() 的两个循环被消灭掉了。

其次，导入了selectors模块，并创建了一个DefaultSelector 实例。Python标准库提供的selectors模块是对底层select/poll/epoll/kqueue的封装。DefaultSelector类会根据 OS 环境自动选择最佳的模块，那在 Linux 2.5.44 及更新的版本上都是epoll了。

然后，在第25行和第31行分别注册了socket可写事件(EVENT_WRITE)和可读事件(EVENT_READ)发生后应该采取的回调函数。

虽然代码结构清晰了，阻塞操作也交给OS去等待和通知了，但是，我们要抓取10个不同页面，就得创建10个Crawler实例，就有20个事件将要发生，那如何从selector里获取当前正发生的事件，并且得到对应的回调函数去执行呢？
'''

'''
事件循环（Event Loop）
为了解决上述问题，那我们只得采用老办法，写一个循环，去访问selector模块，等待它告诉我们当前是哪个事件发生了，应该对应哪个回调。这个等待事件通知的循环，称之为事件循环。
'''


def loop():
    while not stopped:
        # 阻塞，直到一个事件发生
        events = selector.select()
        for event_key, event_mask in events:
            callback = event_key.data
            callback(event_key, event_mask)


'''
上述代码中，我们用stopped全局变量控制事件循环何时停止。当urls_todo消耗完毕后，会标记stopped为True。

重要的是第49行代码，selector.select() 是一个阻塞调用，因为如果事件不发生，那应用程序就没事件可处理，所以就干脆阻塞在这里等待事件发生。那可以推断，如果只下载一篇网页，一定要connect()之后才能send()继而recv()，那它的效率和阻塞的方式是一样的。因为不在connect()/recv()上阻塞，也得在select()上阻塞。

所以，selector机制(后文以此称呼代指epoll/kqueue)是设计用来解决大量并发连接的。当系统中有大量非阻塞调用，能随时产生事件的时候，selector机制才能发挥最大的威力。

下面是如何启创建10个下载任务和启动事件循环的：
'''

if __name__ == '__main__':
    import time

    start = time.time()
    for url in urls_todo:
        crawler = Crawler(url)
        crawler.fetch()
    loop()
    print(time.time() - start)  # 1.4s-0.38948655128479004s

'''
注：总体耗时约0.45秒。

上述执行结果令人振奋。在单线程内用 事件循环+回调 搞定了10篇网页同时下载的问题。这，已经是异步编程了。虽然有一个for 循环顺序地创建Crawler 实例并调用 fetch 方法，但是fetch 内仅有connect()和注册可写事件，而且从执行时间明显可以推断，多个下载任务确实在同时进行！

上述代码异步执行的过程：

创建Crawler 实例；
调用fetch方法，会创建socket连接和在selector上注册可写事件；
fetch内并无阻塞操作，该方法立即返回；
重复上述3个步骤，将10个不同的下载任务都加入事件循环；
启动事件循环，进入第1轮循环，阻塞在事件监听上；
当某个下载任务EVENT_WRITE被触发，回调其connected方法，第一轮事件循环结束；
进入第2轮事件循环，当某个下载任务有事件触发，执行其回调函数；此时已经不能推测是哪个事件发生，因为有可能是上次connected里的EVENT_READ先被触发，也可能是其他某个任务的EVENT_WRITE被触发；（此时，原来在一个下载任务上会阻塞的那段时间被利用起来执行另一个下载任务了）
循环往复，直至所有下载任务被处理完成
退出事件循环，结束整个下载程序
'''

'''
总结
目前为止，我们已经从同步阻塞学习到了异步非阻塞。掌握了在单线程内同时并发执行多个网络I/O阻塞型任务的黑魔法。而且与多线程相比，连线程切换都没有了，执行回调函数是函数调用开销，在线程的栈内完成，因此性能也更好，单机支持的任务规模也变成了数万到数十万个。（不过我们知道：没有免费午餐，也没有银弹。）

部分编程语言中，对异步编程的支持就止步于此（不含语言官方之外的扩展）。需要程序猿直接使用epoll去注册事件和回调、维护一个事件循环，然后大多数时间都花在设计回调函数上。

通过本节的学习，我们应该认识到，不论什么编程语言，但凡要做异步编程，上述的“事件循环+回调”这种模式是逃不掉的，尽管它可能用的不是epoll，也可能不是while循环。如果你找到了一种不属于 “等会儿告诉你” 模型的异步方式，请立即给我打电话（注意，打电话是Call）。

为什么我们在某些异步编程中并没有看到 CallBack 模式呢？这就是我们接下来要探讨的问题。本节是学习异步编程的一个终点，也是另一个起点。毕竟咱们讲 Python 异步编程，还没提到其主角协程的用武之地。
'''
