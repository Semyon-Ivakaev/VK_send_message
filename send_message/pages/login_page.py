from .base_page import BasePage
import time
import pytest
from selenium import webdriver
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def login_user(self, phone, password):
        phone_input = self.browser.find_element(*LoginPageLocators.PHONE).send_keys(phone)
        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD).send_keys(password)
        checkbox_click = self.browser.find_element(*LoginPageLocators.CHECKBOX).click()
        time.sleep(1)
        button_click = self.browser.find_element(*LoginPageLocators.BUTTON_LOGIN_IN).click()
        time.sleep(1)
