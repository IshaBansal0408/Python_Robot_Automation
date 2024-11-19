*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${browserName}   Chrome
${appURL}       https://www.way2automation.com/way2auto_jquery/frames-and-windows.php#load_box

*** Test Cases ***
TestingHandleAlertsTest
    Open Browser    ${appURL}  ${browserName}
    Maximize Browser Window
    select frame    xpath://body/section[@id='wrapper']/div[1]/div[1]/div[3]/div[1]/div[1]/iframe[1]
    sleep  3
    click link  xpath:/html/body/div/p/a
    sleep  3
    unselect frame
    close browser

*** Keywords ***