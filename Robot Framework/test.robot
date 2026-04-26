*** Settings ***
Library           SeleniumLibrary
Library    OperatingSystem

*** Variables ***
${URL_FILE}            report.html

*** Test Cases ***
Verify Login
    [Tags]    smoke
    ${url}=    Get File    ${URL_FILE}
    Open Browser    ${url}    Chrome    arguments=--headless --no-sandbox --disable-dev-shm-usage
    Title Should Be    Apple
    [Teardown]    Close Browser
