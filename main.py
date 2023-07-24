from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from time import sleep
import random

batching = False

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the Nitro Type website
driver.get("https://www.nitrotype.com/login")

username = "username"
password = "password"

# Find the username and password textboxes by their ids
try:
	username_box = driver.find_element(By.ID, "username")
except NoSuchElementException:
	exit("Could not connect to the internet.")
password_box = driver.find_element(By.ID, "password")

# Type in the username and password
username_box.send_keys(username)
password_box.send_keys(password)

# Submit the form (assuming there's a submit button)
password_box.send_keys(Keys.RETURN)

# Create an ActionChains object
actions = ActionChains(driver)

def nitro_type_auto():

	# Wait for the dash-copy (contains elements of the words you need to type) element to be visible on the page
	element = WebDriverWait(driver, 10).until(
		EC.visibility_of_element_located((By.CLASS_NAME, "dash-copy"))
	)

	
        # Get the sub-elements of the dash-copy element
	sub_elements = element.find_elements(By.XPATH, ".//*")


	pos = WebDriverWait(driver, 10).until(
        	EC.visibility_of_element_located((By.CLASS_NAME, "dash-pos"))
        )
	
	times = 0
	pe = pos.find_elements(By.XPATH, ".//*")[0]
	while pe.text == "1": 
		times += 1

	if batching:
		full = ""
		for word in sub_elements:
			full += word.text.strip()+" "
		actions.send_keys(full).perform()
	else:
		# Type out the text of the sub-elements
		for word in sub_elements:
			if driver.current_url != "https://www.nitrotype.com/race":
			if len(word.text) > 1:
				actions.send_keys(f"{word.text.strip()} ").perform()
	sleep(1)

sleep(5)
while True:
	#driver.execute_script("window.stop();")
	#sleep(1)
	#driver.get('https://nitrotype.com/race')
	driver.execute_script("window.location.href='https://nitrotype.com/race';")
	sleep(1)
	try:
		nitro_type_auto()
	except common.exceptions.StaleElementReferenceException:
		print("Element no longer exists")
driver.quit()
