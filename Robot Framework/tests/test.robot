*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem
Library    parquet_helper.py

*** Variables ***
${URL_FILE}    logs/report.html
${PARQUET_FILE}    path/to/data.parquet

*** Test Cases ***
Open Local HTML Headless
    ${options}=    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys, selenium.webdriver
    Call Method    ${options}    add_argument    --headless
    Call Method    ${options}    add_argument    --no-sandbox
    Call Method    ${options}    add_argument    --disable-dev-shm-usage
    ${path}=    Normalize Path    ${URL_FILE}
    Open Browser    file://${path}    chrome    options=${options}
    [Teardown]    Close Browser

Read Parquet Data Example
    ${data}=    Read Parquet File    ${PARQUET_FILE}
    Log    ${data}
    Should Contain    ${data[0]['column_name']}    expected_value
