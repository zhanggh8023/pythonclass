# -*- coding: utf-8 -*-
# @Time    : 2019/3/25 21:17
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : exls数据查询插入.py
# @Software: PyCharm


# from openpyxl import load_workbook
#
# wb= load_workbook('数据.xlsx')
# sheet = wb.get_sheet_by_name('Sheet1')
# for row in sheet.iter_rows():
# 	for cell in row:
# 		print(cell.coordinate, cell.value)
# print('--- END OF ROW ---')
#
#
#
# import pandas as pd
#
# df = pd.read_excel('数据.xlsx')
# print (df[df['总装']=='一']['数学'])

from openpyxl import workbook
from openpyxl import load_workbook


def find_false_in_sheet (sheet):
    for column in sheet.iter_cols():
        for cell2 in column:
            if cell2.value is not None:
                # print cell2.value
                # print type(cell2.value)
                info2 = cell2.value.find('false')
                if info2 == 0:
                    print(cell2)
                    print(cell2.value)



def find_false_in_xlsx (file_name):
    print(file_name)
    wb = load_workbook(file_name)
    all_sheets = wb.sheetnames
    print(all_sheets)

    for i in range(len(all_sheets)):
        sheet = wb[all_sheets[i]]
        print(sheet.title + ': max_row: ' + str(sheet.max_row) + ' max_column: ' + str(sheet.max_column))
        find_false_in_sheet(sheet)


# start
find_false_in_xlsx("数据.xlsx")

# for row in sheet.iter_rows():
#  for cell in row:
#   if cell.value is not None:
#    info = cell.value.find('BB')
#    if info == 0:
#     print cell.value




