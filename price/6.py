#工具库导入

import pandas as pd

import cx_Oracle

# 注：设置环境编码方式，可解决读取数据库乱码问题
import os 
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

#实现查询并返回dataframe

host = "122.112.248.182"  # 数据库ip
port = "1521"  # 端口
sid = "CITYDO"  # 数据库名称
dsn = cx_Oracle.makedsn(host, port, sid)

# scott是数据用户名，tiger是登录密码（默认用户名和密码）
connection = cx_Oracle.connect("hg", "123456", '122.112.248.182:1521/CITYDO')

# 操作游标
cursor = connection.cursor()

sql_1 = 'insert into YJPT_JGXXB(YXJGDM,NBJGH,JRXKZH,YXJGMC,JGLB,YZBM,WDH,YYZT,CLSJ,JGGZKSSJ,JGGZZZSJ,JGDZ,FZRXM,FZRZW,FZRLXDH,CJRQ) ' \
            'value (%(YXJGDM)s,%(NBJGH)s,%(JRXKZH)s,%(YXJGMC)s,%(JGLB)s,%(YZBM)s,%(WDH)s,%(YYZT)s,%(CLSJ)s,%(JGGZKSSJ)s,%(JGGZZZSJ)s,%(JGDZ)s,%(FZRXM)s,%(FZRZW)s,%(FZRLXDH)s,%(CJRQ)s)'
list_1 = [
    {'YXJGDM': 313340000010, 'NBJGH': 9010, 'JRXKZH': 'B0151B233090001', 'YXJGMC': '杭州银行股份有限公司舟山分行', 'JGLB': '基础网店',
     'YZBM': 316000, 'WDH': 9010, 'YYZT': '营业', 'CLSJ': 20010701, 'JGGZKSSJ': '083000', 'JGGZZZSJ': '173000',
     'JGDZ': '舟山市定海区临城街道定沈路619号舟山港航国际大厦B座', 'FZRXM': '张晓燕', 'FZRZW': '行长', 'FZRLXDH': '0580-3807915',
     'CJRQ': '20171027', },
    {'YXJGDM': '', 'NBJGH': 660000, 'JRXKZH': '', 'YXJGMC': '杭州银行股份有限公司金融事业部', 'JGLB': '一级分行(虚拟)',
     'YZBM': 316001, 'WDH': 9011, 'YYZT': '营业', 'CLSJ': 20010701, 'JGGZKSSJ': '083000', 'JGGZZZSJ': '173000',
     'JGDZ': '杭州市沁春路46号', 'FZRXM': '无', 'FZRZW': '无', 'FZRLXDH': '无',
     'CJRQ': '20171028', },
    {'YXJGDM': 313340000011, 'NBJGH': 9011, 'JRXKZH': 'B0151B233090002', 'YXJGMC': '杭州银行股份有限公司杭州分行', 'JGLB': '基础网店',
     'YZBM': 316001, 'WDH': 9010, 'YYZT': '营业', 'CLSJ': 20010701, 'JGGZKSSJ': '083000', 'JGGZZZSJ': '173000',
     'JGDZ': '杭州市舟山港航国际大厦B座', 'FZRXM': '酥饼', 'FZRZW': '行长', 'FZRLXDH': '0580-3807916',
     'CJRQ': '20171027', },
    {'YXJGDM': 313340000012, 'NBJGH': 9012, 'JRXKZH': 'B0151B233090003', 'YXJGMC': '杭州银行股份有限公司上海分行', 'JGLB': '基础网店',
     'YZBM': 316002, 'WDH': 9012, 'YYZT': '营业', 'CLSJ': 20010701, 'JGGZKSSJ': '083000', 'JGGZZZSJ': '173000',
     'JGDZ': '舟山市定海区杭州大厦14楼', 'FZRXM': '王晓鲁', 'FZRZW': '行长', 'FZRLXDH': '0580-3807918',
     'CJRQ': '20171027', },
    {'YXJGDM': 313340000013, 'NBJGH': 9013, 'JRXKZH': 'B0151B233090004', 'YXJGMC': '杭州银行股份有限公司北京分行', 'JGLB': '基础网店',
     'YZBM': 316004, 'WDH': 9014, 'YYZT': '营业', 'CLSJ': 20010701, 'JGGZKSSJ': '083000', 'JGGZZZSJ': '173000',
     'JGDZ': '北京王府井大街9号', 'FZRXM': '章章话', 'FZRZW': '行长', 'FZRLXDH': '0580-3807934',
     'CJRQ': '20171027', },
    {'YXJGDM': 313340000043, 'NBJGH': 9065, 'JRXKZH': 'B0151B233090076', 'YXJGMC': '杭州银行股份有限公司秦山分行', 'JGLB': '基础网店',
     'YZBM': 316009, 'WDH': 9018, 'YYZT': '营业', 'CLSJ': 20010701, 'JGGZKSSJ': '083000', 'JGGZZZSJ': '173000',
     'JGDZ': '广东省秦山市呼噜噜大街98号', 'FZRXM': '吴山石', 'FZRZW': '行长', 'FZRLXDH': '0580-3807956',
     'CJRQ': '20171027', }, ]

# 执行查询
# cursor.execute("select * from v$version ")

#cursor.execute("create table test(id int,name varchar2(10))")
#cursor.execute("insert into test values (1,'aaa')")
#cursor.execute("select * from YJPT_JGXXB where  NBJGH=9010")
# cursor.execute("INSERT INTO YJPT_JGXXB(YXJGDM,NBJGH,JRXKZH,YXJGMC,JGLB,YZBM,WDH,YYZT,CLSJ,JGGZKSSJ,JGGZZZSJ,JGDZ,FZRXM,FZRZW,FZRLXDH,CJRQ) VALUES"
#                "(313340000010,9010,'B0151B233090001','杭州银行股份有限公司舟山分行','基础网店',316000,9010,'营业',20010701,'083000','173000','舟山市定海区临城街道定沈路619号舟山港航国际大厦B座','张晓燕','行长','0580-3807915','20171027'),"
#                "(313340000010,9011,'B0151B233090001','杭州银行股份有限公司杭州分行','基础网点',316001,9010,'营业',20010702,'083000','173000','舟山市定海区临城街道定沈路620号舟山港航国际大厦A座','袁华','科长','0580-3807916','20171027'),"(313340000010,9012,'B0151B233090001',	'杭州银行股份有限公司上海分行	基础网点',	316002,	9010,'营业',20010703,'083000','173000','舟山市定海区临城街道定沈路621号舟山港航国际大厦C座','秋雅','副科长','0580-3807917','20171027'),"
#                "(313340000010,9013,'B0151B23309000','杭州银行股份有限公司北京分行',	'基础网点',	316003,	9010,'营业',20010704,'083000','173000','舟山市定海区临城街道定沈路622号舟山港航国际大厦F座',	'夏洛',	'科长',	'0580-3807918',	'20171027'),"
#                "(313340000010,9014,'B0151B233090001','杭州银行股份有限公司舟山分行','基础网点',316004,9010,'营业',20010705,'083000','173000	','舟山市定海区临城街道定沈路623号舟山港航国际大厦G座','冬梅','主任','0580-3807919','20171027'),"
#                "(313340000011,660000,'B0151B233090001','杭州银行股份有限公司金融事业部','一级分行(虚拟)',316005,9010,'营业','083000','173000','杭州市庆春路46号','无	','无',	'无','20171027')")

#cursor.execute("update YJPT_JGXXB set YXJGDM=313340000210 where NBJGH=9010")

# 执行sql语句
#
# sql = "INSERT INTO YJPT_JGXXB(YXJGDM,NBJGH,JRXKZH,YXJGMC,JGLB,YZBM,WDH,YYZT,CLSJ,JGGZKSSJ,JGGZZZSJ,JGDZ,FZRXM,FZRZW,FZRLXDH,CJRQ) VALUES(:pointId)"
sql = "INSERT INTO YJPT_JGXXB(YXJGDM,NBJGH,JRXKZH,YXJGMC,JGLB,YZBM,WDH,YYZT,CLSJ,JGGZKSSJ,JGGZZZSJ,JGDZ,FZRXM,FZRZW,FZRLXDH,CJRQ) VALUES(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16)"
cursor.prepare(sql)
cursor.execute(None,hh)

# sql = "INSERT INTO T_AUTOMONITOR_TMP(YXJGDM,) VALUES(:1,)"
# cursor.prepare(sql)
# rown = cursor.executemany(None, {'YXJGDM': 313340000010,} )

#cursor.execute("DELETE FROM YJPT_JGXXB WHERE NBJGH =9010 ")
#获取返回信息
# rs = cursor.fetchall()
#
# # 输出信息
# for v in rs:
#     print(v)


#切记一定要执行
cursor.execute('commit')


# 关闭连接，释放资源
cursor.close()
connection.close()

