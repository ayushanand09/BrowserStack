from selenium import webdriver
from selenium.webdriver.common.by import By

class ElPaisLocators:
    MAIN_CONTENT = (By.ID, 'main-content')
    # MAIN_CONTENT = (By.XPATH, '//*[@id="main-content"]')
    AGREEMENT_BUTTON = (By.XPATH, '//*[@id="didomi-notice-agree-button"]')
    
    OPINION_SECTION = (By.XPATH, '//*[@id="csw"]/div/div/h1/a')
    
    ARTICLE_1 = (By.XPATH, '//*[@id="main-content"]/div[1]/section[1]/div[1]/article[1]/header/h2/a')
    ARTICLE_1_HEADING = (By.XPATH, '//*[@id="main-content"]/header/div[1]/h1')
    ARTICLE_1_CONTENT = (By.XPATH, '//*[@id="main-content"]/div[2]')
    ARTICLE_1_IMAGE = (By.XPATH, '//*[@id="main-content"]/header/div[2]/figure/span/img')
    
    ARTICLE_2 = (By.XPATH, '//*[@id="main-content"]/div[1]/section[1]/div[1]/article[2]/header/h2/a')
    ARTICLE_2_HEADING = (By.XPATH, '//*[@id="main-content"]/header/div[1]/h1')
    ARTICLE_2_CONTENT = (By.XPATH, '//*[@id="main-content"]/div[2]')
    ARTICLE_2_IMAGE = (By.XPATH, '//*[@id="main-content"]/header/div[2]/figure/span/img')
    
    ARTICLE_3 = (By.XPATH, '//*[@id="main-content"]/div[1]/section[1]/div[1]/article[3]/header/h2/a')
    ARTICLE_3_HEADING = (By.XPATH, '//*[@id="main-content"]/header/div[1]/h1')
    ARTICLE_3_CONTENT = (By.XPATH, '//*[@id="main-content"]/div[2]')
    ARTICLE_3_IMAGE = (By.XPATH, '//*[@id="main-content"]/header/div[2]/figure/span/img')
    
    ARTICLE_4 = (By.XPATH, '//*[@id="main-content"]/div[1]/section[1]/div[2]/article/header/h2/a')
    ARTICLE_4_HEADING = (By.XPATH, '//*[@id="main-content"]/header/div[1]/h1')
    ARTICLE_4_CONTENT = (By.XPATH, '//*[@id="main-content"]/div[2]')
    ARTICLE_4_IMAGE = (By.XPATH, '//*[@id="main-content"]/header/div[2]/figure/span/img')
    
    ARTICLE_5 = (By.XPATH, '//*[@id="main-content"]/div[1]/section[1]/div[4]/div/article[5]/header/h2/a')
    ARTICLE_5_HEADING = (By.XPATH, '//*[@id="main-content"]/header/div[1]/h1')
    ARTICLE_5_CONTENT = (By.XPATH, '//*[@id="main-content"]/div[2]')
    ARTICLE_5_IMAGE = (By.XPATH, '//*[@id="main-content"]/header/div[2]/figure/span/img')
    
    

    