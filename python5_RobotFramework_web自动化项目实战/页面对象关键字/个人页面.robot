*** Settings ***
Library    SeleniumLibrary
Library    String    


*** Variables ***
${个人可用余额}    //*[@class="personal_info"]//li[@class="color_sub"]

   
*** Keywords ***
获取用户余额
    [Return]    ${临时数据[0]}
    Wait Until Page Contains Element    ${个人可用余额}    40
    Sleep    1
    ${钱}    Get Text    ${个人可用余额}
    @{临时数据}    Split String    ${钱}    元
        
