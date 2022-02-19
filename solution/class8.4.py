from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

options = Options()
browser = webdriver.Firefox(options=options,executable_path="/home/ben/PycharmProjects/class8/web-and-automation/solution/geckodriver")
browser.get('https://translate.google.co.il/')
browser.find_element(by=By.XPATH, value="/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea").send_keys("שלום")

sleep(2)
browser.quit()