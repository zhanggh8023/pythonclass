# -*- coding: utf-8 -*-
# @Time    : 2019/1/9 17:48
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : insert_data.py
# @Software: PyCharm

'''
 表外授信业务：DGBWSXYW
 table_data = [('210' ||count,'3133400000' ||count, 'B0151B23309' ||count,'33' ||count,'90159000'||count, '张笑', '20180207', '杭州银行股份有限公司舟山分行', '13200','信贷', '信用证','币', '9999900', '352000000', '20', '是', '20000101', '20100101', '20200101', '20500101','正常','100','0.66','币','3500','RT4500','IT009600','100','2018020799','币','1000000','商业发票','1001100200','20190108')]


 贸易融资业务信息表：MYRZYWXXB
 table_data = [(1,'3300'||count,'20190108','90159000'||count,'3133400000' ||count, 'B0151B23309' ||count,'33' ||count,'袁立','JKI00'||count,'出口信用抵押证','100'||count,'币','250000000','1000000','1000000','NO001'||count,'TFG1200','币','99999999999','商业发票','杭州银行','自营','100100','币','60000000','20190108','远期信用证','20300109','20190108')]


 银团贷款：YTDK
 table_data = [('20190'||count,'90159000'||count,'3133400000' ||count, 'B0151B23309' ||count,'33' ||count,'合同协议','JKI00'||count,'JKI00'||count,'JKI00'||count,'JKI00'||count,'杭州银行','杭州银行','合同标志','孙艺','1000000','1000000','1000000','1000000','1000000','1000000','410000399','20300109','20190108','有效','lili','20190108')]

 委托贷款：WTDK
 table_data = [('41860'||count,'TI790'||count,'90159000'||count,'3133400000' ||count, 'B0151B23309' ||count,'33' ||count,'JKI00'||count,'魏延','殷桃','4183u2910','杭州银行','5400001343','委托基金','8002000300','8002000300','资金周转','是','续费','2000','20190102','20500102','钱多多','NOR001'||count,'银监会','有效','20190109')]


 个人信贷业务借据：GRXDYWJJ
 table_data = [('41860'||count,'TI790'||count,'90159000'||count,'慧慧','2010'||count,'3133400000' ||count, 'B0151B23309' ||count,'33' ||count,'JKI00'||count,'银行机构','明细科目','项目贷款','币','35000000','20000000','200','20','12','4','自主支付','20190202','20290202','20390202','7000000','3000000','还款中','20500505','贷款','4568000','正常','浮动','0.4','0.2','按月','61270079093398','银行卡','按月结息','0.22','币','2500','HUE370688','盛世','dh2678','转','6','3','是','20180108')]


 信贷业务担保合同：XDYWDBHT
 table_data = [('20190'||count,'3133400000' ||count, 'B0151B23309' ||count,'33' ||count,'抵押','一般担保合同','对公','Jhon','居民身份证','412723199'||count,'1000000','20300109','20190108','已签合同','20300109','20190108','20300109','币','2060001100','求偿权','34909j0'||count,'20190108')]


 担保关系：DBGX
 table_data = [('2010'||count,'2019'||count,'3133400000' ||count, 'B0151B23309' ||count,'33' ||count,'抵押','2222000000','20190209','20400209','正常','67890000','20190108')]


 信贷业务质或抵押物：XDYWZHDYW
 table_data = [('TI790'||count,'20190'||count,'90159000'||count,'3133400000' ||count, 'B0151B23309' ||count,'33' ||count,'房产','国债','30000000','币','3200000','3500000','20190108','银监会','0.55','任丽','3000000','20190102','20200201','工商所','6217002879093398','20101101','20201101','TYUI0001','纸质','IKM192929','34000000','杭州银行','20190208','4567890987','20190305','李翔','李菲','adf56789','银监会','20100706','20500706','是','20100706','20500706')]


会计记账信息
对公活期存款分户账 YJPT_DGHQCKFHZ
YJPT_DGHQCKFHZ_sql = "INSERT INTO YJPT_DGHQCKFHZ(HQCKZH, KHTYBH, YXJGDM, JRXKZH, NBJGH, MXKMBH, YXJGMC, MXKMMC, TJKMBH, BZ, ZHMC, DGHQCKZHLX, BZJZHBZ, LL, CKYE, KHRQ, KHGYH, XHRQ, ZHZT, SCDHRQ, CHLB, CJRQ) VALUES(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21,:22)"
YJPT_DGHQCKFHZ = [('3W13340' ||count, '9000T09015' ||count, '313340' ||count, 'C0151V23309170' ||count,'99170' ||count, '90', '杭州银行股份有限公司舟山分行', '21', '66000' ||count, 'RNB', '钢铁虫', '人民币', '是', '5', '54646', '20111229', '170', '20190810', '正常', '20180504','钞', '20150625')]


借记卡信息YJPT_JJKXX
YJPT_JJKXX_sql="INSERT INTO YJPT_JJKXX(KH, HQCKZH, KHTYBH, YXJGDM, JRXKZH, NBJGH, ZJLB, ZJHM, JJKCPMC, KPZT, YGBZ, KKRQ, KKGYH, CJRQ) VALUES(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14)"
YJPT_JJKXX=[('HZ001'||count, 'HQ9000C8221'||count, '9000T09015' ||count, '313340' ||count, 'C0151V23309170' ||count,'99170' ||count, '居民身份证', '3301682008101' ||count, '杭州银行股份有限公司西湖支行', '正常', '是', '20061203', '170'||count, '20050322')]


个人定期存款分户账
YJPT_GRDQCKFHZ_sql="INSERT INTO YJPT_GRDQCKFHZ(DQCKZH, GRKHTYBH, YXJGDM, JRXKZH, NBJGH, MXKMBH, MXKMMC, YXJGMC, BZ, TJKMBH, ZHMC, GRDQCKZHLX, CKQX, LL, JYJZMC, JYJZH, BZJZHBZ, KHJE, CKYE, KHRQ, KHGYH, XHRQ, DQR, ZHZT, SCDHRQ, CHLB, CJRQ) VALUES(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21,:22,:23,:24,:25,:26,:27)"
YJPT_GRDQCKFHZ=[ ('HQ9000C8221' ||count, '9000T09015' ||count,'313340' ||count, 'C0151V23309170' ||count,'99170' ||count, 'KM302'||count, '科目1'||count, '杭州银行股份有限公司西湖支行', 'RNB', 'TJ901'||count, '钢铁虫', '零存整取',str(ii)+'天', '0.3', '卡', 'K0'||count, '是', '55500', '555'||count, '19960605', '170'||count, ' ', '20501230', '正常', '20160325', '人民币', '20181225')]


个人信贷分户账
YJPT_GRXDFHZ_sql="INSERT INTO YJPT_GRXDFHZ(DKFHZH, XDJJH, KHTYBH, YXJGDM, JRXKZH, NBJGH, MXKMBH, YXJGMC, MXKMMC, ZHMC, BZ, ZJHKRQ, TJKMBH, DKHTH, XDYXM, DKWJFL, HKZH, DKRZZH, DKLL, DKBJZE, DKZCYE, DKYQYE, QBYE, BWQBYE, BWQXYE, DKQX, DQRQ, QXRQ, KHRQ, XHRQ, YQRQ, ZHZT, CJRQ) VALUES(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21,:22,:23,:24,:25,:26,:27,:28,:29,:30,:31,:32,:33)"
YJPT_GRXDFHZ=[( 'DKFH0992'||count, 'JJH908'||count, '9000T09015' ||count, '313340' ||count, 'C0151V23309170' ||count,'99170' ||count,  'KM302'||count,  '杭州银行股份有限公司西湖支行','科目1'||count,'钢铁虫', 'RNB', '20181230', 'TJ901'||count, 'DKHT609'||count, '鲁班1'||count, '关注', 'DKFH0992'||count,'DKFH0992'||count, '12', '60'||count, 600000-i, 5000+i, '600000',' ','6613.3'||count, str(ii), '20181230', '20161230', '20161229', '20190101', '正常', '20181230',)]

对公客户
 YJPT_DGKH_sql="INSERT INTO YJPT_DGKH(KHTYBH, ZZJGDM, YXJGDM, JRXKZH, NBJGH, KHMC, KHYWMC, FRDB, FRDBZJLB, FRDBZJHM, CWRY, " \
               "CWRYZJLB, CWRYZJHM, JBCKZH, JBZHKHXMC, ZCZB, ZCDZ, LXDH, YYZZH, YYZZYXJZRQ, JYFW, CLRQ, SSXY, KHLB, DKZH, GSZH, " \
               "DSZH, MGSKHTYBH, TYSXBZ, SXED, YYED, SSGSBZ, XYDJBH, ZCZBBZ, SSZBBZ, SSZB, ZZC, JZC, NSR, SCJLXDGXNY, YZBM, CZHM," \
               " YGRS, XZQHDM, KHLX, FXYJXH, CJRQ) " \
               "VALUES(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21,:22,:23,:24,:25,:26,:27,:28,:29,:30,:31,:32,:33,:34,:35,:36,:37,:38,:39,:40,:41,:42,:43,:44,:45,:46,:47)"
YJPT_DGKH = [('9000T09015' ||count, 'SH0988733C' ||count, '313340' ||count, 'C0151V23309170' ||count,'99170' ||count, '钢铁虫', 'rate', '萝卜', '小蚂蚁身份证', '3301682008101' ||count, '郭靖' ||count, '身份证','3301682008101' ||count, 'CKZH90980087' ||count, '杭州银行股份有限公司西湖支行', '100000000', '杭州上城区城西银泰','13265412363', 'YYZ9980' ||count, '20180321', '互联网', '20170801', '互联网', '对公', 'DKHT609' ||count,'GS0998' ||count, 'DS0998' ||count, '9000T09015' ||count, 'Y', '300000', '50000', 'Y', '1', 'RNB','RNB', '2000000' ||count, '600000000', '90000000', '6000000', '999912', '', '', '3000', '','集团客户', '', '20181120')]


对公信贷分户账
 YJPT_DGXDFHZ_sql="INSERT INTO YJPT_DGXDFHZ(DKFHZH, XDJJH, KHTYBH, YXJGDM, JRXKZH, NBJGH, MXKMBH, YXJGMC, MXKMMC, ZHMC, BZ," \
                  " ZJHKRQ, TJKMBH, DKHTH, XDYXM, DKWJFL, HKZH, DKRZZH, DKLL,DKBJZE, DKZCYE, DKYQYE, QBYE, BWQBYE,BWQXYE, DKQX, " \
                  "DQRQ, QXRQ, KHRQ, XHRQ, YQRQ, ZHZT, CJRQ) " \
                  "VALUES(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21,:22,:23,:24,:25,:26,:27,:28,:29,:30,:31,:32,:33)"
YJPT_DGXDFHZ=[('DKFH0992'||count, 'JJH908'||count, '9000T09015' ||count,'313340' ||count, 'C0151V23309170' ||count,'99170' ||count,  'KM302'||count,'杭州银行股份有限公司西湖支行','科目1'||count, '钢铁虫','RNB','20181230', 'TJ901'||count, 'DKHT609'||count, '鲁班1'||count, 'GZ', 'DKFH0992'||count,'DKFH0992'||count, '12', '60'||count,'60'||count, 600000-i, 5000+i, '600000',' ',6613.3+ii, str(ii), '20181230', '20161230', '20161229', '20190101', '正常', '20181230')]


对公信贷业务借据
 YJPT_DGXDYWJJ_sql="INSERT INTO YJPT_DGXDYWJJ(XDJJH, DKFHZH, KHTYBH, KHMC, XDHTH, YXJGDM, JRXKZH, NBJGH, MXKMBH, YXJGMC, MXKMMC," \
                   " XDYWZL, BZ, JKJE, JKYE, DKQX, ZQCS, ZQS, DQQS, FKFS, DKSJFFRQ, DKYSDQRQ, DKSJDQRQ, BNQXYE, BWQXYE, DKZT, ZJRQ," \
                   " DKLX, DKRZZH, DKWJFL, LLLX, JZLL, LLFD, HKFS, HKZH, HKQD, JXFS, BZJBL, BZJBZ, BZJJE, BZJZH, PJHM, PMJE, XDYXM, " \
                   "XDYGH, XZBZ, LJQKQS, LXQKQS, CJRQ) " \
                   "VALUES(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21,:22,:23,:24,:25,:26,:27,:28,:29,:30,:31,:32,:33,:34,:35,:36,:37,:38,:39,:40,:41,:42,:43,:44,:45,:46,:47,:48,:49)"
YJPT_DGXDYWJJ = [('JJH908' ||count, 'DKFH0992' ||count, '9000T09015' ||count, '钢铁虫', 'JJH908' ||count, '313340' ||count,'C0151V23309170' ||count, '99170' ||count, 'KM302' ||count, '杭州银行股份有限公司西湖支行','科目1' ||count, '业务', 'RNB', '6000000', '300000', '90' ||count, '30', '90', '12', '自主支付','20180101', '20181230', '20191230', 6613.3 + ii, '6665554', '正常', 20191230, '法人账户透支','DKFH0992' ||count, 'CJ', '浮动', 12, '12', '按月', 'DKFH0992' ||count, '', '按月结息', 12, 'RNB', 655555,'DKFH0992' ||count, 'PJ009' ||count, 626565 + i, '咚咚咚', 'XD90' ||count, '转', 3, 6, 20181230)]


对公活期存款分户账明细记录
 YJPT_DGHQCKFHZMXJL_sql="INSERT INTO YJPT_DGHQCKFHZMXJL(HXJYLSH, ZJYLSH, BCXH, HQCKZH, KHTYBH, YXJGDM, JRXKZH, NBJGH, MXKMBH, YXJGMC, MXKMMC, HXJYRQ, HXJYSJ, ZHMC, JYLX, JYJE, KHHJGH, YWBLJGH, ZHYE, DFZH, DFHM, DFXH, DFXM, JYQD, BZ, XZBZ, DBRXM, DBRZJLB, DBRZJHM, JYGYH, GYLSH, SQGYH, ZY, CBMBZ, JYJDBZ, CJRQ) VALUES(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21,:22,:23,:24,:25,:26,:27,:28,:29,:30,:31,:32,:33,:34,:35,:36)"
 YJPT_DGHQCKFHZMXJL = [('646' ||count, '987465004' ||count, '648665004' ||count, 'DKFH0992' ||count,'9000T09015' ||count, '313340' ||count, 'C0151V23309170' ||count, '99170' ||count,'KM302' ||count, '杭州银行股份有限公司西湖支行', '科目1' ||count, 20180504, 165321, '小六子', '正常','69554' ||count, '313340' ||count, '313340' ||count, '69554' ||count,'DH8877FH0992' ||count, '付丽丽' ||count,'369340' ||count, '建设银行' ||count, '网银', 'RNB', '现', '番薯', '身份证','33016519861225' ||count, '170' ||count, 'LS8833' ||count, '170' ||count, '', '正常','借', 20181230)]


 JGHG_insert_data('YJPT_NBKMDZB')   内部科目对照表
 table_data =  [('KM88646' ||count, '财务1' ||count, '3', 'SJKM0831' ||count,'贷款1' ||count,'12', '信贷', 20181004)]


 JGHG_insert_data('YJPT_GRHQCKFHZ')   个人活期存款分户账
 table_data =  [('62306 531' ||count, 'KH34737' ||count, '94568' ||count,'HZYH7367' ||count,'46885' ||count,
 'XD5457' ||count,'杭州银行股份有限萧山分公司','预付账款','GRC003','CNY', 'KH34737' ||count,'I类','card','3350' ||count,
 '是' ,'0.042','5000.85', 20180111 ,'XSFH4002' ||count, 20201230,'正常',20181019,'人民币',20190105)]


 JGHG_insert_data('YJPT_GRHQCKFHZMXJL')  个人活期存款分户账明细记录
 table_data =  [('A1810' ||count, 'B1810' ||count, '10' ||count ,'6843 543' ||count,'KH34737' ||count, 'HZYH7367' ||count,'B0018463' ||count ,'IN97467' ||count ,
                         'ZQ5472'||count,'杭州银行股份有限萧山分公司','短期投资',20180612, '173858' , 'CNY','KH34737' ||count,'金融','2000' ||count,'XS9002', 'JR4274','1500' ||count,
                         '63523 762' ||count,'Micheal5' ||count,'ZSYH6483' ||count,'杭州银行股份有限舟山分公司','ATM','转','待办1' ||count,'统一社会信用代码','HZYH8426' ||count,
                         '柜员1' ||count,'005' ||count,'65' ||count,'摘要:HZYHJR','正常','贷',20190105)]


 JGHG_insert_data('YJPT_DGHQCKFHZMXJL')    对公活期存款分户账明细记录
 table_data =  [('H8542' ||count, 'Z6432' ||count, '761' ||count ,'6452 330' ||count,'KH00214' ||count, 'HZYH7367' ||count,'B002420' ||count ,'IN7001' ||count ,
                         'RZ372'||count,'杭州银行股份有限萧山分公司','金融融资',20180612, '093742' , 'XX通信公司','融资','50000','HZYH7421','JRRZ900','90000','6721 340' ||count,
                         'XH金融','HZXH53273622','杭州银行股份有限西湖分公司','手机银行','CNY','现','DB1' ||count, '组织机构代码','HZYH5321' ||count, '柜员A' ||count,'009' ||count,
                         '7009','摘要:HZYHJR','冲账','借',20180912)]


 JGHG_insert_data('YJPT_DGDQCKFHZ')    对公定期存款分户账
  table_data =  [('67632' ||count, 'KH00214' ||count,'HZYH7367' ||count,'Z6432' ||count,'IN7001' ||count,  'RZ372'||count,
                         '杭州银行股份有限萧山分公司','金融融资','CNY','093742','duigong','定期','36个月','0.42','是','200','70000',20150321,
                         'HZ782' ,'',20250901,'正常',20180912,'人民币',20190101)]


 JGHG_insert_data('YJPT_DGDQCKFHZMXJL')   对公定期存款分户账明细记录
  table_data =  [('H8542' ||count, 'Z6432' ||count, '549' ||count ,'6452 679' ||count,'KH00214' ||count, 'HZYH7367' ||count,'B002420' ||count ,'IN8001' ||count ,
                         'RZ372'||count,'杭州银行股份有限萧山分公司','金融融资',20181209, '093742' , 'CNY','XX通信公司','融资','50000','HZYH7421','JRRZ900','90000','6935 997' ||count,
                         'XH金融','HZXH53273622','杭州银行股份有限西湖分公司','手机银行','现','是','DB1' ||count, '组织机构代码','DB7009' ||count, '柜员A' ||count,'009' ||count,
                         '摘要:HZYHJR','冲账','借',20190103)]


 JGHG_insert_data('YJPT_NBFHZ')   内部分户账
 table_data =  [('8542' ||count, 'HZYH7367' ||count,'Z6432' ||count, 'IN8001' ||count, 'MX372'||count,'Tony' ||count,
                         '杭州银行股份有限滨江分公司', '商业信贷','贷','CNY','549' ||count ,'借贷账户','50000','90000','是','按年结息',
                         '0.53',20180705,20200905,'正常',20190106)]


 JGHG_insert_data('YJPT_NBFHZMXJL')   内部分户账明细记录
 table_data =  [('H8542' ||count,'Z6432' ||count,'0051' ||count, '98262'||count,'HZYH7367' ||count, 'JR70063' ||count,'IN8001' ||count,'MX372'||count,
                         '杭州银行股份有限滨江分公司', '商业信贷',20170425,130953,'CNY','Arimy' ||count,'借贷','50000','90000','69243' ||count,'DFKM549' ||count ,'借贷',
                         'AB信贷股份有限公司','ZHYH8452' ||count,'手机银行','现','柜员D' ||count,'9354' ||count,20180705,20200905,'摘要AAAAAABBBBCCCC','补账','借',20190106)]

 JGHG_insert_data('YJPT_GRXDFHZ')   个人信贷分户账
 table_data =  [('DKFH742' ||count,'JD6432' ||count,'KH0051' ||count, 'HZYH7367' ||count, 'JR70063' ||count,'IN8001' ||count,'MX372'||count,
                         '杭州银行股份有限滨江分公司', '商业信贷','Arimy' ||count,'CNY',20170425,'TJKM4693' ||count,'DK462' ||count,'Turo' ||count,'关注',
                         '62431' ||count,'64528' ||count,'0.45','50000','90000','2000','3500','5700','1300','560',20200705,20190905,20170715,20250910,20190519,'正常',20190107)]


 JGHG_insert_data('YJPT_DGXDFHZMXJL')   对公信贷分户账明细记录
  table_data =  [('H8542' ||count, 'Z6432' ||count, '549' ||count ,'6452 679' ||count,'KH00214' ||count, 'HZYH7367' ||count,'B002420' ||count ,'IN8001' ||count ,
                         'RZ372' ||count,'JJH749' ||count,'杭州银行股份有限萧山分公司','金融融资',20181209, '093742' ,'DBG信息公司','融资','借','50000','90000','6935 997' ||count,
                         'XH金融','HZXH53273622','杭州银行股份有限西湖分公司','手机银行','CNY', '摘要:HZYHJR','正常','DB1' ||count, '组织机构代码','DB7009' ||count, '柜员A' ||count,'009' ||count,'现',20190103)]



担保关系
 YJPT_DBGX 字段sql：INSERT INTO YJPT_DBGX(DBHTH,BDBHTH,YXJGDM,JRXKZH,NBJGH,DBLX,DBJE,DBQSRQ,DBDQRQ,DBZT,JLDBYGH,CJRQ) VALUES (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12)
 table_data = [('88T646' ||count, '987465004' ||count, '648665004' ||count, 'DKFH0992' ||count,'DKeeeFH0992' ||count, '抵押', '313340' ||count, 20180506, 20180506, '解除', '科目1' ||count, 20180504)]

存折信息
 YJPT_CZXX 执行sql: INSERT INTO YJPT_CZXX(CZH,HQCKZH,KHTYBH,YXJGDM,JRXKZH,NBJGH,ZJLB,ZJHM,CZLX,CZZT,YGBZ,QYRQ,QYGYH,CJRQ) VALUES (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14)
 table_data = [('CZT646' ||count, 'CK465004' ||count, '313340' ||count, 'C0151V23309170' ||count,'99170' ||count, '小蚂蚁身份证', '33016820081013' ||count, '普通存折', '正常', '解除', '是', 20180504,'GY1' ||count, 20180906)]

信用卡信息YJPT_XYKXX
 table_data = [('CZT646' ||count, 'XYK5006224' ||count, '9000T09015' ||count, '313340' ||count,
                'C0151V23309170' ||count, '99170' ||count, '小蚂蚁身份证', '330168200813' ||count,
                '信用卡', '三星', '正常', '集团客户', '是', '是', 'CZT646' ||count, '是', 60000, 500, 'CNY', 88888, 6666, 20180504,
                20180504, 'GY1' ||count, 20180906, 'GY1' ||count, 20190906, 'GY1' ||count, '正常', 4564, 64565456,68886.8, 3255, 66665, 545,
                965553.6, 66542, 99897, 6564464, 6665, 65465, 65456, '信用', '资产上亿', '正常', 63456, 20180630, 20190101)]


 信用卡信息明细表
 YJPT_XYKZHJYMXB
 table_data = [('CZT646' ||count, 'XYK5006224' ||count, '313340' ||count, 'C0151V23309170' ||count,
                '99170' ||count, 'KM302' ||count, '科目1' ||count, 'RNB', 20180213, '646' ||count,
                '987465004' ||count, '890' ||count, '转', '人民币', '现', 'JY097' ||count, '借', 8895654, 600, '取现',
                20060305, 20091203, 20101005, 'CK465004' ||count, '被分期', 'ATM', '', 'GY1' ||count, '313340' ||count,
                '柜员工作站' ||count,
                'GZZBH01' ||count, '无', '无', 20110608)]

授信信息
YJPT_SXXX
 table_data =[('SXXY0946' ||count, '9000T09015' ||count,'313340' ||count, 'C0151V23309170' ||count, '99170' ||count,20180213,'杭州城市大数据运行有限公司' ||count,
         '集团客户授信' ||count,'授信文书'||count,9000000000,'RNB',20060305,'有效',20101005,20131005,20021005,'同意授信' ||count,'老李' ||count,'是','是','GY1' ||count,20110608)]


贷款核销
YJPT_DKHX 执行sql: INSERT INTO YJPT_DKHX(XDJJH,XDHTH,KHTYBH,YXJGDM,JRXKZH,NBJGH,MXKMBH,MXKMMC,KMGSJG,BZ,SHDKBJ,SHBNLX,SHBWLX,HXRQ,HXSHBJ,HXSHBNLX,HXSHBWLX,SHBZ,HXSHGYH,HXSHRQ,BZH,CJRQ) VALUES (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21,:22)
  table_data = [('JJH908' ||count, 'DKHT609'||count, '9000T09015' ||count, '313340' ||count,
                'C0151V23309170' ||count, '99170' ||count, 'KM302' ||count, '科目1' ||count, '313340' ||count,
                'RNB', 8222202 ||count, 56454 ||count, 897654 ||count, 20180213, 4564554 ||count, 4654628 ||count,
                8465645 ||count, '是',
                'GY1' ||count, 20160305, '有效', 20101005)]


贷款展期
YJPT_DKZQ 执行sql: INSERT INTO YJPT_DKZQ(DKZQBH,XDJJH,XDHTH,KHTYBH,YXJGDM,JRXKZH,NBJGH,ZQRQ,ZQDQRQ,ZQJE,YLL,LLLX,ZQJZLL,LLFD,YHTH,YJJH,JYGYH,SQGYH,CJRQ) VALUES (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19)
 table_data = [('DKZQBH9099' ||count, 'JJH908' ||count, 'DKHT609' ||count, '9000T09015' ||count,
                '313340' ||count, 'C0151V23309170' ||count, '99170' ||count, 20160330, 20190330,
                '6565465.99784' ||count, '0.1' ||count, '浮动', '0.1', '0.01' ||count, 'DKHT609' ||count,
                'JJH908' ||count, 'GY1' ||count, 'GY1' ||count, 20180213,)]


 信贷资产转让
 YJPT_XDZCZR 执行sql: INSERT INTO YJPT_XDZCZR(ZRHTH,YXJGDM,JRXKZH,NBJGH,MXKMBH,MXKMMC,JYDSBH,JYDSMC,XDJYLX,JYZCLX,BZ,ZRDKBJZE,ZRDKLXZE,ZRSXF,ZRZJ,HGLL,ZRJGRQ,HGJZRQ,ZRHTQSRQ,ZRHTDQRQ,JYDSZZH,JYDSZZZHHM,JYDSXH,CJRQ) VALUES (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21,:22,:23,:24)
 table_data =[('ZR908322'||count,'313340' ||count, 'C0151V23309170' ||count, '99170' ||count,'KM302' ||count, '科目1' ||count,'DSBH947'||count,'光头强'||count,'网上银行', '票据' ||count,'RNB' ,'6995465'||count,'65465'||count,'68491'||count,'84965465'||count,'0.1' ||count,20110213,20120213,20160213,20190213,'B0151B2330' ||count, '刘翔'||count,'313340' ||count,20120213)]

 资产转让关系表
 YJPT_ZCZRGXB 执行sql: INSERT INTO YJPT_ZCZRGXB(ZRHTH,YXJGDM,XDJJH,JRXKZH,NBJGH,CJRQ) VALUES (:1,:2,:3,:4,:5,:6)
 table_data =[('ZR908322'||count,'313340' ||count, 'JJH908' ||count, 'C0151V23309170' ||count, '99170' ||count,20120213)]


贷款五级心态变动
YJPT_DKWJXTBD 执行sql: INSERT INTO YJPT_DKWJXTBD(TZRQ,XDJJH,XDHTH,KHTYBH,YXJGDM,JRXKZH,NBJGH,YXJGMC,YMXKMBH,YMXKMMC,YWJXT,XMXKMBH,XMXKMMC,XWJXT,BZ,ZRJE,ZCJE,KHMC,JBGYH,TZGYH,SQGYH,SPGYH,BDYY,BDFS,CJRQ) VALUES (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21,:22,:23,:24,:25)
 table_data =[(20160807,'JJH908' ||count, 'DKHT609' ||count, '9000T09015' ||count, '313340' ||count, 'C0151V23309170' ||count, '99170' ||count,'杭州银行股份有限公司西湖支行','KM302' ||count,  '科目1' ||count,'关注','XKM302' ||count,  'X科目1' ||count,'关注','RNB','156746541'||count,'156746881'||count,'钢铁虫'||count,'GY1' ||count,'GY2' ||count,'GY3' ||count,'GY4' ||count,'这是一个寒冷的冻鸡','人工',20120213)]


交易流水
YJPT_JYLS 执行sql: INSERT INTO YJPT_JYLS(HXJYLSH,ZJYLSH,BCXH,JYRQ,YXJGDM,NBJGH,JRXKZH,MXKMBH,JYSJ,JZRQ,JZSJ,JYJGMC,JYZH,JYHM,JYXTMC,DFXH,DFJGMC,DFZH,DFHM,JYJE,ZHYE,JYJDBZ,XZBZ,BZ,YWLX,JYLX,JYQD,JYJZMC,JYJZH,CZGYH,GYLSH,FHGYH,ZY,ZPZZL,ZPZH,FPZZL,FPZH,CBMBZ,SJC,ZHBZ,KXHBZ,CJRQ) VALUES (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21,:22,:23,:24,:25,:26,:27,:28,:29,:30,:31,:32,:33,:34,:35,:36,:37,:38,:39,:40,:41,:42)
 table_data =[('646' ||count, '987465004' ||count,'900' ||count, 20180430,  '313340' ||count, 'C0151V23309170' ||count, '99170' ||count,'KM302' ||count,165863,20160609, 195233, '杭州银行股份有限公司舟山分行'||count, '330102046000132'||count, '支付宝代发交易内部户'||count,'中国银监会'||count, '313340' ||count, '杭州银行股份有限公司西湖支行'||count, '11418102813895'||count,'小鱼'||count, str(i)+'3400.33',6987415,'贷','转','RNB','8','这是自动插入'||count,'POS','卡','KH987773' ||count,'GY1' ||count, 'LS8833' ||count,'GY4' ||count,'这是一个寒冷的冻鸡','高级会员'||count,'ZPH987'||count,'会员'||count,'FZPH987'||count,'冲账',20120213162554000000,'对私','开户',20180525)]


 资产负债科目统计表
执行sql: INSERT INTO YJPT_ZCFZKMTJB(JRJGDM,JRXKZH,NBJGH,TJKMBH,TJKMMC,TJKMJE,QXLX,TJRQ,BZ,DQMC,XZQHDM,CJRQ) VALUES (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12)
 table_data =[('JRJG88646' ||count, '313340' ||count, 'C0151V23309170' ||count, '99170' ||count,'KM302' ||count,'科目1' ||count,str(ii)+'165.863','月', 20160321, 'RNB', '浙江富春支行'||count, str(i),20180525)]


涉农统计表
YJPT_SNTJB 执行sql: INSERT INTO YJPT_SNTJB(JRJGDM,JRXKZH,NBJGH,TJKMBH,TJKMMC,TJKMJE,QXLX,TJRQ,BZ,DQMC,XZQHDM,CJRQ) VALUES (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12)
 table_data =[('JRJG8946' ||count, 'C0151V23366170' ||count, '99166' ||count,'KM359' ||count,'科目16' ||count,str(ii)+'1656.743','半年', 20180321, 'RNB', '浙江富春支行'||count, str(i),20170525)]


汇率信息表
YJPT_HLXXB 执行sql: INSERT INTO YJPT_HLXXB(YXJGDM,JRXKZH,NBJGH,YXJGMC,WB,BB,ZJJ,JZJ,HLRQ,CJRQ) VALUES (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10)
  table_data =[( '313340' ||count,'C0151V23366170' ||count, '99166' ||count,'杭州银行股份有限公司西湖支行','CNY','RNB','6.98','6.3','0.2'||count, 20170525)]


金融工具信息表
YJPT_JRGJXXB 执行sql: INSERT INTO YJPT_JRGJXXB(YXJGDM,JRXKZH,NBJGH,YXJGMC,ZQMC,JRGJBH,ZCLX,BZ,FXJG,YXCZQYDM,FXGB,DBJG,CPPJ,PJJG,FXZTPJ,JYZHLX,PMLL,FXJGE,FXRQ,SSRQ,QXRQ,DQRQ,LLLX,HQBS,ZJPGJG,PGJGSJ,YE,CJRQ) VALUES (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21,:22,:23,:24,:25,:26,:27,:28)
 table_data =[( '313340' ||count,'C0151V23366170' ||count, '99166' ||count,'杭州银行股份有限公司西湖支行','手机银行APP'||count,'JRGJ098'||count,'债券','RNB','杭州银行留下支行'||count,'313340' ||count,'CN', '中国银行'||count,'A++','国际信用','中央银行','银行账户','0.3'||count,'68749',20180321,20180606,20180606,20280606,'浮动','是',468713,20181230,6541635,20181230)]


资金交易信息表
YJPT_ZJJYXXB 执行sql: INSERT INTO YJPT_ZJJYXXB(YXJGDM,JRXKZH,NBJGH,MXKMBH,YXJGMC,MXKMMC,JYBH,LCCPDJBM,JYLX,JYZL,JRGJBH,JYZHLX,HTH,HTJE,BZ,JCZCKHMC,JCZCSSHY,JCZCSFWBHKH,JCZCZXFS,JCZCZXR,JYGY,SPR,JYDSDM,JYDSMC,JYRQ,QSRQ,DQRQ,MMBZ,JYQBZ,MRBZ,MRJE,MCBZ,MCJE,CJJG,YWZT,FHRQ,QXRQ,SJJGRQ,QSBZ,JFZH,DFZH,JFJE,DFJE,JFBZ,DFBZ,JFLL,DFLL,BZJJYBZ,GLBZJZH,GLYWBH,WBGLXTMC,CJRQ) VALUES (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21,:22,:23,:24,:25,:26,:27,:28,:29,:30,:31,:32,:33,:34,:35,:36,:37,:38,:39,:40,:41,:42,:43,:44,:45,:46,:47,:48,:49,:50,:51,:52)
table_data =[( '313340' ||count,'C0151V23366170' ||count, '99166' ||count,'KM359' ||count,'杭州银行股份有限公司西湖支行','科目16' ||count, 'DKHT66609' ||count,'LC09388'||count,'自营','买入','手机银行','交易账户','DKHT66609' ||count,'648654622'||count, 'RNB','国际信用'||count,'中央','是','保证金质押','(๑ŐдŐ)b'||count,'GY1' ||count,'GY4' ||count,'DSBH947'||count,'光头强'||count,20180321,20180606,20280606,'买入','远期','RNB','665'||count,'CNY','4654'||count,'5000千万','成交确认',20181230,20181230,20181230,'是','3W13340' ||count,'D139940' ||count,'6855'||count,'6855'||count,'RNB','RNB','0.6'||count,'0.6'||count,'是','GG3HH40' ||count,'YW0998' ||count,'银湖智慧📱'||count,20180716)]


 客户理财账户信息表
YJPT_KHLCZHXXB 执行sql: INSERT INTO YJPT_KHLCZHXXB(YXJGDM,JRXKZH,NBJGH,MXKMBH,YXJGMC,MXKMMC,BZ,LCZH,KHTYBH,KHXM,GLHQCKZH,LCCPMC,HNBSM,FEZS,DJFE,HLZTZBZ,BQSY,LJSY,MRCB,BQQSRQ,BQDQRQ,KHRQ,SCDHRQ,CJRQ) VALUES (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21,:22,:23,:24)
 table_data =[( '313340' ||count,'C0151V23366170' ||count, '99166' ||count,'KM359' ||count,'杭州银行股份有限公司西湖支行','科目16' ||count,'RNB','LC09388'||count,'KHTY0039'||count,'灭霸'||count,'3W13340' ||count,'小蝌蚪'||count, '小蝌蚪','96666',str(i),'是','66544'||count,'654115'||count,'65554' ||count,20180321,20180606,20280606,20280606,20280606)]


	理财产品销售明细记录
YJPT_LCCPXSMX 执行sql: INSERT INTO YJPT_LCCPXSMX(JYH,HXJYLSH,ZJYLSH,BCXH,YXJGDM,JRXKZH,NBJGH,MXKMBH,YXJGMC,MXKMMC,LCZH,KHTYBH,KHXM,GLHQCKZH,LCCPMC,HNBSM,SGSHBZ,BZ,HXJYRQ,JYJE,JYFE,JYFY,JYQD,KHJLGH,KHJLXM,JYGYH,CJRQ) VALUES (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21,:22,:23,:24,:25,:26,:27)
   table_data =[( 'XS008'||count,'646' ||count, '987465004' ||count, '648665004' ||count,'313340' ||count,'C0151V23366170' ||count, '99166' ||count,'KM359' ||count,'杭州银行股份有限公司西湖支行','科目16' ||count,'LC09388'||count,'KHTY0039'||count,'灭霸'||count,'3W13340' ||count,'小蝌蚪'||count, '小蝌蚪','申购','RNB',20180321,'65554' ||count,'4654'||count,'665'||count,'柜面','KHJL098'||count,'GH09'||count,'GY2'||count,20280606)]


	理财产品信息表
YJPT_LCCPXXB 执行sql: INSERT INTO YJPT_LCCPXXB(YXJGDM,JRXKZH,NBJGH,MXKMBH,YXJGMC,MXKMMC,CPMC,CPDJBM,HNBSM,CPPP,CPQC,CPSPRSFZH,CPSPRXM,CPSJRSFZH,CPSJRXM,TZJLSFZH,TZJLXM,CPSYLX,CPQX,TZZLX,ZJTXDQ,CPTZGJHDQ,LCYWFWMS,CPYZMS,KJHSFS,CPZCPZFS,CPGLMS,SJGLLMC,CPDJFS,TZLX,HZMS,HZJGMC,TZZCZLJBL,SFYYQSYL,YJKHZGNSYL,YJKHZDNSYL,SFYSYLCSYJ,TZZFXPH,CPXSQY,MJBZ,DFBJBZ,DFSYBZ,QDXSJE,JHMJJE,MJQSRQ,TZBJDZR,TZSYDZR,XSSXFL,JNTGJGMC,JNTGJGDM,JWTGJGGB,JWTGJGMC,LCCPZJTGZH,LCCPZJTGZHMC,TGFL,CPFXDJ,FXJGTQZZQBS,KHSHQBS,CPZXBS,CPZXJGLX,CPZXXS,CJRQ) VALUES (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21,:22,:23,:24,:25,:26,:27,:28,:29,:30,:31,:32,:33,:34,:35,:36,:37,:38,:39,:40,:41,:42,:43,:44,:45,:46,:47,:48,:49,:50,:51,:52,:53,:54,:55,:56,:57,:58,:59,:60,:61,:62)
  table_data =[( '313340' ||count,'C0151V23366170' ||count, '99166' ||count,'KM359' ||count,'杭州银行股份有限公司西湖支行','科目16' ||count,'蜘蛛'||count,'LC0908'||count,'TY0039'||count,'犀牛'||count, 36,'33018319960625'||count,'tager'||count, '33018319860915'||count,'rabot'||count, '33018319761221'||count,'会长'||count,'保本浮动收益类',48,'机构专属','境外','US'||count,'综合理财服务'||count,'封闭式净值型'||count,'表内','资产组合配置'||count,'银行','何华'||count,'综合定价','非标准化债权类','银保','画得很好'||count,'现金','是','0.6'||count,'0.2'||count,'是','稳健型','浙江','CNY','CNY','CNY','65465465','600000',20280606,'T500','T1','0.1'||count,'和众国际'||count,'HZ89'||count,'US','husaer'||count,'LCTG9065558'||count,'小缸'||count,'0.01','三级','是','是','否','金融性公司','外部增级',20181230)]


	理财产品状态表
YJPT_LCCPZTB INSERT INTO YJPT_LCCPZTB(YXJGDM,JRXKZH,NBJGH,MXKMBH,YXJGMC,MXKMMC,LCCPMC,HNBSM,SJMJJE,CPQSRQ,CPYJZZRQ,FXDJR,YHDSJSXSR,DFKHSY,KHDSJNHSYL,CPDSJNHSYL,ZZDJR,CJRQ) VALUES (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18)
table_data =[( '313340' ||count,'C0151V23366170' ||count, '99166' ||count,'KM359' ||count,'杭州银行股份有限公司西湖支行','科目16' ||count,'蜘蛛'||count,'T55039'||count,'60000000'||count,20080606,20280606,20080606,'600000000'||count,'550000000','0.1'||count,'0.2'||count,20181230,20181230)]

'''