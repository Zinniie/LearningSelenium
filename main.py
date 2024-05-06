from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Start a new instance of Chrome web browser
driver = webdriver.Chrome()

# Open the Jumia website
driver.get("https://www.jumia.com.ng")

# Find the search box element and input the product name
search_box = driver.find_element(By.ID, "fi-q")
search_box.send_keys("Macbook")

# Press Enter to search for the product
search_box.send_keys(Keys.RETURN)

# Wait for the search results to load
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(@href,'/macbook-air-13-m1-chip-8gb-256gb-2020-model-gray-apple-mpg2158971.html')]")))

# Find the link to the particular product
product_link = driver.find_element(By.XPATH, "//a[contains(@href,'/macbook-air-13-m1-chip-8gb-256gb-2020-model-gray-apple-mpg2158971.html')]")

# Get the URL of the product page
product_url = product_link.get_attribute("href")

# Use/Execute JavaScript to navigate to the product page directly.. i was having a problem here
# product_link = (driver.find_element("xpath", "//a[contains(@href,'/macbook-air-13-m1-chip-8gb-256gb-2020-model-gray-apple-mpg2158971.html')]"))
driver.execute_script("window.location.href = arguments[0];", product_url)

# Add a short delay to ensure the page loads before further actions
time.sleep(5)

# scraping the details from the product page
# Wait for the product description element to load
wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"markup.-mhm.-pvl.-oxa.-sc")))

# Find the element containing the product description
product_description_element = driver.find_element(By.CLASS_NAME, "markup.-mhm.-pvl.-oxa.-sc")

# Extract the description
product_description = product_description_element.text

# Print the scraped product description
print("Product Description:", product_description)

# delay to keep the browser window open for a few seconds... just added this; dont think it is necessary
time.sleep(10)

# Close the browser window
driver.quit()


# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
#
# # Start a new instance of Chrome web browser
# driver = webdriver.Chrome()
#
# # Open the Jumia website
# driver.get("https://www.jumia.com.ng")
#
# # Wait for 5 seconds to allow the page to load
# time.sleep(5)
#
# # Find the search box element and input the product name
# # search_box = driver.find_element_by_id("fi-q")
# search_box = driver.find_element("id", "fi-q")
# search_box.send_keys("Macbook")
#
# # Press Enter to search for the product
# search_box.send_keys(Keys.RETURN)
#
# # Wait for 5 seconds to allow the search results to load
# time.sleep(5)
#
# # Find the link to the particular product and click on it
# product_link = (driver.find_element("xpath", "//a[contains(@href,'/macbook-air-13-m1-chip-8gb-256gb-2020-model-gray-apple-mpg2158971.html')]"))
# product_link.click()
#
# # Wait for 5 seconds to allow the product page to load
# time.sleep(5)

# # Close the browser window
# driver.quit()
