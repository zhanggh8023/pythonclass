# -*- coding: utf-8 -*-
# @Time    : 2020/7/29 13:43
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : ppt_unzip.py
# @Software: PyCharm

import os
import sys
import zipfile
import unrar  # 直接pip install unrar
from unrar import rarfile
import shutil
from PPTdownload.ppt_downadr import readExcel

def unzip(filename: str):
    try:
        file = zipfile.ZipFile(filename)
        dirname = filename.replace('.zip', '')
        # 如果存在与压缩包同名文件夹 提示信息并跳过
        if os.path.exists(dirname):
            print(f'{filename} dir has already existed')
            return
        else:
            # 创建文件夹，并解压
            os.mkdir(dirname)
            file.extractall(dirname)
            file.close()
            # 递归修复编码
            rename(dirname)
    except:
        print(f'{filename} unzip fail')

    return dirname


def rename(pwd: str, filename=''):
    """压缩包内部文件有中文名, 解压后出现乱码，进行恢复"""

    path = f'{pwd}/{filename}'
    if os.path.isdir(path):
        for i in os.scandir(path):
            rename(path, i.name)
    newname = filename.encode('cp437').decode('gbk')
    os.rename(path, f'{pwd}/{newname}')


def main():
    """如果指定文件，则解压目标文件，否则解压当前目录下所有文件"""

    if len(sys.argv) != 1:
        i: str
        for i in sys.argv:
            if i.endswith('.zip') and os.path.isfile(i):
                unzip(i)
    else:
        for file in os.scandir(os.getcwd()):
            if file.name.endswith('.zip') and file.is_file():
                unzip(file.name)


def un_rar(filename):  # filename是文件的绝对路径
    rar = rarfile.RarFile(filename)
    # 判断是否存在同名文件夹，若不存在则创建同名文件夹：
    if os.path.isdir(os.path.splitext(filename)[0]):
        pass
    else:
        os.mkdir(os.path.splitext(filename)[0])
    rar.extractall(os.path.splitext(filename)[0])



# 路径获取
def file_name(file_dir):
    L=[]
    K = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.zip':
                L.append(os.path.join(root, file))

            if os.path.splitext(file)[1] == '.ppt':
                K.append(os.path.join(root, file))

            if os.path.splitext(file)[1] == '.pptx':
                K.append(os.path.join(root, file))
    print(L, K)
    return L, K


def pptMove(Pgroup,Pname):
    try:
        with zipfile.ZipFile(file_name('./PPT/' + Pgroup + '/' + Pname + '/')[0][0], 'a', ) as z:
            print(z.namelist())
            # print(z.namelist()[1].split('/', -1)[1])

            f_name = 'PPT/' + Pgroup + '/' + Pname + '/'
            # 把压缩包里的 文件解压出来
            z.extractall(f_name)
            z.close()

            shutil.move(f_name + z.namelist()[1], f_name + Pname + ".pptx")
            shutil.rmtree(f_name + z.namelist()[1].split('/', -1)[0])
        print("{}/{}：解压成功！".format(Pgroup, Pname))
    except:
        un_rar(file_name('./PPT/' + Pgroup + '/' + Pname + '/')[0][0])

        f_name = 'PPT/' + Pgroup + '/' + Pname + '/'
        print(file_name(f_name)[1][0])
        shutil.move(file_name(f_name)[1][0], f_name + Pname + ".pptx")
        shutil.rmtree(f_name + '/' + Pname)
        print("{}/{}：解压成功！".format(Pgroup, Pname))


def pptDel(Pgroup, Pname):
    with zipfile.ZipFile(file_name('./PPT/' + Pgroup + '/' + Pname.replace(':', '') + '/')[0], 'r') as z:
        print(z.namelist()[1])
        # print(z.namelist()[1].split('/', -1)[1])

        f_name = 'PPT/' + Pgroup + '/' + Pname.replace(':', '') + '/'

        os.remove(f_name + z.namelist()[1].split('/', -1)[0] + '.zip')




if __name__ == '__main__':
    # main()
    # k = file_name('./PPT/经典PPT模板/三生三世十里桃花PPT模板')
    # print(k[0])

    pptMove('社会生活PPT模板', '蓝色公司简介PPT模板下载')

    # list = readExcel()
    #
    # for i in range(len(list)):
    #     if '√' == list[i]['status']:
    #         pptDel(list[i]['Pgroup'], list[i]['Pname'])
    #     else:
    #         pass
    # print(list)
