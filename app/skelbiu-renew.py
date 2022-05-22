#! /usr/bin/python3

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import os


options = Options()
options.headless = True
s = Service('./geckodriver')
driver = webdriver.Firefox(service=s, options=options)

USERNAME = os.environ.get('APP_USERNAME')
PASSWORD = os.environ.get('APP_PASSWORD')


def main():
    driver.get('https://www.skelbiu.lt/users/renew')
    driver.find_element(By.ID, 'nick-input').send_keys(USERNAME)
    driver.find_element(By.ID, 'password-input').send_keys(PASSWORD)
    login_button = driver.find_element(By.XPATH, '//*[@id="submit-button"]')
    driver.execute_script("arguments[0].click();", login_button)
    driver.implicitly_wait(1)
    renew_button = driver.find_element(By.XPATH, '//*[@id="default_page_content"]/form/button')
    driver.execute_script("arguments[0].click();", renew_button)
    
    
if __name__ == "__main__":
    main()
