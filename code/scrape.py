import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import time

# To Configure Chrome options 
chrome_options = Options()
chrome_options.add_argument("--headless") 
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Set up WebDriver
driver_path = "D:\\chromedriver-win32\\chromedriver.exe"  
driver_service = Service(driver_path)
driver = webdriver.Chrome(service=driver_service, options=chrome_options)

url = "https://github.com/SUKHMAN-SINGH-1612/Data-Science-Projects/blob/main/Salary%20Prediction/Salary_Data_Based_country_and_race.csv?plain=1#L904"
driver.get(url)

try:
    textarea = driver.find_element(By.ID, "read-only-cursor-text-area")
    csv_content = textarea.get_attribute("value")

    from io import StringIO
    df = pd.read_csv(StringIO(csv_content))
    
    # Defined the relative path for our folder
    output_folder = os.path.join(os.getcwd(), 'data')
    output_file = os.path.join(output_folder, "salary_data.csv")
    
    # Save the DataFrame to CSV
    df.to_csv(output_file, index=False)
    print(f"Successfully scraped {len(df)} rows.")

except Exception as e:
    print("An error occurred:", e)

finally:
    driver.quit()
