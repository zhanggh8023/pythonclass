#!/usr/bin/env pythontest
# coding=utf-8
# author: zengyuetian
# read data from csv, write to mysql

import os
import pymysql

from lib.utility.path import DATA_PATH
from lib.city.city import *
from lib.utility.date import *
from lib.utility.version import PYTHON_3
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

pymysql.install_as_MySQLdb()


def create_prompt_text():
    city_info = list()
    num = 0
    for en_name, ch_name in cities.items():
        num += 1
        city_info.append(en_name)
        city_info.append(": ")
        city_info.append(ch_name)
        if num % 4 == 0:
            city_info.append("\n")
        else:
            city_info.append(", ")
    return 'Which city data do you want to save ?\n' + ''.join(city_info)


if __name__ == '__main__':
    # 设置目标数据库
    # mysql or mongodb or excel
    # database = "mysql"
    # database = "mongodb"
    database = "excel"
    db = None
    collection = None
    workbook = None

    if database == "mysql":
        pass
    elif database == "mongodb":
        pass
    elif database == "excel":
        import xlsxwriter
        print 111,'excel'
        workbook = xlsxwriter.Workbook('loupan.xlsx')
        worksheet = workbook.add_worksheet()
    elif database == "sqlite":
        pass


    # 让用户选择爬取哪个城市的二手房小区价格数据
    prompt = create_prompt_text()
    import sys

    if sys.version_info < (3, 0):  # 如果小于Python3
        city = raw_input(prompt)
    else:
        city = input(prompt)

    # 准备日期信息，爬到的数据存放到日期相关文件夹下
    date = get_date_string()
    # 获得 csv 文件路径
    # date = "20180331"   # 指定采集数据的日期
    # city = "sh"         # 指定采集数据的城市
    city_ch = get_chinese_city(city)
    csv_dir = "{0}\\loupan\\{1}\\{2}".format(DATA_PATH, city, date)

    files = list()
    if not os.path.exists(csv_dir):
        print("{0} does not exist.".format(csv_dir))
        print("Please run 'python xiaoqu.py' firstly.")
        printpythontest")
        exit(0)
    else:
        print('OK, start to process ' + get_chinese_city(city))
    for csv in os.listdir(csv_dir):
        data_csv = csv_dir + "/" + csv
        # print(data_csv)
        files.append(data_csv)

    # 清理数据
    count = 0
    row = 0
    col = 0
    for csv in files:
        with open(csv, 'r') as f:
            for line in f:
                count += 1

                text = line.strip()
                print text
                try:
                    # 如果小区名里面没有逗号，那么总共是7项
                    if text.count(',') == 4:
                        date, xiaoqu, price, totles, url = text.split(',')
                    elif text.count(',') < 4:
                        continue
                    else:
                        fields = text.split(',')
                        date = fields[0]
                        xiaoqu = ','.join(fields[3:-3])
                        price = fields[-3]
                        totles = fields[-2]
                        url = fields[-1]
                except Exception as e:
                    print(text)
                    print(e.message)
                    continue
                totles = totles.replace(r'万', '')
                price = price.replace(r'价格待定', '0')
                price = price.replace(r'元/m2', '')
                price = int(price)
                totles = int(totles)
                print("{0} {1} {2} {3} {4}".format(date, xiaoqu, price, totles, url))
                # 写入mysql数据库
                if database == "mysql":
                   pass
                elif database == "mongodb":
                    pass
                elif database == "sqlite":
                    pass
                    
                elif database == "excel":
                    price = str(price)+'元/平(均价)'
                    totles = str(totles)+'万'
                    if not PYTHON_3:
                        worksheet.write_string(row, col, unicode(city_ch, 'utf-8'))
                        worksheet.write_string(row, col + 1, date)
                        worksheet.write_string(row, col + 2, unicode(xiaoqu, 'utf-8'))
                        worksheet.write_string(row, col + 3, price)
                        worksheet.write_string(row, col + 4, unicode(totles, 'utf-8'))
                        worksheet.write_string(row, col + 5, unicode(url, 'utf-8'))
                    else:
                        worksheet.write_string(row, col, city_ch)
                        worksheet.write_string(row, col + 1, area)
                        worksheet.write_string(row, col + 2, xiaoqu)
                        worksheet.write_string(row, col + 3, price)
                        worksheet.write_string(row, col + 4, totles)
                        worksheet.write_string(row, col + 5, url)
                    row += 1
    if database == "excel":
        workbook.close()
    if database == "sqlite":    
        pass
    print("Total write {0} items to database.".format(count))
