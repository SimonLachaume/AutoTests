import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service

# s = Service('C:\\Users\\ARUT\\PycharmProjects\\PyLesson\\files\\chromedriver.exe')
# driver = webdriver.Chrome(service=s)
#
# base_url = 'https://krakatauwear.com/'
# driver.get(base_url)
# driver.maximize_window()

class Merch():
    def __init__(self, driver):
        self.driver = driver

    def product_purchase(self):

        choose_merch = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//span[@class='header-nav-link-title МУЖСКОЕ']")))
        ActionChains(self.driver).move_to_element(choose_merch).perform()

        jackets = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='header-nav-link-title']")))
        jackets.click()

        filters = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//i[@class='las la-plus']")))
        filters.click()

        color = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//label[@for='color_1']")))
        color.click()

        size = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//label[@for='size_0']")))
        size.click()

        time.sleep(1)

        self.driver.execute_script("window.scrollTo(0, 1250)")

        action = ActionChains(self.driver)
        product = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='Двойная парка Qm375-1 PLANCK']")))
        action.move_to_element(product).click(product).perform()

        choose_size = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//label[@variant-availability='2']")))
        choose_size.click()

        add_to_shop = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='button button__funnel']")))
        add_to_shop.click()

        confirm_purchase = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='button button__wide button__funnel button__lg']")))
        confirm_purchase.click()



# test = Merch(driver)
# test.product_purchase()
#
# time.sleep(2000)