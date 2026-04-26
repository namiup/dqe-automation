*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${URL}            requirements.txt

*** Test Cases ***
Verify Login
    [Tags]    smoke
    Open Browser    Get File    ${URL}    Chrome    arguments=--headless --no-sandbox --disable-dev-shm-usage
    Title Should Be    Apple
    [Teardown]    Close Browser
