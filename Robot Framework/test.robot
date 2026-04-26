*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${REMOTE_URL}    http://localhost:4444/wd/hub

*** Test Cases ***
Verify Login
    [Tags]    smoke
    Open Browser    https://apple.com    chrome    remote_url=${REMOTE_URL}
    Title Should Be    Apple
    [Teardown]    Close Browser
