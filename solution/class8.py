from time import sleep

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

chromeOptions = webdriver.ChromeOptions()
chrome_driver = webdriver.Chrome(chrome_options=chromeOptions,executable_path="/home/ben/PycharmProjects/class8/solution/chromedriver123")

chrome_driver.get('https://www.walla.co.il')
site_title1 = chrome_driver.title
chrome_driver.refresh()
site_title2 = chrome_driver.title
if site_title1 == site_title2:
    print("Same Title")
else:
    print("Not the same Title")
sleep(1)
chrome_driver.close()

options = Options()
browser = webdriver.Firefox(options=options,executable_path="/home/ben/PycharmProjects/class8/solution/geckodriver")
browser.get('https://ynet.co.il')
sleep(1)
browser.close()
