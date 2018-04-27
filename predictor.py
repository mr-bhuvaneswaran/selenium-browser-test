from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
# WebDriverWait(driver, 10).until(EC.title_contains("home"))

def site_login():
    driver.get ("http://www.camsmkce.in/")
    driver.find_element_by_id("user_username").send_keys("15bcs2015")
    driver.find_element_by_id ("user_password").send_keys("Baskaran1")
    driver.find_element_by_id("Button1").click()

site_login()

if __name__ == '__main__':
    site_login()