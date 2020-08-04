# -*- coding: utf-8 -*-
# @Time    : 2020/7/30 16:20
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : ppt_down.py
# @Software: PyCharm

import aiohttp
import asyncio
import time, os
from PPTdownload.ppt_downadr import readExcel, writeExcel
from PPTdownload.ppt_unzip import pptMove


def list():
    list = readExcel()
    n = 0

    for i in range(len(list)):
        # print(i - n, len(list))
        # print(list[i - n]['status'])
        if '√' == list[i - n]['status']:
            list.pop(i - n)
            n += 1

        else:
            pass
    print(list)
    return list


listDown = list()
falseDown = []


async def job(session, url):
    # 申明为异步函数
    try:
        # 出发到await就切换，等待get到数据
        img = await session.get(url['PnameImg'])
        p_zip = await session.get(url['Pdownadr'])
        # 读取内容
        imgcode = await img.read()
        zipcode = await p_zip.read()

        os.makedirs('./PPT/' + url['Pgroup'] + '/' + url['Pname'].replace(':', '').replace('/', '') + '/',
                    exist_ok=True)

        with open('./PPT/' + url['Pgroup'] + '/' + url['Pname'].replace(':', '').replace('/', '') + '/' + url[
            'Pname'].replace(':',
                             '').replace('/', '') + '.jpg',
                  'wb') as f:
            # 写入至文件
            f.write(imgcode)
            print(url['Pname'] + '.jpg：写入成功！')

        with open('./PPT/' + url['Pgroup'] + '/' + url['Pname'].replace(':', '').replace('/', '') + '/' + url[
            'Pname'].replace(':',
                             '').replace('/', '') + '.zip',
                  'wb') as f:
            # 写入至文件
            f.write(zipcode)
            print(url['Pname'] + '.zip：写入成功！')

        writeExcel(url['id'], eval("{'status':'√'}"))
        pptMove(url['Pgroup'], url['Pname'].replace(':', '').replace('/', ''))

        print(listDown.index(url), len(listDown))
        listDown.pop(listDown.index(url))

        return str('图片：' + url['PnameImg'] + ' ---||--- ppt: ' + url['Pdownadr'])
    except Exception as e:
        falseDown.append(listDown.pop(listDown.index(url)))
        print(falseDown, "\n", e)
        writeExcel(url['id'], eval("{'status':'X'}"))
        return print(url['Pname'] + "：Zip获取失败！ " + url['Pdownadr'])


async def main(loop, URL):
    async with aiohttp.ClientSession() as session:
        # 建立会话session
        tasks = [loop.create_task(job(session, URL[_])) for _ in range(1)]
        # 建立所有任务
        finished, unfinished = await asyncio.wait(tasks)
        # 触发await,等待任务完成
        # all_results = [r.result() for r in finished]
        # 获取所有结果
        # print("ALL RESULT:" + str(all_results))



loop = asyncio.get_event_loop()

while len(listDown) > 0:
    loop.run_until_complete(main(loop, listDown))

# loop.run_until_complete(main(loop, falseDown))
print(falseDown)
loop.close()
