# -*- coding: utf-8 -*-
# @Time    : 2019/6/6 4:33
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : RWexcel.py
# @Software: PyCharm


from openpyxl import load_workbook

wb= load_workbook('voicedata.xlsx')

def readexcel(sheet):
    data=[]

    sheet = wb[sheet]
    for i in range(sheet.max_row-1):
        name = sheet.cell(row=i + 2, column=1).value
        phone = sheet.cell(row=i + 2, column=3).value
        score = sheet.cell(row=i + 2, column=5).value

        dict = {'id': i + 1, 'name': name, 'phone': phone,'score':score}
        data.append(dict)
    print('读取数据成功：',data)
    return data

def write_Excel(file,sheet,i,dcit):
    try:
        wb_new = load_workbook(file)
        sheet = wb_new[sheet]
        for ii in range(0,23):
            sheet.cell(i, ii+6).value = dcit[ii]
        wb_new.save(file)
        print('执行写入excel成功！')
    except Exception as e:
        print('数据写入失败！%s'%e)
        raise e

if __name__ == '__main__':
    readexcel('Sheet1')
    write_Excel('voicedata.xlsx','Sheet1',2,['1','2','3','4','1','2','3','4','1','2','3','4','1','2','3','4','1','2','3','4','1','2','3'])


