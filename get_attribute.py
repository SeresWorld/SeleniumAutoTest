from selenium import webdriver
import time

link = 'http://suninjuly.github.io/math.html'

browser = webdriver.Chrome()
browser.get(link)

# Находим объект radiobutton по id
people_rule = browser.find_element_by_id('robotsRule')
# Получаем аттрибут от нашего объекта
people_checked = people_rule.get_attribute('checked')
# Проверяем, что значение checked == "true", иначе пишем текст
assert people_checked == "true", "People radio isn't selected by default"


time.sleep(2)

browser.quit()

