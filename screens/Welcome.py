from utils.DriverHelper import DriverHelper


class Welcome(object):
    def __init__(self, driver):
        self.driver = driver

    @property
    def register_now(self):
        return self.driver.find_element_by_name('Register Now')

    def click_register_now(self):
        self.register_now.click()
        DriverHelper.switch_to_current_window(self.driver)

