# -*- coding: utf-8 -*-
# @Time    : 2019/11/29 17:27
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : spider_txt.py
# @Software: PyCharm

import os, sys, time, asyncio, aiohttp

FLAGS = ('CN IN US ID BR PK NG BD RU JP '
         'MX PH VN ET EG DE IR TR CD FR').split()
BASE_URL = 'http://flupy.org/data/flags'  # 下载url
DEST_DIR = 'downloads/'  # 保存目录


async def fetch(session: aiohttp.ClientSession, url: str, path: str, flag: str):
    print(flag, ' 开始下载')
    async with session.get(url) as resp:
        with open(path, 'wb') as fd:
            while 1:
                chunk = await resp.content.read(8196)
                if not chunk:
                    break
                fd.write(chunk)
    return flag


async def download():
    tasks = []
    async with aiohttp.ClientSession() as session:
        for flag in FLAGS:
            path = os.path.join(DEST_DIR, flag.lower() + '.gif')
            print(path)
            url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=flag.lower())
            print(url)
            tasks.append(asyncio.ensure_future(fetch(session, url, path, flag)))
        await asyncio.wait(tasks)
        # for coroutine in asyncio.as_completed(tasks):
        #     res = await coroutine
        #     print('%s下载完成' % res)


os.makedirs(DEST_DIR, exist_ok=True)
lp = asyncio.get_event_loop()
start = time.time()
lp.run_until_complete(download())
end = time.time()
lp.close()
print('耗时:', end - start)
