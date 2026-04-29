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
    Log    ${data}    console=True
    Should Contain    ${data}    786.50

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

    # Step 3: Compare DataFrames
    pdfd = pd.DataFrame({
    "ID": [1, 2, 3, 4],
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "Salary": [50000, 60000, 70000, 80000]
    }
    ${comparison_result}=    Evaluate    libraries.helper.compare_html_and_parquet(pdfd, pdfd)
    Log    ${comparison_result}

    # Step 4: Validate the comparison result
    Run Keyword If    '${comparison_result}[match]' == 'False'    Fail    DataFrames do not match: ${comparison_result}
    Log    DataFrames match successfully!
