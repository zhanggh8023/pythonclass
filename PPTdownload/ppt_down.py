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

        os.makedirs('./PPT/' + url['Pgroup'] + '/' + url['Pname'].replace(':', '') + '/', exist_ok=True)

        with open('./PPT/' + url['Pgroup'] + '/' + url['Pname'].replace(':', '') + '/' + url['Pname'].replace(':',
                                                                                                              '') + '.jpg',
                  'wb') as f:
            # 写入至文件
            f.write(imgcode)
            print(url['Pname'] + '.jpg：写入成功！')

        with open('./PPT/' + url['Pgroup'] + '/' + url['Pname'].replace(':', '') + '/' + url['Pname'].replace(':',
                                                                                                              '') + '.zip',
                  'wb') as f:
            # 写入至文件
            f.write(zipcode)
            print(url['Pname'] + '.zip：写入成功！')

        writeExcel(url['id'], eval("{'status':'√'}"))
        pptMove(url['Pgroup'], url['Pname'].replace(':', ''))

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
        tasks = [loop.create_task(job(session, URL[_])) for _ in range(20)]
        # 建立所有任务
        finished, unfinished = await asyncio.wait(tasks)
        # 触发await,等待任务完成
        # all_results = [r.result() for r in finished]
        # 获取所有结果
        # print("ALL RESULT:" + str(all_results))


list1 = [{'id': 1401, 'Pname': '超精美收费级圣诞节PPT模板', 'PnameImg': 'https://cdn.52ppt.com/images/o3fwjdnnk24.jpg-longsm.jpg',
          'Pdown': 'https://www.52ppt.com/e/DownSys/DownSoft/?classid=49&id=975&pathid=0', 'status': 'X',
          'Pgroup': '圣诞节PPT模板',
          'Pdownadr': 'https://www.52ppt.com/e/DownSys/doaction.php?enews=DownSoft&classid=49&id=975&pathid=0&pass=93d17745624fead47c59769c0ca70bd7&p=::::::'},
         {'id': 1430, 'Pname': '黑板背景感恩教师节PPT模板', 'PnameImg': 'https://cdn.52ppt.com/images/tg2ir52i53w.jpg-longsm.jpg',
          'Pdown': 'https://www.52ppt.com/e/DownSys/DownSoft/?classid=44&id=1053&pathid=0', 'status': 'X',
          'Pgroup': '教师节PPT模板',
          'Pdownadr': 'https://www.52ppt.com/e/DownSys/doaction.php?enews=DownSoft&classid=44&id=1053&pathid=0&pass=fcbee0e6186b19eec77fba952b60befe&p=::::::'},
         {'id': 1437, 'Pname': '浪漫粉色七夕情人节PPT模板', 'PnameImg': 'https://cdn.52ppt.com/images/td54dabwphl.jpg-longsm.jpg',
          'Pdown': 'https://www.52ppt.com/e/DownSys/DownSoft/?classid=38&id=991&pathid=0', 'status': 'X',
          'Pgroup': '情人节PPT模板',
          'Pdownadr': 'https://www.52ppt.com/e/DownSys/doaction.php?enews=DownSoft&classid=38&id=991&pathid=0&pass=fe872dd89414ff269207dc15e8bc53e1&p=::::::'},
         {'id': 2256, 'Pname': '货币金融相关产业PPT模板', 'PnameImg': 'https://cdn.52ppt.com/file/101/10151.jpg-longsm.jpg',
          'Pdown': 'https://www.52ppt.com/e/DownSys/DownSoft/?classid=25&id=151&pathid=0', 'status': 'X',
          'Pgroup': '经济金融PPT模板',
          'Pdownadr': 'https://www.52ppt.com/e/DownSys/doaction.php?enews=DownSoft&classid=25&id=151&pathid=0&pass=06c3d34bc6a2aee160c006257f9b3aef&p=::::::'},
         {'id': 1415, 'Pname': '通用年终述职报告PPT模板', 'PnameImg': 'https://cdn.52ppt.com/images/at2wog3mn1n.jpg-longsm.jpg',
          'Pdown': 'https://www.52ppt.com/e/DownSys/DownSoft/?classid=10&id=2118&pathid=0', 'status': 'X',
          'Pgroup': '商务PPT模板',
          'Pdownadr': 'https://www.52ppt.com/e/DownSys/doaction.php?enews=DownSoft&classid=10&id=2118&pathid=0&pass=b4cc2fa4004f1659b7c71fe5ab7f4523&p=::::::'},
         {'id': 1378, 'Pname': '紫色微立体年终总结PPT模板', 'PnameImg': 'https://cdn.52ppt.com/images/qnoe0ylewbi.jpg-longsm.jpg',
          'Pdown': 'https://www.52ppt.com/e/DownSys/DownSoft/?classid=10&id=1764&pathid=0', 'status': 'X',
          'Pgroup': '商务PPT模板',
          'Pdownadr': 'https://www.52ppt.com/e/DownSys/doaction.php?enews=DownSoft&classid=10&id=1764&pathid=0&pass=23825454eb31751c1439ed3319454b22&p=::::::'},
         {'id': 2612, 'Pname': '科技电子/电子商务/楼盘房地产PPT模板',
          'PnameImg': 'https://cdn.52ppt.com/images/br1k2tr0e5w.jpg-longsm.jpg',
          'Pdown': 'https://www.52ppt.com/e/DownSys/DownSoft/?classid=35&id=2751&pathid=0', 'status': 'X',
          'Pgroup': '社会生活PPT模板',
          'Pdownadr': 'https://www.52ppt.com/e/DownSys/doaction.php?enews=DownSoft&classid=35&id=2751&pathid=0&pass=5cacb2ba304c6bd9e461b274d49b09d4&p=::::::'},
         {'id': 2686, 'Pname': '韩国风格房地产/商务PowerPoint模板下载',
          'PnameImg': 'https://cdn.52ppt.com/images/vg1guvzvpw4.jpg-longsm.jpg',
          'Pdown': 'https://www.52ppt.com/e/DownSys/DownSoft/?classid=35&id=2919&pathid=0', 'status': 'X',
          'Pgroup': '社会生活PPT模板',
          'Pdownadr': 'https://www.52ppt.com/e/DownSys/doaction.php?enews=DownSoft&classid=35&id=2919&pathid=0&pass=e45dff1c75e4e1900d19a548c3a26c32&p=::::::'},
         {'id': 2796, 'Pname': '《税务会计》教学课件PPT下载', 'PnameImg': 'https://cdn.52ppt.com/images/onx5dmtud4i.jpg-longsm.jpg',
          'Pdown': 'https://www.52ppt.com/e/DownSys/DownSoft/?classid=35&id=2535&pathid=0', 'status': 'X',
          'Pgroup': '社会生活PPT模板',
          'Pdownadr': 'https://www.52ppt.com/e/DownSys/doaction.php?enews=DownSoft&classid=35&id=2535&pathid=0&pass=63284f71f4a6a3bfd6b98d82a7dd78ff&p=::::::'},
         {'id': 2923, 'Pname': '韩国电子商务/科技PowerPoint模板下载',
          'PnameImg': 'https://cdn.52ppt.com/images/v3uuvnkcqyb.jpg-longsm.jpg',
          'Pdown': 'https://www.52ppt.com/e/DownSys/DownSoft/?classid=35&id=2915&pathid=0', 'status': 'X',
          'Pgroup': '社会生活PPT模板',
          'Pdownadr': 'https://www.52ppt.com/e/DownSys/doaction.php?enews=DownSoft&classid=35&id=2915&pathid=0&pass=f46c2c54bebb3ce3e6d7aea8434b9093&p=::::::'},
         {'id': 2985, 'Pname': '健康饮食主题的草莓水果沙拉PPT模板下载',
          'PnameImg': 'https://cdn.52ppt.com/images/iummgp3yaxk.jpg-longsm.jpg',
          'Pdown': 'https://www.52ppt.com/e/DownSys/DownSoft/?classid=35&id=2615&pathid=0', 'status': 'X',
          'Pgroup': '社会生活PPT模板',
          'Pdownadr': 'https://www.52ppt.com/e/DownSys/doaction.php?enews=DownSoft&classid=35&id=2615&pathid=0&pass=3ad1d4d245fd2f6131d4384d5c5d8272&p=::::::'},
         {'id': 2986, 'Pname': '粉色爱情主题PPT模板下载', 'PnameImg': 'https://cdn.52ppt.com/images/nlxtnxsfpv3.jpg-longsm.jpg',
          'Pdown': 'https://www.52ppt.com/e/DownSys/DownSoft/?classid=35&id=2581&pathid=0', 'status': 'X',
          'Pgroup': '社会生活PPT模板',
          'Pdownadr': 'https://www.52ppt.com/e/DownSys/doaction.php?enews=DownSoft&classid=35&id=2581&pathid=0&pass=5d63188581928917cfbf5c2599cc08cd&p=::::::'},
         {'id': 2987, 'Pname': '《月亮你好吗》绘本故事PPT', 'PnameImg': 'https://cdn.52ppt.com/images/diq25lmqyfg.jpg-longsm.jpg',
          'Pdown': 'https://www.52ppt.com/e/DownSys/DownSoft/?classid=35&id=3027&pathid=0', 'status': 'X',
          'Pgroup': '社会生活PPT模板',
          'Pdownadr': 'https://www.52ppt.com/e/DownSys/doaction.php?enews=DownSoft&classid=35&id=3027&pathid=0&pass=dbca25acfab66c38e9cac9f38ef47b9a&p=::::::'},
         {'id': 2988, 'Pname': '年会发言技巧PowerPoint下载',
          'PnameImg': 'https://cdn.52ppt.com/images/lf0omdoi4u2.jpg-longsm.jpg',
          'Pdown': 'https://www.52ppt.com/e/DownSys/DownSoft/?classid=35&id=2966&pathid=0', 'status': 'X',
          'Pgroup': '社会生活PPT模板',
          'Pdownadr': 'https://www.52ppt.com/e/DownSys/doaction.php?enews=DownSoft&classid=35&id=2966&pathid=0&pass=021ea63b8e28a74778da2774f1cc7d4e&p=::::::'},
         {'id': 2989, 'Pname': '个人知识管理PPT下载', 'PnameImg': 'https://cdn.52ppt.com/images/zm1vd52qt24.jpg-longsm.jpg',
          'Pdown': 'https://www.52ppt.com/e/DownSys/DownSoft/?classid=35&id=2933&pathid=0', 'status': 'X',
          'Pgroup': '社会生活PPT模板',
          'Pdownadr': 'https://www.52ppt.com/e/DownSys/doaction.php?enews=DownSoft&classid=35&id=2933&pathid=0&pass=b434c03f26e0c7990505a78203d1375d&p=::::::'},
         {'id': 2990, 'Pname': '蓝色公司简介PPT模板下载', 'PnameImg': 'https://cdn.52ppt.com/images/dk5soot1rm2.jpg-longsm.jpg',
          'Pdown': 'https://www.52ppt.com/e/DownSys/DownSoft/?classid=35&id=2849&pathid=0', 'status': 'X',
          'Pgroup': '社会生活PPT模板',
          'Pdownadr': 'https://www.52ppt.com/e/DownSys/doaction.php?enews=DownSoft&classid=35&id=2849&pathid=0&pass=c6108fcb5060afe46063e6d7f95fe416&p=::::::'},
         {'id': 2991, 'Pname': 'win8风格的公司简介PowerPoint模板下载',
          'PnameImg': 'https://cdn.52ppt.com/images/bvg3vwdgptr.jpg-longsm.jpg',
          'Pdown': 'https://www.52ppt.com/e/DownSys/DownSoft/?classid=35&id=2848&pathid=0', 'status': 'X',
          'Pgroup': '社会生活PPT模板',
          'Pdownadr': 'https://www.52ppt.com/e/DownSys/doaction.php?enews=DownSoft&classid=35&id=2848&pathid=0&pass=359c6177d4fbca22c3ec499f95774d7b&p=::::::'},
         {'id': 2992, 'Pname': '什么是肾，如何保护肾脏PPT课件下载',
          'PnameImg': 'https://cdn.52ppt.com/images/01wwiasu5pf.jpg-longsm.jpg',
          'Pdown': 'https://www.52ppt.com/e/DownSys/DownSoft/?classid=35&id=2526&pathid=0', 'status': 'X',
          'Pgroup': '社会生活PPT模板',
          'Pdownadr': 'https://www.52ppt.com/e/DownSys/doaction.php?enews=DownSoft&classid=35&id=2526&pathid=0&pass=4836d48114dfff1af47aa0fd2d1f0ca4&p=::::::'},
         {'id': 2993, 'Pname': '《蛤蟆爷爷的秘诀》绘本故事PPT',
          'PnameImg': 'https://cdn.52ppt.com/images/34foevxt1sk.jpg-longsm.jpg',
          'Pdown': 'https://www.52ppt.com/e/DownSys/DownSoft/?classid=35&id=2995&pathid=0', 'status': 'X',
          'Pgroup': '社会生活PPT模板',
          'Pdownadr': 'https://www.52ppt.com/e/DownSys/doaction.php?enews=DownSoft&classid=35&id=2995&pathid=0&pass=dadad9cd50c511df10ec330ae657f1e0&p=::::::'},
         {'id': 2994, 'Pname': '大气磅礴的天安门背景十一国庆节PPT模板',
          'PnameImg': 'https://cdn.52ppt.com/images/df2oz0bl0qw.jpg-longsm.jpg',
          'Pdown': 'https://www.52ppt.com/e/DownSys/DownSoft/?classid=35&id=2889&pathid=0', 'status': 'X',
          'Pgroup': '社会生活PPT模板',
          'Pdownadr': 'https://www.52ppt.com/e/DownSys/doaction.php?enews=DownSoft&classid=35&id=2889&pathid=0&pass=5ef2e92ce8ec898f06cdd2c6e58b3e8f&p=::::::'},
         {'id': 2995, 'Pname': '黄色渐变背景纯色幻灯片模板下载', 'PnameImg': 'https://cdn.52ppt.com/images/f0xe2qejd2v.jpg-longsm.jpg',
          'Pdown': 'https://www.52ppt.com/e/DownSys/DownSoft/?classid=35&id=2666&pathid=0', 'status': 'X',
          'Pgroup': '社会生活PPT模板',
          'Pdownadr': 'https://www.52ppt.com/e/DownSys/doaction.php?enews=DownSoft&classid=35&id=2666&pathid=0&pass=f6b3064a7273a16629a5f11011459aac&p=::::::'},
         {'id': 2996, 'Pname': '蓝色墨迹简约PPT模板下载', 'PnameImg': 'https://cdn.52ppt.com/images/catgay0jn0z.jpg-longsm.jpg',
          'Pdown': 'https://www.52ppt.com/e/DownSys/DownSoft/?classid=35&id=2664&pathid=0', 'status': 'X',
          'Pgroup': '社会生活PPT模板',
          'Pdownadr': 'https://www.52ppt.com/e/DownSys/doaction.php?enews=DownSoft&classid=35&id=2664&pathid=0&pass=226342f61c33c0fc40f5993b01a140ed&p=::::::'},
         {'id': 2997, 'Pname': '卡通美食类PPT模板下载', 'PnameImg': 'https://cdn.52ppt.com/images/yadzrbnqt2k.jpg-longsm.jpg',
          'Pdown': 'https://www.52ppt.com/e/DownSys/DownSoft/?classid=35&id=2641&pathid=0', 'status': 'X',
          'Pgroup': '社会生活PPT模板',
          'Pdownadr': 'https://www.52ppt.com/e/DownSys/doaction.php?enews=DownSoft&classid=35&id=2641&pathid=0&pass=0e58392374be228137fd4421b8e03d24&p=::::::'},
         {'id': 2998, 'Pname': '京剧及欣赏PPT下载', 'PnameImg': 'https://cdn.52ppt.com/images/xq4q5rahdqr.jpg-longsm.jpg',
          'Pdown': 'https://www.52ppt.com/e/DownSys/DownSoft/?classid=35&id=2543&pathid=0', 'status': 'X',
          'Pgroup': '社会生活PPT模板',
          'Pdownadr': 'https://www.52ppt.com/e/DownSys/doaction.php?enews=DownSoft&classid=35&id=2543&pathid=0&pass=af19f23b56b3735b1ecd81a1a49d94b6&p=::::::'},
         {'id': 2999, 'Pname': '儿童绘本故事：booboo波波PPT下载',
          'PnameImg': 'https://cdn.52ppt.com/images/2ztjx01hsfk.jpg-longsm.jpg',
          'Pdown': 'https://www.52ppt.com/e/DownSys/DownSoft/?classid=35&id=2994&pathid=0', 'status': 'X',
          'Pgroup': '社会生活PPT模板',
          'Pdownadr': 'https://www.52ppt.com/e/DownSys/doaction.php?enews=DownSoft&classid=35&id=2994&pathid=0&pass=df585c3621128855a7f3861114748a18&p=::::::'},
         {'id': 3000, 'Pname': '旅游服务公司简介PPT下载', 'PnameImg': 'https://cdn.52ppt.com/images/vju3dznnthf.jpg-longsm.jpg',
          'Pdown': 'https://www.52ppt.com/e/DownSys/DownSoft/?classid=35&id=2863&pathid=0', 'status': 'X',
          'Pgroup': '社会生活PPT模板',
          'Pdownadr': 'https://www.52ppt.com/e/DownSys/doaction.php?enews=DownSoft&classid=35&id=2863&pathid=0&pass=ea2c054862efcaed45d4398243528fb2&p=::::::'},
         {'id': 3001, 'Pname': '精美氢气球背景个人简历PPT模板下载',
          'PnameImg': 'https://cdn.52ppt.com/images/pc5e3si4ems.jpg-longsm.jpg',
          'Pdown': 'https://www.52ppt.com/e/DownSys/DownSoft/?classid=35&id=2796&pathid=0', 'status': 'X',
          'Pgroup': '社会生活PPT模板',
          'Pdownadr': 'https://www.52ppt.com/e/DownSys/doaction.php?enews=DownSoft&classid=35&id=2796&pathid=0&pass=9752dd5c41ec56f22eea994e59d2f632&p=::::::'},
         {'id': 3002, 'Pname': '淡雅蜜蜂背景PPT模板下载', 'PnameImg': 'https://cdn.52ppt.com/images/wcbhxp2pgvg.jpg-longsm.jpg',
          'Pdown': 'https://www.52ppt.com/e/DownSys/DownSoft/?classid=35&id=2723&pathid=0', 'status': 'X',
          'Pgroup': '社会生活PPT模板',
          'Pdownadr': 'https://www.52ppt.com/e/DownSys/doaction.php?enews=DownSoft&classid=35&id=2723&pathid=0&pass=1babed2d59d07001662817d69bedd953&p=::::::'},
         {'id': 3003, 'Pname': '党徽背景的建党节或党政汇报PPT模板下载',
          'PnameImg': 'https://cdn.52ppt.com/images/gxy5og4kayw.jpg-longsm.jpg',
          'Pdown': 'https://www.52ppt.com/e/DownSys/DownSoft/?classid=35&id=2692&pathid=0', 'status': 'X',
          'Pgroup': '社会生活PPT模板',
          'Pdownadr': 'https://www.52ppt.com/e/DownSys/doaction.php?enews=DownSoft&classid=35&id=2692&pathid=0&pass=3c2c293b27f4322bb7b3e8bc8a7f9702&p=::::::'}]


loop = asyncio.get_event_loop()

while len(listDown) > 0:
    loop.run_until_complete(main(loop, listDown))

loop.run_until_complete(main(loop, falseDown))
print(falseDown)
loop.close()
