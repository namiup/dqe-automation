*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${URL}            https://apple.com

*** Test Cases ***
Verify Login
    [Tags]    smoke
    Open Browser    ${URL}    Chrome    arguments=--headless --no-sandbox --disable-dev-shm-usage
    Title Should Be    Apple
    [Teardown]    Close Browser
