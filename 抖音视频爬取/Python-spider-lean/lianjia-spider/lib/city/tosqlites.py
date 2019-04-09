#!/usr/bin/env weathersemper
# -*- coding:utf-8 -*-  
"""
@author: YuFei 
@email: yufei6808@163.com
@site: http://www.antuan.com
@version: 0.0.1
@date: 2018-08-23
@explain: 功能介绍
"""
from macpath import split
import sqlite3


def tosqlite(dbname,date_string,datas):
    '''
    create table zufang(
        [id]    integer PRIMARY KEY autoincrement,
        [area]    varchar default 0,
        [circle]    varchar default 0,
        [community]    varchar default 0,
        [room]     varchar default 0,
        [size]     varchar default 0,
        [price]    varchar default 0,
        [dates]    datetime default (datetime('now', 'localtime'))
    );
    
    INSERT INTO OilPrice(area,circle,community,room,size,price,dates)  VALUES('高新','汽车西站','海亮九玺','2室2厅','88平米','1800','20180404');
    '''

    tablename = dbname
    dbname = 'F:\ID\python\sqlpythontestianjia.db'
    con = sqlite3.connect(dbname)
    cur = con.cursor()
    sql = 'INSERT INTO '+tablename+' (area,circle,community,room,size,price,dates) VALUES(?,?,?,?,?,?,?)'
    print sql
    cur.execute(sql,datas+','+date_string)
    con.commit()
    cur.close()
    con.close()