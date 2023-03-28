import time

from selenium.webdriver.common.by import By


class HomePage():

    def __init__(self, driver):
        self.driver = driver

    def click_on_user_icon(self):
        self.driver.find_element(By.CSS_SELECTOR, ".oxd-userdropdown-tab").click()
        time.sleep(2)

    def click_logout_button(self):
        self.driver.find_element(By.LINK_TEXT, "Logout").click()
        time.sleep(2)