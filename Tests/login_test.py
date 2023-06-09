import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from selenium import webdriver
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global driver
        driver = webdriver.Chrome()
        driver.implicitly_wait(3)
        driver.maximize_window()

    def test_login(self):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        login_page.click_login()

        home_page = HomePage(driver)
        home_page.click_on_user_icon()
        home_page.click_logout_button()
        assert driver.title == 'OrangeHRM'

    @classmethod
    def tearDownClass(cls):
        driver.close()
        driver.quit()
        print("Test completed")

if __name__ == '__main__':
    unittest.main()