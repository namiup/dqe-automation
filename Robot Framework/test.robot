*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem

*** Variables ***
${URL_FILE}            report.html

*** Test Cases ***
Verify Login
    [Tags]    smoke
    File Should Exist    ${URL_FILE}
    ${url}=    Get File    ${URL_FILE}
    Open Browser    ${url}    Chrome    options=add_argument("--headless"),add_argument("--no-sandbox"),add_argument("--disable-dev-shm-usage"),add_argument("--disable-gpu"),add_argument("--window-size=1920,1080")
    Title Should Be    Apple
    [Teardown]    Close Browser
