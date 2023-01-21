import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service

class Login_page():
    def __init__(self, driver):
        self.driver = driver

    def authorization(self, login_mail, login_pass):

        print("Инициализация авторизации")

        user_profile = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//i[@class='la la-user']")))
        user_profile.click()

        email = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='CustomerEmail']")))
        email.send_keys(login_mail)

        time.sleep(1)

        password = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='CustomerPassword']")))
        password.send_keys(login_pass)

        time.sleep(1)

        login_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='button button__primary']")))
        login_button.click()

        time.sleep(1)

        go_to_catalog = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='translation-error']")))
        go_to_catalog.click()
