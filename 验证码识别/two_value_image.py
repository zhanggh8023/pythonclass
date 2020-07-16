# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 17:12
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : two_value_image.py
# @Software: PyCharm


from aip import AipOcr


def _get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


# 调用百度图片识别
def baidu_discern(filename):
    """ 你的 APPID AK SK """
    APP_ID = '19456011'
    API_KEY = '6TzNcVWatnRIGW5z48Z3W4c0'
    SECRET_KEY = '0bAxGcT4fip7bWzsF4Ak6BevobuXwXCF '

    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    image = _get_file_content(filename)

    """ 调用网络图片文字识别, 图片参数为本地图片 """
    ret = client.webImage(image)
    words = ret.get('words_result')
    if words:
        return ''.join(words[0]['words'].split(' '))
    else:
        return ''


if __name__ == '__main__':
    ret = baidu_discern('./image/_num1000.jpg')
    print(ret)

