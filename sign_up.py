import pytest
from selenium import webdriver 

link = "https://box-test.boxbattle.ru/game/"

@pytest.fixture(scope="class")
def test_begin():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
    

class TestSignUp1():
    def test_success_signup(self, test_begin):
        browser = webdriver.Chrome()
        browser.get(link)
        email = browser.find_element_by_name('email')
        email.send_keys('aga')
    
    def test_test(self, test_begin):
        browser = webdriver.Chrome()
        browser.get(link)
        email = browser.find_element_by_name('email')
        email.send_keys('aga')
        password = browser.find_element_by_name('password')
        password.send_keys('nu')
        browser.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[3]/div[1]/div/button').click()

