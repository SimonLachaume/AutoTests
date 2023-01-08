import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='C:\\Users\\ARUT\\PycharmProjects\\PyLesson\\chromedriver.exe')

base_url = 'https://www.saucedemo.com/'

driver.get(base_url)
driver.maximize_window()

login = 'standard_user'
invalid_login = 'user'


password = 'secret_sauce'

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login)  # ввод логина для авторизации

time.sleep(1)

user_password = driver.find_element(By.XPATH, "//input[@id='password']")
user_password.send_keys(password)   # ввод пароля для авторизации

time.sleep(1)

button_login = driver.find_element(By.XPATH, "//*[@id='login-button']")
button_login.click()    # клик на кнопку логина

time.sleep(1)

name_product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_name_product_1 = name_product_1.text  # сохраняем название первого товара
print(value_name_product_1)

name_product_2 = driver.find_element(By.XPATH, "//a[@id='item_0_title_link']")
value_name_product_2 = name_product_2.text  # сохраняем название второго товара товара
print(value_name_product_2)

button_product_1 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
button_product_1.click()    # выюор первого товара

button_product_2 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']")
button_product_2.click()    # выбор второго товара

time.sleep(1)

shopping_basket = driver.find_element(By.XPATH, "//div[@id='shopping_cart_container']")
shopping_basket.click() # переход в корзину

time.sleep(1)

checkout_button = driver.find_element(By.XPATH, "//button[@id='checkout']")
checkout_button.click() # нажатие на нопку чекаут

first_name_checkout = driver.find_element(By.XPATH, "//input[@id='first-name']")
first_name_checkout.send_keys('test first name')    # ввод имени

time.sleep(1)

last_name_checkout = driver.find_element(By.XPATH, "//input[@id='last-name']")
last_name_checkout.send_keys('test last name')  # ввод фамилии

time.sleep(1)

postal_code_checkout = driver.find_element(By.XPATH, "//input[@id='postal-code']")
postal_code_checkout.send_keys('test postal code')  # ввод индекса

time.sleep(1)

continue_button = driver.find_element(By.XPATH, "//input[@id='continue']")
continue_button.click() # нажатие на кнопку продолжения

time.sleep(1)

price_product_1 = driver.find_element(By.XPATH, "//div[@class='inventory_item_price']")
value_price_product_1 = price_product_1.text
value_price_product_1_without_dollar = value_price_product_1.replace("$", "")
print("Стоимость первого товара: " + value_price_product_1_without_dollar)  # сохраняем цену первого товара

price_product_2 = driver.find_elements(By.XPATH, "//div[@class='inventory_item_price']")[1]
value_price_product_2 = price_product_2.text
value_price_product_2_without_dollar = value_price_product_2.replace("$", "")
print("Стоимость второго товара: " + value_price_product_2_without_dollar)  # сохраняем цену второго товара

price_tax = driver.find_element(By.XPATH, "//div[@class='summary_tax_label']")
value_price_tax = price_tax.text
value_price_tax_without_dollar = value_price_tax.replace("Tax: $", "")
print("Сумма процента равна: " + value_price_tax_without_dollar)    # сохраняем процент

sum_with_procent = (float(value_price_product_1_without_dollar) + float(value_price_product_2_without_dollar) + float(value_price_tax_without_dollar))
print(sum_with_procent) # сохраняем общую сумму

total_price = driver.find_element(By.XPATH, "//div[@class='summary_total_label']")
value_total_price = total_price.text
value_total_price_without_dollar = value_total_price.replace("Total: $", "")
print(value_total_price_without_dollar)

assert float(sum_with_procent) == float(value_total_price_without_dollar)   # сравнием отдельно общую стоимость
print("Цена корректная")

finish_button = driver.find_element(By.XPATH, "//button[@id='finish']")
finish_button.click()   # завершаем флоу покупки товара

time.sleep(300)

