from utils.DriverHelper import DriverHelper
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class OnlineUpdate(object):
    def __init__(self, driver):
        self.driver = driver

    @property
    def next_btn(self):
        return self.driver.find_element_by_name('Next')

    @property
    def serial_number(self):
        return self.driver.find_element_by_accessibility_id('1080')

    @property
    def update_license_error(self):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, "//Text[contains(@Name, 'Update license failed!')]")))

    def click_next(self):
        self.next_btn.click()
        DriverHelper.switch_to_current_window(self.driver)

    def set_serial_number(self, s_num):
        self.serial_number.send_keys(s_num)

    def is_license_failed_error_displayed(self):
        return self.update_license_error.is_displayed()
