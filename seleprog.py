from selenium.webdriver import Chrome, ChromeOptions
import time

# from selenium import webdriver

# driver = webdriver.Chrome(r"C:/Users/michael/Downloads/chrome-win64/chrome-win64/chromedriver.exe")

x = ChromeOptions()
x.add_experimental_option("detach", True)
driver = Chrome(options=x)







