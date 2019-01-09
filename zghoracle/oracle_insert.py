'''DECLARE count INTEGER;
BEGIN-- Test statements here
  dbms_output.put_line ( 'start:' || SYSDATE );
  FOR count IN 500000..900000
  loop
  INSERT INTO HG.YJPT_JGGXB
  VALUES
    ( '313340'||count, '9015', 'B0151B233'||count, '杭州银行股份有限公司舟山分行', count, '660000', '31334'||count, '20180810' );
  commit;

END loop;
dbms_output.put_line ( 'end:' || SYSDATE );

end;'''



'''
#公共信息类
#机构信息表
YJPT_JGXXB_sql = "INSERT INTO YJPT_JGXXB(YXJGDM,NBJGH,JRXKZH,YXJGMC,JGLB,YZBM,WDH,YYZT,CLSJ,JGGZKSSJ,JGGZZZSJ,JGDZ,FZRXM,FZRZW,FZRLXDH,CJRQ) VALUES(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16)"
YJPT_JGXXB = [(313340000010, 9010, 'B0151B233090001', '杭州银行股份有限公司舟山分行', '基础网店', 316000, 9010, '营业', 20010701,'083000', '173000', '舟山市定海区临城街道定沈路619号舟山港航国际大厦B座', '张晓燕', '行长', '0580-3807915', '20171027'),
              (313340000010, 9011, 'B0151B233090001', '杭州银行股份有限公司杭州分行', '基础网点', 316001, 9010, '营业', 20010702,'083000', '173000', '舟山市定海区临城街道定沈路620号舟山港航国际大厦A座', '袁华', '科长', '0580-3807916', '20171027'),
              (313340000010, 9012, 'B0151B233090001', '杭州银行股份有限公司上海分行', '基础网点', 316002, 9010, '营业', 20010703, '083000', '173000', '舟山市定海区临城街道定沈路621号舟山港航国际大厦C座', '秋雅', '副科长', '0580-3807917', '20171027'),
              (313340000010, 9013, 'B0151B233090001', '杭州银行股份有限公司北京分行', '基础网点', 316003, 9010, '营业', 20010704,'083000', '173000', '舟山市定海区临城街道定沈路622号舟山港航国际大厦F座', '夏洛', '科长', '0580-3807918', '20171027'),
              (313340000010, 9014, 'B0151B233090001', '杭州银行股份有限公司舟山分行', '基础网点', 316004, 9010, '营业', 20010705,'083000', '173000', '舟山市定海区临城街道定沈路623号舟山港航国际大厦G座', '冬梅', '主任', '0580-3807919', '20171027'),
              (313340000011, 660000, 'B0151B233090001', '杭州银行股份有限公司金融事业部', '一级分行(虚拟)', 316005, 9010, '营业',20010705, '083000', '173000', '杭州市庆春路46号', '无	', '无', '无', '20171027')]


# 员工表
YJPT_YGB_sql = "INSERT INTO YJPT_YGB(GH,YXJGDM,NBJGH,JRXKZH,YXJGMC,XM,SFZH,LXDH,WDH,SSBM,ZW,YGZT,GWBH,CJRQ) VALUES(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14)"
YJPT_YGB = [('001', 313340000010, 9010, 'B0151B233090001', '杭州银行股份有限公司舟山分行', '张晓燕', 110101199003078000, 15824196565,9010, '营业部', '员工', '在职', '000001','20171028'),
            ('002', 313340000010, 9011, 'B0151B233090001', '杭州银行股份有限公司杭州分行', '袁华', 110101199003078000, 15824196566,9010, '营业部', '员工', '在职', '000002','20171028'),
            ('003', 313340000010, 9012, 'B0151B233090001', '杭州银行股份有限公司上海分行', '秋雅	', 110101199003078000,15824196567, 9010, '营业部', '员工', '在职', '000003','20171028'),
            ('004', 313340000010, 9013, 'B0151B233090001', '杭州银行股份有限公司北京分行', '夏洛', 110101199003078000, 15824196568,9010, '营业部', '员工', '在职', '000004','20171028'),
            ('005', 313340000010, 9014, 'B0151B233090001', '杭州银行股份有限公司舟山分行', '冬梅', 110101199003078000, 15824196569,9010, '营业部', '员工', '在职', '000005','20171028'),
            ('006', 313340000011, 660000, 'B0151B233090001', '杭州银行股份有限公司金融事业部', '无', '无', '无', 9010, '营业部', '无', '无', '无','20171028')]


#柜员表
YJPT_GYB_sql = "INSERT INTO YJPT_GYB(GYH,GH,YXJGDM,NBJGH,ZXJGDM,JRXKZH,YXJGMC,GYLX,SFSTGY,KHJLBZ,JBZWBZ,QXGLBZ,YBGLBZ,XDYBZ,KGYBZ,ZHGYBZ,SQBZ,SQFW,GWBH,GYYHJB,GYQXJB,SGRQ,GWZT,CJRQ) VALUES(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21,:22,:23,:24)"
YJPT_GYB = [('1', '001', 313340000010, 9010,'', 'B0151B233090001', '杭州银行股份有限公司舟山分行', '综合柜员', '是', '是', '是','是', '是', '是', '是', '是', '是','', '000001','1', '1', '20171102', '在岗', '20180213'),
            ('2', '002', 313340000010, 9011,'', 'B0151B233090001', '杭州银行股份有限公司杭州分行', '普通柜员', '是', '是', '否','否', '否', '否', '否', '否', '是','', '000002', '4', '4', '20171103', '在岗', '20180214'),
            ('3', '003', 313340000010, 9012,'', 'B0151B233090001', '杭州银行股份有限公司上海分行', '现金柜员', '是', '是', '否','否', '是', '否', '否', '是', '是','', '000003', '2', '2', '20171104', '在岗', '20180215'),
            ('4', '004', 313340000010, 9013,'', 'B0151B233090001', '杭州银行股份有限公司北京分行', '低柜柜员', '是', '是', '否','否', '否', '否', '否', '否', '是', '','000004', '3', '3', '20171105', '在岗', '20180216'),
            ('5', '005', 313340000010, 9014,'', 'B0151B233090001', '杭州银行股份有限公司舟山分行', '大堂经理', '是', '是','是', '是', '是', '否', '否', '是', '是', '','000005', '1', '1', '20171106', '在岗', '20180217'),
            ('6', '006',31334000001, 660000,'', 'B0151B233090001', '杭州银行股份有限公司金融事业部','无', '否', '否', '否', '否', '否', '否', '否', '否', '否', '','无', '1', '1', '', '', '20180218')]


#岗位信息表
YJPT_GWXXB_sql= "INSERT INTO YJPT_GWXXB(GWBH,YXJGDM,NBJGH,JRXKZH,GWZL	,GWMC,GWSM,GWZT,CJRQ) VALUES(:1,:2,:3,:4,:5,:6,:7,:8,:9)"
YJPT_GWXXB=[('000001', 313340000010, 9010, 'B0151B233090001', '行政', '管理人员', '无', '满员', '20171105'),
            ('000002', 313340000010, 9011,	'B0151B233090001',	'财务',	'柜员', '无',	'满员', '20171105'),
            ('000003', 313340000010, 9012,	'B0151B233090001',	'信贷', '客户经理', '无', '满员', '20171105'),
            ('000004', 313340000010, 9013,	'B0151B233090001',	'运营',	'柜员', '无',	'满员', '20171105'),
            ('000005', 313340000010, 9014,	'B0151B233090001',	'行政',	'管理人员', '无',	'满员', '20171105'),
            ('000006', '', 660000, 'B0151B233090001', '', '', '无', '缺编', '20171105')]


#机构关系表
YJPT_JGGXB_sql="INSERT INTO YJPT_JGGXB(YHJGDM,NBJGH,JRXKZH,YHJGMC,YZBM,SJGLJGDM,SJGLJGMC,CJRQ) VALUES(:1,:2,:3,:4,:5,:6,:7,:8)"
YJPT_JGGXB = [(313340000010, 9010, 'B0151B233090001', '杭州银行股份有限公司舟山分行', 316000, '', '', 20171027),
              (313340000010, 9011, 'B0151B233090001', '杭州银行股份有限公司杭州分行', 316001, '', '', 20171027),
              (313340000010, 9012, 'B0151B233090001', '杭州银行股份有限公司上海分行', 316002, '', '', 20171027),
              (313340000010, 9013, 'B0151B233090001', '杭州银行股份有限公司北京分行', 316003, '', '', 20171027),
              (313340000010, 9014, 'B0151B233090001', '杭州银行股份有限公司舟山分行	', 316004, '', '', 20171027),
              (313340000011, 660000, 'B0151B233090001', '杭州银行股份有限公司金融事业部', 316005, '', '', 20171027)]

#交易流水信息
#交易流水YJPT_JYLS
YJPT_JYLS_sql = "INSERT INTO YJPT_JYLS(HXJYLSH,ZJYLSH,	BCXH,JYRQ,YXJGDM,NBJGH,JRXKZH,MXKMBH,JYSJ,JZRQ,JZSJ,JYJGMC,JYZH,JYHM,JYXTMC,DFXH,DFJGMC,DFZH,DFHM,JYJE,ZHYE,JYJDBZ,XZBZ,BZ,YWLX,JYLX,JYQD,JYJZMC,JYJZH,CZGYH,GYLSH,FHGYH,ZY,ZPZZL,ZPZH,FPZZL,FPZH,CBMBZ,SJC,ZHBZ,KXHBZ,CJRQ) VALUES(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21,:22,:23,:24,:25,:26,:27,:28,:29,:30,:31,:32,:33,:34,:35,:36,:37,:38,:39,:40,:41,:42)"
YJPT_JYLS = [(201810152771284, '', 3369533, 20180201, 313340000010, 9010, 'B0151B233090001', 10001001, 202752,20180201, 202752, '杭州银行股份有限公司舟山分行', 3301020460001329144, '支付宝代发交易内部户', '', '', '',11418102813895, '叶晓丹', 3400.33, -6696985474.66, '借', '转', 'CNY', 5, '支付宝单笔实时提现', '其他', '', '','ALOPER', '', '', '支付宝代发', '', 62306157101068677, '', '', '正常', 20180226203019000000, '内部', '', 20180608),
             (201810152771285, '', 6, 20180201, 313340000010, 9011, 'B0151B233090001', 10002002, 173935,20180201, 173935, '杭州银行股份有限公司杭州分行', 75118300002814, '柜员现金', '', 7518, '', 3301020460001074260,'代扣杭州天然气有限公司现金', 75.30, -696666.32, '贷', '转', 'CNY', 1, '代理项目支付宝转账缴费', '其他', '', '', 'ALOPER','', '', '支付宝代发', '', 62306157101068678, '', '', '正常', 20180226203019000000, '内部', '',20180608),
             (201810152771286, '', 168036, 20180201, 313340000010, 9012, 'B0151B233090001', 10003003, 121554,20180201, 121554, '杭州银行股份有限公司上海分行', 17618102694749, '同城通存通兑', '', '', '', 603367100127987101,'江宁一体机1680927', 50000.01, 699.00, '借', '现', 'CNY', 2, '本行借记卡本行ATM取款', 'ATM机', '', '','ALOPER', '', '', 'ATM取款', '',62306157101068679, '', '', '正常', 20180226203019000000, '内部', '',20180608),
             (201810152771287, '', 576252, 20180201, 313340000010, 9013, 'B0151B233090001', 10004004, 183111,20180201, 183111, '杭州银行股份有限公司北京分行', 3302093128300000655, '卡通资金清算专户', '', '', '', 161183000009663,'西溪支行', 6666.66, 66.66, '借', '现', 'CNY', 5, '现金取款', '柜面', '', '', 'ALOPER', '', '', '缴费','',62306157101068683, '', '', '正常', 20180226203019000000, '内部','', 20180608),
             (201810152771288, '', 666, 20180201, 313340000010, 9014, 'B0151B233090001', 10005005, 174114,20180201, 174114, '杭州银行股份有限公司舟山分行', 16118300009663, '张扬','', 7582,'', 15618102952773, '东莞分行hhhhhhhhhhhhhhhhh', 9999.90, 0.01, '贷', '现', 'CNY', 5, '支付宝快捷支付', '其他', '', '', 'ALOPER', '', '', '现支','',62306157101068686, '', '', '正常', 20180226203019000000, '内部', '',20180608),
             (201810152771289, '', 58499996, 20180201, 313340000011, 660000, 'B0151B233090001', 10006006,174115, 20180201, 174115, '杭州银行股份有限公司金融事业部', 69542158326542, '傻春',  '', '', '', 13418114762554, '王晓宇',71.40, 775421263.00, '贷', '转', 'CNY', 5, '他代本POS消费', '其他', '', '', 'ALOPER', '', '', '卡通支付','',62306157101068699, '', '', '正常', 20180226203019000000, '内部', '',20180608)]
'''
# 客户信息：
# 个人基础信息表：GRJCXX
# table_data =[('90159000' + str(i), '41272319991234' + str(i),'3133400000' + str(i),'B0151B23309' + str(ii), '500' + str(i),'查找资料','李丽' + str(i), 'DELL', '居民身份证','中国', '汉族','女', '本科','19990402','学校','杭州市萧山飞虹路','5811677', '银行职员','湖北省武汉市洪山区','湖北省武汉市洪山区','58116867','13545002776', '10000','50000', '已婚','李塞诺','58191234', '17712344321', '200' + str(i), '是', '否','20180312', '不良行为','466100','保密单位','信息员','否', '20190107',)]
#
#
# 个人客户关系信息表：GRKHGXXX
# table_data =[('90159000' + str(i), '3133400000' + str(i),'B0151B23309' + str(ii), '33' + str(i), '200' + str(i),'党员','高帅','银行','浙江杭州','56788765','20190107',)]
#
#
# 股东信息表：GDXX
# table_data =[('90159000' + str(i), '4127231234'+ str(ii),'3133400000' + str(i),'B0151B23309' + str(ii), '33' + str(i),'赵飞','居民身份证','41273319900705'+ str(ii),'有效', '90', '20180107', '20180107',)]
#
#
# 关联关系表：GLGX
# table_data =[('90159000' + str(i),'3133400000' + str(i),'B0151B23309' + str(ii), '33' + str(i),'4100'+ str(i),'1100','对公','3100'+ str(i), '李楠', '对私', '亲属关系','效','20190107','20190107',)]
#
#
#
# 授权交易对手信息：
# 信贷合同表：XDHTB
# table_data = [('JK20190109'+ str(i),'JE20190106'+ str(i),'90159000' + str(i), '3133400000' + str(i),'B0151B23309' + str(ii), '33' + str(i),'李闪闪','贷款','个贷','贴现','钱','1000000','20001010','20201010','浮动','0.9','0.5','抵押','NONE001','201010','自主支付','打款','投资','杭州','金融','否','20190107',)]
#
#
# 项目贷款信息表：XMDKXXB
# table_data = [('JK20190109' + str(i), '90159000' + str(i), '3133400000' + str(i), 'B0151B23309' + str(ii), '33' + str(i), '张三', '投资项目', '房地产', '是', '10000'+ str(ii), '1000000', '200000000','20201010', 'CHRU'+ str(i), '投资款项文件', 'AAA'+ str(i), 'BBB'+ str(i), 'CCC'+ str(i), 'DDD'+ str(i), 'FFF'+ str(i), 'GGG'+ str(i),'20191010','20190107')]
#
#
# 票据票面信息表：PJPMXXB
# table_data = [('2019'+ str(i),'NOE001'+ str(i), '621700287002909'+ str(i), '3133400000' + str(i), 'B0151B23309' + str(ii), '33' + str(i), '银行承兑汇票', '欧阳丹','31001700200', '中国银行','币', '1300020000', '20101010','20201010','赵燕', 'ERT001'+ str(i), '建设银行','200045454', '币', '1300020000', '商业发票','20190107')]
#
#
# 表外授信业务：DGBWSXYW
# table_data = [('210' + str(i),'3133400000' + str(i), 'B0151B23309' + str(ii),'33' + str(i),'90159000'+ str(i), '张笑', '20180207', '杭州银行股份有限公司舟山分行', '13200','信贷', '信用证','币', '9999900', '352000000', '20', '是', '20000101', '20100101', '20200101', '20500101','正常','100','0.66','币','3500','RT4500','IT009600','100','2018020799','币','1000000','商业发票','1001100200','20190108')]
#
#
# 贸易融资业务信息表：MYRZYWXXB
# table_data = [(1,'3300'+ str(i),'20190108','90159000'+ str(i),'3133400000' + str(i), 'B0151B23309' + str(ii),'33' + str(i),'袁立','JKI00'+ str(i),'出口信用抵押证','100'+ str(i),'币','250000000','1000000','1000000','NO001'+ str(i),'TFG1200','币','99999999999','商业发票','杭州银行','自营','100100','币','60000000','20190108','远期信用证','20300109','20190108')]
#
#
# 银团贷款：YTDK
# table_data = [('20190'+ str(i),'90159000'+ str(i),'3133400000' + str(i), 'B0151B23309' + str(ii),'33' + str(i),'合同协议','JKI00'+ str(i),'JKI00'+ str(i),'JKI00'+ str(i),'JKI00'+ str(i),'杭州银行','杭州银行','合同标志','孙艺','1000000','1000000','1000000','1000000','1000000','1000000','410000399','20300109','20190108','有效','lili','20190108')]
#
# 委托贷款：WTDK
# table_data = [('41860'+ str(i),'TI790'+ str(i),'90159000'+ str(i),'3133400000' + str(i), 'B0151B23309' + str(ii),'33' + str(i),'JKI00'+ str(i),'魏延','殷桃','4183u2910','杭州银行','5400001343','委托基金','8002000300','8002000300','资金周转','是','续费','2000','20190102','20500102','钱多多','NOR001'+ str(i),'银监会','有效','20190109')]
#
#
# 个人信贷业务借据：GRXDYWJJ
# table_data = [('41860'+ str(i),'TI790'+ str(i),'90159000'+ str(i),'慧慧','2010'+ str(i),'3133400000' + str(i), 'B0151B23309' + str(ii),'33' + str(i),'JKI00'+ str(i),'银行机构','明细科目','项目贷款','币','35000000','20000000','200','20','12','4','自主支付','20190202','20290202','20390202','7000000','3000000','还款中','20500505','贷款','4568000','正常','浮动','0.4','0.2','按月','61270079093398','银行卡','按月结息','0.22','币','2500','HUE370688','盛世','dh2678','转','6','3','是','20180108')]
#
#
# 信贷业务担保合同：XDYWDBHT
# table_data = [('20190'+ str(i),'3133400000' + str(i), 'B0151B23309' + str(ii),'33' + str(i),'抵押','一般担保合同','对公','Jhon','居民身份证','412723199'+ str(ii),'1000000','20300109','20190108','已签合同','20300109','20190108','20300109','币','2060001100','求偿权','34909j0'+ str(i),'20190108')]
#
#
# 担保关系：DBGX
# table_data = [('2010'+ str(i),'2019'+ str(i),'3133400000' + str(i), 'B0151B23309' + str(ii),'33' + str(i),'抵押','2222000000','20190209','20400209','正常','67890000','20190108')]
#
#
# 信贷业务质或抵押物：XDYWZHDYW
# table_data = [('TI790'+ str(i),'20190'+ str(i),'90159000'+ str(i),'3133400000' + str(i), 'B0151B23309' + str(ii),'33' + str(i),'房产','国债','30000000','币','3200000','3500000','20190108','银监会','0.55','任丽','3000000','20190102','20200201','工商所','6217002879093398','20101101','20201101','TYUI0001','纸质','IKM192929','34000000','杭州银行','20190208','4567890987','20190305','李翔','李菲','adf56789','银监会','20100706','20500706','是','20100706','20500706')]


#会计记账信息
#对公活期存款分户账 YJPT_DGHQCKFHZ
YJPT_DGHQCKFHZ_sql = "INSERT INTO YJPT_DGHQCKFHZ(HQCKZH, KHTYBH, YXJGDM, JRXKZH, NBJGH, MXKMBH, YXJGMC, MXKMMC, TJKMBH, BZ, ZHMC, DGHQCKZHLX, BZJZHBZ, LL, CKYE, KHRQ, KHGYH, XHRQ, ZHZT, SCDHRQ, CHLB, CJRQ) VALUES(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21,:22)"
#YJPT_DGHQCKFHZ = [('3W13340' + str(ii), '9000T09015' + str(ii), '313340' + str(ii), 'C0151V23309170' + str(ii),'99170' + str(ii), '90', '杭州银行股份有限公司舟山分行', '21', '66000' + str(ii), 'RNB', '钢铁虫', '人民币', '是', '5', '54646', '20111229', '170', '20190810', '正常', '20180504','钞', '20150625')]


#借记卡信息YJPT_JJKXX
YJPT_JJKXX_sql="INSERT INTO YJPT_JJKXX(KH, HQCKZH, KHTYBH, YXJGDM, JRXKZH, NBJGH, ZJLB, ZJHM, JJKCPMC, KPZT, YGBZ, KKRQ, KKGYH, CJRQ) VALUES(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14)"
#YJPT_JJKXX=[('HZ001'+ str(ii), 'HQ9000C8221'+ str(ii), '9000T09015' + str(ii), '313340' + str(ii), 'C0151V23309170' + str(ii),'99170' + str(ii), '居民身份证', '3301682008101' + str(ii), '杭州银行股份有限公司西湖支行', '正常', '是', '20061203', '170'+str(i), '20050322')]


#个人定期存款分户账
YJPT_GRDQCKFHZ_sql="INSERT INTO YJPT_GRDQCKFHZ(DQCKZH, GRKHTYBH, YXJGDM, JRXKZH, NBJGH, MXKMBH, MXKMMC, YXJGMC, BZ, TJKMBH, ZHMC, GRDQCKZHLX, CKQX, LL, JYJZMC, JYJZH, BZJZHBZ, KHJE, CKYE, KHRQ, KHGYH, XHRQ, DQR, ZHZT, SCDHRQ, CHLB, CJRQ) VALUES(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21,:22,:23,:24,:25,:26,:27)"
#YJPT_GRDQCKFHZ=[ ('HQ9000C8221' + str(ii), '9000T09015' + str(ii),'313340' + str(ii), 'C0151V23309170' + str(ii),'99170' + str(ii), 'KM302'+ str(ii), '科目1'+str(i), '杭州银行股份有限公司西湖支行', 'RNB', 'TJ901'+ str(ii), '钢铁虫', '零存整取',str(ii)+'天', '0.3', '卡', 'K0'+str(ii), '是', '55500', '555'+str(ii), '19960605', '170'+str(i), ' ', '20501230', '正常', '20160325', '人民币', '20181225')]


#个人信贷分户账
YJPT_GRXDFHZ_sql="INSERT INTO YJPT_GRXDFHZ(DKFHZH, XDJJH, KHTYBH, YXJGDM, JRXKZH, NBJGH, MXKMBH, YXJGMC, MXKMMC, ZHMC, BZ, ZJHKRQ, TJKMBH, DKHTH, XDYXM, DKWJFL, HKZH, DKRZZH, DKLL, DKBJZE, DKZCYE, DKYQYE, QBYE, BWQBYE, BWQXYE, DKQX, DQRQ, QXRQ, KHRQ, XHRQ, YQRQ, ZHZT, CJRQ) VALUES(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21,:22,:23,:24,:25,:26,:27,:28,:29,:30,:31,:32,:33)"
#YJPT_GRXDFHZ=[( 'DKFH0992'+str(ii), 'JJH908'+str(ii), '9000T09015' + str(ii), '313340' + str(ii), 'C0151V23309170' + str(ii),'99170' + str(ii),  'KM302'+ str(ii),  '杭州银行股份有限公司西湖支行','科目1'+str(i),'钢铁虫', 'RNB', '20181230', 'TJ901'+ str(ii), 'DKHT609'+ str(ii), '鲁班1'+ str(i), '关注', 'DKFH0992'+str(ii),'DKFH0992'+str(ii), '12', '60'+str(ii), 600000-i, 5000+i, '600000',' ','6613.3'+str(ii), str(ii), '20181230', '20161230', '20161229', '20190101', '正常', '20181230',)]

#对公客户
YJPT_DGKH_sql="INSERT INTO YJPT_DGKH(KHTYBH, ZZJGDM, YXJGDM, JRXKZH, NBJGH, KHMC, KHYWMC, FRDB, FRDBZJLB, FRDBZJHM, CWRY, " \
              "CWRYZJLB, CWRYZJHM, JBCKZH, JBZHKHXMC, ZCZB, ZCDZ, LXDH, YYZZH, YYZZYXJZRQ, JYFW, CLRQ, SSXY, KHLB, DKZH, GSZH, " \
              "DSZH, MGSKHTYBH, TYSXBZ, SXED, YYED, SSGSBZ, XYDJBH, ZCZBBZ, SSZBBZ, SSZB, ZZC, JZC, NSR, SCJLXDGXNY, YZBM, CZHM," \
              " YGRS, XZQHDM, KHLX, FXYJXH, CJRQ) " \
              "VALUES(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21,:22,:23,:24,:25,:26,:27,:28,:29,:30,:31,:32,:33,:34,:35,:36,:37,:38,:39,:40,:41,:42,:43,:44,:45,:46,:47)"
#YJPT_DGKH = [('9000T09015' + str(ii), 'SH0988733C' + str(ii), '313340' + str(ii), 'C0151V23309170' + str(ii),'99170' + str(ii), '钢铁虫', 'rate', '萝卜', '小蚂蚁身份证', '3301682008101' + str(ii), '郭靖' + str(i), '身份证','3301682008101' + str(i), 'CKZH90980087' + str(ii), '杭州银行股份有限公司西湖支行', '100000000', '杭州上城区城西银泰','13265412363', 'YYZ9980' + str(i), '20180321', '互联网', '20170801', '互联网', '对公', 'DKHT609' + str(ii),'GS0998' + str(i), 'DS0998' + str(i), '9000T09015' + str(ii), 'Y', '300000', '50000', 'Y', '1', 'RNB','RNB', '2000000' + str(ii), '600000000', '90000000', '6000000', '999912', '', '', '3000', '','集团客户', '', '20181120')]


#对公信贷分户账
YJPT_DGXDFHZ_sql="INSERT INTO YJPT_DGXDFHZ(DKFHZH, XDJJH, KHTYBH, YXJGDM, JRXKZH, NBJGH, MXKMBH, YXJGMC, MXKMMC, ZHMC, BZ," \
                 " ZJHKRQ, TJKMBH, DKHTH, XDYXM, DKWJFL, HKZH, DKRZZH, DKLL,DKBJZE, DKZCYE, DKYQYE, QBYE, BWQBYE,BWQXYE, DKQX, " \
                 "DQRQ, QXRQ, KHRQ, XHRQ, YQRQ, ZHZT, CJRQ) " \
                 "VALUES(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21,:22,:23,:24,:25,:26,:27,:28,:29,:30,:31,:32,:33)"
#YJPT_DGXDFHZ=[('DKFH0992'+str(ii), 'JJH908'+str(ii), '9000T09015' + str(ii),'313340' + str(ii), 'C0151V23309170' + str(ii),'99170' + str(ii),  'KM302'+ str(ii),'杭州银行股份有限公司西湖支行','科目1'+str(i), '钢铁虫','RNB','20181230', 'TJ901'+ str(ii), 'DKHT609'+ str(ii), '鲁班1'+ str(i), 'GZ', 'DKFH0992'+str(ii),'DKFH0992'+str(ii), '12', '60'+str(ii),'60'+str(ii), 600000-i, 5000+i, '600000',' ',6613.3+ii, str(ii), '20181230', '20161230', '20161229', '20190101', '正常', '20181230')]


#对公信贷业务借据
YJPT_DGXDYWJJ_sql="INSERT INTO YJPT_DGXDYWJJ(XDJJH, DKFHZH, KHTYBH, KHMC, XDHTH, YXJGDM, JRXKZH, NBJGH, MXKMBH, YXJGMC, MXKMMC," \
                  " XDYWZL, BZ, JKJE, JKYE, DKQX, ZQCS, ZQS, DQQS, FKFS, DKSJFFRQ, DKYSDQRQ, DKSJDQRQ, BNQXYE, BWQXYE, DKZT, ZJRQ," \
                  " DKLX, DKRZZH, DKWJFL, LLLX, JZLL, LLFD, HKFS, HKZH, HKQD, JXFS, BZJBL, BZJBZ, BZJJE, BZJZH, PJHM, PMJE, XDYXM, " \
                  "XDYGH, XZBZ, LJQKQS, LXQKQS, CJRQ) " \
                  "VALUES(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21,:22,:23,:24,:25,:26,:27,:28,:29,:30,:31,:32,:33,:34,:35,:36,:37,:38,:39,:40,:41,:42,:43,:44,:45,:46,:47,:48,:49)"
#YJPT_DGXDYWJJ = [('JJH908' + str(ii), 'DKFH0992' + str(ii), '9000T09015' + str(ii), '钢铁虫', 'JJH908' + str(ii), '313340' + str(ii),'C0151V23309170' + str(ii), '99170' + str(ii), 'KM302' + str(ii), '杭州银行股份有限公司西湖支行','科目1' + str(i), '业务', 'RNB', '6000000', '300000', '90' + str(ii), '30', '90', '12', '自主支付','20180101', '20181230', '20191230', 6613.3 + ii, '6665554', '正常', 20191230, '法人账户透支','DKFH0992' + str(ii), 'CJ', '浮动', 12, '12', '按月', 'DKFH0992' + str(ii), '', '按月结息', 12, 'RNB', 655555,'DKFH0992' + str(ii), 'PJ009' + str(ii), 626565 + i, '咚咚咚', 'XD90' + str(i), '转', 3, 6, 20181230)]


#对公活期存款分户账明细记录
YJPT_DGHQCKFHZMXJL_sql="INSERT INTO YJPT_DGHQCKFHZMXJL(HXJYLSH, ZJYLSH, BCXH, HQCKZH, KHTYBH, YXJGDM, JRXKZH, NBJGH, MXKMBH, YXJGMC, MXKMMC, HXJYRQ, HXJYSJ, ZHMC, JYLX, JYJE, KHHJGH, YWBLJGH, ZHYE, DFZH, DFHM, DFXH, DFXM, JYQD, BZ, XZBZ, DBRXM, DBRZJLB, DBRZJHM, JYGYH, GYLSH, SQGYH, ZY, CBMBZ, JYJDBZ, CJRQ) VALUES(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21,:22,:23,:24,:25,:26,:27,:28,:29,:30,:31,:32,:33,:34,:35,:36)"
# YJPT_DGHQCKFHZMXJL = [('646' + str(ii), '987465004' + str(ii), '648665004' + str(i), 'DKFH0992' + str(ii),'9000T09015' + str(ii), '313340' + str(ii), 'C0151V23309170' + str(ii), '99170' + str(ii),'KM302' + str(ii), '杭州银行股份有限公司西湖支行', '科目1' + str(i), 20180504, 165321, '小六子', '正常','69554' + str(ii), '313340' + str(ii), '313340' + str(ii), '69554' + str(ii),'DH8877FH0992' + str(ii), '付丽丽' + str(i),'369340' + str(ii), '建设银行' + str(i), '网银', 'RNB', '现', '番薯', '身份证','33016519861225' + str(ii), '170' + str(i), 'LS8833' + str(ii), '170' + str(i), '', '正常','借', 20181230)]

#
# JGHG_insert_data('YJPT_NBKMDZB')   内部科目对照表
# table_data =  [('KM88646' + str(ii), '财务1' + str(i), '3', 'SJKM0831' + str(ii),'贷款1' + str(i),'12', '信贷', 20181004)]
#
#
# JGHG_insert_data('YJPT_GRHQCKFHZ')   个人活期存款分户账
# table_data =  [('62306 531' + str(ii), 'KH34737' + str(ii), '94568' + str(i),'HZYH7367' + str(i),'46885' + str(ii),
# 'XD5457' + str(ii),'杭州银行股份有限萧山分公司','预付账款','GRC003','CNY', 'KH34737' + str(ii),'I类','card','3350' + str(ii),
# '是' ,'0.042','5000.85', 20180111 ,'XSFH4002' + str(i), 20201230,'正常',20181019,'人民币',20190105)]
#
#
# JGHG_insert_data('YJPT_GRHQCKFHZMXJL')  个人活期存款分户账明细记录
# table_data =  [('A1810' + str(ii), 'B1810' + str(ii), '10' + str(i) ,'6843 543' + str(ii),'KH34737' + str(ii), 'HZYH7367' + str(i),'B0018463' + str(ii) ,'IN97467' + str(ii) ,
#                         'ZQ5472'+ str(ii),'杭州银行股份有限萧山分公司','短期投资',20180612, '173858' +str(i) , 'CNY','KH34737' + str(ii),'金融','2000' + str(ii),'XS9002', 'JR4274','1500' + str(ii),
#                         '63523 762' + str(ii),'Micheal5' +str(i),'ZSYH6483' +str(i),'杭州银行股份有限舟山分公司','ATM','转','待办1' + str(i),'统一社会信用代码','HZYH8426' + str(ii),
#                         '柜员1' + str(i),'005' + str(i),'65' + str(i),'摘要:HZYHJR','正常','贷',20190105)]
#
#
# JGHG_insert_data('YJPT_DGHQCKFHZMXJL')    对公活期存款分户账明细记录
# table_data =  [('H8542' + str(ii), 'Z6432' + str(ii), '761' + str(i) ,'6452 330' + str(ii),'KH00214' + str(ii), 'HZYH7367' + str(i),'B002420' + str(ii) ,'IN7001' + str(ii) ,
#                         'RZ372'+ str(ii),'杭州银行股份有限萧山分公司','金融融资',20180612, '093742' , 'XX通信公司','融资','50000','HZYH7421','JRRZ900','90000','6721 340' + str(ii),
#                         'XH金融','HZXH53273622','杭州银行股份有限西湖分公司','手机银行','CNY','现','DB1' + str(i), '组织机构代码','HZYH5321' + str(ii), '柜员A' + str(i),'009' + str(i),
#                         '7009','摘要:HZYHJR','冲账','借',20180912)]
#
#
# JGHG_insert_data('YJPT_DGDQCKFHZ')    对公定期存款分户账
#  table_data =  [('67632' + str(ii), 'KH00214' + str(ii),'HZYH7367' + str(i),'Z6432' + str(ii),'IN7001' + str(ii),  'RZ372'+ str(ii),
#                         '杭州银行股份有限萧山分公司','金融融资','CNY','093742','duigong','定期','36个月','0.42','是','200','70000',20150321,
#                         'HZ782' ,'',20250901,'正常',20180912,'人民币',20190101)]
#
#
# JGHG_insert_data('YJPT_DGDQCKFHZMXJL')   对公定期存款分户账明细记录
#  table_data =  [('H8542' + str(ii), 'Z6432' + str(ii), '549' + str(i) ,'6452 679' + str(ii),'KH00214' + str(ii), 'HZYH7367' + str(i),'B002420' + str(ii) ,'IN8001' + str(ii) ,
#                         'RZ372'+ str(ii),'杭州银行股份有限萧山分公司','金融融资',20181209, '093742' , 'CNY','XX通信公司','融资','50000','HZYH7421','JRRZ900','90000','6935 997' + str(ii),
#                         'XH金融','HZXH53273622','杭州银行股份有限西湖分公司','手机银行','现','是','DB1' + str(i), '组织机构代码','DB7009' + str(ii), '柜员A' + str(i),'009' + str(i),
#                         '摘要:HZYHJR','冲账','借',20190103)]
#
#
# JGHG_insert_data('YJPT_NBFHZ')   内部分户账
# table_data =  [('8542' + str(ii), 'HZYH7367' + str(i),'Z6432' + str(ii), 'IN8001' + str(ii), 'MX372'+ str(ii),'Tony' + str(i),
#                         '杭州银行股份有限滨江分公司', '商业信贷','贷','CNY','549' + str(i) ,'借贷账户','50000','90000','是','按年结息',
#                         '0.53',20180705,20200905,'正常',20190106)]
#
#
# JGHG_insert_data('YJPT_NBFHZMXJL')   内部分户账明细记录
# table_data =  [('H8542' + str(ii),'Z6432' + str(ii),'0051' + str(i), '98262'+ str(i),'HZYH7367' + str(i), 'JR70063' + str(ii),'IN8001' + str(ii),'MX372'+ str(ii),
#                         '杭州银行股份有限滨江分公司', '商业信贷',20170425,130953,'CNY','Arimy' + str(i),'借贷','50000','90000','69243' + str(ii),'DFKM549' + str(i) ,'借贷',
#                         'AB信贷股份有限公司','ZHYH8452' +str(ii),'手机银行','现','柜员D' +str(i),'9354' + str(i),20180705,20200905,'摘要AAAAAABBBBCCCC','补账','借',20190106)]
# JGHG_insert_data('YJPT_GRXDFHZ')   个人信贷分户账
# table_data =  [('DKFH742' + str(ii),'JD6432' + str(ii),'KH0051' + str(i), 'HZYH7367' + str(i), 'JR70063' + str(ii),'IN8001' + str(ii),'MX372'+ str(ii),
#                         '杭州银行股份有限滨江分公司', '商业信贷','Arimy' + str(i),'CNY',20170425,'TJKM4693' + str(ii),'DK462' + str(ii),'Turo' + str(i),'关注',
#                         '62431' + str(ii),'64528' + str(ii),'0.45','50000','90000','2000','3500','5700','1300','560',20200705,20190905,20170715,20250910,20190519,'正常',20190107)]
#
#
# JGHG_insert_data('YJPT_DGXDFHZMXJL')   对公信贷分户账明细记录
#  table_data =  [('H8542' + str(ii), 'Z6432' + str(ii), '549' + str(i) ,'6452 679' + str(ii),'KH00214' + str(ii), 'HZYH7367' + str(i),'B002420' + str(ii) ,'IN8001' + str(ii) ,
#                         'RZ372' + str(ii),'JJH749' + str(ii),'杭州银行股份有限萧山分公司','金融融资',20181209, '093742' ,'DBG信息公司','融资','借','50000','90000','6935 997' + str(ii),
#                         'XH金融','HZXH53273622','杭州银行股份有限西湖分公司','手机银行','CNY', '摘要:HZYHJR','正常','DB1' + str(i), '组织机构代码','DB7009' + str(ii), '柜员A' + str(i),'009' + str(i),'现',20190103)]
#


#担保关系
# YJPT_DBGX 字段sql：INSERT INTO YJPT_DBGX(DBHTH,BDBHTH,YXJGDM,JRXKZH,NBJGH,DBLX,DBJE,DBQSRQ,DBDQRQ,DBZT,JLDBYGH,CJRQ) VALUES (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12)
# table_data = [('88T646' + str(ii), '987465004' + str(ii), '648665004' + str(i), 'DKFH0992' + str(ii),'DKeeeFH0992' + str(ii), '抵押', '313340' + str(ii), 20180506, 20180506, '解除', '科目1' + str(i), 20180504)]

#存折信息
# YJPT_CZXX 执行sql: INSERT INTO YJPT_CZXX(CZH,HQCKZH,KHTYBH,YXJGDM,JRXKZH,NBJGH,ZJLB,ZJHM,CZLX,CZZT,YGBZ,QYRQ,QYGYH,CJRQ) VALUES (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14)
# table_data = [('CZT646' + str(ii), 'CK465004' + str(ii), '313340' + str(ii), 'C0151V23309170' + str(ii),'99170' + str(ii), '小蚂蚁身份证', '33016820081013' + str(ii), '普通存折', '正常', '解除', '是', 20180504,'GY1' + str(i), 20180906)]

#信用卡信息YJPT_XYKXX
# table_data = [('CZT646' + str(ii), 'XYK5006224' + str(ii), '9000T09015' + str(ii), '313340' + str(ii),
#                'C0151V23309170' + str(ii), '99170' + str(ii), '小蚂蚁身份证', '330168200813' + str(ii),
#                '信用卡', '三星', '正常', '集团客户', '是', '是', 'CZT646' + str(ii), '是', 60000, 500, 'CNY', 88888, 6666, 20180504,
#                20180504, 'GY1' + str(i), 20180906, 'GY1' + str(i), 20190906, 'GY1' + str(i), '正常', 4564, 64565456,68886.8, 3255, 66665, 545,
#                965553.6, 66542, 99897, 6564464, 6665, 65465, 65456, '信用', '资产上亿', '正常', 63456, 20180630, 20190101)]


# 信用卡信息明细表
# YJPT_XYKZHJYMXB
# table_data = [('CZT646' + str(ii), 'XYK5006224' + str(ii), '313340' + str(ii), 'C0151V23309170' + str(ii),
#                '99170' + str(ii), 'KM302' + str(ii), '科目1' + str(i), 'RNB', 20180213, '646' + str(ii),
#                '987465004' + str(ii), '890' + str(i), '转', '人民币', '现', 'JY097' + str(i), '借', 8895654, 600, '取现',
#                20060305, 20091203, 20101005, 'CK465004' + str(ii), '被分期', 'ATM', '', 'GY1' + str(i), '313340' + str(ii),
#                '柜员工作站' + str(i),
#                'GZZBH01' + str(i), '无', '无', 20110608)]

#授信信息
#YJPT_SXXX
# table_data =[('SXXY0946' + str(ii), '9000T09015' + str(ii),'313340' + str(ii), 'C0151V23309170' + str(ii), '99170' + str(ii),20180213,'杭州城市大数据运行有限公司' + str(i),
#         '集团客户授信' + str(i),'授信文书'+str(i),9000000000,'RNB',20060305,'有效',20101005,20131005,20021005,'同意授信' + str(ii),'老李' + str(i),'是','是','GY1' + str(i),20110608)]


#贷款核销
#YJPT_DKHX 执行sql: INSERT INTO YJPT_DKHX(XDJJH,XDHTH,KHTYBH,YXJGDM,JRXKZH,NBJGH,MXKMBH,MXKMMC,KMGSJG,BZ,SHDKBJ,SHBNLX,SHBWLX,HXRQ,HXSHBJ,HXSHBNLX,HXSHBWLX,SHBZ,HXSHGYH,HXSHRQ,BZH,CJRQ) VALUES (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21,:22)
#  table_data = [('JJH908' + str(ii), 'DKHT609'+ str(ii), '9000T09015' + str(ii), '313340' + str(ii),
#                'C0151V23309170' + str(ii), '99170' + str(ii), 'KM302' + str(ii), '科目1' + str(i), '313340' + str(ii),
#                'RNB', 8222202 + str(i), 56454 + str(i), 897654 + str(i), 20180213, 4564554 + str(i), 4654628 + str(i),
#                8465645 + str(i), '是',
#                'GY1' + str(i), 20160305, '有效', 20101005)]


#贷款展期
#YJPT_DKZQ 执行sql: INSERT INTO YJPT_DKZQ(DKZQBH,XDJJH,XDHTH,KHTYBH,YXJGDM,JRXKZH,NBJGH,ZQRQ,ZQDQRQ,ZQJE,YLL,LLLX,ZQJZLL,LLFD,YHTH,YJJH,JYGYH,SQGYH,CJRQ) VALUES (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19)
# table_data = [('DKZQBH9099' + str(ii), 'JJH908' + str(ii), 'DKHT609' + str(ii), '9000T09015' + str(ii),
#                '313340' + str(ii), 'C0151V23309170' + str(ii), '99170' + str(ii), 20160330, 20190330,
#                '6565465.99784' + str(ii), '0.1' + str(i), '浮动', '0.1', '0.01' + str(i), 'DKHT609' + str(ii),
#                'JJH908' + str(ii), 'GY1' + str(i), 'GY1' + str(i), 20180213,)]


# 信贷资产转让
# YJPT_XDZCZR 执行sql: INSERT INTO YJPT_XDZCZR(ZRHTH,YXJGDM,JRXKZH,NBJGH,MXKMBH,MXKMMC,JYDSBH,JYDSMC,XDJYLX,JYZCLX,BZ,ZRDKBJZE,ZRDKLXZE,ZRSXF,ZRZJ,HGLL,ZRJGRQ,HGJZRQ,ZRHTQSRQ,ZRHTDQRQ,JYDSZZH,JYDSZZZHHM,JYDSXH,CJRQ) VALUES (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21,:22,:23,:24)
# table_data =[('ZR908322'+str(ii),'313340' + str(ii), 'C0151V23309170' + str(ii), '99170' + str(ii),'KM302' + str(ii), '科目1' + str(i),'DSBH947'+str(ii),'光头强'+str(i),'网上银行', '票据' + str(i),'RNB' ,'6995465'+ str(ii),'65465'+ str(ii),'68491'+ str(i),'84965465'+str(ii),'0.1' + str(i),20110213,20120213,20160213,20190213,'B0151B2330' + str(ii), '刘翔'+ str(i),'313340' + str(ii),20120213)]

# 资产转让关系表
# YJPT_ZCZRGXB 执行sql: INSERT INTO YJPT_ZCZRGXB(ZRHTH,YXJGDM,XDJJH,JRXKZH,NBJGH,CJRQ) VALUES (:1,:2,:3,:4,:5,:6)
# table_data =[('ZR908322'+str(ii),'313340' + str(ii), 'JJH908' + str(ii), 'C0151V23309170' + str(ii), '99170' + str(ii),20120213)]


#贷款五级心态变动
#YJPT_DKWJXTBD 执行sql: INSERT INTO YJPT_DKWJXTBD(TZRQ,XDJJH,XDHTH,KHTYBH,YXJGDM,JRXKZH,NBJGH,YXJGMC,YMXKMBH,YMXKMMC,YWJXT,XMXKMBH,XMXKMMC,XWJXT,BZ,ZRJE,ZCJE,KHMC,JBGYH,TZGYH,SQGYH,SPGYH,BDYY,BDFS,CJRQ) VALUES (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21,:22,:23,:24,:25)
# table_data =[(20160807,'JJH908' + str(ii), 'DKHT609' + str(ii), '9000T09015' + str(ii), '313340' + str(ii), 'C0151V23309170' + str(ii), '99170' + str(ii),'杭州银行股份有限公司西湖支行','KM302' + str(ii),  '科目1' + str(i),'关注','XKM302' + str(ii),  'X科目1' + str(i),'关注','RNB','156746541'+str(ii),'156746881'+str(ii),'钢铁虫'+str(i),'GY1' + str(i),'GY2' + str(i),'GY3' + str(i),'GY4' + str(i),'这是一个寒冷的冻鸡','人工',20120213)]


#交易流水
#YJPT_JYLS 执行sql: INSERT INTO YJPT_JYLS(HXJYLSH,ZJYLSH,BCXH,JYRQ,YXJGDM,NBJGH,JRXKZH,MXKMBH,JYSJ,JZRQ,JZSJ,JYJGMC,JYZH,JYHM,JYXTMC,DFXH,DFJGMC,DFZH,DFHM,JYJE,ZHYE,JYJDBZ,XZBZ,BZ,YWLX,JYLX,JYQD,JYJZMC,JYJZH,CZGYH,GYLSH,FHGYH,ZY,ZPZZL,ZPZH,FPZZL,FPZH,CBMBZ,SJC,ZHBZ,KXHBZ,CJRQ) VALUES (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21,:22,:23,:24,:25,:26,:27,:28,:29,:30,:31,:32,:33,:34,:35,:36,:37,:38,:39,:40,:41,:42)
# table_data =[('646' + str(ii), '987465004' + str(ii),'900' + str(ii), 20180430,  '313340' + str(ii), 'C0151V23309170' + str(ii), '99170' + str(ii),'KM302' + str(ii),165863,20160609, 195233, '杭州银行股份有限公司舟山分行'+str(i), '330102046000132'+str(ii), '支付宝代发交易内部户'+str(i),'中国银监会'+str(i), '313340' + str(ii), '杭州银行股份有限公司西湖支行'+str(i), '11418102813895'+str(ii),'小鱼'+str(i), str(i)+'3400.33',6987415,'贷','转','RNB','8','这是自动插入'+str(i),'POS','卡','KH987773' + str(ii),'GY1' + str(i), 'LS8833' + str(ii),'GY4' + str(i),'这是一个寒冷的冻鸡','高级会员'+str(i),'ZPH987'+str(i),'会员'+str(i),'FZPH987'+str(i),'冲账',20120213162554000000,'对私','开户',20180525)]


# 资产负债科目统计表
#执行sql: INSERT INTO YJPT_ZCFZKMTJB(JRJGDM,JRXKZH,NBJGH,TJKMBH,TJKMMC,TJKMJE,QXLX,TJRQ,BZ,DQMC,XZQHDM,CJRQ) VALUES (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12)
# table_data =[('JRJG88646' + str(ii), '313340' + str(ii), 'C0151V23309170' + str(ii), '99170' + str(ii),'KM302' + str(ii),'科目1' + str(i),str(ii)+'165.863','月', 20160321, 'RNB', '浙江富春支行'+str(ii), str(i),20180525)]


#涉农统计表
#YJPT_SNTJB 执行sql: INSERT INTO YJPT_SNTJB(JRJGDM,JRXKZH,NBJGH,TJKMBH,TJKMMC,TJKMJE,QXLX,TJRQ,BZ,DQMC,XZQHDM,CJRQ) VALUES (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12)
# table_data =[('JRJG8946' + str(ii), 'C0151V23366170' + str(ii), '99166' + str(ii),'KM359' + str(ii),'科目16' + str(i),str(ii)+'1656.743','半年', 20180321, 'RNB', '浙江富春支行'+str(ii), str(i),20170525)]


#汇率信息表
#YJPT_HLXXB 执行sql: INSERT INTO YJPT_HLXXB(YXJGDM,JRXKZH,NBJGH,YXJGMC,WB,BB,ZJJ,JZJ,HLRQ,CJRQ) VALUES (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10)
#  table_data =[( '313340' + str(ii),'C0151V23366170' + str(ii), '99166' + str(ii),'杭州银行股份有限公司西湖支行','CNY','RNB','6.98','6.3','0.2'+str(ii), 20170525)]


#金融工具信息表
#YJPT_JRGJXXB 执行sql: INSERT INTO YJPT_JRGJXXB(YXJGDM,JRXKZH,NBJGH,YXJGMC,ZQMC,JRGJBH,ZCLX,BZ,FXJG,YXCZQYDM,FXGB,DBJG,CPPJ,PJJG,FXZTPJ,JYZHLX,PMLL,FXJGE,FXRQ,SSRQ,QXRQ,DQRQ,LLLX,HQBS,ZJPGJG,PGJGSJ,YE,CJRQ) VALUES (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21,:22,:23,:24,:25,:26,:27,:28)
# table_data =[( '313340' + str(ii),'C0151V23366170' + str(ii), '99166' + str(ii),'杭州银行股份有限公司西湖支行','手机银行APP'+str(i),'JRGJ098'+str(ii),'债券','杭州银行留下支行'+str(i),'313340' + str(ii),'CN', '中国银行'+str(ii),'A++','国际信用','中央银行','银行账户','0.3'+str(ii),'68749',20180321,20180606,20180606,20280606,'浮动','是',468713,20181230,6541635,20181230)]


#资金交易信息表
#YJPT_ZJJYXXB 执行sql: INSERT INTO YJPT_ZJJYXXB(YXJGDM,JRXKZH,NBJGH,MXKMBH,YXJGMC,MXKMMC,JYBH,LCCPDJBM,JYLX,JYZL,JRGJBH,JYZHLX,HTH,HTJE,BZ,JCZCKHMC,JCZCSSHY,JCZCSFWBHKH,JCZCZXFS,JCZCZXR,JYGY,SPR,JYDSDM,JYDSMC,JYRQ,QSRQ,DQRQ,MMBZ,JYQBZ,MRBZ,MRJE,MCBZ,MCJE,CJJG,YWZT,FHRQ,QXRQ,SJJGRQ,QSBZ,JFZH,DFZH,JFJE,DFJE,JFBZ,DFBZ,JFLL,DFLL,BZJJYBZ,GLBZJZH,GLYWBH,WBGLXTMC,CJRQ) VALUES (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21,:22,:23,:24,:25,:26,:27,:28,:29,:30,:31,:32,:33,:34,:35,:36,:37,:38,:39,:40,:41,:42,:43,:44,:45,:46,:47,:48,:49,:50,:51,:52)
#table_data =[( '313340' + str(ii),'C0151V23366170' + str(ii), '99166' + str(ii),'KM359' + str(ii),'杭州银行股份有限公司西湖支行','科目16' + str(i), 'DKHT66609' + str(ii),'LC09388'+str(i),'自营','买入','手机银行','交易账户','DKHT66609' + str(ii),'648654622'+str(i), 'RNB','国际信用'+str(i),'中央','是','保证金质押','(๑ŐдŐ)b'+str(i),'GY1' + str(i),'GY4' + str(i),'DSBH947'+str(ii),'光头强'+str(i),20180321,20180606,20280606,'买入','远期','RNB','665'+str(i),'CNY','4654'+str(i),'5000千万','成交确认',20181230,20181230,20181230,'是','3W13340' + str(ii),'D139940' + str(ii),'6855'+str(ii),'6855'+str(ii),'RNB','RNB','0.6'+str(i),'0.6'+str(i),'是','GG3HH40' + str(ii),'YW0998' + str(ii),'银湖智慧📱'+str(i),20180716)]







import cx_Oracle


# 注：设置环境编码方式，可解决读取数据库乱码问题
import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

# scott是数据用户名，tiger是登录密码（默认用户名和密码）
connection = cx_Oracle.connect("hg", "123456", '122.112.248.182:1521/CITYDO')

# 操作游标
cursor = connection.cursor()

def JGHG_insert_data(table):
    sql = auto_insert(table)
    print(sql)

    #批量生成数据进行插入
    for i in range(1,60000):
        ii=1000+i

        #插入数据格式（修改内容）
        table_data =[( '313340' + str(ii),'C0151V23366170' + str(ii), '99166' + str(ii),'KM359' + str(ii),'杭州银行股份有限公司西湖支行','科目16' + str(i), 'DKHT66609' + str(ii),'LC09388'+str(i),'自营','买入','手机银行','交易账户','DKHT66609' + str(ii),'648654622'+str(i), 'RNB','国际信用'+str(i),'中央','是','保证金质押','(๑ŐдŐ)b'+str(i),'GY1' + str(i),'GY4' + str(i),'DSBH947'+str(ii),'光头强'+str(i),20180321,20180606,20280606,'买入','远期','RNB','665'+str(i),'CNY','4654'+str(i),'5000千万','成交确认',20181230,20181230,20181230,'是','3W13340' + str(ii),'D139940' + str(ii),'6855'+str(ii),'6855'+str(ii),'RNB','RNB','0.6'+str(i),'0.6'+str(i),'是','GG3HH40' + str(ii),'YW0998' + str(ii),'银湖智慧📱'+str(i),20180716)]

        cursor.prepare(sql)#sql语句，需要与数据库字段相对应，value值长度与字段对应
        cursor.execute(None,table_data[0])#插入数据集
        print('执行sql:', sql)
        print('插入内容：', table_data[0])

        # 切记一定要执行
        cursor.execute('commit')


    # 关闭连接，释放资源
    cursor.close()
    connection.close()

#定义一个函数传入表名称从数据库自动获取字段，拼接成sql
def auto_insert(table):
    #执行SQL语句
    curs = cursor.execute("select column_name from all_tab_columns where  TABLE_NAME = '" + table + "'order by column_id")
    #查看数据库数据
    data = curs.fetchall()
    data_1=[]
    test=[]
    for i in range(len(data)):
        data_1.append(data[i][0])
        print(data[i][0])
        test.append(':'+str(i+1))#生成value数列

    table_sql="INSERT INTO "+ table + "("+ ','.join(data_1) + ")" + " VALUES " + "("+ ','.join(test) + ")"

    # data_2=[i for i in reversed(data_1)]#反序排列
    # print(','.join(data_1))  # 转为元组
    # print(','.join(test))#转为元组
    # print(data)
    # print(len(data))
    return table_sql



JGHG_insert_data('YJPT_ZJJYXXB')






