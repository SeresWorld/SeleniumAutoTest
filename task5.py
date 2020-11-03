from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element_by_id('book')

price = WebDriverWait(browser, 12).until (
    EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
)
button.click()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_id('input_value')
x = x_element.text
y = calc(x)

answer = browser.find_element_by_id('answer')
answer.send_keys(y)
browser.find_element_by_tag_name('[type = "submit"]').click()





