*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem

*** Variables ***
${URL_FILE}            report.html

*** Test Cases ***
Verify Login
    [Tags]    smoke
    ${url}=    Get File    ${URL_FILE}
    Open Browser    ${url}    Edge
    Title Should Be    Apple
    [Teardown]    Close Browser
