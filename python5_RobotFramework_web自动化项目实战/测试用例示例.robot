*** Settings ***
Library    DateTime
Library    SeleniumLibrary
Library    Collections    



*** Test Cases ***
获取当前的时间
    #变量表达式 - ${变量名}
    ${cur_date}=    Get Current Date    
    
    
我是测试版
    Log    我是测试版hello
    
加法计算
    ${a}=    Set Variable    10
    ${b}=    Set Variable    15
    ${add}=    Evaluate    ${a}+${b}
    Should Be Equal As Integers   25    ${add}
    
创建变量
    #字典的创建和取值 - 
    #& - 多组数据 
    #$ - 单值数据
    &{dict_my}    Create Dictionary    hello=world    hobby=wzry
    ${dict_my}    Create Dictionary    hello=world    hobby=wzry
    Log    ${dict_my.hello}
    #列表的创建和取值
    @{list_my}    Create List    123    world    heheda    ${dict_my}
    #取值
    Log    ${list_my[-1]}
       
    Set To Dictionary    ${dict_my}    key=value 
    Log    ${dict_my}      
    
        
      
       
    