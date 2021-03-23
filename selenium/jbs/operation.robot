*** Settings ***
Documentation    Suite description

*** Test Cases ***
登录
    open browser                    http://larp.api.mgtv.com/oss        chrome
    set browser implicit wait       5
    input text                      name=form-username                  18674831947
    input text                      id=form-password                    12345678
    ${firstRet}=                    get text                   id=1
    should contain                  ${firstRet}                hello


*** Keywords ***
Provided precondition
    Setup system under test