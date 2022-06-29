import pytest
from selenium import webdriver

from Config_data.config import TestData
from Pages.Login_page import LoginPage

web_driver = None


@pytest.fixture(params=["chrome"], scope="class")
def driver_init(request):
    print("\u001b[42m This is Conftest page \u001b[0m")
    print("\u001b[44m This is Conftest page,driver_init Method \u001b[0m")
    global web_driver

    if request.param == "chrome":
        web_driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)
    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=TestData.FIREFOX_EXECUTABLE_PATH)
    request.cls.driver = web_driver
    yield
    web_driver.close()


@pytest.fixture
def login_page_obj_fun(request):
    print("\u001b[44m This is Conftest page,login_page_obj_fun Method \u001b[0m")
    login_page = LoginPage(request.cls.driver)
    request.cls.login_page_obj = login_page
