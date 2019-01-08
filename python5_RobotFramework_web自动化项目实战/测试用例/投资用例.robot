*** Settings ***
Resource    ../页面对象关键字/登陆页面.robot
Resource    ../页面对象关键字/首页.robot
Resource    ../页面对象关键字/标详情页面.robot
Resource    ../页面对象关键字/个人页面.robot

Test Setup  登陆页面.登陆    http://120.79.176.157:8012/Index/login.html    18684720553    python  
Test Teardown    Close Browser
Force Tags   invest 
    

*** Test Cases ***
投资成功用例
    [Tags]    smoke
    #前提条件
    #步骤
    #首页 - 点击投资按钮
    首页.点击抢投标按钮-进入标详情页面-随机选取一个
    # 进入标的详情页面后，获取当前用户余额，实例化标详情页面对象
    ${投资前的余额}    标详情页面.获取用户可用余额
    # 输入金额，并提交投标操作
    标详情页面.投资操作    1000
    标详情页面.点击查看并激活_跳转到个人页面
    #获取用户的余额
    ${投资后的余额}    个人页面.获取用户余额
    #比对操作
    ${差值}    Evaluate    ${投资前的余额}-${投资后的余额}
    Should Be Equal As Integers    ${差值}    1000
    
    
    