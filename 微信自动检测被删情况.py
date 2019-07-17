# -*- coding: utf-8 -*-
# @Time    : 2019/3/25 14:14
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : 微信僵尸粉检测.py
# @Software: PyCharm


import itchat
import time

itchat.auto_login(hotReload=True)  # 热加载

print('检测结果可能会引起不适。')
print('检测结果请在手机上查看，此处仅显示检测信息。')
print('消息被拒收为被拉黑， 需要发送验证信息为被删。')
print('没有结果就是好结果。')
print('检测1000位好友需要34分钟， 以此类推。')
print('为了你的账号安全着想，这个速度刚好。')
print('在程序运行期间请让程序保持运行，网络保持连接。')
print('请不要从手机端手动退出。')
print('按ENTER键继续...')

friends = itchat.get_friends(update=True)
lenght = len(friends)

for i in range(1, lenght):
    # 微信bug，用自己账户给所有好友发送"జ్ఞా"消息，当添加自己为好友时，只有自己能收到此信息，如果没添加自己为好友\
    # 没有人能收到此信息，笔者此刻日期为2019/1/6 8:30，到目前为止微信bug还没修复。
    # 所以迭代从除去自己后的第二位好友开始 range(1, lenght)。
    itchat.send("జ్ఞా", toUserName=friends[i]['UserName'])
    print(f'检测到第{i}位好友: {str(friends[i]["NickName"]).center(20, " ")}')
    # 发送信息速度过快会被微信检测到异常行为。
    time.sleep(2)

print('已检测完毕，请在手机端查看结果。')

itchat.run()



# from wxpy import *
# import time
# print("本软件采用特殊字符检测，即对方收不到任何信息！")
# print("或许某个版本微信就会修复该字符了，不作通知哈！")
# print("软件编写日期：2019-2-20！")
# input("任意键继续...(非电源键)")
# try:
#     bot = Bot()#机器人对象
#     all_friends = bot.friends()#把微信所有好友放进列表
#     for i in all_friends:
#         try:
#             print("检测 "+i.name+" 中...")#如果好友备注有表情这句会报错，所以报错直接跳过
#         except:
#             pass
#         try:
#             i.send('జ్ఞ ‌ా')#发送检测字符
#         except:
#             pass
#         time.sleep(2) #延时防频繁
#     bot.file_helper.send('检测结束，请退出网页微信!')#通过文件传输助手发送检测结束
#     bot.logout()
#
#     input("检测结束，任意键退出...")
# except KeyError:#这个错误是因为微信官方封禁了这个微信号登陆网页微信的接口
#     print("该微信暂时不能登录网页微信！")
#     input("检测失败，任意键退出...")