*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${browserName}   Chrome
${appURL}       https://www.knowledgeware.in/Automation/alerts.html

*** Test Cases ***
TestingHandleAlertsTest
    Open Browser    ${appURL}  ${browserName}
    Maximize Browser Window

    Click Element   xpath://tbody/tr[1]/td[2]/button[1]
    sleep   3
#    alert should be present     You Clicked a Button
    handle alert    accept

    Click Element   xpath://tbody/tr[1]/td[2]/button[1]
    sleep   3
    handle alert    leave


    close browser

*** Keywords ***