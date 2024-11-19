*** Settings ***
Library    SeleniumLibrary
Resource  ../Resources/resources.robot

*** Variables ***
${browser}   Chrome
${url}   https://www.saucedemo.com/

*** Test Cases ***
TestingUserDefKey
    ${pageTitle}    loadApplication     ${url}  ${browser}
    log to console  Title of page is ${pageTitle}
    sleep   3
    shutdownApplication


