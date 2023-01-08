import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path='C:\\Users\\ARUT\\PycharmProjects\\PyLesson\\chromedriver.exe')

base_url = 'https://www.saucedemo.com/'

driver.get(base_url)
# driver.maximize_window()

login = ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user']
password = 'secret_sauce'
wait = WebDriverWait(driver, 5)

class authorization():
    def __init__(self):
        print("")

    def login (self, login, password):
        self.login = login
        self.password = password

        self.login = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='user-name']")))
        self.login.send_keys(login)

        self.password = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
        self.password.send_keys(password)

        button_login = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='login-button']")))
        button_login.click()

        title = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@class='title']")))
        value_title = title.text
        if value_title == "PRODUCTS":
            print(value_title)
            print("Пользователь на главной странице")
        else:
            print("Пользователь не авторизован")
            self.login.send_keys(Keys.BACKSPACE(len(self.login.send_keys(login))))
            self.password.send_keys(Keys.BACKSPACE(len(self.password.send_keys(password))))

        menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='react-burger-menu-btn']")))
        menu.click()

        logout = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@id='logout_sidebar_link']")))
        logout.click()

for i in login:
    auth = authorization()
    auth.login(i, password)

time.sleep(100)



