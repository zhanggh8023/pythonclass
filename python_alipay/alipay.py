# -*- coding: utf-8 -*-
# @Time    : 2020/2/21 19:43
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : alipay.py
# @Software: PyCharm

import logging

from alipay.aop.api.AlipayClientConfig import AlipayClientConfig
from alipay.aop.api.DefaultAlipayClient import DefaultAlipayClient

from alipay.aop.api.domain.AlipayTradeCreateModel import AlipayTradeCreateModel
from alipay.aop.api.request.AlipayTradeCreateRequest import AlipayTradeCreateRequest
from alipay.aop.api.response.AlipayTradeCreateResponse import AlipayTradeCreateResponse

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    filemode='a',)
logger = logging.getLogger('')

if __name__ == '__main__':
    # 实例化客户端
    alipay_client_config = AlipayClientConfig()
    alipay_client_config.server_url = 'https://openapi.alipaydev.com/gateway.do'
    alipay_client_config.app_id = '请填写appi_id'
    alipay_client_config.app_private_key = '请填写开发者私钥去头去尾去回车，单行字符串'
    alipay_client_config.alipay_public_key = '请填写支付宝公钥，单行字符串'
    client = DefaultAlipayClient(alipay_client_config, logger)

    # 构造请求参数对象
    model = AlipayTradeCreateModel()
    model.out_trade_no = "20150320010101001";
    model.total_amount = "88.88";
    model.subject = "Iphone6 16G";
    model.buyer_id = "2088102177846880";
    request = AlipayTradeCreateRequest(biz_model=model)

    # 执行API调用
    try:
        response_content = client.execute(request)
    except Exception as e:
        print(traceback.format_exc())

    if not response_content:
        print("failed execute")
    else:
        # 解析响应结果
        response = AlipayTradeCreateResponse()
        response.parse_response_content(response_content)
        # 响应成功的业务处理
        if response.is_success():
            # 如果业务成功，可以通过response属性获取需要的值
            print("get response trade_no:" + response.trade_no)
        # 响应失败的业务处理
        else:
            # 如果业务失败，可以从错误码中可以得知错误情况，具体错误码信息可以查看接口文档
            print(response.code + "," + response.msg + "," + response.sub_code + "," + response.sub_msg)