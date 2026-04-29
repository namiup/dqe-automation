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

def compare_dataframes_and_return_differences(df1, df2):
    """
    Compares two Pandas DataFrames for an exact match and returns the differences.

    Args:
        df1: First DataFrame.
        df2: Second DataFrame.

    Returns:
        A dictionary containing differences:
            - 'missing_in_df1': Rows present in df2 but missing in df1.
            - 'missing_in_df2': Rows present in df1 but missing in df2.
    """
    # Find rows missing in df1
    missing_in_df1 = pd.concat([df2, df1]).drop_duplicates(keep=False)
    
    # Find rows missing in df2
    missing_in_df2 = pd.concat([df1, df2]).drop_duplicates(keep=False)
    
    return {
        "missing_in_df1": missing_in_df1,
        "missing_in_df2": missing_in_df2
    }



