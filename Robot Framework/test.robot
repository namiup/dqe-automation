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
    Open Browser    ${url}    Chrome    executable_path=/usr/local/bin/chromedriver
