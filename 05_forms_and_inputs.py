#!/usr/bin/env python3
"""
Demo 5: Forms and Input Handling
===============================

This program demonstrates:
- Working with different input types
- Handling dropdowns and select elements
- Checkbox and radio button interactions
- Form submission
- File uploads (if available)

Learning Objectives:
- Handle various form input types
- Work with Select dropdowns
- Manage checkboxes and radio buttons
- Submit forms properly
- Deal with form validation
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

def demo_forms_and_inputs():
    print("📝 Demo 5: Forms and Input Handling")
    print("=" * 40)
    
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
        
        print("📝 Demo 5: Forms and Inputs - Interactive Elements")
        
        # Navigate to DemoQA practice form
        driver.get("https://demoqa.com/automation-practice-form")
        print("🌐 Navigated to Practice Form page")
        
        print("\n📝 Starting form interactions...")
        
        # 1. Fill text inputs
        print("1️⃣ Filling text inputs...")
        
        # First Name
        first_name_field = driver.find_element(By.ID, "firstName")
        first_name_field.clear()
        first_name_field.send_keys("John")
        print("   ✅ First name entered: John")
        
        # Last Name  
        last_name_field = driver.find_element(By.ID, "lastName")
        last_name_field.clear()
        last_name_field.send_keys("Doe")
        print("   ✅ Last name entered: Doe")
        
        # Email
        email_field = driver.find_element(By.ID, "userEmail")
        email_field.clear()
        email_field.send_keys("john.doe@example.com")
        print("   ✅ Email entered: john.doe@example.com")
        
        # Mobile Number
        mobile_field = driver.find_element(By.ID, "userNumber")
        mobile_field.clear()
        mobile_field.send_keys("1234567890")
        print("   ✅ Mobile number entered: 1234567890")
        
        print("\n2️⃣ Working with radio buttons (Gender):")
        try:
            # Click Male radio button
            male_radio = driver.find_element(By.CSS_SELECTOR, "label[for='gender-radio-1']")
            male_radio.click()
            print("   ✅ Selected gender: Male")
            
            # Verify selection
            male_radio_input = driver.find_element(By.ID, "gender-radio-1")
            if male_radio_input.is_selected():
                print("   ✅ Male radio button is selected")
        except Exception as e:
            print(f"   ❌ Could not interact with radio buttons: {str(e)}")
        
        print("\n3️⃣ Working with checkboxes (Hobbies):")
        try:
            # Select Sports hobby
            sports_checkbox = driver.find_element(By.CSS_SELECTOR, "label[for='hobbies-checkbox-1']")
            sports_checkbox.click()
            print("   ✅ Selected hobby: Sports")
            
            # Select Reading hobby
            reading_checkbox = driver.find_element(By.CSS_SELECTOR, "label[for='hobbies-checkbox-2']")
            reading_checkbox.click()
            print("   ✅ Selected hobby: Reading")
            
        except Exception as e:
            print(f"   ❌ Could not interact with checkboxes: {str(e)}")
        
        print("\n4️⃣ Working with textarea (Address):")
        try:
            address_field = driver.find_element(By.ID, "currentAddress")
            address_text = "123 Main Street, Anytown, ST 12345"
            address_field.clear()
            address_field.send_keys(address_text)
            print("   ✅ Current address entered")
        except Exception as e:
            print(f"   ❌ Could not interact with textarea: {str(e)}")
        
        print("\n5️⃣ Working with dropdowns (State/City):")
        try:
            # Click state dropdown
            state_dropdown = driver.find_element(By.ID, "state")
            state_dropdown.click()
            time.sleep(1)
            
            # Select a state
            state_option = driver.find_element(By.XPATH, "//div[text()='NCR']")
            state_option.click()
            print("   ✅ State selected: NCR")
            
            # Wait for city dropdown to be populated
            time.sleep(1)
            
            # Click city dropdown
            city_dropdown = driver.find_element(By.ID, "city")
            city_dropdown.click()
            time.sleep(1)
            
            # Select a city
            city_option = driver.find_element(By.XPATH, "//div[text()='Delhi']")
            city_option.click()
            print("   ✅ City selected: Delhi")
            
        except Exception as e:
            print(f"   ❌ Could not interact with dropdowns: {str(e)}")
        
        print("\n6️⃣ Form submission:")
        try:
            submit_button = driver.find_element(By.ID, "submit")
            submit_button.click()
            print("   ✅ Form submitted!")
            
            # Wait for modal/confirmation
            time.sleep(2)
            
            # Check if modal appeared
            try:
                modal = driver.find_element(By.CSS_SELECTOR, ".modal-content")
                if modal.is_displayed():
                    print("   ✅ Confirmation modal appeared!")
                    
                    # Close modal
                    close_button = driver.find_element(By.ID, "closeLargeModal")
                    close_button.click()
                    print("   ✅ Modal closed")
                    
            except:
                print("   ❌ No confirmation modal found")
                
        except Exception as e:
            print(f"   ❌ Could not submit form: {str(e)}")
        
        print("\n7️⃣ Testing simpler text box form...")
        driver.get("https://demoqa.com/text-box")
        
        try:
            # Fill simple form
            full_name = driver.find_element(By.ID, "userName")
            full_name.clear()
            full_name.send_keys("Jane Smith")
            
            email = driver.find_element(By.ID, "userEmail") 
            email.clear()
            email.send_keys("jane.smith@example.com")
            
            current_addr = driver.find_element(By.ID, "currentAddress")
            current_addr.clear()
            current_addr.send_keys("456 Oak Avenue")
            
            permanent_addr = driver.find_element(By.ID, "permanentAddress")
            permanent_addr.clear()
            permanent_addr.send_keys("456 Oak Avenue")
            
            submit_btn = driver.find_element(By.ID, "submit")
            submit_btn.click()
            
            print("   ✅ Simple form completed and submitted")
            
            # Wait for output
            time.sleep(2)
            try:
                output = driver.find_element(By.ID, "output")
                if output.is_displayed():
                    print("   ✅ Form output displayed!")
            except:
                print("   ❌ No output displayed")
                
        except Exception as e:
            print(f"   ❌ Could not complete simple form: {str(e)}")
        
        print("\n8️⃣ Form interaction completed!")
        
        print("\n⏳ Pausing to observe final state...")
        time.sleep(3)
        
        print("\n✅ Demo 5 completed successfully!")
        
    except Exception as e:
        print(f"❌ An error occurred: {str(e)}")
    
    finally:
        if driver:
            print("🔒 Closing browser...")
            driver.quit()

if __name__ == "__main__":
    demo_forms_and_inputs()
