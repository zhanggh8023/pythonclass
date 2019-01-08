*** Settings ***
Library    SeleniumLibrary    


*** Variables ***
#元素定位表达式
${金额输入框}    //input[@data-url="/Invest/invest"]
${投标按钮}    //button[text()='投标']
${投资成功-弹出框}    //div[contains(@class,"layui-layer-page")]
${投资成功弹出框_查看并激活_按钮}    //div[contains(@class,"layui-layer-page")]//button


*** Keywords ***
投资操作
    [Arguments]    ${投资金额}
    Wait Until Page Contains Element    ${金额输入框}    40
    Sleep    1
    Focus    ${金额输入框}
    Input Text    ${金额输入框}    ${投资金额}
    Focus    ${投标按钮}
    Click Element    ${投标按钮}
    
获取用户可用余额
    [Return]    ${余额}
    Wait Until Page Contains Element    ${金额输入框}    40
    ${余额}    Get Element Attribute    ${金额输入框}    data-amount
    
点击查看并激活_跳转到个人页面
    Wait Until Element Is Visible    ${投资成功弹出框_查看并激活_按钮}    20
    Click Element    ${投资成功弹出框_查看并激活_按钮}
    
    
    
    