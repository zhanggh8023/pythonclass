# -*- coding: utf-8 -*-
# @Time    : 2018/9/4 9:27
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : class1.py
# @Software: PyCharm

days=365

days_1=367
days_2=366


number_of_days = 365
number_of_days_1 = 366

print(365)

print(number_of_days)
print('hello! python')


str_test = 'China'
int_test = 123
float_test = 1222.5


print(type(str_test),str_test)
print(type(int_test),int_test)
print(type(float_test),float_test)


str_eight=str(8)
#str_eight+10
print(type(str_eight))
eight=8
str_eight_two = str(eight)

str_eight1='8'
int_eight=int(str_eight1)
int_eight+10
print(type(int_eight))

# str_test='test'
# int(str_test)
# print(type(str_test))





china=10
print(china**2)


#List
months = []
print(type(months))
months.append('January')
months.append('February')
print(months)

months = []
print(type(months))
months.append('January')
months.append(1)
months.append('February')
months.append((1,2,3,4,5,))
print(months)


countries=[]
temperaturer=[]

countries.append('China')
countries.append('India')
countries.append('United')

temperaturer.append(30.5)
temperaturer.append(25.0)
temperaturer.append(15.1)
print(countries)
print(temperaturer)
china=countries[0]
china_temperature=temperaturer[1]
print(china)
print(china_temperature)

int_months=[1,2,3,4,5,6,7,8,9,10,11,12]
length=len(int_months)
print(length)

int_months=[1,2,3,4,5,6,7,8,9,10,11,12]
index=len(int_months)-1
print(index)
last_value=int_months[index]
print(last_value)
print(int_months[-1])


months=['Jan','Feb','Mar','Apr','May','Jun','Jul']
two_four=months[2:4]
print(two_four)
three_six=months[3:]
print(three_six)

cities =['Houston','Austin','Dallas']
for city in cities:
    print(city,),
print('123')


i = 0
while i <3:
    i +=1
    print(i,),


for i in range(10):
    print(i)

cities=[['Jan','Feb','Mar','Apr','May','Jun','Jul'],['Houston','Austin','Dallas']]
for city in cities:
    print(city,)

for i in cities:
    for j in i:
        print(j),


#Booleans

cat=True
dog=False
print(type(cat))

print(8 == 8)
print(8!=8)
print(8==10)
print(8!=10)
print('abc'=='8')


rates=[10,15,20]
print(rates[0]>rates[1])


sample_rate=700
greater=(sample_rate>5)
if greater:
    print(sample_rate)
else:
    print('less than')


animals=['cat','dog','rabbit']
if 'cat' in animals:
    print('Cat found' )




months1=['Jan','Feb','Mar','Apr','May','Jun','Jul']
cities1 =['Houston','Austin','Dallas']

index1=[0,1,2,3,]
name='Houston'

for i in index1:
    if months1[i]=='Jan':
        name=cities1[i]
print(name)


scores ={}
print(type(scores))
scores['Jim']=80
scores['Sue']=85
scores['Ann']=75

print(scores)
print(scores.keys())
print(scores['Sue'])


import os

f=open('test.txt','r')
g=f.read()
print(g)
f.close()

f=open('test_write.txt','w')
f.write('Hello,Python!')
f.write('\n')
f.write('Hello.world!')
f.close()

f=open('test_write.txt','r')
g=f.read()
print(g)
f.close()

























