import random
import string
import unittest
from appium import webdriver
from screens.SystemLogin import SystemLogin
from screens.Welcome import Welcome
from screens.OfflineUpdate import OffLineUpdate
from screens.OnlineUpdate import OnlineUpdate
from screens.LicenseInformation import LicenseInformation
from utils.WindowsSSHManager import WindowsSSHManager


class ClassRoomManagerTest(unittest.TestCase):

    def tearDown(self):
        self.driver.close()
        sshC = WindowsSSHManager('admin:Control123:10.31.18.10')
        sshC.execute("powershell -command Stop-Process -Name 'TeacherMain'")

    def setUp(self):
        desired_caps = dict()
        desired_caps["app"] = "C:\Program Files (x86)\Mythware\Classroom Management by Mythware\TeacherMain.exe"
        self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4723',
                                       desired_capabilities=desired_caps)
        self.driver.implicitly_wait(10)
        system_login = SystemLogin(self.driver)
        self.welcome = Welcome(self.driver)
        self.offline_update = OffLineUpdate(self.driver)
        self.online_update = OnlineUpdate(self.driver)
        self.license_inf = LicenseInformation(self.driver)
        system_login.set_password('Control123')
        system_login.click_login()

    def test_select_blank_ath_file(self):
        self.welcome.click_register_now()
        self.license_inf.click_offline_update()
        self.offline_update.click_browse()
        self.offline_update.click_file('auth.lic')
        self.offline_update.click_open()
        self.offline_update.click_next()
        self.assertTrue(self.offline_update.is_license_failed_error_displayed())

    def test_insert_path_file(self):
        self.welcome.click_register_now()
        self.license_inf.click_offline_update()
        self.offline_update.set_authorization_file_path('C:\\Users\\fernando\\Desktop\\pom.xml')
        self.offline_update.click_next()
        self.assertTrue(self.offline_update.is_license_failed_error_displayed())

    def test_register_online_update(self):
        self.welcome.click_register_now()
        self.license_inf.click_online_update()
        self.online_update.set_serial_number(''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10)))
        self.online_update.click_next()
        self.assertTrue(self.online_update.is_license_failed_error_displayed())


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ClassRoomManagerTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
