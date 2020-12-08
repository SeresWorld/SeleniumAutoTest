import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"

#Создаём фикстуру для запуска браузера с названием browser, затем возвращаем значение этйо фикстуры в тест
@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    return browser

#В методах класса мы вызываем нашу фикстуру browser как параметр по типу (self, browser)
class TestMainPage1():
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")