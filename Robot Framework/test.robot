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
    Open Browser    ${url}    Chrome    options=--headless,--no-sandbox,--disable-dev-shm-usage,--disable-gpu,--window-size=1920,1080
    Title Should Be    Apple
    [Teardown]    Close Browser
