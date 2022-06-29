import pytest

from Config_data.config import TestData
from Pages.Login_page import *
from Tests.test_Base import BaseTest


class TestLogin(BaseTest):
    print("\u001b[41m This is Test class \u001b[0m")
    pass

    @pytest.mark.usefixtures("login_page_obj_fun")
    def test_sign_link_visible(self):
        print("\u001b[44m This is Test_login page, test_sign_link_visible method \u001b[0m")
        flag = self.login_page_obj.is_signup_link_exist()
        assert flag

    @pytest.mark.usefixtures("login_page_obj_fun")
    def test_login_page_title(self):
        print("\u001b[44m This is Test_login, test_login_page_title method \u001b[0m")
        title = self.login_page_obj.get_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE

    @pytest.mark.usefixtures("login_page_obj_fun")
    def test_login(self):
        print("\u001b[44m This is Test_login, test_login method \u001b[0m")
        self.login_page_obj.do_login(TestData.USERNAME, TestData.PASSWORD)
