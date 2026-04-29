*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem
Library    libraries/helper.py

*** Variables ***
${HTML_FILE}    logs/report.html

*** Test Cases ***
Open Local HTML Headless
    ${options}=    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys, selenium.webdriver
    Call Method    ${options}    add_argument    --headless
    Call Method    ${options}    add_argument    --no-sandbox
    Call Method    ${options}    add_argument    --disable-dev-shm-usage
    ${path}=    Normalize Path    ${HTML_FILE}
    Open Browser    file://${path}    chrome    options=${options}
    [Teardown]    Close Browser

Read Html Data
    ${data}=    Read Html File    ${HTML_FILE}
    Log    ${data}
    Should Contain    ${data}    'some text'
