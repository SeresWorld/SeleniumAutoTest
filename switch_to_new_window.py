from selenium import webdriver
import math

link = "http://suninjuly.github.io/redirect_accept.html"

browser = webdriver.Chrome()
browser.get(link)

browser.find_element_by_tag_name('[type = "submit"]').click()
first_window = browser.window_handles[1]
browser.switch_to.window(first_window)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_id('input_value')
x = x_element.text
y = calc(x)

answer = browser.find_element_by_id('answer')
answer.send_keys(y)

browser.find_element_by_tag_name('[type = "submit"]').click()