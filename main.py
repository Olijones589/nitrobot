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
print("CREATING INSTANCE...")
driver = webdriver.Chrome()

# Navigate to the Nitro Type website
print("NAVIGATING TO NITROTYPE LOGIN...")
driver.get("https://www.nitrotype.com/login")

username = "bobiscoolbobiscool"
password = "43-31-7"

# Find the username and password textboxes by their ids
print("GETTING USERNAME ELEMENT...")
try:
	username_box = driver.find_element(By.ID, "username")
except NoSuchElementException:
	exit("Could not connect to the internet.")
print("GETTING PASSWORD ELEMENT...")
password_box = driver.find_element(By.ID, "password")

# Type in the username and password
print("ENTERING USERNAME...")
username_box.send_keys(username)
print("ENTERING PASSWORD...")
password_box.send_keys(password)

# Submit the form (assuming there's a submit button)
print("LOGGING IN...")
password_box.send_keys(Keys.RETURN)

# Create an ActionChains object
print("CREATING ACTIONCHAINS OBJECT...")
actions = ActionChains(driver)

def nitro_type_auto():
	print('WAITING FOR TEXT...')

	# Wait for the dash-copy (contains elements of the words you need to type) element to be visible on the page
	element = WebDriverWait(driver, 10).until(
		EC.visibility_of_element_located((By.CLASS_NAME, "dash-copy"))
	)

	print('GETTING TEXT ELEMENTS...')
	
        # Get the sub-elements of the dash-copy element
	sub_elements = element.find_elements(By.XPATH, ".//*")

	print("WAITING FOR RANKING ELEMENT...")

	pos = WebDriverWait(driver, 10).until(
        	EC.visibility_of_element_located((By.CLASS_NAME, "dash-pos"))
        )
	
	print("WAITING FOR RACE TO START...")
	
	times = 0
	pe = pos.find_elements(By.XPATH, ".//*")[0]
	while pe.text == "1": 
		print(f"WAITING... {times}")
		times += 1
	print("RACE STARTED")

	if batching:
		print("BATCH MODE ENABLED")
		full = ""
		for word in sub_elements:
			full += word.text.strip()+" "
		actions.send_keys(full).perform()
	else:
		print("BATCH MODE DISABLED")
		# Type out the text of the sub-elements
		for word in sub_elements:
			if driver.current_url != "https://www.nitrotype.com/race":
				print("RACE HALTED.")
			if len(word.text) > 1:
				print(f'{word.text.strip()} ')
				actions.send_keys(f"{word.text.strip()} ").perform()
	sleep(1)

print("WAITING FOR AUTH...")
sleep(5)
print("COMPLETE.")

while True:
	#driver.execute_script("window.stop();")
	#sleep(1)
	print("REDIRECTING TO RACE...")
	#driver.get('https://nitrotype.com/race')
	driver.execute_script("window.location.href='https://nitrotype.com/race';")
	sleep(1)
	print("COMPLETE!")
	try:
		nitro_type_auto()
	except common.exceptions.StaleElementReferenceException:
		print("AN ELEMENT NO LONGER EXISTS")
driver.quit()
