import time
import os
import pandas as pd
import csv

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class SeleniumWebDriverContextManager:
    def __init__(self):
        self.driver = None

    def __enter__(self):
        self.driver = webdriver.Chrome()
        return self.driver

    def __exit__(self, exc_type, exc_value, traceback):
        if self.driver:
            self.driver.quit()


if __name__ == "__main__":
    with SeleniumWebDriverContextManager() as driver:
        html_file_path = os.path.abspath("Documents/Learning/Automation/generated_report/report.html")
        driver.get(f"file://{html_file_path}")

        # get table content
        elements = driver.find_elements(By.CLASS_NAME, "y-column")

        columns = [element.text.splitlines() for element in elements]

        rows = list(zip(*columns))

        csv_file_path = "Documents/Learning/Automation/generated_report/table.csv"
        with open(csv_file_path, "w", newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            for row in rows:
                writer.writerow(row)




        # get charts screenshots
        chart_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "pielayer")))
        driver.save_screenshot("Documents/Learning/Automation/generated_report/initial_screenshot.png")
        
        elements = driver.find_elements(By.CLASS_NAME, "legendtoggle")
        i = 0

        for element in elements:
            time.sleep(1)
            element.click()

        for element in elements:
            time.sleep(1)
            if i > 0:
                elements[i-1].click()
            time.sleep(1)
            element.click()
            time.sleep(1)
            driver.save_screenshot(f"Documents/Learning/Automation/generated_report/screenshot{i}.png")

            csv_file_path = f"Documents/Learning/Automation/generated_report/doughnut{i}.csv"
            data = []
            with open(csv_file_path, "w", newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                chart_slice = driver.find_elements(By.CLASS_NAME, "slicetext")
                tspans = chart_slice[0].find_elements(By.TAG_NAME, 'tspan')
                text_lines = [tspan.text for tspan in tspans]
                data.append(text_lines)
                writer.writerow(data)

            i = i + 1


        input("Press Enter to close the browser...")
