from selenium.webdriver.common.by import By


class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    def open_login_page(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

    def enter_username(self, username):
        self.driver.find_element(By.CSS_SELECTOR, "input[name='username']").clear()
        self.driver.find_element(By.CSS_SELECTOR, "input[name='username']").send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.CSS_SELECTOR, "input[name='password']").clear()
        self.driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys(password)

    def click_login(self):
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()