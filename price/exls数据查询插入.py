# -*- coding: utf-8 -*-
# @Time    : 2019/3/25 21:17
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : exls数据查询插入.py
# @Software: PyCharm



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
#


# from openpyxl import workbook
# from openpyxl import load_workbook
#
#
# def find_false_in_sheet (sheet):
#     for column in sheet.iter_cols():
#         for cell2 in column:
#             if cell2.value is not None:
#                 # print(cell2.value)
#                 # print(type(cell2.value))
#                 info2 = cell2.value.find('false')
#                 if info2 == 0:
#                     print(cell2)
#                     print(cell2.value)
#
#
#
# def find_false_in_xlsx (file_name):
#     print(file_name)
#     wb = load_workbook(file_name)
#     all_sheets = wb.sheetnames
#     print(all_sheets)
#
#     for i in range(len(all_sheets)):
#         sheet = wb[all_sheets[i]]
#         print(sheet.title + ': max_row: ' + str(sheet.max_row) + ' max_column: ' + str(sheet.max_column))
#         find_false_in_sheet(sheet)
#
#
# # start
# find_false_in_xlsx("数据.xlsx")
#
# # for row in sheet.iter_rows():
# #  for cell in row:
# #   if cell.value is not None:
# #    info = cell.value.find('BB')
# #    if info == 0:
# #     print cell.value


from openpyxl import load_workbook

wb= load_workbook('数据.xlsx')

data=[]
data1=[]

def red_GD():
    sheet = wb['工单拆分']
    # print(sheet)
    for i in range(3,sheet.max_row):
        number_id=sheet.cell(row=i,column=7).value
        data1.append(number_id)
    # print(data1)
    # number_id=sheet['G3'].value
    # print(number_id)
    # return number_id

def red_ZZ():
    sheet = wb['总装']
    for i in range(sheet.max_row):
        for ii in range(sheet.max_column):
            dd=sheet.cell(row=i+3,column=ii+1).value
            # print(dd)
            dict={'i':i+3,'data':dd}
            # print(dict)
            data.append(dict)

red_ZZ()
red_GD()



for ii in range(len(data1)):
    for i in range(len(data)):
        sheet1=wb['总装']
        sheet = wb['日计划量']
        ff=data[i]['data']
        if data1[ii]==ff:
            tt=sheet1.cell(row=data[i]['i'],column=2).value
            print(ff,data1[ii])
            print(str(ii)+'-------------------对比正确班组：'+tt)
            sheet.cell(ii + 3, 6).value =tt
            break
wb.save('数据.xlsx')
print(data,data1)

