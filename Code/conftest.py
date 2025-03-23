# conftest.py
import logging
from selenium import webdriver
from utils.helpers import Utils
# from functions.login_page import LoginPage 
import os
import pytest

config = Utils.load_config()
link = config['host_name']['host']

# Create necessary directories under Tests
base_test_dir = os.path.dirname(__file__)
download_folder_path = os.path.join(base_test_dir, 'Tests', 'Download')

for folder_path in download_folder_path:
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": os.path.abspath(download_folder_path),
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
}
options.add_experimental_option("prefs", prefs)

@pytest.fixture(scope="module")
def driver():
    # setup
    driver = webdriver.Chrome(options=options)
    # teardown
    yield driver
    driver.quit()

# @pytest.fixture(scope="module")

# def login(driver):
#     # Create a logger for the login process
#     log = Utils.custom_logger(logLevel=logging.INFO, log_file_name="LoginPage.log")
#     login_page = LoginPage(driver, log)
#     login_page.load(link)
#     login_page.handle_error_page()
#     login_page.login(username, password)
#     yield driver

# def pytest_configure(config):
#     # Get the current working directory
#     cwd = os.getcwd()

#     report_dir = os.path.join(cwd, 'tests', 'Report')
#     report_file = os.path.join(report_dir, 'report.html')

#     # Set the report path in the pytest config
#     config.option.htmlpath = report_file
