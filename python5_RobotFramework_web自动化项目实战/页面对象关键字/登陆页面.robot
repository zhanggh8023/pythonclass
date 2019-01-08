
*** Setting ***
Library    SeleniumLibrary


*** Variables ***
${登陆用户名输入框}    //*[@name='phone']
${登陆密码输入框}    //*[@name='password']
${登陆按钮}    //button
${错误提示框_登陆区域}    //*[@class="form-error-info"]


*** Keyword ***
登陆
    [Arguments]    ${url}    ${username}    ${passwd}     
    Open Browser    ${url}    chrome
    Maximize Browser Window
    输入用户名   ${username}
    输入密码    ${passwd}
    点击登陆按钮


获取错误提示信息_登录区域
    [Return]    ${error_msg}
    ${error_msg}    Get Text    ${错误提示框_登陆区域}

输入用户名
    [Arguments]    ${username}
    Input Text    ${登陆用户名输入框}    ${username}
    
输入密码
    [Arguments]    ${passwd}
    Input Text    ${登陆密码输入框}     ${passwd}
    
点击登陆按钮
     Click Element    ${登陆按钮}
     
打开浏览器
    [Arguments]    ${url}  
    Open Browser    ${url}    chrome
    Maximize Browser Window
    
