#initial commit file

from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("disable-infobars")
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(executable_path = "C:/Users/Andrew/Documents/selenium_driver/chromedriver.exe",chrome_options = chrome_options )

url = "https://createmycookbook.com/projects/VjM4tW5Ey?default_email=andrew_dau%40hotmail.com"

driver.get(url)