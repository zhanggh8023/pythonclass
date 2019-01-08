import mysql.connector
from zghmysql.db_config import readConfig
from zghmysql.readexcel import readExcel

#连接数据库
#1、数据库连接信息
config={'host':'119.3.6.221',
        'user':'root',
        'password':'citydo@123',
        'port':3306,
        'database':'zgh_jghg',
        }

#2、登录数据库
#conection=mysql.connector.connect(**config)#  **后面加上配置文件名

#调用配置文件模块读取配置信息进行登录
connector=mysql.connector.connect(**readConfig().read_config('db.conf','DBCONFIG','config'))

#建游标
cursor=connector.cursor()

#新建数据库
#cursor.execute("CREATE DATABASE zgh1practice")

#删除数据库
#cursor.execute("drop database zgh_practice")

#cursor.execute(zgh)#新建表单
#cursor.execute(sql_create_table)

#cursor.execute('drop table zgh_practice')#删除表单

#机构信息表
sql_1='insert into YJPT_JGXXB(YXJGDM,NBJGH,JRXKZH,YXJGMC,JGLB,YZBM,WDH,YYZT,CLSJ,JGGZKSSJ,JGGZZSSJ,JGDZ,FZRXM,FZRZW,FZRLXDH,CJRQ) ' \
    'value (%(YXJGDM)s,%(NBJGH)s,%(JRXKZH)s,%(YXJGMC)s,%(JGLB)s,%(YZBM)s,%(WDH)s,%(YYZT)s,%(CLSJ)s,%(JGGZKSSJ)s,%(JGGZZSSJ)s,%(JGDZ)s,%(FZRXM)s,%(FZRZW)s,%(FZRLXDH)s,%(CJRQ)s)'
list_1=[{'YXJGDM':313340000010,'NBJGH':9010,'JRXKZH':'B0151B233090001','YXJGMC':'杭州银行股份有限公司舟山分行','JGLB':'基础网店','YZBM':316000,'WDH':9010,'YYZT':'营业','CLSJ':20010701,'JGGZKSSJ':'083000','JGGZZSSJ':'173000','JGDZ':'舟山市定海区临城街道定沈路619号舟山港航国际大厦B座','FZRXM':'张晓燕','FZRZW':'行长','FZRLXDH':'0580-3807915','CJRQ':'20171027',},
        {'YXJGDM': '', 'NBJGH': 660000, 'JRXKZH': '', 'YXJGMC': '杭州银行股份有限公司金融事业部', 'JGLB': '一级分行(虚拟)',
         'YZBM': 316001, 'WDH': 9011, 'YYZT': '营业', 'CLSJ': 20010701, 'JGGZKSSJ': '083000', 'JGGZZSSJ': '173000',
         'JGDZ': '杭州市沁春路46号', 'FZRXM': '无', 'FZRZW': '无', 'FZRLXDH': '无',
         'CJRQ': '20171028', },
        {'YXJGDM': 313340000011, 'NBJGH': 9011, 'JRXKZH': 'B0151B233090002', 'YXJGMC': '杭州银行股份有限公司杭州分行', 'JGLB': '基础网店',
         'YZBM': 316001, 'WDH': 9010, 'YYZT': '营业', 'CLSJ': 20010701, 'JGGZKSSJ': '083000', 'JGGZZSSJ': '173000',
         'JGDZ': '杭州市舟山港航国际大厦B座', 'FZRXM': '酥饼', 'FZRZW': '行长', 'FZRLXDH': '0580-3807916',
         'CJRQ': '20171027', },
        {'YXJGDM': 313340000012, 'NBJGH': 9012, 'JRXKZH': 'B0151B233090003', 'YXJGMC': '杭州银行股份有限公司上海分行', 'JGLB': '基础网店',
         'YZBM': 316002, 'WDH': 9012, 'YYZT': '营业', 'CLSJ': 20010701, 'JGGZKSSJ': '083000', 'JGGZZSSJ': '173000',
         'JGDZ': '舟山市定海区杭州大厦14楼', 'FZRXM': '王晓鲁', 'FZRZW': '行长', 'FZRLXDH': '0580-3807918',
         'CJRQ': '20171027', },
        {'YXJGDM': 313340000013, 'NBJGH': 9013, 'JRXKZH': 'B0151B233090004', 'YXJGMC': '杭州银行股份有限公司北京分行', 'JGLB': '基础网店',
         'YZBM': 316004, 'WDH': 9014, 'YYZT': '营业', 'CLSJ': 20010701, 'JGGZKSSJ': '083000', 'JGGZZSSJ': '173000',
         'JGDZ': '北京王府井大街9号', 'FZRXM': '章章话', 'FZRZW': '行长', 'FZRLXDH': '0580-3807934',
         'CJRQ': '20171027', },
        {'YXJGDM': 313340000043, 'NBJGH': 9065, 'JRXKZH': 'B0151B233090076', 'YXJGMC': '杭州银行股份有限公司秦山分行', 'JGLB': '基础网店',
         'YZBM': 316009, 'WDH': 9018, 'YYZT': '营业', 'CLSJ': 20010701, 'JGGZKSSJ': '083000', 'JGGZZSSJ': '173000',
         'JGDZ': '广东省秦山市呼噜噜大街98号', 'FZRXM': '吴山石', 'FZRZW': '行长', 'FZRLXDH': '0580-3807956',
         'CJRQ': '20171027', },]

#员工表
sql_2='insert into YJPT_JGXXB(YXJGDM,NBJGH,JRXKZH,YXJGMC,JGLB,YZBM,WDH,YYZT,CLSJ,JGGZKSSJ,JGGZZZSJ,JGDZ,FZRXM,FZRZW,FZRLXDH,CJRQ) ' \
    'value (%(YXJGDM)s,%(NBJGH)s,%(JRXKZH)s,%(YXJGMC)s,%(JGLB)s,%(YZBM)s,%(WDH)s,%(YYZT)s,%(CLSJ)s,%(JGGZKSSJ)s,%(JGGZZZSJ)s,%(JGDZ)s,%(FZRXM)s,%(FZRZW)s,%(FZRLXDH)s,%(CJRQ)s)'
list_2=readExcel().read_Excel('机构信息表YJPT_JGXXB')
print(list_2)
#list_2=[{'YXJGDM': 313340000010, 'NBJGH': 9010, 'JRXKZH': 'B0151B233090001', 'YXJGMC': '杭州银行股份有限公司舟山分行', 'JGLB': '基础网点', 'YZBM': 316000, 'WDH': 9010, 'YYZT': '营业', 'CLSJ': 20010701, 'JGGZKSSJ': '083000', 'JGGZJSSJ': '173000', 'JGDZ': '舟山市定海区临城街道定沈路619号舟山港航国际大厦1座', 'FZRXM': '张晓燕', 'FZRZW': '行长', 'FZRLXDH': '0580-3807915', 'CJRQ': 20171027}]


cursor.executemany(sql_2,list_2)#对表进行内容插入X

#修改表中名字为seleath的age值为3
#cursor.execute("update yyt_practice set age=3 where name='seleath4'")

#表中插入一条数据对应值
#cursor.execute("insert into yyt_practice(id,name,age) value(99,'seleath66',55)")


#切记一定要执行
cursor.execute('commit')


#关闭游标
cursor.close()

#关闭连接
connector.close()