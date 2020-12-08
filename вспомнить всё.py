from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link = "https://box-test.labmedia.su/admin"

browser = webdriver.Chrome()
browser.get(link)

waiting = WebDriverWait(browser, 5).until (
    EC.visibility_of_element_located((By.ID, "site-name"))
) 

username = browser.find_element_by_name("username")
username.send_keys("mimic")

password = browser.find_element_by_name("password")
password.send_keys("hit#it#first")
time.sleep(2)

submit = browser.find_element_by_tag_name('[type = "submit"]')
submit.click()
