*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Open Google Headless
    ${options}=    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys, selenium.webdriver
    Call Method    ${options}    add_argument    --headless
    Call Method    ${options}    add_argument    --no-sandbox
    Call Method    ${options}    add_argument    --disable-dev-shm-usage
    Open Browser    https://www.apple.com    chrome    options=${options}
    Title Should Be    Apple
    [Teardown]    Close Browser
