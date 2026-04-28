*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}     https://www.apple.com

*** Test Cases ***
Open Example Website
    Open Browser    ${URL}    chrome
    Title Should Be    Apple
    [Teardown]    Close Browser
