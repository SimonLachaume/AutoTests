import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service

class Confirm_purchase():

    def __init__(self, driver):
        self.driver = driver

    def submit(self):

        coutry = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//select[@id='Select1']")))
        coutry.click()

        coutry.choose = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//option[@value='RU']")))
        coutry.choose.click()

        first_name = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='TextField1']")))
        first_name.send_keys("Test Name")

        last_name = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='TextField2']")))
        last_name.send_keys("Test Last Name")

        address = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='TextField6']")))
        address.send_keys("Test Address")

        appartament = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='TextField4']")))
        appartament.send_keys("Test City")

        city = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='TextField7']")))
        city.send_keys("Test City")

        action = ActionChains(self.driver)
        region = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//select[@id='Select3']")))
        action.move_to_element(region).click(region).perform()  # Курсор наводится на товар и кликает на него

        region_name = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//option[@value='AL']")))
        region_name.click()

        index = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='TextField8']")))
        index.send_keys("446460")

        phone = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='phone_field']")))
        phone.send_keys("123")

        submit = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        submit.click()














