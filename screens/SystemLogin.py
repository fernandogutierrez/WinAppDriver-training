from selenium.webdriver.common.action_chains import ActionChains
from utils.DriverHelper import DriverHelper


class SystemLogin:
    def __init__(self, driver):
        self.driver = driver

    @property
    def password(self):
        return self.driver.find_element_by_name('Login password:')

    @property
    def login(self):
        return self.driver.find_element_by_name('Login')

    def set_password(self, password):
        self.password.click()
        action = ActionChains(self.driver)
        action.send_keys(password).perform()

    def click_login(self):
        self.login.click()
        DriverHelper.switch_to_current_window(self.driver)
