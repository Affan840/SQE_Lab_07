
from selenium import webdriver
import time

# Launch Chrome
driver = webdriver.Chrome()

# Open first website
driver.get("https://www.google.com")
print("Website 1:")
print("Title:", driver.title)
print("URL:", driver.current_url)
time.sleep(2)

# Open second website
driver.get("https://www.wikipedia.org")
print("\nWebsite 2:")
print("Title:", driver.title)
print("URL:", driver.current_url)
time.sleep(2)

# Open third website
driver.get("https://www.python.org")
print("\nWebsite 3:")
print("Title:", driver.title)
print("URL:", driver.current_url)
time.sleep(2)

# Go back twice
driver.back()
time.sleep(2)
driver.back()
time.sleep(2)
print("\nAfter going back twice:")  
print("Title:", driver.title)

# Go forward once
driver.forward()
time.sleep(2)
print("\nAfter going forward once:")
print("Title:", driver.title)

# Close browser
driver.quit()
