# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By

def manage_cart (inventory_items, action):

    if action == "Add":
        print("Adding items to cart")
    else: 
        print("Removing items from cart")

    for inventory_item in inventory_items:
        item_name = inventory_item.find_element(By.CLASS_NAME, "inventory_item_label").find_element(By.CLASS_NAME, "inventory_item_name").text

        price_bar = inventory_item.find_element(By.CLASS_NAME, "pricebar")

        print("    " + item_name)
        price_bar.find_element(By.CLASS_NAME, "btn_inventory").click()
	
	
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

    driver.find_element(By.ID, "user-name").send_keys(user)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

    print(user + " logged in successfully!")

    inventory_items = driver.find_elements(By.CLASS_NAME, "inventory_item")
    print("getting inventory items")
    print("Items found: " + str(len(inventory_items)))

    if inventory_items:    
        manage_cart (inventory_items, 'Add')
        print("All items added to cart")

        manage_cart (inventory_items, 'Remove')
        print("All items removed from cart")
                                                                    

login('standard_user', 'secret_sauce')
