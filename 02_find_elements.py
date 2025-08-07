#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

def demo_find_elements():
    print("Demo 2: Finding and Interacting with Elements")
    print("=" * 50)
    
    # Setup ChromeDriver
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    service = Service(ChromeDriverManager().install())
    driver = None
    
    try:
        print("Launching browser...")
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.implicitly_wait(10)
        
        driver.get("https://demoqa.com/text-box")
        print("Navigated to DemoQA Text Box demo")
        
        print("\nFinding form elements...")
        
        try:
            name_field = driver.find_element(By.ID, "userName")
            print("Found name field by ID: 'userName'")
        except:
            print("Could not find name field by ID")
        
        try:
            email_field = driver.find_element(By.CSS_SELECTOR, "input[id='userEmail']")
            print("Found email field by CSS_SELECTOR: 'input[id=\"userEmail\"]'")
        except:
            print("Could not find email field by CSS selector")
        
        try:
            current_address = driver.find_element(By.XPATH, "//textarea[@id='currentAddress']")
            print("Found current address by XPATH: '//textarea[@id=\"currentAddress\"]'")
        except:
            print("Could not find current address by XPath")
        
        print("\nElement Properties:")
        if 'name_field' in locals():
            print(f"   Tag name: {name_field.tag_name}")
            print(f"   Element size: {name_field.size}")
            print(f"   Element location: {name_field.location}")
            print(f"   Is displayed: {name_field.is_displayed()}")
            print(f"   Is enabled: {name_field.is_enabled()}")
        
        print("\nInteracting with form fields...")
        name_field.clear()
        name_field.send_keys("John Doe")
        print("   Typed: 'John Doe' in name field")
        
        email_field.clear()
        email_field.send_keys("john.doe@example.com")
        print("   Typed: 'john.doe@example.com' in email field")
        
        time.sleep(2)
        
        name_value = name_field.get_attribute("value")
        email_value = email_field.get_attribute("value")
        print(f"   Name field value: '{name_value}'")
        print(f"   Email field value: '{email_value}'")
        
        name_field.clear()
        email_field.clear()
        print("   Cleared all fields")
        
        time.sleep(2)
        
        print("\nDemo 2 completed successfully!")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    
    finally:
        if driver:
            print("Closing browser...")
            driver.quit()

if __name__ == "__main__":
    demo_find_elements()
