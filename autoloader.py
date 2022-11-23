#initial commit file

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("disable-infobars")
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(executable_path = "C:/Users/Andrew/Documents/selenium_driver/chromedriver.exe",chrome_options = chrome_options )

url = "https://createmycookbook.com/projects/VjM4tW5Ey?default_email=andrew_dau%40hotmail.com"

driver.get(url)


def fill_form(var1, var2, var3):
    recipe_name = driver.find_element("name", "name")
    #recipe_name = driver.find_element(By.CLASS_NAME, "form-control ng-pristine ng-valid")

    time.sleep(3)

    recipe_name.send_keys('Fake Recipe Name')

    recipe_name.submit()

    #print(inputs)

    #inputs[0].send_keys(var1)


fill_form('Andrew',2, 3)
