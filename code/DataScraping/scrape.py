
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

# Set up Selenium WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (optional)
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver_path = "D:\\chromedriver-win32\\chromedriver.exe"  # Replace with your ChromeDriver path
driver_service = Service(driver_path)
driver = webdriver.Chrome(service=driver_service, options=chrome_options)


# Open the webpage
url = "https://github.com/SUKHMAN-SINGH-1612/Data-Science-Projects/blob/main/Salary%20Prediction/Salary_Data_Based_country_and_race.csv"  # Replace with the URL of the webpage
driver.get(url)

try:
    # Locate the table by its attributes
    table = driver.find_element(By.XPATH, '//*[@id="highlighted-line-menu-positioner"]/div[1]/table')

    # Extract table headers
    headers = [header.text for header in table.find_elements(By.XPATH, './/thead//th')]

    # Extract table rows inside tbody
    rows = table.find_elements(By.XPATH, './/tbody//tr')
    data = []
    for row in rows:
        cells = row.find_elements(By.XPATH, './/td')
        data.append([cell.text for cell in cells])

    # Save to a CSV file using pandas
    df = pd.DataFrame(data, columns=headers)
    df.to_csv("output.csv", index=False)
    print("Data has been successfully saved to output.csv")

except Exception as e:
    print("An error occurred:", e)

finally:
    # Close the browser
    driver.quit()
