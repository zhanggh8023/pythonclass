#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/21 17:50
# @Author  : 侯瑞辉
# @File    : createdb.py  创建数据库

import pymysql
from flask import render_template

# 插入信息
def insert(StuId,NAME):
    conn1 = pymysql.connect(host='localhost', user='root', passwd='123456', db='student', port=3306, charset='utf8')
    cur = conn1.cursor()  # 获取一个游标
    insert_sql = "INSERT INTO StudentTable(StuId,StuName) VALUES ('%s','%s');" %(StuId,NAME)
    cur.execute(insert_sql)
    conn1.commit()
    cur.close()  # 关闭游标
    conn1.close()  # 释放数据库资源
    return render_template('login.html')

# 由学生id查询学生信息
def selectStu(stuid,username):
    conn = pymysql.connect(host='localhost', user='root', passwd='123456', db='student', port=3306, charset='utf8')
    cur = conn.cursor()  # 获取一个游标
    select_sql = "SELECT * FROM StudentTable WHERE StuName = '%s';" %(username)
    flag = False
    # 执行sql语句
    student = cur.execute(select_sql)
    # 获取结果
    results = cur.fetchall()
    print(results)
    for row in results:
        if row[1] == stuid and row[2] == username:
            flag = True
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源
    return flag

# 添加图书
def addBook(bookName,bookAuthor):
    conn1 = pymysql.connect(host='localhost', user='root', passwd='123456', db='student', port=3306, charset='utf8')
    cur = conn1.cursor()  # 获取一个游标
    insert_sql = "INSERT INTO BookTable(BookName,Author) VALUES ('%s','%s');" % (bookName, bookAuthor)
    cur.execute(insert_sql)
    conn1.commit()
    cur.close()  # 关闭游标
    conn1.close()  # 释放数据库资源
    return render_template('index.html')

# 查询所有图书
def queryAllBook():
    conn = pymysql.connect(host='localhost', user='root', passwd='123456', db='student', port=3306, charset='utf8')
    cur = conn.cursor()  # 获取一个游标
    select_sql = "SELECT * FROM BookTable ;"
    # 执行sql语句
    cur.execute(select_sql)
    # 获取结果
    results = cur.fetchall()
    bookList = []
    for i in range(len(results)):
        bookList.append(list(results[i]))
    print(bookList)
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源
    return render_template('showBook.html',bookList = bookList)

# 借阅图书
def Borrow(username,stuid,bookName,bookAuthor):
    conn1 = pymysql.connect(host='localhost', user='root', passwd='123456', db='student', port=3306, charset='utf8')
    cur = conn1.cursor()  # 获取一个游标
    insert_sql = "INSERT INTO BorrowTable(StuId,StudentNAME,BookName,Author) VALUES ('%s','%s','%s','%s');" % (stuid,username,bookName, bookAuthor)
    cur.execute(insert_sql)
    conn1.commit()
    cur.close()  # 关闭游标
    conn1.close()  # 释放数据库资源
    return render_template('index.html')

# 查询所有借阅图书
def queryBorrowBook():
    conn = pymysql.connect(host='localhost', user='root', passwd='123456', db='student', port=3306, charset='utf8')
    cur = conn.cursor()  # 获取一个游标
    select_sql = "SELECT * FROM BorrowTable ;"
    # 执行sql语句
    cur.execute(select_sql)
    # 获取结果
    results = cur.fetchall()
    BorrowBookList = []
    for i in range(len(results)):
        BorrowBookList.append(list(results[i]))
    print(BorrowBookList)
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源
    return render_template('BorrowBook.html',BorrowBookList = BorrowBookList)

# 归还图书
def ReturnBook(bookName):
    conn1 = pymysql.connect(host='localhost', user='root', passwd='123456', db='student', port=3306, charset='utf8')
    cur = conn1.cursor()  # 获取一个游标
    delete_sql = "DELETE FROM BorrowTable WHERE BookName = '%s';" % (bookName)
    cur.execute(delete_sql)
    conn1.commit()
    cur.close()  # 关闭游标
    conn1.close()  # 释放数据库资源··
    return render_template('index.html')

