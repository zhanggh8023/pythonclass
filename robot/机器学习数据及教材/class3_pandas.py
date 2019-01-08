# -*- coding: utf-8 -*-
# @Time    : 2018/9/14 14:09
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : class3_pandas.py
# @Software: PyCharm


import pandas as pd
import  numpy as  np



# food_info= pandas.read_csv('food_info.cvs')
# print(type(food_info))
# print(food_info.dtypes)
# print(help((pandas.read_csv)))

# food_info.head()
# food_info.tail(4)
# print(food_info.coumns)
# print(food_info.shape)

titanic_survival = pd.read_csv("titanic_train.csv")
titanic_survival.head()

age=titanic_survival['Age']
print(age.loc[0:10])
age_is_null=pd.isnull(age)
print(age_is_null)
age_null_true=age[age_is_null]
print(age_null_true)
age_null_count=len(age_null_true)
print(age_null_count)

mean_age = sum(titanic_survival['Age'])/len(titanic_survival['Age'])
print(mean_age)

good_ages=titanic_survival['Age'][age_is_null==False]
print(good_ages)
correct_mean_age=sum(good_ages)/len(good_ages)
print(correct_mean_age)

passenger_classes=[1,2,3]
fares_by_class={}
for this_class in passenger_classes:
    pclass_rows=titanic_survival[titanic_survival['Pclass']==this_class]
    pclass_fares=pclass_rows['Fare']
    fare_for_class=pclass_fares.mean()
    fares_by_class[this_class]=fare_for_class
print(fares_by_class)

#获救几率和船舱等级
passenger_survival=titanic_survival.pivot_table(index='Pclass',values='Survived',aggfunc=np.mean)
print(passenger_survival)
#几率和年龄
passenger_survival=titanic_survival.pivot_table(index='Pclass',values='Age')
print(passenger_survival)
#几率和登船地点
passenger_survival=titanic_survival.pivot_table(index='Embarked',values=['Fare','Survived'],aggfunc=np.sum)
print(passenger_survival)
#
drop_na_columns=titanic_survival.dropna(axis=1)
new_titanic_survival=titanic_survival.dropna(axis=0,subset=['Age','Sex'])
print(new_titanic_survival)

row_index_83_age = titanic_survival.loc[83,'Age']
row_index_1000_pclass = titanic_survival.loc[766,'Pclass']
print(row_index_83_age)
print(row_index_1000_pclass)

#排序
pd.set_option('display.width', 300) # 设置字符显示宽度
# pd.set_option('display.max_rows', None) # 设置显示最大行
pd.set_option('display.max_columns', None) # 设置显示最大列，None为显示所有列
new_titanic_survival = titanic_survival.sort_values('Age',ascending=False)
print(new_titanic_survival[0:10])
titanic_reindexed = new_titanic_survival.reset_index(drop=True)
print('-----------------------------------')
print(titanic_reindexed.loc[0:10])


#自定义函数
def hundredth_row(colum):
    hundredth_item = colum.loc[99]
    return hundredth_item

hundredth_row = titanic_survival.apply(hundredth_row)
print(hundredth_row)

#每一列缺失值
def not_null_count(column):
    column_null = pd.isnull(column)
    null = column[column_null]
    return len(null)
column_null_count = titanic_survival.apply(not_null_count)
print(column_null_count)


#
def which_class(row):
    pclass = row['Pclass']
    if pd.isnull(pclass):
        return 'Unknown'
    elif pclass == 1:
        return 'First Class'
    elif pclass ==2:
        return 'Second Class'
    elif pclass ==3:
        return 'Third Class'
classes = titanic_survival.apply(which_class,axis=1)
print(classes)

import pandas as pd
#Series类似于numpy.ndarray
fandango = pd.read_csv('fandango_score_comparison.csv')
series_film = fandango['FILM']
print(type(series_film))
print(series_film[0:5])
series_rt = fandango['RottenTomatoes']
print(series_rt[0:5])

print('================================================')
#获取电影评分
from pandas import Series
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030') #改变标准输出的默认编码

film_names = series_film.values
# print('1',type(film_names))
# print('2',film_names)
rt_scores = series_rt.values
# print('3',rt_scores)
series_custom = Series(rt_scores,index=film_names)
hh=series_custom[['The Water Diviner (2015)','Top Five (2014)']]
# print(series_custom)
print(hh)

print('================================================')

series_custom =Series(rt_scores,index=film_names)
ii=series_custom[['The Water Diviner (2015)','Top Five (2014)']]
fiveten = series_custom[5:10]
print(fiveten)

print('================================================')

original_index = series_custom.index.tolist()
#print(original_index)
sorted_index=sorted(original_index)
sorted_by_index = series_custom.reindex(sorted_index)
print(sorted_by_index)

print('================================================')

sc2= series_custom.sort_index()
sc3= series_custom.sort_values()
print(sc2[0:10])
print(sc3[0:10])

print('================================================')
#可以和np一起使用
print(np.add(series_custom,series_custom))
np.sin(series_custom)
np.max(series_custom)
#可以选取范围
ee=series_custom>50
print(ee)

















