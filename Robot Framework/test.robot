*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}     https://www.apple.com

*** Test Cases ***
Open Apple Website
    Open Browser    ${URL}    chrome    options=add_argument(--headless),add_argument(--no-sandbox),add_argument(--disable-dev-shm-usage)
    Title Should Be    Apple
    [Teardown]    Close Browser
