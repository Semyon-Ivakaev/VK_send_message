import time
import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.base_page import BasePage

class TestUser:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "https://vk.com/"
        login_page = LoginPage(browser, link)
        login_page.open()
        phone = 'login'
        password = "pass"
        login_page.login_user(phone, password)


    def test_user_attack(self, browser):
        link = "https://vk.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_message_page()
        time.sleep(1)
        page.go_to_dialog()
        time.sleep(1)
        message1 = "1"
        page.message(message1)
        time.sleep(1)
