*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${URL}            https://apple.com
${USERNAME}       test_user
${PASSWORD}       secret_password

*** Test Cases ***
Verify Login
    [Tags]    smoke
    Open Browser    ${URL}    Chrome    options=add_argument('--headless')    add_argument('--no-sandbox')    add_argument('--disable-dev-shm-usage')
    Title Should Be    Apple
