#autoloader.py
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv as csv 
import pandas as pd

#in order to get the selenium chrome driver to work, you must download it.
#more info can be found at the following sites:
#https://pypi.org/project/selenium/
#https://chromedriver.chromium.org/downloads
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("disable-infobars")
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(executable_path = "C:/Users/Andrew/Documents/selenium_driver/chromedriver.exe",chrome_options = chrome_options )

url = "https://createmycookbook.com/projects/VjM4tW5Ey?default_email=andrewdau21%40yahoo.com"

#here is where I read in the data I want to use to build the cookbook.
filename = 'Recipe Builder.csv'
df = pd.read_csv(filename)


driver.get(url)

#I used two functions to control this program.  First a login, second the actual form filler.
def login_form(userid, pwd):
     #this login screen comes as a popup, so I use handles to figure out where I am
     main = driver.current_window_handle
     driver.find_element("xpath", "//*[text()='Login Here']").click()
     
     time.sleep(3)
     popup = driver.window_handles
     driver.switch_to.window(popup[1])
     #login and password are passed to the function when called below
     login = driver.find_element("id", "email_address")
     password = driver.find_element("name", "password")
     

     login.send_keys(userid)
     password.send_keys(pwd)

     driver.find_element("name", "commit").click()

     driver.switch_to.window(popup[0])
     #here is the call to the function that fills the form.  I used several delays to allow the site to load.
     time.sleep(5)
     for x in (range(len(df.index))):
        fill_form(df['Recipe Name'][x],df['Number of Servings (approximate)'][x], df['Ingredients'][x], df['Directions'][x], df['Cooking Time (Total cooking time, add more details in the instructions below)'][x], df['Dish Type'][x], df['Your Name'][x])
        time.sleep(6)



     


#find the elements, then fill them.  The hard part here was just figuring out the object names.
def fill_form(var1, var2, var3, var4, var5, var6, var7):
    print(driver.current_window_handle)
    recipe_name = driver.find_element("name", "name")
    recipe_yields = driver.find_element("id","recipe_yields")
    recipe_ingredients = driver.find_element("id","recipe_ingredients")
    recipe_directions = driver.find_element("id","recipe_directions")
    recipe_notes= driver.find_element("id","recipe_notes")
    recipe_category= driver.find_element("id","recipe_category")
    #recipe_author= driver.find_element("id","recipe_original_author")
    #contributor_first_name= driver.find_element("id","contributor_first_name")
    #contributor_last_name= driver.find_element("id","contributor_last_name")
    
    
    time.sleep(3)

    recipe_name.send_keys(var1)
    recipe_yields.send_keys(var2)
    recipe_ingredients.send_keys(var3)
    recipe_directions.send_keys(var4)
    recipe_notes.send_keys(var5)
    recipe_category.send_keys(var6)
    
    driver.find_element("xpath", "//*[text()='Contribute Recipe']").click()

    time.sleep(5)

    driver.find_element("xpath", "//*[text()='Submit New Recipe']").click()

    
    
    



login_form('aaa@yahoo.com', 'aaa')
