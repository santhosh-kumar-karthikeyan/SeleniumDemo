#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

def demo_search_functionality():
    print("Demo 3: Search Functionality and Results")
    print("=" * 45)
    
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
        
        print("\nFinding form fields...")
        name_field = driver.find_element(By.ID, "userName")
        email_field = driver.find_element(By.ID, "userEmail")
        current_address = driver.find_element(By.ID, "currentAddress")
        permanent_address = driver.find_element(By.ID, "permanentAddress")
        submit_button = driver.find_element(By.ID, "submit")
        
        # Fill out the form
        form_data = {
            'name': 'John Doe',
            'email': 'john.doe@example.com',
            'current_address': '123 Main St, Anytown, USA',
            'permanent_address': '456 Oak Ave, Hometown, USA'
        }
        
        print(f"⌨️  Filling form with test data...")
        name_field.clear()
        name_field.send_keys(form_data['name'])
        
        email_field.clear()
        email_field.send_keys(form_data['email'])
        
        current_address.clear()
        current_address.send_keys(form_data['current_address'])
        
        permanent_address.clear()
        permanent_address.send_keys(form_data['permanent_address'])
        
        print("⏎ Submitting form...")
        submit_button.click()
        
        # Wait for results to appear
        print("⏳ Waiting for form submission results...")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "output"))
        )
        
        # Verify form submission
        output_div = driver.find_element(By.ID, "output")
        if output_div.is_displayed():
            print("✅ Form submitted successfully!")
            
            # Get the output text
            output_text = output_div.text
            print(f"📋 Form submission output:")
            print(f"   {output_text}")
            
            # Check if submitted data appears in output
            for key, value in form_data.items():
                if value in output_text:
                    print(f"   ✅ {key}: Found in output")
                else:
                    print(f"   ⚠️ {key}: Not found in output")
        
        else:
            print("❌ Form submission output not visible")
        
        # Wait to observe results
        print("\n⏳ Pausing to observe results...")
        time.sleep(3)
        
        print("\n✅ Demo 3 completed successfully!")
        
    except Exception as e:
        print(f"❌ An error occurred: {str(e)}")
    
    finally:
        if driver:
            print("🔒 Closing browser...")
            driver.quit()

if __name__ == "__main__":
    demo_search_functionality()
