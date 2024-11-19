*** Settings ***
Library    SeleniumLibrary


*** Keywords ***
loadApplication
    [Arguments]  ${appURL}  ${browserName}
    Log To Console    Loading Application with URL: ${appURL} in browser: ${browserName}
    Open Browser    ${appURL}  ${browserName}
    Maximize Browser Window
    ${title}    get title
    [Return]  ${title}

shutdownApplication
    Close All Browsers