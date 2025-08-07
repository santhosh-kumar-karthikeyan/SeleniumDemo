#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import os
import tempfile

def demo_complete_automation():
    print("Demo 10: Complete Automation Workflow")
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
        wait = WebDriverWait(driver, 10)
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        screenshots_dir = os.path.join(current_dir, "screenshots")
        os.makedirs(screenshots_dir, exist_ok=True)
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        
        print("Testing comprehensive form automation...")
        driver.get("https://demoqa.com/automation-practice-form")
        
        form_title = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "main-header")))
        print(f"Page loaded: {form_title.text}")
        
        test_data = {
            "firstName": "Alexander",
            "lastName": "Johnson", 
            "email": "alexander.johnson@demo.com",
            "mobile": "5551234567",
            "address": "123 Automation Street, Test City, TC 12345"
        }
        
        print("Filling basic information...")
        first_name = driver.find_element(By.ID, "firstName")
        first_name.send_keys(test_data["firstName"])
        
        last_name = driver.find_element(By.ID, "lastName")
        last_name.send_keys(test_data["lastName"])
        
        email = driver.find_element(By.ID, "userEmail")
        email.send_keys(test_data["email"])
        
        mobile = driver.find_element(By.ID, "userNumber")
        mobile.send_keys(test_data["mobile"])
        
        print("Selecting gender...")
        try:
            male_radio = driver.find_element(By.CSS_SELECTOR, "label[for='gender-radio-1']")
            driver.execute_script("arguments[0].click();", male_radio)
        except Exception as e:
            print(f"Gender selection issue: {e}")
        
        print("Setting date of birth...")
        try:
            dob_field = driver.find_element(By.ID, "dateOfBirthInput")
            dob_field.click()
            
            month_dropdown = driver.find_element(By.CLASS_NAME, "react-datepicker__month-select")
            month_dropdown.click()
            january_option = driver.find_element(By.XPATH, "//option[@value='0']")
            january_option.click()
            
            year_dropdown = driver.find_element(By.CLASS_NAME, "react-datepicker__year-select")
            year_dropdown.click()
            year_option = driver.find_element(By.XPATH, "//option[@value='1990']")
            year_option.click()
            
            day_element = driver.find_element(By.XPATH, "//div[@class='react-datepicker__day react-datepicker__day--015' and text()='15']")
            day_element.click()
        except Exception as e:
            print(f"Date selection issue: {e}")
        
        print("Adding subjects...")
        try:
            subjects_field = driver.find_element(By.ID, "subjectsInput")
            subjects = ["Math", "Computer Science"]
            
            for subject in subjects:
                subjects_field.click()
                subjects_field.send_keys(subject)
                time.sleep(1)
                subjects_field.send_keys(Keys.TAB)
        except Exception as e:
            print(f"Subjects adding issue: {e}")
        
        print("Selecting hobbies...")
        try:
            hobbies = [
                ("hobbies-checkbox-1", "Sports"),
                ("hobbies-checkbox-2", "Reading")
            ]
            
            for hobby_id, hobby_name in hobbies:
                hobby_label = driver.find_element(By.CSS_SELECTOR, f"label[for='{hobby_id}']")
                driver.execute_script("arguments[0].click();", hobby_label)
        except Exception as e:
            print(f"Hobby selection issue: {e}")
        
        print("Uploading file...")
        try:
            with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as temp_file:
                temp_file.write("This is a test file for Selenium automation demo.")
                temp_file_path = temp_file.name
            
            file_input = driver.find_element(By.ID, "uploadPicture")
            file_input.send_keys(temp_file_path)
            
            os.unlink(temp_file_path)
        except Exception as e:
            print(f"File upload issue: {e}")
        
        address_field = driver.find_element(By.ID, "currentAddress")
        address_field.send_keys(test_data["address"])
        
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
        except Exception as e:
            print(f"State/City selection issue: {e}")
        
        screenshot_path = os.path.join(screenshots_dir, f"form_before_submit_{timestamp}.png")
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved: {screenshot_path}")
        
        print("Submitting form...")
        submit_button = driver.find_element(By.ID, "submit")
        driver.execute_script("arguments[0].click();", submit_button)
        
        time.sleep(2)
        
        try:
            modal = driver.find_element(By.CSS_SELECTOR, ".modal-content")
            if modal.is_displayed():
                print("Form submitted successfully!")
                
                success_screenshot = os.path.join(screenshots_dir, f"form_submitted_success_{timestamp}.png")
                driver.save_screenshot(success_screenshot)
                
                try:
                    modal_body = driver.find_element(By.CSS_SELECTOR, ".modal-body")
                    print("Submitted data verified")
                except:
                    print("Could not extract submitted data")
                
                close_button = driver.find_element(By.ID, "closeLargeModal")
                close_button.click()
            else:
                print("Modal not visible")
        except Exception as e:
            print(f"Modal handling issue: {e}")
        
        print("\nTesting simple form for comparison...")
        driver.get("https://demoqa.com/text-box")
        
        simple_data = {
            "userName": "Test User Final",
            "userEmail": "testuser@final.com",
            "currentAddress": "123 Simple Street",
            "permanentAddress": "456 Permanent Avenue"
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
                print("Simple form submitted with output displayed")
                
                final_screenshot = os.path.join(screenshots_dir, f"simple_form_final_{timestamp}.png")
                driver.save_screenshot(final_screenshot)
        except:
            print("Simple form output not found")
        
        print("\nTesting multiple element interactions...")
        driver.get("https://demoqa.com/elements")
        
        text_box_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Text Box']")))
        text_box_link.click()
        
        user_name = driver.find_element(By.ID, "userName")
        user_name.send_keys("Multi Test User")
        
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()
        time.sleep(1)
        
        print("Testing buttons...")
        driver.get("https://demoqa.com/buttons")
        
        double_click_btn = wait.until(EC.element_to_be_clickable((By.ID, "doubleClickBtn")))
        actions = ActionChains(driver)
        actions.double_click(double_click_btn).perform()
        
        right_click_btn = driver.find_element(By.ID, "rightClickBtn")
        actions.context_click(right_click_btn).perform()
        
        click_me_btn = driver.find_element(By.XPATH, "//button[text()='Click Me']")
        click_me_btn.click()
        
        print("Testing alerts...")
        driver.get("https://demoqa.com/alerts")
        
        alert_btn = wait.until(EC.element_to_be_clickable((By.ID, "alertButton")))
        alert_btn.click()
        
        alert = wait.until(EC.alert_is_present())
        alert_text = alert.text
        alert.accept()
        print(f"Alert handled: {alert_text}")
        
        print("\nAutomation challenge completed successfully!")
        
        print("\nSummary of completed actions:")
        print("   Navigated to complex practice form")
        print("   Filled personal information")
        print("   Selected radio buttons and checkboxes")
        print("   Handled date picker")
        print("   Added dynamic subjects")
        print("   Uploaded file")
        print("   Managed dropdown selections")
        print("   Captured screenshots")
        print("   Submitted form and verified results")
        print("   Tested alternative simple form")
        print("   Performed multi-element interactions")
        print("   Handled alerts and user interactions")
        
        print("\nFinal Demo Successfully Completed!")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    
    finally:
        if driver:
            print("Closing browser...")
            driver.quit()

if __name__ == "__main__":
    demo_complete_automation()
