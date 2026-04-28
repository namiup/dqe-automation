*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Open Google Headless
    Open Browser    https://www.google.com    chrome    options=add_argument(--headless),add_argument(--no-sandbox),add_argument(--disable-dev-shm-usage)
    [Teardown]    Close Browser
