from selenium.webdriver import Chrome, ChromeOptions
import time

o = ChromeOptions()
o.add_experimental_option("detach", True)

driver = Chrome(options=o)
driver.get('https://www.flipkart.com/')

x = driver.title
print(x)

x1 = driver.page_source
print(x1)

