
from selenium import webdriver
import time

# Launch Chrome
driver = webdriver.Chrome()

# Open a website
driver.get("https://www.python.org")
time.sleep(2)

# Store title before refresh
title_before = driver.title
print("Title before refresh:", title_before)

# Refresh the page
driver.refresh()
time.sleep(2)

# Store title after refresh
title_after = driver.title
print("Title after refresh:", title_after)

# Compare both titles
if title_before == title_after:
    print("Result: Page title remained the same.")
else:
    print("Result: Page title changed.")

# Close browser
driver.quit()
