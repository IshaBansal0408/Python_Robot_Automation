*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${browserName}   Chrome
${appURL}       https://www.knowledgeware.in/Automation/practiceform.html

*** Test Cases ***
TestingSelectBoxesTest
    Open Browser    ${appURL}  ${browserName}
    Maximize Browser Window

    # Varify Select Box
    select from list by label   id:countrySelect    Karnataka
    select from list by label   id:citySelect    Hibbali
    sleep   10
    select from list by index   id:countrySelect    4
    select from list by index   id:citySelect    3
    sleep   10

    close browser

*** Keywords ***