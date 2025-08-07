#!/usr/bin/env python3
"""
Demo 2: Finding and Interacting with Web Elements
=================================================

This program demonstrates:
- Finding elements by different locators
- Interacting with search box
- Getting element properties
- Basic element interactions

Learning Objectives:
- Understand element locators (ID, Name, Class, XPath, CSS Selector)
- Learn to find web elements
- Interact with input fields
- Get element text and attributes
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

def demo_find_elements():
    print("🔍 Demo 2: Finding and Interacting with Elements")
    print("=" * 50)
    
    # Setup ChromeDriver
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    service = Service(ChromeDriverManager().install())
    driver = None
    
    try:
        # Launch browser
        print("🚀 Launching browser...")
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.implicitly_wait(10)
        
        # Navigate to DemoQA
        driver.get("https://demoqa.com/text-box")
        print("🌐 Navigated to DemoQA Text Box demo")
        
        # Find the form elements using different methods
        print("\n🎯 Finding form elements...")
        
        # Method 1: By ID
        try:
            name_field = driver.find_element(By.ID, "userName")
            print("✅ Found name field by ID: 'userName'")
        except:
            print("❌ Could not find name field by ID")
        
        # Method 2: By CSS Selector
        try:
            email_field = driver.find_element(By.CSS_SELECTOR, "input[id='userEmail']")
            print("✅ Found email field by CSS_SELECTOR: 'input[id=\"userEmail\"]'")
        except:
            print("❌ Could not find email field by CSS selector")
        
        # Method 3: By XPath
        try:
            current_address = driver.find_element(By.XPATH, "//textarea[@id='currentAddress']")
            print("✅ Found current address by XPATH: '//textarea[@id=\"currentAddress\"]'")
        except:
            print("❌ Could not find current address by XPath")
        
        # Get element properties
        print("\n📋 Element Properties:")
        if 'name_field' in locals():
            print(f"   Tag name: {name_field.tag_name}")
            print(f"   Element size: {name_field.size}")
            print(f"   Element location: {name_field.location}")
            print(f"   Is displayed: {name_field.is_displayed()}")
            print(f"   Is enabled: {name_field.is_enabled()}")
        
        # Interact with the form fields
        print("\n⌨️  Interacting with form fields...")
        name_field.clear()  # Clear any existing text
        name_field.send_keys("John Doe")
        print("   Typed: 'John Doe' in name field")
        
        email_field.clear()
        email_field.send_keys("john.doe@example.com")
        print("   Typed: 'john.doe@example.com' in email field")
        
        # Wait to see the typing
        time.sleep(2)
        
        # Get the values that were typed
        name_value = name_field.get_attribute("value")
        email_value = email_field.get_attribute("value")
        print(f"   Name field value: '{name_value}'")
        print(f"   Email field value: '{email_value}'")
        
        # Clear the fields
        name_field.clear()
        email_field.clear()
        print("   Cleared all fields")
        
        time.sleep(2)
        
        print("\n✅ Demo 2 completed successfully!")
        
    except Exception as e:
        print(f"❌ An error occurred: {str(e)}")
    
    finally:
        if driver:
            print("🔒 Closing browser...")
            driver.quit()

if __name__ == "__main__":
    demo_find_elements()
