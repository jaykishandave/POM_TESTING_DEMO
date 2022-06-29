from selenium.webdriver.common.by import By

from Config_data.config import TestData
from Pages.BasePage import BasePage


class LoginPage(BasePage):
    EMAIL = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "loginBtn")
    SIGNUP_LINK = (By.LINK_TEXT, "Sign up")

    def __init__(self, driver):
        print("\u001b[41m This is Login page file class \u001b[0m")
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def get_login_page_title(self, title):
        print("\u001b[44m This is page file, get_login_page_title method \u001b[0m")
        return self.get_title(title)

    def is_signup_link_exist(self):
        print("\u001b[44m This is page file, is_signup_link_exist method \u001b[0m")
        return self.is_visible(self.SIGNUP_LINK)

    def do_login(self, username, password):
        print("\u001b[44m This is page file, do_login method \u001b[0m")
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
