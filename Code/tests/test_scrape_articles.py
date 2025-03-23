from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.translate import translate_text
import time
import json
import requests
from locators.locators import ElPaisLocators

# Initialize WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 10)  # Create a wait object with 10 seconds timeout

# Visit El País Website
driver.get("https://elpais.com/america/")
wait.until(EC.presence_of_element_located((ElPaisLocators.MAIN_CONTENT)))
# print("Page loaded successfully")

# Retrieving the language of the website 
language_code = driver.execute_script("return window.ENP.siteProperties.languageCode;")
# print('The default language code is: ', language_code);
print('********************************************* LANGUAGE OF WEBSITE *************************************************************')
if language_code == 'es':
    print('The language of the page is Spanish')
else:
    print('The language of the page is not Spanish')
print('*******************************************************************************************************************************')

# Click on the Opinion section
# driver.find_element(By.XPATH, '//*[@id="csw"]/div[1]/nav/div/a[2]').click()
driver.get("https://elpais.com/opinion/")
time.sleep(5)
try:
    agreement_btn = wait.until(EC.presence_of_element_located((ElPaisLocators.AGREEMENT_BUTTON)))
    agreement_btn.click()
except Exception as e:
    print("No consent popup found or already accepted")
    # print(e)

# Checking the visibility of the opinion header
wait.until(EC.visibility_of_element_located((ElPaisLocators.OPINION_SECTION)))
# opinion_header = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="csw"]/div/div/h1/a')))
# opinion_header_txt = opinion_header.text
# print(opinion_header_txt)

# Create directory for storing articles
folder_name = "spanish article scraping"
img_folder_name = "article images"
headers_converted_folder_name = "headers converted"

if not os.path.exists(folder_name): 
    os.makedirs(folder_name)

if not os.path.exists(img_folder_name):
    os.makedirs(img_folder_name)

if not os.path.exists(headers_converted_folder_name):
    os.makedirs(headers_converted_folder_name)

# Retrieving the articles
article_1 = wait.until(EC.presence_of_element_located((ElPaisLocators.ARTICLE_1)))
article_1.click()
print('/n********************************************************** ARTICLE 1 **********************************************************')

article_1_heading = wait.until(EC.presence_of_element_located((ElPaisLocators.ARTICLE_1_HEADING)))
article_1_heading_txt = article_1_heading.text
print(article_1_heading_txt)

article_1_content = wait.until(EC.presence_of_element_located((ElPaisLocators.ARTICLE_1_CONTENT)))
article_1_content_txt = article_1_content.text
print(article_1_content_txt)

article_1_img = wait.until(EC.presence_of_element_located((ElPaisLocators.ARTICLE_1_IMAGE)))
img_url = article_1_img.get_attribute('src')
img_name = f"article_1_image.jpg"
response = requests.get(img_url)
if response.status_code == 200:
    with open(os.path.join(img_folder_name, img_name), 'wb') as f:
        f.write(response.content)

# After getting article 1 content
with open(os.path.join(folder_name, 'article_1.json'), 'w', encoding='utf-8') as f:
    json.dump({
        "heading": article_1_heading_txt,
        "content": article_1_content_txt
    }, f, ensure_ascii=False, indent=4)
print('*******************************************************************************************************************************')

# Going back to Opinion Page 
driver.back()

article_2 = wait.until(EC.presence_of_element_located((ElPaisLocators.ARTICLE_2)))
article_2.click()
print('********************************************************** ARTICLE 2 **********************************************************')

article_2_heading = wait.until(EC.presence_of_element_located((ElPaisLocators.ARTICLE_2_HEADING)))
article_2_heading_txt = article_2_heading.text
print(article_2_heading_txt)

article_2_content = wait.until(EC.presence_of_element_located((ElPaisLocators.ARTICLE_2_CONTENT)))
article_2_content_txt = article_2_content.text
print(article_2_content_txt)

article_2_img = wait.until(EC.presence_of_element_located((ElPaisLocators.ARTICLE_2_IMAGE)))
img_url = article_2_img.get_attribute('src')
img_name = f"article_2_image.jpg"
response = requests.get(img_url)
if response.status_code == 200:
    with open(os.path.join(img_folder_name, img_name), 'wb') as f:
        f.write(response.content)

# After getting article 2 content
with open(os.path.join(folder_name, 'article_2.json'), 'w', encoding='utf-8') as f:
    json.dump({
        "heading": article_2_heading_txt,
        "content": article_2_content_txt
    }, f, ensure_ascii=False, indent=4)
print('*******************************************************************************************************************************')

driver.back()

article_3 = wait.until(EC.presence_of_element_located((ElPaisLocators.ARTICLE_3)))
article_3.click()
print('********************************************************** ARTICLE 3 **********************************************************')

article_3_heading = wait.until(EC.presence_of_element_located((ElPaisLocators.ARTICLE_3_HEADING)))
article_3_heading_txt = article_3_heading.text
print(article_3_heading_txt)

article_3_content = wait.until(EC.presence_of_element_located((ElPaisLocators.ARTICLE_3_CONTENT)))
article_3_content_txt = article_3_content.text
print(article_3_content_txt)

article_3_img = wait.until(EC.presence_of_element_located((ElPaisLocators.ARTICLE_3_IMAGE)))
img_url = article_3_img.get_attribute('src')
img_name = f"article_3_image.jpg"
response = requests.get(img_url)
if response.status_code == 200:
    with open(os.path.join(img_folder_name, img_name), 'wb') as f:
        f.write(response.content)

# After getting article 3 content
with open(os.path.join(folder_name, 'article_3.json'), 'w', encoding='utf-8') as f:
    json.dump({
        "heading": article_3_heading_txt,
        "content": article_3_content_txt
    }, f, ensure_ascii=False, indent=4)
print('*******************************************************************************************************************************')

driver.back()

article_4 = wait.until(EC.presence_of_element_located((ElPaisLocators.ARTICLE_4)))
article_4.click()
print('********************************************************** ARTICLE 4 **********************************************************')

article_4_heading = wait.until(EC.presence_of_element_located((ElPaisLocators.ARTICLE_4_HEADING)))
article_4_heading_txt = article_4_heading.text
print(article_4_heading_txt)

article_4_content = wait.until(EC.presence_of_element_located((ElPaisLocators.ARTICLE_4_CONTENT)))
article_4_content_txt = article_4_content.text
print(article_4_content_txt)

article_4_img = wait.until(EC.presence_of_element_located((ElPaisLocators.ARTICLE_4_IMAGE)))
img_url = article_4_img.get_attribute('src')
img_name = f"article_4_image.jpg"
response = requests.get(img_url)
if response.status_code == 200:
    with open(os.path.join(img_folder_name, img_name), 'wb') as f:
        f.write(response.content)

# After getting article 4 content
with open(os.path.join(folder_name, 'article_4.json'), 'w', encoding='utf-8') as f:
    json.dump({
        "heading": article_4_heading_txt,
        "content": article_4_content_txt
    }, f, ensure_ascii=False, indent=4)
print('*******************************************************************************************************************************')

driver.back()

article_5 = wait.until(EC.presence_of_element_located((ElPaisLocators.ARTICLE_5)))
article_5.click()
print('********************************************************** ARTICLE 5 **********************************************************')

article_5_heading = wait.until(EC.presence_of_element_located((ElPaisLocators.ARTICLE_5_HEADING)))
article_5_heading_txt = article_5_heading.text
print(article_5_heading_txt)

article_5_content = wait.until(EC.presence_of_element_located((ElPaisLocators.ARTICLE_5_CONTENT)))
article_5_content_txt = article_5_content.text
print(article_5_content_txt)

article_5_img = wait.until(EC.presence_of_element_located((ElPaisLocators.ARTICLE_5_IMAGE)))
img_url = article_5_img.get_attribute('src')
img_name = f"article_5_image.jpg"
response = requests.get(img_url)
if response.status_code == 200:
    with open(os.path.join(img_folder_name, img_name), 'wb') as f:
        f.write(response.content)

# After getting article 5 content
with open(os.path.join(folder_name, 'article_5.json'), 'w', encoding='utf-8') as f:
    json.dump({
        "heading": article_5_heading_txt,
        "content": article_5_content_txt
    }, f, ensure_ascii=False, indent=4)
print('*******************************************************************************************************************************')

print('/n****************************************** WORD COUNT ***********************************************************************')

# Read all the articles 
for i in range(1, 6):
    with open(os.path.join(folder_name, f'article_{i}.json'), 'r', encoding='utf-8') as f:
        article_data = json.load(f)
    # print(article_data['heading'])
    translated_heading = translate_text(article_data['heading'])
    # print(translated_heading)
    with open(os.path.join(headers_converted_folder_name, f'article_{i}_heading_converted.json'), 'w', encoding='utf-8') as f:
        json.dump({
            "original_heading": article_data['heading'],
            "translated_heading": translated_heading,
        }, f, ensure_ascii=False, indent=4)

# Read all the articles and collect translated headers
translated_headers = []
for i in range(1, 6):
    with open(os.path.join(headers_converted_folder_name, f'article_{i}_heading_converted.json'), 'r', encoding='utf-8') as f:
        header_data = json.load(f)
        translated_headers.append(header_data['translated_heading'])

# Process words and count frequencies
word_frequency = {}
for header in translated_headers:
    # Convert to lowercase and split into words
    words = header.lower().split()
    # Remove common punctuation from words
    words = [word.strip('.,!?()[]{}":;') for word in words]
    # words_array = []
    # for word in words:
    #     tmp = word.strip('.,!?()[]{}":;')
    #     words_array.append(tmp)
    # words = tmparr
    
    # for word in words_array:
    for word in words:
        if word:  # Skip empty strings
            word_frequency[word] = word_frequency.get(word, 0) + 1

# Sort by frequency (most frequent first)
sorted_frequencies = dict(sorted(word_frequency.items(), key=lambda x: x[1], reverse=True))

# Save the word frequency analysis
with open('header_word_frequency.json', 'w', encoding='utf-8') as f:
    json.dump(sorted_frequencies, f, ensure_ascii=False, indent=4)

print("Word Frequency:")
for word, count in sorted_frequencies.items():
    print(f"{word}: {count}")

print('Words appearing more than twice:')
for word, count in sorted_frequencies.items():
    if count > 2:
        print(f"{word}: {count}")

print('*******************************************************************************************************************************')

# Close the browser
# driver.quit()
