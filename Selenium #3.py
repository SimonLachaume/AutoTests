import time
from selenium import webdriver
from selenium.webdriver.common.by import By

print("Приветствую тебя в нашем интернет магазине \n ")

print("Выбери один из следующих товаров и укажи его номер: 1 - Sauce Labs Backpack, 2 - Sauce Labs Bike Light, \
3 - Sauce Labs Bolt T-Shirt, 4 - Sauce Labs Fleece Jacket, 5 - Sauce Labs Onesie, 6 - Test.allTheThings() T-Shirt (Red)")

merchandise = {"1" : ["//button[@id='add-to-cart-sauce-labs-backpack']", "/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/a/div", "/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div" ],  \
               "2" : ["//button[@id='add-to-cart-sauce-labs-bike-light']", "/html/body/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/a/div", "/html/body/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/div" ],\
               "3" : ["//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']", "/html/body/div/div/div/div[2]/div/div/div/div[3]/div[2]/div[1]/a/div", "/html/body/div/div/div/div[2]/div/div/div/div[3]/div[2]/div[2]/div" ],\
               "4" : ["//button[@id='add-to-cart-sauce-labs-fleece-jacket']", "/html/body/div/div/div/div[2]/div/div/div/div[4]/div[2]/div[1]/a/div", "/html/body/div/div/div/div[2]/div/div/div/div[4]/div[2]/div[2]/div" ],\
               "5" : ["//button[@id='add-to-cart-sauce-labs-onesie']", "/html/body/div/div/div/div[2]/div/div/div/div[5]/div[2]/div[1]/a/div", "/html/body/div/div/div/div[2]/div/div/div/div[5]/div[2]/div[2]/div" ],\
               "6" : ["//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']", "/html/body/div/div/div/div[2]/div/div/div/div[6]/div[2]/div[1]/a/div", "/html/body/div/div/div/div[2]/div/div/div/div[6]/div[2]/div[2]/div" ],}

def error_handler():
    try:
        global user_choice
        user_choice = merchandise[input()]


    except KeyError as ex:
        print("Вы не выбрали товар! Выберете товар, указав его номер: ")
        error_handler()

error_handler()

add_to_cart_locator = user_choice[0]
title_product_locator = user_choice[1]
prie_product_locator = user_choice[2]

driver = webdriver.Chrome(executable_path='C:\\Users\\ARUT\\PycharmProjects\\PyLesson\\chromedriver.exe')

base_url = 'https://www.saucedemo.com/'

driver.get(base_url)
driver.maximize_window()

login = 'standard_user'
password = 'secret_sauce'

class authorization():
    def __init__(self):
        print("Авторизаци пользователя \n")

    def login (self, login, password):
        self.login = login
        self.password = password

        time.sleep(1)

        self.login = driver.find_element(By.XPATH, "//input[@id='user-name']")
        self.login.send_keys(login)

        time.sleep(1)

        self.password = driver.find_element(By.XPATH, "//input[@id='password']")
        self.password.send_keys(password)

        time.sleep(1)

        button_login = driver.find_element(By.XPATH, "//*[@id='login-button']")
        button_login.click()

class merch():
    def __init__(self):
        print("Выбор товара \n")

    def product_purchase (self, add_to_cart_locator, title_product_locator, prie_product_locator):
        add_merch = driver.find_element(By.XPATH, add_to_cart_locator)
        add_merch.click()

        time.sleep(1)

        title_product = driver.find_element(By.XPATH, title_product_locator)
        value_title_product = title_product.text
        print(value_title_product)

        price_product = driver.find_element(By.XPATH, prie_product_locator)
        value_price_product = price_product.text
        value_price_product_without_dollar = value_price_product.replace("$", "")
        print("Стоимость товара: " + value_price_product_without_dollar)

        shopping_basket = driver.find_element(By.XPATH, "//div[@id='shopping_cart_container']")
        shopping_basket.click()

        time.sleep(1)

        checkout = driver.find_element(By.XPATH, "//button[@id='checkout']")
        checkout.click()

        time.sleep(1)

        first_name_checkout = driver.find_element(By.XPATH, "//input[@id='first-name']")
        first_name_checkout.send_keys('Test First Name')

        time.sleep(1)

        last_name_checkout = driver.find_element(By.XPATH, "//input[@id='last-name']")
        last_name_checkout.send_keys('Test Last Name')

        time.sleep(1)

        postal_code_checkout = driver.find_element(By.XPATH, "//input[@id='postal-code']")
        postal_code_checkout.send_keys('Test Code 123')

        continue_btn = driver.find_element(By.XPATH, "//input[@id='continue']")
        continue_btn.click()

        price_tax = driver.find_element(By.XPATH, "//div[@class='summary_tax_label']")
        value_price_tax = price_tax.text
        value_price_tax_without_dollar = value_price_tax.replace("Tax: $", "")
        print("Сумма процента равна: " + value_price_tax_without_dollar)

        sum_with_procent = (float(value_price_product_without_dollar) + float(value_price_tax_without_dollar))
        print("Общая стоимость продукта равна: " + str(sum_with_procent))

        total_price = driver.find_element(By.XPATH, "//div[@class='summary_total_label']")
        value_total_price = total_price.text
        value_total_price_without_dollar = value_total_price.replace("Total: $", "")
        print(value_total_price_without_dollar)

        try:
            assert float(sum_with_procent) == float(value_total_price_without_dollar)  # сравнием, отдельно, общую стоимость
            print("Цена корректная")
        except AssertionError:
            print("Некорректная цена")

        time.sleep(1)

        finish = driver.find_element(By.XPATH, "//button[@id='finish']")
        finish.click()



auth = authorization()
auth.login(login, password)

sauce_labs = merch()
sauce_labs.product_purchase(add_to_cart_locator, title_product_locator, prie_product_locator)

time.sleep(500)





