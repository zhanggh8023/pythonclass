*** Settings ***
Resource    ../页面对象关键字/登陆页面.robot
Resource    ../测试数据/登陆_测试数据.robot
Resource    ../页面对象关键字/首页.robot
Test Teardown    Close Browser


*** Test Cases ***
登录用例1_成功登陆
    #步骤
    登陆页面.登陆    ${url}    ${login_success_data.username}    ${login_success_data.passwd}
    #断言 - 作业 -
    ${用户昵称}    首页.获取用户昵称
    #比对是否相等
    Should Be Equal    ${用户昵称}       ${login_success_data.check_msg} 
    Sleep    5    