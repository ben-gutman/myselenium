from selenium import webdriver

chromeOptions = webdriver.ChromeOptions()
chrome_driver = webdriver.Chrome(chrome_options=chromeOptions,executable_path="/home/ben/PycharmProjects/class8/web-and-automation/solution/chromedriver123")
chrome_driver.get('https://www.facebook.com')
chrome_driver.delete_all_cookies()
chrome_cookie = chrome_driver.get_cookies()
print(chrome_cookie)

chrome_driver.close()