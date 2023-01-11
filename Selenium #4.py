import time
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys

webdriver = webdriver.Chrome(executable_path='C:\\Users\\ARUT\\PycharmProjects\\PyLesson\\chromedriver.exe')

base_url = 'https://www.saucedemo.com/'

webdriver.get(base_url)
# driver.maximize_window()

logins = ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user']
main_pass = 'secret_sauce'


class Authorization:
    def __init__(self, driver):
        self.driver = driver

    def login(self, login, password):
        wait = WebDriverWait(self.driver, 5)
        login_locator = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='user-name']")))
        login_locator.send_keys(login)

        password_locator = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
        password_locator.send_keys(password)

        button_login_locator = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='login-button']")))
        button_login_locator.click()
        try:
            title_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@class='title']")))
            value_title = title_locator.text
            print("Пользователь на главной странице", end='\n')

            menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='react-burger-menu-btn']")))
            menu.click()

            logout = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@id='logout_sidebar_link']")))
            logout.click()
        except TimeoutException:
            print("Пользователь не авторизован")
            error_button_locator = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='error-button']")))
            error_button_locator.click()
            login_locator.send_keys(Keys.BACKSPACE)
            password_locator.send_keys(Keys.BACKSPACE)


auth = Authorization(webdriver)

for i in logins:
    print("Пользователь : ", i)
    auth.login(i, main_pass)


time.sleep(50)


