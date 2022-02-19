from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

chromeOptions = webdriver.ChromeOptions()
chrome_driver = webdriver.Chrome(chrome_options=chromeOptions,executable_path="/home/ben/PycharmProjects/class8/web-and-automation/solution/chromedriver123")
chrome_driver.get('https://www.facebook.com')
chrome_driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input").send_keys("benben85@gmail.com")
chrome_driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input").send_keys("NotMyRealPassword")
chrome_driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input").send_keys(Keys.ENTER)

sleep(3)
chrome_driver.close()

