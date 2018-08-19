from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class OffLineUpdate(object):
    def __init__(self, driver):
        self.driver = driver

    @property
    def browse(self):
        return self.driver.find_element_by_name('Browse...')

    @property
    def open(self):
        return self.driver.find_element_by_name('Open')

    @property
    def next_btn(self):
        return self.driver.find_element_by_name('Next')

    @property
    def update_license_error(self):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, "//Text[contains(@Name, 'Update license failed!')]")))

    @property
    def select_auth_file(self):
        return self.driver.find_element_by_accessibility_id('1077')

    def click_browse(self):
        self.browse.click()

    def click_open(self):
        self.open.send_keys(Keys.ENTER)

    def click_next(self):
        self.next_btn.click()

    def is_license_failed_error_displayed(self):
        return self.update_license_error.is_displayed()

    def click_file(self, f_name):
        self.driver.find_element_by_name(f_name).click()

    def set_authorization_file_path(self, path):
        self.select_auth_file.click()
        action = ActionChains(self.driver)
        action.send_keys(path).perform()
