# -*- coding: utf-8 -*-


import os
from interface_atuo_cases0508.public.config import config
from openpyxl import load_workbook
from interface_atuo_cases0508.conf import Allpath
from interface_atuo_cases0508.public.logger import Log

logger=Log('auto_cases',Allpath.log_path)
url_1=str(config ().read_config (Allpath.http_conf_path, 'HTTP', 'url'))
mode = config ().read_config (Allpath.case_conf_path, 'FLAG', 'mode')
print(url_1)
case_list=config ().read_config (Allpath.case_conf_path, 'FLAG', 'case_list')
#print(case_list)


class readExcel:
    def __init__(self,file,sheet,init):
        self.file=file
        self.sheet=sheet
        self.init=init

    def read_Excel(self):
        rd=load_workbook(self.file)
        sheet=rd[self.sheet]
        logger.info('获取表单成功：%s'%sheet)

        initphone=self.get_init_phone()
        #print(initphone)#当作一个局部变量来看这个，一轮循环下来后在更新到excel

        data_list=[]
        if mode == 1:
            for i in range(sheet.max_row-1):
                method = sheet.cell(row=i + 2, column=2).value
                url=url_1+sheet.cell(row=i + 2, column=3).value
                data=eval(sheet.cell(row=i+2,column=4).value)#取值excel中的字典
                #print(url)
                sql=eval(sheet.cell(row=i+2,column=5).value)
                code=sheet.cell(row=i+2,column=6).value
                if data['mobilephone']==initphone:#判断是否与保存的最后一次相同
                    data['mobilephone'] = initphone+1#相同就加一
                    sql['condition']=initphone+1
                    logger.info('全部执行用例%s，手机号已使用，自动加1'%(i+1))
                else:
                    data['mobilephone'] = initphone#给字典赋值变量中的号码
                    sql['condition'] = initphone
                    logger.info('全部执行用例%s，手机号可以使用'%(i+1))
                initphone += 1#作为局部变量累加存储
                dict={'id':i+1,'url':url,'method':method,'data':data,'sql':sql,'code':code}
                data_list.append(dict)
            #self.update_phone(initphone)#把最后的值更新到excel中

        if mode == 0:
            for i in range(sheet.max_row - 1):
                id=sheet.cell(row=i + 2, column=1).value
                if id in case_list:
                    method = sheet.cell(row=i + 2, column=2).value
                    url = url_1+str(sheet.cell(row=i + 2, column=3).value)
                    data=eval(sheet.cell(row=i+2,column=4).value)#取值excel中的字典
                    sql=eval(sheet.cell(row=i+2,column=5).value)
                    code=sheet.cell(row=i+2,column=6).value
                    if data['mobilephone']==initphone:#判断是否与保存的最后一次相同
                        data['mobilephone'] = initphone+1#相同就加一
                        sql['condition']=initphone+1
                        logger.info('选择执行用例%s，手机号已使用，自动加1'%(i+1))
                    else:
                        data['mobilephone'] = initphone#给字典赋值变量中的号码
                        sql['condition'] = initphone
                        logger.info('选择执行用例%s，手机号可以使用'%(i+1))
                    initphone += 1#作为局部变量累加存储
                    dict={'id':i+1,'url':url,'method':method,'data':data,'sql':sql,'code':code}
                    data_list.append(dict)
                #self.update_phone(initphone)#把最后的值更新到excel中
        print(data_list)
        return data_list

    #读取初始化手机
    def get_init_phone(self):
        wb=load_workbook(self.file)
        sheet=wb[self.init]
        initphone=sheet.cell(row=1,column=2).value
        return initphone
    def update_phone(self,phone):#更新手机
        wb = load_workbook (self.file)
        sheet=wb.get_sheet_by_name(self.init)
        sheet.cell(1,2).value=phone
        wb.save(self.file)


if __name__ == '__main__':
    readExcel(Allpath.test_data_path,'rechargetestcases','init').read_Excel()
