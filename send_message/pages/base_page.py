from .locators import BasePageLocators
from .locators import MessagePageLocators
from .locators import DialogPageLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pytest

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        #self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)


    def go_to_message_page(self):
        click_message = self.browser.find_element(*BasePageLocators.message_button).click()

    def go_to_dialog(self):
        click_dialog = self.browser.find_element(*MessagePageLocators.KUCH).click()

    def message(self, message):
        time.sleep(3)
        for i in range(10):
            try:
                squade = self.browser.find_element(*DialogPageLocators.SQUADE).send_keys(message)
                self.browser.find_element(*DialogPageLocators.SQUADE).send_keys(Keys.ENTER)
                time.sleep(1)
                #self.browser.find_element_by_xpath("//div[contains(text(), 'Подтверждение действия')]")
                #self.browser.find_element(*DialogPageLocators.CHECKBOX_CAPTCHA).click()
            except NoSuchElementException:
               
                continue

    def find_captcha(self):
        assert self.browser.is_element_present(*DialogPageLocators.CAPTCHA), "Captcha not found"
    
