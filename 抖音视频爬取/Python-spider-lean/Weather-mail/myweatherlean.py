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

from json import *
import urllib.request
import re
from playhouse.sqlite_udf import tonumber
import sys


config_info = {
    'high':35,
    'low':1,
    }

def getrequest(url):
    html=urllib.request.urlopen(link) #就可以访问了，不会报异常
    rehtml = html.read().decode('utf-8')#读入打开的url
    rejson = JSONDecoder().decode(rehtml)#创建json
    if rejson['status'] == 200:
        return rejson
    else:
        print('请求失败')
        sys.exit()

def getwinfo(winfo):
    '''
    forecast{
    "date": "31日星期三",
    "sunrise": "06:25",
    "high": "高温 23.0℃",
    "low": "低温 9.0℃",
    "sunset": "17:23",
    "aqi": 68.0,
    "fx": "东风",
    "fl": "<3级",
    "type": "晴",
    "notice": "愿你拥有比阳光明媚的心情"
    }
    '''
    #print(type(winfo))
    ndata = {}
    for key in winfo:
        #print(key,winfo[key])
        if key == "date":
            date = winfo['date']
#             print(date)
#             pattern = re.compile('(\d+)(.*)')
#             result = pattern.findall(date)
#             date = result[0][0]
#             week = result[0][1]
            ndata['date']=winfo['date']
            ndata['week']=winfo['week']
            ndata['date']=winfo['ymd']
        if key == "high":
            high = winfo['high']
            pattern = re.compile('高温 (.*)℃')
            result = pattern.findall(high)
            high = result[0]
            ndata['high']=tonumber(high)
        if key == "low":
            low = winfo['low']
            pattern = re.compile('低温 (.*)℃')
            result = pattern.findall(low)
            low = result[0]     
            ndata['low']=tonumber(low)  
        if key == "aqi":
            aqi = winfo['aqi']
            ndata['aqi']=aqi   
        if key == "fx":
            fx = winfo['fx']
            ndata['fx']=fx   
        if key == "fl":
            fl = winfo['fl']
            ndata['fl']=fl  
        if key == "type":
            types = winfo['type']
            ndata['types']=types  
        if key == "notice":
            notice = winfo['notice']
            ndata['notice']=notice  
    
    
    print('获取数字',ndata)
    #print("今天是%s,天气%s,最%s 最%s,%s%s" % (ndata['date'],ndata['types'],ndata['high'],ndata['low'],ndata['fx'],ndata['fl']) ) 
    return ndata
       
#合肥天气url
link = 'http://t.weather.sojson.com/api/weather/city/101220101'

def getweatherinfo():
    redata = getrequest(link)
    timesinfo = redata['time']
    cityInfo = redata['cityInfo']
    weatherdata = redata['data']
    print(weatherdata)
    
    #今天
    '''
        "shidu":"74%",
        "pm25":53,
        "pm10":57,
        "quality":"良",
        "wendu":"12",
        "ganmao":"极少数敏感人群应减少户外活动",
    '''
    shidu = weatherdata['shidu']        
    pm25 = weatherdata['pm25']
    quality = weatherdata['quality']
    wendu = weatherdata['wendu']
    ganmao = weatherdata['ganmao']

    #昨天
    yesterday = weatherdata['yesterday']
    N_yesterday = getwinfo(yesterday)
    #未来几天
    forecast = weatherdata['forecast']
    #今天
    today = forecast[0]
    N_today = getwinfo(today)
    N_today['shidu'] = shidu
    N_today['pm25'] = pm25
    N_today['ganmao'] = ganmao
    
    #明天
    Tomor = forecast[1]
    N_Tomor = getwinfo(Tomor)
    
    return N_yesterday,N_today,N_Tomor
   
def aboutwend(day1,day2,Boole):
    day1_high = tonumber(day1['high'])
    day1_low = tonumber(day1['low'])
    day2_high = tonumber(day2['high'])
    day2_low = tonumber(day2['low'])
    
    h_wencha = day1_high - day2_high
    l_wencha = day1_low - day2_low
    #今天对比昨天
    if Boole == 0:
        texts = '最高气温%s度，最低气温%s度，' % (day2_high,day2_low)
        if day1_high > 35:
            texts += '天气十分炎热，尽量不要出门' 
        elif day1_high > 30:
            texts += '天气炎热，注意防暑' 
        elif day1_high > 20:
            texts += '天气不错适合出去走走' 
        elif day1_low > 10:   
            texts += '出门带件外套' 
        elif day1_low > 5:
            texts += '比较冷注意防寒!' 
        elif day1_low > 0:
            texts += '很冷哦，出门带穿厚厚哦' 
        elif day2_low <= -4 :
            texts += '注意大雪！' 
        elif day2_low < 0:
            texts += '零下了，气温低要防寒保暖，注意下雪天气，' 
        
        else:
            pass
        
        print('温差',l_wencha)
        if day2_high > 20 and l_wencha > 3:
            texts += ' 今天要降温%s度   ' % l_wencha
        elif day2_high < 20 :
            if l_wencha > 5:
                texts += '气温骤降%s度一定要注意温差大引发流感！' % int(l_wencha)
        else:
            pass
    #今天对比明天
    elif Boole == 1:
        texts = '最高气温%s，最低气温%s度，' % (day1_high,day1_low)
        if day1_high > 35:
            texts += '最高温度%s度，天气十分炎热，尽量不要出门' % (day1_high)
        elif day1_high > 30:
            texts += '最高温度%s度，天气炎热，注意防暑' % (day1_high)
        elif day1_high > 20:
            texts += '最高温度%s度，天气不错适合出去走走' % (day1_high)
        elif day1_low > 10:   
            texts += '最低气温%s度，出门带件外套' % (day1_low)
        elif day1_low > 5:
            texts += '最低气温%s度，有点冷注意防寒' % (day1_low)
        elif day1_low > 0:
            texts += '最低气温%s度，很冷哦，出门带穿厚厚哦' % (day1_low)
        else:
            pass
        
        if day2_high > 20 and h_wencha > 3:
            texts += ' 明天要降温%s度   ' % h_wencha
        elif day2_high < 20 and h_wencha > -3:
            texts += ' 冷空气要来了，明天要降温%s度   ' % h_wencha
        else:
            pass
    return texts
 
def duibi(today,yesterday):
    #print(tonumber(today['high']))
    #print(tonumber(yesterday['high']))
    WD_high = tonumber(today['high']) - tonumber(yesterday['high'])
    WD_low = tonumber(today['low']) - tonumber(yesterday['low'])
    if WD_high > 3:
        print('升温',WD_high)
 
#天气话术形成
def text_build():
    yesterday,today,tomorrow = getweatherinfo()
    
    texts = aboutwend(yesterday,today,int(0))
    #print(texts)
    #duibi(N_today,N_yesterday)
    
    #今天温度怎么样
    dates = today['date'].split('-')
    dates = '%s年%s月%s日%s' % (dates[0],dates[1],dates[2],today['week'])
    
    print("今天是%s,%s,%s,%s%s,温馨提醒：%s %s" % (dates,today['types'],texts,today['fx'],today['fl'],today['ganmao'],today['notice']))
    #对比昨天
    


text_build()


    
    
    