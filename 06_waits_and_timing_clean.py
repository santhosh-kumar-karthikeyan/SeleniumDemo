#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

def demo_waits_and_timing():
    print("Demo 6: Wait Strategies and Timing")
    print("=" * 40)
    
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    service = Service(ChromeDriverManager().install())
    driver = None
    
    try:
        print("Launching browser...")
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.implicitly_wait(10)
        
        print("Testing dynamic properties...")
        driver.get("https://demoqa.com/dynamic-properties")
        
        print("Waiting for elements to become enabled...")
        wait = WebDriverWait(driver, 10)
        
        try:
            enable_button = wait.until(EC.element_to_be_clickable((By.ID, "enableAfter")))
            print("Button became enabled successfully")
        except TimeoutException:
            print("Enable button timeout")
        
        try:
            color_change = wait.until(EC.presence_of_element_located((By.ID, "colorChange")))
            print("Color change button found")
        except TimeoutException:
            print("Color change button timeout")
        
        try:
            visible_after = wait.until(EC.visibility_of_element_located((By.ID, "visibleAfter")))
            print("Visible after button appeared")
        except TimeoutException:
            print("Visible after button timeout")
        
        print("\nTesting progress bar...")
        driver.get("https://demoqa.com/progress-bar")
        
        start_button = driver.find_element(By.ID, "startStopButton")
        start_button.click()
        print("Progress bar started")
        
        print("Waiting for progress to complete...")
        try:
            WebDriverWait(driver, 15).until(
                lambda driver: driver.find_element(By.CSS_SELECTOR, ".progress-bar").get_attribute("aria-valuenow") == "100"
            )
            print("Progress bar completed successfully")
        except TimeoutException:
            print("Progress bar did not complete in time")
        
        print("\nTesting alerts with timing...")
        driver.get("https://demoqa.com/alerts")
        
        timer_alert_button = driver.find_element(By.ID, "timerAlertButton")
        timer_alert_button.click()
        print("Clicked timer alert button")
        
        try:
            alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
            alert_text = alert.text
            print(f"Timer alert appeared: {alert_text}")
            alert.accept()
        except TimeoutException:
            print("Timer alert did not appear")
        
        print("\nTesting text box with waits...")
        driver.get("https://demoqa.com/text-box")
        
        name_field = wait.until(EC.presence_of_element_located((By.ID, "userName")))
        name_field.send_keys("Wait Strategy Test")
        
        submit_button = wait.until(EC.element_to_be_clickable((By.ID, "submit")))
        submit_button.click()
        
        try:
            output = wait.until(EC.visibility_of_element_located((By.ID, "output")))
            print("Output appeared successfully with explicit wait")
        except TimeoutException:
            print("Output did not appear in time")
        
        print("\nDemo 6 completed successfully!")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    
    finally:
        if driver:
            print("Closing browser...")
            driver.quit()

if __name__ == "__main__":
    demo_waits_and_timing()
