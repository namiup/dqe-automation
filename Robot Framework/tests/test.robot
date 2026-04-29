*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem
Library    libraries.helper

*** Variables ***
${HTML_FILE}    /var/jenkins_home/workspace/Robot/Robot Framework/logs/report.html
${PARQUET_FOLDER}    /parquet_data/visits
${DATE_COLUMN}     visit_timestamp
${START_DATE}     2000-01-01
${END_DATE}     2100-01-01

*** Test Cases ***
Open Local HTML Headless
    ${options}=    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys, selenium.webdriver
    Call Method    ${options}    add_argument    --headless
    Call Method    ${options}    add_argument    --no-sandbox
    Call Method    ${options}    add_argument    --disable-dev-shm-usage
    ${path}=    Normalize Path    ${HTML_FILE}
    Open Browser    file://${path}    chrome    options=${options}
    [Teardown]    Close Browser

Read Html Data
    ${path}=    Normalize Path    ${HTML_FILE}
    File Should Exist    ${path}
    ${data}=    Read Html File    ${path}
    Log    ${data}
    Should Contain    ${data}    1,356.18

Read Parquet Data
    ${data}=    Read Parquet File    ${PARQUET_FOLDER}    ${DATE_COLUMN}    ${START_DATE}    ${END_DATE}
    Log    ${data}

Compare HTML and Parquet Data
    # Step 1: Read HTML data
    ${html_path}=    Normalize Path    ${HTML_FILE}
    File Should Exist    ${html_path}
    ${html_data}=    Evaluate    libraries.helper.read_html_file("${html_path}")

    # Step 2: Read Parquet data
    ${parquet_data}=    Evaluate    libraries.helper.read_parquet_file("${PARQUET_FOLDER}", "${DATE_COLUMN}", "${START_DATE}", "${END_DATE}")


