import pandas as pd

import cx_Oracle


# 实现插入功能
def input_to_db(data, table):
    # scott是数据用户名，tiger是登录密码（默认用户名和密码）
    connection = cx_Oracle.connect("hg", "123456", '122.112.248.182:1521/CITYDO')

    # 建立游标
    cursor = connection.cursor()

    # sql语句,注意%s要加引号，否则会报ora-01036错误

    query = "INSERT INTO" + table + "(YXJGDM,NBJGH,,) VALUES ('%s', '%s', '%s')"
    # 逐行插入数据
    for i in range(len(data)):
        YXJGDM = data.ix[i, 0]
        NBJGH = data.ix[i, 1]
        JRXKZH = data.ix[i, 2]

    # 执行sql语句
    cursor.execute(query % (YXJGDM, NBJGH, JRXKZH))

    cursor.commit()

    # 关闭游标

    cursor.close()
    connection.close()

    # 测试插入数据库

# 测试数据
test_data = pd.DataFrame([['小明', '男', 18], ['小芳', '女', 18]], index=[1, 2], columns=['YXJGDM', 'NBJGH', 'JRXKZH'])

# 调用函数实现插入
input_to_db(test_data, 'YJPT_JGXXB')