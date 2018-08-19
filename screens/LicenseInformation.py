from utils.DriverHelper import DriverHelper


class LicenseInformation:
    def __init__(self, driver):
        self.driver = driver

    @property
    def offline_update(self):
        return self.driver.find_element_by_name('Offline Update')

    @property
    def online_update(self):
        return self.driver.find_element_by_name('Online Update')

    def click_offline_update(self):
        self.offline_update.click()
        DriverHelper.switch_to_current_window(self.driver)

    def click_online_update(self):
        self.online_update.click()
        DriverHelper.switch_to_current_window(self.driver)
