from pages.login_page import Login_page
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import time
from pages.merchandise_page import Merch
from pages.confirm_purchase_page import Confirm_purchase

s = Service('C:\\Users\\ARUT\\PycharmProjects\\PyLesson\\files\\chromedriver.exe')
driver = webdriver.Chrome(service=s)

base_url = 'https://krakatauwear.com/'
driver.get(base_url)
driver.maximize_window()

login_mail = 'test86527@gmail.com'

login_pass = '741258963qQ'


login = Login_page(driver)
login.authorization(login_mail, login_pass)

buy_product = Merch(driver)
buy_product.product_purchase()

confrim_purchase = Confirm_purchase(driver)
confrim_purchase.submit()

time.sleep(500)

