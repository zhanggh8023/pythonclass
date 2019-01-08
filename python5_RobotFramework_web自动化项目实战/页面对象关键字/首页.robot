*** Settings ***
Library    SeleniumLibrary
Library    String     


*** Variables ***
${个人昵称链接}    //a[@href="/Member/index.html"]
${抢投标匹配}    //div[@class="b-unit"]
${抢投标按钮}    //div[@class="b-unit"][%s]//a[text()="抢投标"]


*** Keywords ***
获取用户昵称
    [Return]    ${用户昵称}
    #等待操作
    Wait Until Element Is Visible    ${个人昵称链接}    40
    #获取文本内容
    ${用户昵称}    Get Text    ${个人昵称链接} 
    

点击抢投标按钮-进入标详情页面-随机选取一个
    Wait Until Element Is Visible    ${抢投标匹配}    40
    ${标个数}    Get Element Count    ${抢投标匹配}  
    ${random}    Evaluate    random.randint(0,${标个数})    modules=random
    ${要投的标按钮}    Replace String    ${抢投标按钮}    %s    ${random} 
    Click Element    ${要投的标按钮}
    
           
    
      