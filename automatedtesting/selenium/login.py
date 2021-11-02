# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By

# Start the browser and login with standard_user
def login (user, password):
    print ('Starting the browser...')
    # --uncomment when running in Azure DevOps.
    options = ChromeOptions()
    options.add_argument("--headless") 
    driver = webdriver.Chrome(options=options)
#     driver = webdriver.Chrome()
    print ('Browser started successfully. Navigating to the demo page to login.')
    driver.get('https://www.saucedemo.com/')
    
    driver.find_element(By.CSS_SELECTOR, "input[id='user-name']").send_keys(user)
    driver.find_element(By.CSS_SELECTOR, "input[id='password']").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

    print(" User " + user + " logged in successfully!")
    
    inventory_items = driver.find_elements(By.CLASS_NAME, "inventory_item")
    print("getting inventory items")
    print(inventory_items.length)

    if inventory_items:    
        for inventory_item in inventory_items:
            item_name = inventory_item.find_element(By.CLASS_NAME, "inventory_item_label").find_element(By.CLASS_NAME, "inventory_item_name").text
            print("Found Item Name: " + item_name)

            price_bar = inventory_item.find_element(By.CLASS_NAME, "pricebar")

            print("adding item " + item_name)
            add_to_cart = price_bar.find_element(By.CLASS_NAME, "btn_inventory").click()
            print("------")
        
        cart_badge = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
        print("Items in cart " + cart_badge)
        print("All items have been added")
        print("******")
        
        for inventory_item in inventory_items:
            item_name = inventory_item.find_element(By.CLASS_NAME, "inventory_item_label").find_element(By.CLASS_NAME, "inventory_item_name").text
            print("Found Item Name: " + item_name)

            price_bar = inventory_item.find_element(By.CLASS_NAME, "pricebar")

            print("removing item " + item_name)
            add_to_cart = price_bar.find_element(By.CLASS_NAME, "btn_inventory").click()
            print("------")
        
        cart_badge = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
        print("Items in cart " + cart_badge)
        print("All items have been removed")
        print("******")

login('standard_user', 'secret_sauce')

