#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time
import tempfile
import os

def demo_forms_and_inputs():
    print("Demo 5: Forms and Input Handling")
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
        
        print("Testing comprehensive form...")
        driver.get("https://demoqa.com/automation-practice-form")
        
        form_data = {
            'firstName': 'John',
            'lastName': 'Smith',
            'email': 'john.smith@example.com',
            'mobile': '1234567890',
            'address': '123 Test Street, Test City, TX 12345'
        }
        
        first_name = driver.find_element(By.ID, "firstName")
        first_name.send_keys(form_data['firstName'])
        
        last_name = driver.find_element(By.ID, "lastName")
        last_name.send_keys(form_data['lastName'])
        
        email = driver.find_element(By.ID, "userEmail")
        email.send_keys(form_data['email'])
        
        mobile = driver.find_element(By.ID, "userNumber")
        mobile.send_keys(form_data['mobile'])
        
        print("Selecting gender...")
        try:
            gender_radio = driver.find_element(By.CSS_SELECTOR, "label[for='gender-radio-1']")
            driver.execute_script("arguments[0].click();", gender_radio)
        except:
            print("Gender selection may have failed")
        
        print("Setting date of birth...")
        try:
            dob_input = driver.find_element(By.ID, "dateOfBirthInput")
            dob_input.click()
            
            month_select = driver.find_element(By.CLASS_NAME, "react-datepicker__month-select")
            month_select.click()
            jan_option = driver.find_element(By.XPATH, "//option[@value='0']")
            jan_option.click()
            
            year_select = driver.find_element(By.CLASS_NAME, "react-datepicker__year-select")
            year_select.click()
            year_option = driver.find_element(By.XPATH, "//option[@value='1990']")
            year_option.click()
            
            day_option = driver.find_element(By.XPATH, "//div[contains(@class, 'react-datepicker__day') and text()='15']")
            day_option.click()
        except:
            print("Date selection may have encountered issues")
        
        print("Adding subjects...")
        try:
            subjects_input = driver.find_element(By.ID, "subjectsInput")
            subjects_input.send_keys("Math")
            subjects_input.send_keys(Keys.TAB)
        except:
            print("Subject addition may have failed")
        
        print("Selecting hobbies...")
        try:
            hobbies = ["hobbies-checkbox-1", "hobbies-checkbox-2"]
            for hobby_id in hobbies:
                hobby_label = driver.find_element(By.CSS_SELECTOR, f"label[for='{hobby_id}']")
                driver.execute_script("arguments[0].click();", hobby_label)
        except:
            print("Hobby selection may have failed")
        
        print("Uploading file...")
        try:
            with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as temp_file:
                temp_file.write("Test file content")
                temp_file_path = temp_file.name
            
            file_input = driver.find_element(By.ID, "uploadPicture")
            file_input.send_keys(temp_file_path)
            
            os.unlink(temp_file_path)
        except:
            print("File upload may have failed")
        
        address_field = driver.find_element(By.ID, "currentAddress")
        address_field.send_keys(form_data['address'])
        
        print("Selecting state and city...")
        try:
            state_dropdown = driver.find_element(By.ID, "state")
            state_dropdown.click()
            time.sleep(1)
            ncr_option = driver.find_element(By.XPATH, "//div[text()='NCR']")
            ncr_option.click()
            
            time.sleep(1)
            city_dropdown = driver.find_element(By.ID, "city")
            city_dropdown.click()
            time.sleep(1)
            delhi_option = driver.find_element(By.XPATH, "//div[text()='Delhi']")
            delhi_option.click()
        except:
            print("State/City selection may have failed")
        
        print("Submitting form...")
        submit_button = driver.find_element(By.ID, "submit")
        driver.execute_script("arguments[0].click();", submit_button)
        
        time.sleep(2)
        
        try:
            modal = driver.find_element(By.CSS_SELECTOR, ".modal-content")
            if modal.is_displayed():
                print("Form submitted successfully!")
                close_button = driver.find_element(By.ID, "closeLargeModal")
                close_button.click()
            else:
                print("Form submission modal not visible")
        except:
            print("Form submission status unclear")
        
        print("\nTesting simple text box form...")
        driver.get("https://demoqa.com/text-box")
        
        simple_data = {
            "userName": "Simple Test User",
            "userEmail": "simple@test.com",
            "currentAddress": "123 Simple St",
            "permanentAddress": "456 Permanent Ave"
        }
        
        for field_id, value in simple_data.items():
            field = driver.find_element(By.ID, field_id)
            field.clear()
            field.send_keys(value)
        
        submit_btn = driver.find_element(By.ID, "submit")
        submit_btn.click()
        
        time.sleep(2)
        
        try:
            output = driver.find_element(By.ID, "output")
            if output.is_displayed():
                print("Simple form submitted successfully!")
        except:
            print("Simple form output not found")
        
        print("\nDemo 5 completed successfully!")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    
    finally:
        if driver:
            print("Closing browser...")
            driver.quit()

if __name__ == "__main__":
    demo_forms_and_inputs()
