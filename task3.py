from selenium import webdriver
import time
import math

link = 'http://suninjuly.github.io/get_attribute.html'

browser = webdriver.Chrome()
browser.get(link)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_id('treasure')
x = x_element.get_attribute('valuex')
y = calc(x)

answer = browser.find_element_by_id('answer')
answer.send_keys(y)

for selector in [("robotCheckbox"), ("robotsRule")]:
    browser.find_element_by_id(selector).click()

submit = browser.find_element_by_tag_name('[type = "submit"]')
submit.click()





