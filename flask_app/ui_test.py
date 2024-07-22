from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Start WebDriver
driver = webdriver.Chrome()

try:
    # Open the Flask app
    driver.get("http://localhost:5000")
    time.sleep(2)

    # Find the password input field and enter a password
    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys("YourPassword123!")

    # Find the login button and click it
    login_button = driver.find_element(By.TAG_NAME, "button")
    login_button.click()
    time.sleep(2)

    # Check if the welcome message is displayed
    assert "Welcome" in driver.page_source

finally:
    # Close the WebDriver
    driver.quit()
