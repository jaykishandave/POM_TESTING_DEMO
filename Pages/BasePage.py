from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""This class is parent of all the pages"""
"""It contains all the generic methods and utilities for all the pages"""


class BasePage:

    def __init__(self, driver):
        print("\u001b[41m This is Base page class \u001b[0m")
        self.driver = driver

    def do_click(self, by_locator):
        print("\u001b[44m This is Base page do_click method \u001b[0m")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        print("\u001b[44m This is Base page do_send_keys method \u001b[0m")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        print("\u001b[44m This is Base page get_element_text method \u001b[0m")
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        element_text = element.text
        return element_text

    def is_visible(self, by_locator):
        print("\u001b[44m This is Base page is_visible method \u001b[0m")
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title):
        print("\u001b[44m This is Base page get_title method \u001b[0m")
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title
