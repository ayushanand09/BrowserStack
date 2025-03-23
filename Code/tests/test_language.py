from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 10)  # Create a wait object with 10 seconds timeout

# Visit El País
driver.get("https://elpais.com/america/")
wait.until(EC.presence_of_element_located((By.ID, "main-content")))
print("Page loaded successfully")

language_code = driver.execute_script("return window.ENP.siteProperties.languageCode;")
# print('The default language code is: ', language_code);

if language_code == 'es':
    print('The language of the page is Spanish')
else:
    print('The language of the page is not Spanish')
