*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem

*** Variables ***
${URL_FILE}    report.html

*** Test Cases ***
Open Local HTML Headless
    ${options}=    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys, selenium.webdriver
    Call Method    ${options}    add_argument    --headless
    Call Method    ${options}    add_argument    --no-sandbox
    Call Method    ${options}    add_argument    --disable-dev-shm-usage
    ${path}=    Normalize Path    ${URL_FILE}
    Open Browser    file://${path}    chrome    options=${options}
    [Teardown]    Close Browser
