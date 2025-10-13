from getgauge.python import step
from selenium import webdriver
import time


@step("Open the demo web app and click the button")
def open_demo_and_click():
    driver = webdriver.Firefox()
    driver.get("http://localhost:5000")  # Assuming emulator hosting port
    button = driver.find_element("id", "addBtn")
    button.click()
    time.sleep(1)
    driver.quit()
