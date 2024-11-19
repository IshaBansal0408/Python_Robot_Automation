*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${browserName}   Chrome
${appURL}   https://www.saucedemo.com/

*** Test Cases ***
Login to DemoBlaze
    Open Browser    ${appURL}  ${browserName}
    Maximize Browser Window
    login2Application
    Close Browser

*** Keywords ***
login2Application
    Input Text      id:user-name    standard_user
    Input Text      id:password     secret_sauce
    Click Element   xpath://input[@id='login-button']