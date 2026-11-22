
from selenium import webdriver
import time

# Launch Chrome
driver = webdriver.Chrome()

# Open three websites
driver.get("https://www.google.com")
time.sleep(2)

driver.get("https://www.wikipedia.org")
time.sleep(2)

driver.get("https://www.python.org")
time.sleep(2)

# Go back twice
driver.back()
time.sleep(2)

driver.back()
time.sleep(2)

print("Title after going back twice:", driver.title)

# Go forward once
driver.forward()
time.sleep(2)

print("Title after going forward once:", driver.title)

# Close browser
driver.quit()
