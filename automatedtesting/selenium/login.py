# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By

def process_inventory_items(inventory_items, action):
    

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

	logout = driver.find_element(By.ID, 'logout_sidebar_link'.size() > 0
	assert logout == True, 'logged in successfully!'

def manage_cart(inventory_items, action):
	for inventory_item in inventory_items:
		item_name = inventory_item.find_element(By.CLASS_NAME, "inventory_item_label").find_element(By.CLASS_NAME, "inventory_item_name").text
		print("Selecting Item: " + item_name)

		price_bar = inventory_item.find_element(By.CLASS_NAME, "pricebar")

		print(action + "item " + item_name)
		price_bar.find_element(By.CLASS_NAME, "btn_inventory").click()
		print("------")
           
def main():
	driver = login('standard_user', 'secret_sauce')
    
	inventory_items = driver.find_elements(By.CLASS_NAME, "inventory_item")
	print("getting inventory items")
	print("Items found: " + str(len(inventory_items)))

	if inventory_items:
	manage_cart(inventory_items,'Add')

	cart_badge = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
	assert cart_badge == len(inventory_items), 'All Items added to cart'

	manage_cart(inventory_items,'Remove')

	cart_badge = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge'.size() > 0
	assert cart_badge == Fasle, 'All Items removed to cart'
					 
if __name__ == '__main__':
	main()

