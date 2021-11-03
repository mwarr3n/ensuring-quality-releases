# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
import datetime

def log (status, description):

    time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print ("{0} {1} {2}".format(str(time_stamp), status, description))

def manage_cart (inventory_items, action):

    for inventory_item in inventory_items:
        item_name = inventory_item.find_element(By.CLASS_NAME, "inventory_item_label").find_element(By.CLASS_NAME, "inventory_item_name").text

        price_bar = inventory_item.find_element(By.CLASS_NAME, "pricebar")

        price_bar.find_element(By.CLASS_NAME, "btn_inventory").click()

        if action == "Add":
            log('success', 'added to cart: ' + item_name)
        else: 
            log('success', 'removed from cart: ' + item_name)
	
	
# Start the browser and login with standard_user
def login (user, password):
    # print ('Starting the browser...')
    url = 'https://www.saucedemo.com/'
    log('info', 'staring browser.')

    # --uncomment when running in Azure DevOps.
    options = ChromeOptions()
    options.add_argument("--headless") 
    driver = webdriver.Chrome(options=options)
    #     driver = webdriver.Chrome()

    log('success', 'browser started.')
    log('info', ' navigating to login page of ' + url)

    driver.get(url)

    driver.find_element(By.ID, "user-name").send_keys(user)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

    # print(user + " logged in successfully!")
    log('success', user + ' logged in' )

    inventory_items = driver.find_elements(By.CLASS_NAME, "inventory_item")
    # print("getting inventory items")
    log('info', 'getting inventory items' )
    # print("Items found: " + str(len(inventory_items)))
    log('info', 'items found: ' + str(len(inventory_items)) )

    if inventory_items:    
        manage_cart (inventory_items, 'Add')
        # print("All items added to cart")
        log('success', 'all items added to cart')

        manage_cart (inventory_items, 'Remove')
        # print("All items removed from cart")
        log('success', 'all items removed from cart')
    
    driver.quit()
    log('info', 'done')

                                                                    

login('standard_user', 'secret_sauce')
