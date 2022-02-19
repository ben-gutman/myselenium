from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By

chromeOptions = webdriver.ChromeOptions()
chrome_driver = webdriver.Chrome(chrome_options=chromeOptions,executable_path="/home/ben/PycharmProjects/class8/solution/chromedriver123")
chrome_driver.get('https://translate.google.com')
locat1 = chrome_driver.find_element(by=By.XPATH, value="/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea").text
print (locat1)

#locat2 = chrome_driver.find_element(By.CSS_SELECTOR == '#yDmH0d > c-wiz > div > div.WFnNle > c-wiz > div.OlSOob > c-wiz > div.ccvoYb > div.AxqVh > div.OPPzxe > c-wiz.rm1UF.UnxENd.dHeVVb > span > span > div > textarea')
chrome_driver.close()