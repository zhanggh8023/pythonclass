# -*- coding: utf-8 -*-
# @Time    : 2020/7/30 13:44
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : 1.py
# @Software: PyCharm

'''
 核心问题
通过前面的学习，我们清楚地认识到异步编程最大的困难：异步任务何时执行完毕？接下来要对异步调用的返回结果做什么操作？

上述问题我们已经通过事件循环和回调解决了。但是回调会让程序变得复杂。要异步，必回调，又是否有办法规避其缺点呢？那需要弄清楚其本质，为什么回调是必须的？还有使用回调时克服的那些缺点又是为了什么？

答案是程序为了知道自己已经干了什么？正在干什么？将来要干什么？换言之，程序得知道当前所处的状态，而且要将这个状态在不同的回调之间延续下去。

多个回调之间的状态管理困难，那让每个回调都能管理自己的状态怎么样？链式调用会有栈撕裂的困难，让回调之间不再链式调用怎样？不链式调用的话，那又如何让被调用者知道已经完成了？那就让这个回调通知那个回调如何？而且一个回调，不就是一个待处理任务吗？

任务之间得相互通知，每个任务得有自己的状态。那不就是很古老的编程技法：协作式多任务？然而要在单线程内做调度，啊哈，协程！每个协程具有自己的栈帧，当然能知道自己处于什么状态，协程之间可以协作那自然可以通知别的协程。
'''

import socket
from selectors import DefaultSelector, EVENT_WRITE, EVENT_READ

'''
不用回调的方式了，怎么知道异步调用的结果呢？先设计一个对象，异步调用执行完的时候，就把结果放在它里面。这种对象称之为未来对象。
'''

selector = DefaultSelector()
stopped = False
urls_todo = {'/', '/1', '/2', '/3', '/4', '/5', '/6', '/7', '/8', '/9'}


class Future:
    def __init__(self):
        self.result = None
        self._callbacks = []

    def add_done_callback(self, fn):
        self._callbacks.append(fn)

    def set_result(self, result):
        self.result = result
        for fn in self._callbacks:
            fn(self)


'''
未来对象有一个result属性，用于存放未来的执行结果。还有个set_result()方法，是用于设置result的，并且会在给result绑定值以后运行事先给future添加的回调。回调是通过未来对象的add_done_callback()方法添加的。

不要疑惑此处的callback，说好了不回调的嘛？难道忘了我们曾经说的要异步，必回调。不过也别急，此处的回调，和先前学到的回调，还真有点不一样。
'''


class Crawler:
    def __init__(self, url):
        self.url = url
        self.response = b''

    def fetch(self):
        sock = socket.socket()
        sock.setblocking(False)
        try:
            sock.connect(("example.com", 80))
        except BlockingIOError:
            pass
        f = Future()

        def on_connected():
            f.set_result(None)

        selector.register(sock.fileno(), EVENT_WRITE, on_connected)
        yield f
        selector.unregister(sock.fileno())
        get = 'GET {0}/ HTTP/1.0 \r\nHost: example.com\r\n\r\n'.format(self.url)
        sock.send(get.encode('ascii'))

        global stopped
        while True:
            f = Future()

            def on_readable():
                f.set_result(sock.recv(4096))

            selector.register(sock.fileno(), EVENT_READ, on_readable)

            chunk = yield f
            selector.unregister(sock.fileno())
            if chunk:
                self.response += chunk
            else:
                urls_todo.remove(self.url)
                if not urls_todo:
                    stopped = True
                break


'''
和先前的回调版本对比，已经有了较大差异。fetch 方法内有了yield表达式，使它成为了生成器。

我们知道生成器需要先调用next()迭代一次或者是先send(None)启动，遇到yield之后便暂停。

那这fetch生成器如何再次恢复执行呢？至少 Future 和 Crawler都没看到相关代码。
'''


class Task:
    def __init__(self, coro):
        self.coro = coro
        f = Future()
        f.set_result(None)
        self.step(f)

    def step(self, future):
        try:
            # send会进入到coro执行，即fetch，直到下次yield
            # next_future 为yield返回的 对象
            next_future = self.coro.send(future.result)
        except StopIteration:
            return
        next_future.add_done_callback(self.step)


'''
上述代码中Task封装了coro对象，即初始化时传递给他的对象，被管理的任务是待执行的协程，故而这里的coro就是fetch()生成器。它还有个step()方法，在初始化的时候就会执行一遍。step()内会调用生成器的send()方法，初始化第一次发送的是None就驱动了coro即fetch()的第一次执行。

send()完成之后，得到下一次的future，然后给下一次的future添加step()回调。原来add_done_callback()不是给写爬虫业务逻辑用的。此前的callback可就干的是业务逻辑呀。

再看fetch()生成器，其内部写完了所有的业务逻辑，包括如何发送请求，如何读取响应。而且注册给selector的回调相当简单，就是给对应的future对象绑定结果值。两个yield表达式都是返回对应的future对象，然后返回Task.step()之内，这样Task, Future, Coroutine三者精妙地串联在了一起。

初始化Task对象以后，把fetch()给驱动到了第44行yied f就完事了，接下来怎么继续？
'''


def loop():
    while not stopped:
        # 阻塞，直到一个事件发生
        events = selector.select()
        for event_key, event_mask in events:
            callback = event_key.data
            callback()


if __name__ == '__main__':
    import time

    start = time.time()
    for url in urls_todo:
        crawler = Crawler(url)
        Task(crawler.fetch())
    loop()
    print(time.time() - start)  # 1.35s

'''
注：总体耗时约0.43秒。

现在loop有了些许变化，callback()不再传递event_key和event_mask参数。也就是说，这里的回调根本不关心是谁触发了这个事件，结合fetch()可以知道，它只需完成对future设置结果值即可f.set_result()。而且future是谁它也不关心，因为协程能够保存自己的状态，知道自己的future是哪个。也不用关心到底要设置什么值，因为要设置什么值也是协程内安排的。

此时的loop()，真的成了一个心脏，它只管往外泵血，不论这份血液是要输送给大脑还是要给脚趾，只要它还在跳动，生命就能延续。
'''

'''
生成器协程风格和回调风格对比总结
在回调风格中：

存在链式回调（虽然示例中嵌套回调只有一层）
请求和响应也不得不分为两个回调以至于破坏了同步代码那种结构
程序员必须在回调之间维护必须的状态。
还有更多示例中没有展示，但确实存在的问题。

而基于生成器协程的风格：

无链式调用
selector的回调里只管给future设置值，不再关心业务逻辑
loop 内回调callback()不再关注是谁触发了事件
已趋近于同步代码的结构
无需程序员在多个协程之间维护状态，例如哪个才是自己的sock
'''
