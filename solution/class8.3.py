from selenium import webdriver

from selenium.webdriver.firefox.options import Options


options = Options()
browser1 = webdriver.Firefox(options=options,executable_path="/home/ben/PycharmProjects/class8/web-and-automation/solution/geckodriver")
browser1.get('https://www.google.com')



browser2 = webdriver.Firefox(options=options,executable_path="/home/ben/PycharmProjects/class8/web-and-automation/solution/geckodriver")
browser2.get('https://www.google.com')


browser3 = webdriver.Firefox(options=options,executable_path="/home/ben/PycharmProjects/class8/web-and-automation/solution/geckodriver")
browser3.get('https://www.google.com')


browser4 = webdriver.Firefox(options=options,executable_path="/home/ben/PycharmProjects/class8/web-and-automation/solution/geckodriver")
browser4.get('https://www.google.com')

#-----------------------------------------------------------------------------------
#Yes they have the same locators.
#----------------------------------------------------------------------------------

browser1.close()
browser2.close()
browser3.close()
browser4.close()