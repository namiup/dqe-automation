*** Variables ***
@{CHROME_OPTS}    --headless    --no-sandbox    --disable-dev-shm-usage

*** Test Cases ***
Open Google Headless
    Open Browser    https://www.google.com    chrome    options=add_argument(${CHROME_OPTS}[0])    options=add_argument(${CHROME_OPTS}[1])    options=add_argument(${CHROME_OPTS}[2])
    [Teardown]    Close Browser
