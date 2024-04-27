from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from typing import List
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.options import Options
import json

options = webdriver.ChromeOptions()
options.page_load_strategy = 'eager'
# options.add_experimental_option("detach", True) # --> Prevents browser window from closing
options.add_argument("--headless=new")  # --> Prevents browser window from opening
driver = webdriver.Chrome(options=options)

# Page will all the the products
driver.get("https://www.nccustom.com/brand/all?abpo=0")

# Grid with all the products
product_grid = driver.find_elements(By.CLASS_NAME, 'unit.col-xs-12.col-sm-4.col-md-3.txtC')
products = []
# product = {}
counter = 0
## Iterate through the product_grid and collect specific data with different variables
for items in product_grid:
    product = {}
    link = items.find_element(By.TAG_NAME, 'a')
    item = link.text.split('\n')
    product["code"] = item[0]
    product["name"] = item[1]
    product["prices"] = items.find_element(By.CLASS_NAME, 'heavy').text
    products.append(product)

## Output files
# JSON
with open('./data.json', 'w+') as json_file:
    json_data = json.dumps(products, indent=4)
    json_file.write(json_data)

# CSV
with open('./data.csv', 'w+') as data:
    data.writelines((str(i)+'\n' for i in products))



# driver.quit()