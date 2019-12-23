from selenium.webdriver.common.by import By

class BasePageLocators():
    message_button = (By.CSS_SELECTOR, "#l_msg .left_label.inl_bl")

class LoginPageLocators():
    PHONE = (By.ID, "index_email")
    PASSWORD = (By.ID, "index_pass")
    CHECKBOX = (By.ID, "index_expire")
    BUTTON_LOGIN_IN = (By.ID, "index_login_button")

class MessagePageLocators():
    KUCH = (By.XPATH, "//span[contains(text(), 'Напиши Мне')]")

class DialogPageLocators():
    SQUADE = (By.ID, "im_editable0")
    #BUTTON_SEND = (By.CSS_SELECTOR, "im-chat-input--txt-wrap._im_text_wrap button:nth-child(6)")
    CAPTCHA = (By.XPATH, "//div[contains(text(), 'Подтверждение действия')]")
    CHECKBOX_CAPTCHA = (By.CLASS_NAME, "recaptcha-checkbox-borderAnimation")
