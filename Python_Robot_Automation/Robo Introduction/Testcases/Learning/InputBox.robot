*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${browserName}   Chrome
${appURL}   https://www.saucedemo.com/

*** Test Cases ***
TestingInputBoxTest
    Open Browser    ${appURL}  ${browserName}
    Maximize Browser Window

    title should be     Swag Labs

    ${"usernameCSS"}    set variable   id:user-name
    ${"passwordCSS"}    set variable   id:password

    element should be visible       ${"usernameCSS"}
#    element should not be visible       ${"usernameCSS"}
    element should be enabled       ${"usernameCSS"}

    Input Text      ${"usernameCSS"}    standard_user
    sleep   10
    Clear element Text      ${"usernameCSS"}
    sleep   10

    Close Browser

*** Keywords ***