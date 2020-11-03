from selenium import webdriver
import math
import time

link = 'http://SunInJuly.github.io/execute_script.html'

browser = webdriver.Chrome()
browser.get(link)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_id('input_value')
x = x_element.text
y = calc(x)

submit = browser.find_element_by_tag_name('[type = "submit"]')

input_value = browser.find_element_by_id("input_value")
browser.execute_script("return arguments[0].scrollIntoView(true)", input_value)

answer = browser.find_element_by_id('answer')
answer.send_keys(y)

browser.find_element_by_id('robotCheckbox').click()
time.sleep(1)
browser.find_element_by_id('robotsRule').click()

submit.click()


