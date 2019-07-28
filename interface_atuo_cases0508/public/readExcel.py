# -*- coding: utf-8 -*-
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : readExcel.py
# @Software: PyCharm


import os
from public.config import config
from openpyxl import load_workbook
from conf import Allpath
from public.logger import Log

logger = Log('auto_cases', Allpath.log_path)
url_1 = str(config().read_config(Allpath.http_conf_path, 'HTTP', 'url'))
mode = config().read_config(Allpath.case_conf_path, 'FLAG', 'mode')
logger.info("用例执行模式：0全部执行，1执行指定配置接口:%s" % mode)
logger.info("服务地址配置：%s" % url_1)
case_list = config().read_config(Allpath.case_conf_path, 'FLAG', 'case_list')
logger.info("用例列表：%s" % case_list)


class readExcel:
    def __init__(self, file, sheet):
        self.file = file
        self.sheet = sheet

    def read_Excel(self):
        rd = load_workbook(self.file)
        sheet = rd[self.sheet]
        logger.info('获取表单成功：%s' % sheet)

        # initphone=self.get_init_phone()
        # print(initphone)#当作一个局部变量来看这个，一轮循环下来后在更新到excel

        data_list = []
        if mode == 0:
            for i in range(sheet.max_row - 1):
                method = sheet.cell(row=i + 2, column=2).value
                case_name = sheet.cell(row=i + 2, column=3).value
                url = url_1 + sheet.cell(row=i + 2, column=4).value
                data = eval(sheet.cell(row=i + 2, column=5).value)  # 取值excel中的字典
                sql = eval(sheet.cell(row=i + 2, column=6).value)
                code = sheet.cell(row=i + 2, column=7).value
                dict = {'id': i + 1, 'case_name': case_name, 'url': url, 'method': method, 'sql': sql, 'data': data,
                        'code': code}
                data_list.append(dict)
            # self.update_phone(initphone)#把最后的值更新到excel中

        if mode == 1:
            for i in range(sheet.max_row - 1):
                id = sheet.cell(row=i + 2, column=1).value
                if id in case_list:
                    # print(i)
                    method = sheet.cell(row=i + 2, column=2).value
                    case_name = sheet.cell(row=i + 2, column=3).value
                    url = url_1 + str(sheet.cell(row=i + 2, column=4).value)
                    data = eval(sheet.cell(row=i + 2, column=5).value)  # 取值excel中的字典
                    sql = eval(sheet.cell(row=i + 2, column=6).value)
                    code = sheet.cell(row=i + 2, column=7).value
                    dict = {'id': i + 1, 'case_name': case_name, 'url': url, 'method': method, 'sql': sql, 'data': data,
                            'code': code}
                    data_list.append(dict)
        # print(data_list)
        return data_list


def readexcel():
    file = Allpath.test_data_path
    sheet = 'Sheet2'
    rd = load_workbook(file)
    sheet = rd[sheet]
    logger.info('获取历史测试表单成功：%s' % sheet)
    dict = {'restult': '', 'sum': [], 'ok': [], 'fail': [], 'error': [],'error_1':[]}
    max = sheet.max_row + 1
    mix = sheet.max_row - 10
    if mix <= 1:
        mix = 2
    else:
        mix = max - 10
    for i in range(mix, max):
        dict['restult'] = sheet.cell(row=2, column=1).value
        dict['sum'].append(sheet.cell(row=i, column=2).value)
        dict['ok'].append(sheet.cell(row=i, column=3).value)
        dict['fail'].append(sheet.cell(row=i, column=4).value)
        dict['error'].append(sheet.cell(row=i, column=5).value)
        dict['error_1'].append(sheet.cell(row=i, column=5).value)
    return dict

    # 读取初始化手机
    # def get_init_phone(self):
    #     wb=load_workbook(self.file)
    #     sheet=wb[self.init]
    #     initphone=sheet.cell(row=1,column=2).value
    #     return initphone
    # def update_phone(self,phone):#更新手机
    #     wb = load_workbook (self.file)
    #     sheet=wb.get_sheet_by_name(self.init)
    #     sheet.cell(1,2).value=phone
    #     wb.save(self.file)


if __name__ == '__main__':
    readexcel()
    readExcel(Allpath.test_data_path, 'Sheet1').read_Excel()
