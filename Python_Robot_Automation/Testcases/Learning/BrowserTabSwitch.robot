*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${browserName}   Chrome
${appURL1}       https://www.google.com/
${appURL2}       https://www.bing.com/

*** Test Cases ***
TestingHandleAlertsTest
    Open Browser    ${appURL1}  ${browserName}
    Maximize Browser Window
    sleep  3
    Open Browser    ${appURL2}  ${browserName}
    Maximize Browser Window
    sleep  3

    switch browser  1
    ${title1}   get title
    log to console  Title of the first browser window: ${title1}
    switch browser  2
    ${title2}   get title
    log to console  Title of the second browser window: ${title2}

    close all browsers

*** Keywords ***