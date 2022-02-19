from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

chromeOptions = webdriver.ChromeOptions()
chrome_driver = webdriver.Chrome(chrome_options=chromeOptions,executable_path="/home/ben/PycharmProjects/class8/solution/chromedriver123")
chrome_driver.get('https://github.com')
chrome_driver.find_element(by=By.XPATH, value="/html/body/div[1]/header/div/div[2]/div[2]/div[1]/div/div/form/label/input[1]").send_keys("selenium")
chrome_driver.find_element(by=By.XPATH, value="/html/body/div[1]/header/div/div[2]/div[2]/div[1]/div/div/form/label/input[1]").send_keys(Keys.ENTER)

sleep(3)
chrome_driver.close()
