from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

chromeOptions = webdriver.ChromeOptions()
chrome_driver = webdriver.Chrome(chrome_options=chromeOptions,executable_path="/home/ben/PycharmProjects/class8/web-and-automation/solution/chromedriver123")
chrome_driver.get('https://www.youtube.com')
chrome_driver.find_element(by=By.XPATH, value="/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input").send_keys("rap god eminem")
chrome_driver.find_element(by=By.XPATH, value="/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input").send_keys(Keys.ENTER)


chrome_driver.close()
