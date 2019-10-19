"""
通过 pymsql 模块
连接操作数据库
"""

import pymysql

class Mysql:
	connect_db = None
	# 配置信息
	config = {
		'host':'47.110.127.36',
		'user':'root',
		'password':'citydo@123',
		'database':'test',
		'charset':'utf8'
	}
	# 初始化
	def __init__(self):
		self.connect()
	# 连接数据库
	def connect(self):
		self.connect_db = pymysql.connect(
			host = self.config['host'],
			user = self.config['user'],
			password = self.config['password'],
			database = self.config['database'],
			charset = self.config['charset']
		)
		return self.connect_db
	# 查询
	def query(self,_sql):
		cursor = self.connect().cursor()
		try:
			cursor.execute(_sql)
			data = cursor.fetchall()
			self.connect().commit()
			return data
		except:
			self.connect_db.rollback()
			return False
		finally:
			cursor.close()
			self.connect_db.close()
	# 插入
	def insert(self,_sql):
		cursor = self.connect().cursor()
		try:
			cursor.execute(_sql)
			self.connect_db.commit()
			return True
		except:
			self.connect_db.rollback()
			return False
		finally:
			cursor.close()
			self.connect_db.close()
	# 批量插入
	def insert_many(self,_sql,_values):
		cursor = self.connect().cursor()
		try:
			cursor.executemany(_sql,_values)
			self.connect_db.commit()
			return True
		except:
			self.connect_db.rollback()
			return False
		finally:
			cursor.close()
			self.connect_db.close()
	# 更新
	def update(self,_sql):
		cursor = self.connect().cursor()
		try:
			cursor.execute(_sql)
			self.connect_db.commit()
			return True
		except:
			self.connect_db.rollback()
			return False
		finally:
			cursor.close()
			self.connect_db.close()
	# 删除
	def delete(self,_sql):
		cursor = self.connect().cursor()
		try:
			cursor.execute(_sql)
			self.connect_db.commit()
			return True
		except:
			self.connect_db.rollback()
			return False
		finally:
			cursor.close()
			self.connect_db.close()
