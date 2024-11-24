*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${browserName}   Chrome
${appURL}       https://www.knowledgeware.in/Automation/practiceform.html

*** Test Cases ***
TestingRadioButtonsTest
    Open Browser    ${appURL}  ${browserName}
    Maximize Browser Window

    # Verify radio buttons
    page should contain radio button    xpath:(//input[@name='gender'])[1]
    select radio button    gender   female
    sleep   10
    # Verify checkboxes
    select checkbox     sports
    select checkbox     reading
    sleep   10
    unselect checkbox   sports
    sleep   10
    close browser

*** Keywords ***
