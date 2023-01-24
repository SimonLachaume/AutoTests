import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service

class Merch():
    def __init__(self, driver):
        self.driver = driver

    def product_purchase(self):

        choose_merch = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//span[@class='header-nav-link-title МУЖСКОЕ']")))
        ActionChains(self.driver).move_to_element(choose_merch).perform()   # Перевод курсора на нав. баг с категорией "МУЖСКОЕ"

        jackets = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='header-nav-link-title']")))
        jackets.click() #Нажатие на категорию "Куртки"

        filters = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//i[@class='las la-plus']")))
        filters.click() #Нажатие на кнопку "Фильтры"

        color = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//label[@for='color_1']")))
        color.click()   #Выбор цвета

        size = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//label[@for='size_0']")))
        size.click()    #Выбор размера

        time.sleep(1)

        self.driver.execute_script("window.scrollTo(0, 1250)") #Скролл на товар

        action = ActionChains(self.driver)
        product = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='Двойная парка Qm375-1 PLANCK']")))
        action.move_to_element(product).click(product).perform() #Курсор наводится на товар и кликает на него

        name_locator = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//h1[@class='page-row-heading']")))
        value_name_locator = name_locator.text
        print(value_name_locator)

        price_locator = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//span[@class='product-price']")))
        value_price_locator = price_locator.text
        value_price_locator_without_mark = value_price_locator.replace(" ₽", "").replace(",", "").replace(" ", "")
        print(value_price_locator_without_mark)

        choose_size = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//label[@variant-availability='2']")))
        choose_size.click() #Выбор размера

        add_to_shop = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='button button__funnel']")))
        add_to_shop.click() #добавление товара на в корзину

        confirm_purchase = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='button button__wide button__funnel button__lg']")))
        confirm_purchase.click() #подтверждение покупки

        submit = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='button button__funnel button__wide button__lg']")))
        submit.click()

        submit_name_locator = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//p[@class='_1x52f9s1 _1fragemd5 _1x52f9sn _1fragem1t _1x52f9s3 _1x52f9sh']")))
        value_submit_name_locator = submit_name_locator.text
        print(value_submit_name_locator)

        submit_price_locator = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//span[@class='_19gi7yt0 _19gi7ytg _1fragem1t _19gi7yt2 _19gi7yt9 notranslate']")))
        value_submit_price_locator = submit_price_locator.text
        value_submit_price_locator_without_mark = value_submit_price_locator.replace(" ₽", "").replace(" ", "").replace(",", "")
        print(value_submit_price_locator_without_mark)

        try:
            assert float(value_price_locator_without_mark) == float(value_submit_price_locator_without_mark)  # сравнием стоимость
            print("Цена корректная")
            assert value_name_locator == submit_name_locator #сравниваем название
            print("Названия совпадают")
        except AssertionError:
            print("Некорректная цена")