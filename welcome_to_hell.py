from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = 'http://suninjuly.github.io/selects1.html'

browser = webdriver.Chrome()
browser.get(link)


x = browser.find_element_by_id('num1').text
y = browser.find_element_by_id('num2').text

def sum(x, y):
    return str(int(x) + int(y))

z = sum(x, y)

selection = Select(browser.find_element_by_id('dropdown'))
selection.select_by_value(z)

submit = browser.find_element_by_tag_name('[type = "submit"]')
submit.click()




