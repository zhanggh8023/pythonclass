# -*- coding: utf-8 -*-
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : manage.py
# @Software: PyCharm

import requests
import json, time
from conf import Allpath
from public.logger import Log
from public.get_mysql_info import getMysqlInfo
from public.all_method import message_code, get_f_login_cookie, lock_time, time_version, set_user_token, \
    set_admin_token, data_time_replace

logger = Log('httpRequest', Allpath.log_path)


class httpRequest:
    requests.packages.urllib3.disable_warnings()

    def httpGet (self, url, method, data, sql, env):
        # global request
        if 'env' in env.keys() and env['env'] == 1:
            if 'stationId' in env.keys():
                headers = set_user_token(stationId=env['stationId'], db=2)
            else:
                headers = set_user_token(stationId='HL99998')
        elif 'env' in env.keys() and env['env'] == 2:
            # redis：b2h 使用 2传值；  h2b 使用 1传值
            headers = set_admin_token(2)
        elif 'env' in env.keys() and env['env'] == 3:
            headers = set_admin_token(2)
        else:
            headers = get_f_login_cookie()

        if 'lock' in env.keys():
            data = data_time_replace(data, env)

        if method == 'GET':
            logger.info('现在开始进行GET方法调用请求')
            if 'sms' in env.keys() and env['sms'] == 1:
                # 短信验证码返回替换，五分钟短信验证
                data["valicode"] = message_code()
                data["verifycode"] = data["valicode"]
                time.sleep(0.5)

            if 'my_sql' in sql.keys() and env['get'] == 1:
                logger.info('现在开始进行get请求')
                sql_result = getMysqlInfo(Allpath.db_conf_path, 'config').get_mysql_info(sql['my_sql'],
                                                                                         sql['condition'], sql['code'])
                logger.info('get中数据库返回：{}'.format(sql_result))
                if sql['sql'] == 0:
                    data['reportIds'] = sql_result[1]
                    logger.info('现在开始进行【reportIds替换】get,参数格式请求')
                    request = requests.get(url, data, headers=headers, verify=False).json()
                    logger.info('请求返回：{}'.format(request))

                elif sql['sql'] == 1:
                    data['reserveId'] = sql_result[1]
                    data['userCardId'] = sql_result[1]
                    logger.info('现在开始进行【reserveId替换】get,参数格式请求')
                    request = requests.get(url, data, headers=headers, verify=False).json()
                    logger.info('请求返回：{}'.format(request))
                    request['code'] = str(request['result'])
                    if request['result'] != True and request['result'] != False:
                        request['code'] = str(request['result']['data'])

                elif sql['sql'] == 2:
                    url = url + str(sql_result[1])
                    logger.info('现在开始进行【reserveId,url替换】get,参数格式请求')
                    request = requests.get(url, data, headers=headers, verify=False).json()
                    request['code'] = str(request['result']['pkgId']) + str(request['result']['reserveDay']) + str(
                        request['result']['additionNames'])
                    logger.info('请求返回【配置后套餐、时间、名称】code：{}'.format(request))

                elif sql['sql'] == 3:
                    url = url + str(sql_result[1])
                    logger.info('现在开始进行【reserveId,url替换】get,参数格式请求')
                    request = requests.get(url, data, headers=headers, verify=False).json()
                    # 状态 0:未支付, 10:待预约, 20: 待确认, 30:待体检 40: 同步失败, 50: 已完成
                    request['code'] = str(request['result']['serviceStatus'])
                    logger.info('请求返回【配置后预约状态id】code：{}'.format(request))

                elif sql['sql'] == 4:
                    url = url + str(sql_result[1])
                    logger.info('现在开始进行【订单trade_id,url替换】get,参数格式请求')
                    request = requests.get(url, data, headers=headers, verify=False).json()
                    if env['pay'] == 1:
                        request['code'] = '优惠券抵扣:' + str(request['result']['orderInfoList'][2]['value']) + '实付款:' + str(
                            request['result']['orderInfoList'][3]['value']) + '支付款:' + str(
                            request['result']['payInfo'][1]['value'])
                    elif env['pay'] == 2:
                        request['code'] = '优惠券抵扣:' + str(request['result']['orderInfoList'][3]['value']) + '实付款:' + str(
                            request['result']['orderInfoList'][4]['value']) + '体检卡:' + str(
                            request['result']['orderInfoList'][2]['value'])
                    elif env['pay'] == 3:
                        request['code'] = '支付方式:' + str(request['result']['payInfo'][0]['value']) + '实付款:' + str(
                            request['result']['orderInfoList'][2]['value']) + '支付款:' + str(
                            request['result']['payInfo'][1]['value'])
                    elif env['pay'] == 4:
                        request['code'] = '支付方式:' + str(request['result']['payInfo'][0]['value']) + '实付款:' + str(
                            request['result']['orderInfoList'][1]['value']) + '支付款:' + str(
                            request['result']['payInfo'][1]['value'])

                    else:
                        request['code'] = '支付方式:' + str(request['result']['payInfo'][0]['value']) + '实付款:' + str(
                            request['result']['orderInfoList'][2]['value']) + '支付款:' + str(
                            request['result']['payInfo'][2]['value'])

                    logger.info('请求返回【配置后优惠券、实付款、支付款】code：{}'.format(request))

                else:
                    request = requests.get(url, data, headers=headers, verify=False).json()
                    logger.info('请求返回：{}'.format(request))

            else:
                request = requests.get(url, data, headers=headers, verify=False).json()
                logger.info('请求返回：{}'.format(request))

        elif method == 'POST':
            if 'sql' in sql.keys() and env['sql'] == 1:
                logger.info('现在开始进行post请求')
                sql_result = getMysqlInfo(Allpath.db_conf_path, 'config').get_mysql_info(sql['my_sql'],
                                                                                         sql['condition'], sql['code'])
                logger.info('post中数据库返回：{}'.format(sql_result))
                if sql['sql'] == 0:
                    data['userName'] = sql_result[1]
                    logger.info('现在开始进行【userName替换】post,body格式请求')
                    request = requests.post(url, json=data, headers=headers, verify=False).json()
                    logger.info('请求返回：{}'.format(request))

                elif sql['sql'] == 1:
                    data['id'] = sql_result[1]
                    logger.info('现在开始进行【id替换】post,参数格式请求')
                    request = requests.post(url, data, headers=headers, verify=False).json()
                    logger.info('请求返回：{}'.format(request))

                elif sql['sql'] == 2:
                    url = url + sql_result[1]
                    logger.info('现在开始进行【地址拼接】post,参数格式请求')
                    request = requests.post(url, data, headers=headers, verify=False).json()
                    logger.info('请求返回：{}'.format(request))

                elif sql['sql'] == 3:
                    data['tradeId'] = sql_result[1]
                    data['thirdpartTradeId'] = sql_result[2]
                    logger.info('现在开始进行【模拟支付tradeId，thirdpartTradeId替换】post,参数格式请求')
                    request = requests.post(url, json=data, headers=headers, verify=False).json()
                    logger.info('请求返回：{}'.format(request))

                elif sql['sql'] == 4:
                    a = eval(data['ext'])
                    a['groupUserCardId'] = sql_result[1]
                    data['ext'] = a
                    logger.info('现在开始进行【团检卡groupUserCardId替换】post,参数格式请求')
                    request = requests.post(url, json=data, headers=headers, verify=False).json()
                    logger.info('请求返回：{}'.format(request))

                elif sql['sql'] == 5:
                    a = eval(data['ext'])
                    a['groupUserCardId'] = sql_result[1]
                    a['hostTradeId'] = sql_result[2]
                    data['ext'] = a
                    logger.info('现在开始进行【团检约前加项groupUserCardId,hostTradeId替换】post,参数格式请求')
                    request = requests.post(url, json=data, headers=headers, verify=False).json()
                    logger.info('请求返回：{}'.format(request))

                elif sql['sql'] == 6:
                    data['userCardId'] = sql_result[1]
                    data['hostTradeId'] = sql_result[2]
                    logger.info('现在开始进行【团检卡约后加项groupUserCardId,hostTradeId替换】post,参数格式请求')
                    request = requests.post(url, json=data, headers=headers, verify=False).json()
                    logger.info('请求返回：{}'.format(request))

                elif sql['sql'] == 7:
                    data['userCardId'] = sql_result[1]
                    logger.info('现在开始进行【团检卡groupUserCardId替换】post,参数格式请求')
                    request = requests.post(url, json=data, headers=headers, verify=False).json()
                    logger.info('请求返回：{}'.format(request))

                elif sql['sql'] == 8:
                    a = data['ext']
                    a['groupUserCardId'] = sql_result[1]
                    if env['lock'] == 0:
                        reserveDay = lock_time(0)
                    else:
                        reserveDay = lock_time(1)
                    a['examinationReservePo']['reserveTime'] = reserveDay
                    data['ext'] = a
                    logger.info('现在开始进行【团检卡groupUserCardId,锁定2天预约时间替换】post,参数格式请求')
                    request = requests.post(url, json=data, headers=headers, verify=False).json()
                    logger.info('请求返回：{}'.format(request))

                elif sql['sql'] == 9:
                    data['userCouponId'] = sql_result[1]
                    logger.info('现在开始进行【优惠券userCouponId替换】post,参数格式请求')
                    request = requests.post(url, json=data, headers=headers, verify=False).json()
                    logger.info('请求返回：{}'.format(request))

                elif sql['sql'] == 10:
                    a = eval(data['ext'])
                    a['groupUserCardId'] = sql_result[1]
                    data['ext'] = a
                    data['userCouponId'] = sql_result[2]
                    logger.info('现在开始进行【优惠券userCouponId替换】post,参数格式请求')
                    request = requests.post(url, json=data, headers=headers, verify=False).json()
                    logger.info('请求返回：{}'.format(request))

                elif sql['sql'] == 11:
                    a = eval(data['ext'])
                    a['reportCode'] = sql_result[1]
                    data['ext'] = a
                    data['userCouponId'] = sql_result[2]
                    logger.info('现在开始进行【报告code，优惠券userCouponId替换】post,参数格式请求')
                    request = requests.post(url, json=data, headers=headers, verify=False).json()
                    logger.info('请求返回：{}'.format(request))

                elif sql['sql'] == 12:
                    data['reserveId'] = sql_result[1]
                    logger.info('现在开始进行【reserveId替换】post,参数格式请求')
                    request = requests.post(url, json=data, headers=headers, verify=False).json()
                    logger.info('请求返回：{}'.format(request))

                elif sql['sql'] == 13:
                    data['reserveId'] = sql_result[1]
                    data['reserveTime'] = lock_time(0)
                    logger.info('现在开始进行【reserveId，reserveTime替换】post,参数格式请求')
                    request = requests.post(url, json=data, headers=headers, verify=False).json()
                    logger.info('请求返回：{}'.format(request))

                elif sql['sql'] == 14:
                    data['analyzeId'] = sql_result[1]
                    data['reserveDateTimeStamp'] = lock_time(1)
                    logger.info('现在开始进行【reserveId，reserveTime替换】post,参数格式请求')
                    request = requests.post(url, json=data, headers=headers, verify=False).json()
                    logger.info('请求返回：{}'.format(request))

                elif sql['sql'] == 15:
                    data['reserveNumber'] = sql_result[1]
                    data['uniqReserveCode'] = sql_result[2]
                    logger.info('现在开始进行【reserveNumber，uniqReserveCode】post,参数格式请求')
                    request = requests.post(url, json=data, headers=headers, verify=False).json()
                    logger.info('请求返回：{}'.format(request))

            elif 'cxfa' in env.keys():
                t_head1 = time_version(cxfa=env['cxfa'])
                t_head2 = t_head1
                if 'phone' in env.keys():
                    t_head2 = time_version(cxfa=env['cxfa'], phone=env['phone'])

                if 'cxfaid' in env.keys() and 'post' in env.keys():
                    logger.info('现在开始进行时间戳版本长效方案post,参数格式请求')
                    request1 = requests.post(url, data, headers=t_head1, verify=False).json()
                    logger.info('第一次保存headers：{},返回：{}'.format(t_head1, request1))
                    request = requests.post(url, data, headers=t_head2, verify=False).json()
                    logger.info('第二次保存headers：{},返回：{}'.format(t_head2, request))
                elif 'cxfa' in env.keys() and 'cxfaid' in env.keys():
                    logger.info('现在开始进行时间戳版本长效方案post,body格式请求')
                    request1 = requests.post(url, json=data, headers=t_head1, verify=False).json()
                    logger.info('第一次保存headers：{},返回：{}'.format(t_head1, request1))
                    request = requests.post(url, json=data, headers=t_head2, verify=False).json()
                    logger.info('第二次保存headers：{},返回：{}'.format(t_head2, request))
                elif 'post' in env.keys() and env['post'] == 1:
                    logger.info('现在开始进行时间戳版本长效方案post,参数格式请求')
                    request = requests.post(url, data, headers=t_head1, verify=False).json()

                else:
                    logger.info('现在开始进行时间戳版本长效方案post,body格式请求')
                    request = requests.post(url, json=data, headers=t_head1, verify=False).json()

            elif 'post' in env.keys() and env['post'] == 1:
                logger.info('现在开始进行post,参数格式请求')
                if 'sms' in env.keys() and env['sms'] == 1:
                    data["vcode"] = message_code()
                    # 参数格式
                    request = requests.post(url, data, headers=headers, verify=False).json()
                else:
                    # 参数格式
                    request = requests.post(url, data, headers=headers, verify=False).json()

            elif 'post' in env.keys() and env['post'] == 2:
                logger.info('现在开始进行post_file请求')
                path = Allpath.project_path + "/request_file/" + sql['filename']
                files = {sql['name']: (sql['filename'], open(path, 'rb'))}
                # body格式
                request = requests.post(url, data=data, files=files, headers=headers, verify=False).json()
                logger.info('请求返回：{}'.format(request))

            elif 'post' in env.keys() and env['post'] == 3:
                logger.info('现在开始进行post参数params格式请求')

                # body格式
                request = requests.post(url, params=data, headers=headers, verify=False).json()
                logger.info('请求返回：{}'.format(request))

            else:
                logger.info('现在开始进行post,body格式请求')
                # body格式
                request = requests.post(url, json=data, headers=headers, verify=False).json()
                logger.info('请求返回：{}'.format(request))


        elif method == 'POST_file':
            logger.info('现在开始进行post_file请求')
            path = Allpath.project_path + "/request_file/" + sql['filename']
            print(sql['name'], headers, path)
            files = {sql['name']: (sql['filename'], open(path, 'rb'))}
            # body格式
            request = requests.post(url, data=data, files=files, headers=headers, verify=False).json()
            logger.info('请求返回：{}'.format(request))


        elif method == 'POST_word':
            logger.info('现在开始进行post_word请求')
            request = {}
            # 参数格式,返回的是字符串格式
            text = requests.post(url, data, headers, verify=False).text
            request['code'] = text


        elif method == 'PUT':
            logger.info('现在开始进行put请求')
            headers["Content-Type"] = "application/json"

            # print(data)
            # .encode("UTF-8")对字符串进行`UTF-8`编码格式编码
            # 用dumps转义成json格式
            # json.dump()函数的使用，将json信息写进文件
            # json.dumps()   编码：把一个Python对象编码转换成Json字符串
            # json.load()函数的使用，将读取json信息
            # json.loads()  解码：把Json格式字符串解码转换成Python对象
            # body格式
            request = requests.put(url, data=json.dumps(data), headers=headers, verify=False).json()
            logger.info('请求返回：{}'.format(request))


        elif method == 'DELETE':
            logger.info('现在开始进行delete请求')
            # excel的data中指定：0表示正常请求，1取数据库返回第一个值，2指定数据库返回第二个值，3指定删除规则
            if '1' in data.keys() and data['1'] == 1:
                sql_result = getMysqlInfo(Allpath.db_conf_path, "config").get_mysql_info(sql['my_sql'],
                                                                                         sql['condition'], sql['code'])
                logger.info('数据库返回:' + str(sql_result))
                logger.info("excel取值获取数据库返回第%s位：" % data['1'])
                url_del = url + str(sql_result[0])
                logger.info("请求URL：%s" % url_del)
                request = requests.delete(url_del, headers=headers, verify=False).json()
            elif sql['1'] == 0:
                request = requests.delete(url, data=data, headers=headers, verify=False).json()
            else:
                request = requests.delete(url, headers=headers, verify=False).json()

        else:
            logger.info('请求方法未知！请核对后在尝试！')

        return request


if __name__ == '__main__':
    # data = {"age":18,"birthday":"1998-01-01","bookingName":"接口测试","bookingPhone":"17681829051","cardId":"110101199003075314","cardType":1,"couponFee":1000100,"couponInfo":[{"id": "a123","type": "discount","fee":1000100}] ,"marriageStatus":2,"medicalTime":"2021-03-07","name":"zgh5","orgId":"HL99998","orgName":"杭州-禾连内网测试医院98","packageId":"2671","packageName":"接口自动化不限套餐","phone":"15258814180","profitsharing":1,"reportAddress":"邮件纸质报告地址","reportReceiver":"邮件纸质报告收件人","reportType":1,"sex":2,"time":"","usedCoupon":1,"userId":"zgh005"}
    # data = {"couponFee":1000100,"couponInfo":[{"id": "a123","type": "discount","fee":1000100}] ,"fee":1,"orderCountPrice":1000000,"orderId":"3527","payId":"11111111","receiptNo":"3527","usedCoupon":1,"userId":"zgh005"}
    data = {"orderId": "3527", "userId": "zgh006"}
    # data = {'tradeId':'TJTC2021012122541819154','payType':0,"thirdpartTradeId":""}
    # data = {"gender":1,"skuId":14698}
    # data = {"name": "测试zgh", "gender": "0", "birthday": "1990-03-18", "married": "0", "phone": "18767137391",
    #         "certType": "2", "certNumber": "66549879846", "company": "阿里健康", "department": "技术部",
    #         "address": "北京市朝阳区望京SOHO，1011", "addPacks": [{"isvPackId": "123", "version": "123456"}],
    #         "addItems": [{"version": "123456", "isvItemId": "123"}], "havaReport": "demo", "employeeNumber": "178170"}
    # data = {}

    sql = {}

    env = {"env": 2}

    # url = 'http://management-fed-gray.helianhealth.com/envk8s/healthcheck-web-client/wx/api/market/trade/test/notifySuccess'
    # url = 'http://management-fed-gray.helianhealth.com/env-b2h/healthmanage-web/wx/api/market/reserve/list'
    # url = 'http://b2htest.helianhealth.com/healthmanage-web/tencent/order/apply'
    # url = 'http://b2htest.helianhealth.com/healthmanage-web/tencent/order/confirm'
    url = 'http://b2htest.helianhealth.com/healthmanage-web/tencent/order/report/detail'
    # url = 'http://b2htest.helianhealth.com/healthmanage-web/tencent/order/cancel'
    # url = 'http://b2htest.helianhealth.com/healthmanage-admin/admin/enterprise/card/issue'
    # url = 'http://management-fed-gray.helianhealth.com/env-b2h/healthmanage-web/wx/api/card/v2/matchCardSuccess'
    # url = 'http://b2htest.helianhealth.com/healthmanage-web/app/market/aliordernotify?method=alibaba.alihealth.examination.reserve.confirm&merchantCode=10.81.17&reserveNumber=2020102981&reserveDate=2021-02-18&packageCode=2776&storeId=HL99998'

    # DELETE,PUT,POST_del,POST_word,POST,POST_file,GET
    hh = httpRequest().httpGet(url, 'GET', data, sql, env)
    print(hh)

    #  assert_value列默认为空列表[],[{"336":"result['userCardId']"},["data['result']"]],为满足同时需要替换指定用例value和指定断言value，当同时存在需求时规定0位是字典格式指定用例取值，1位指定返回断言值。  #  assert_value列默认为空列表[]，断言取code值；["data['result']['serviceStatus']"] 当存在指定路径是用data为返回体，后面跟返回值的准确路径，注意双引号和单引号要区分，外层用双，内层就单  #  多字段不同用例返回结果取值方法，根据key为用例id，value为指定用例想获取值的路径[{"329":"result['batchId']","332":"result['normalData'][0]['bigBitchId']"}] data中替换内容使用%s替代，填入顺序如获取顺序一致。  #  添加path字段，控制使用url路径替换方法调用，方法使用等同于id字段的使用。[{"path":4,"groupId":"result['normalData'][0]['groupId']","companyId":"result['normalData'][0]['companyId']"}]  #  添加idlist字段，控制不同位置获取用例返回值内容，列表中表示用例id，后面获取值依次对应替换位置和对应获取路径[{"idlist":[1,2,3],"userCardId":"result['userCardId']","userCardId":"result['userCardId']","userCardId":"result['userCardId']"}]  #  env:默认0取url_f域名,1取url_h,2取url_a  #  sms：默认0不发送短信 1发送  #  post：0正常json格式 1参数格式  2上传文件  #  cxfa：长效方案对应时间戳版本信息查询模块  #  time：控制单条用例执行后等待时间，用于数据库更新时间差控制，'time':2 表示等待两秒  #  random：通过随机生成名称避免重复，value表示生成次数  #  new： 通过new字段设置：1控制是否设置新建单位是否走新流程  #  {"env": 0, "sms": 0, "post": 0, "cxfa":"获取机构","cxfaid":"不同","phone":"15990106283","get": 1, "sql":1,'time':2}  #  def request (self, method, url, params=None, data=None, headers=None, cookies=None, files=None, auth=None,  #              timeout=None, allow_redirects=True, proxies=None, hooks=None, stream=None, verify=None, cert=None,  #              json=None):

'''
腾讯报告修改状态
UPDATE `tencent_order_history` 
SET medical_time = '2021-01-18',
order_status = 41 
WHERE
  id = 3478

  update trade_sub set service_status=50,sub_status=50 where trade_id='TJTC20210303195354707036';
  
  update trade_info set trade_Status=50 where id='TJTC20210303195354707036';

'''
