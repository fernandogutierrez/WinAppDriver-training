class DriverHelper(object):

    @staticmethod
    def switch_to_current_window(driver):
        driver.switch_to.window(driver.window_handles[0])
