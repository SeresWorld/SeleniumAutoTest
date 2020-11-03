from selenium import webdriver
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

link = "https://dropmefiles.com/"

browser = webdriver.Chrome()
browser.get(link)

current_dir = os.path.abspath(os.path.abspath(''))
file_path = os.path.join(current_dir, 'new.txt')
addfile = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "logo")))
addfile.send_keys(file_path)