#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

def demo_multiple_elements():
    print("Demo 4: Working with Multiple Elements")
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
        
        driver.get("https://demoqa.com/elements")
        print("Navigated to DemoQA Elements page")
        
        print("\nTesting Text Box functionality...")
        text_box_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Text Box']"))
        )
        text_box_link.click()
        
        name_field = driver.find_element(By.ID, "userName")
        email_field = driver.find_element(By.ID, "userEmail")
        
        name_field.send_keys("Multiple Elements Test")
        email_field.send_keys("test@multiple.com")
        
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()
        
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "output"))
        )
        print("Text Box test completed successfully")
        
        print("\nTesting Buttons functionality...")
        driver.get("https://demoqa.com/buttons")
        
        double_click_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "doubleClickBtn"))
        )
        right_click_btn = driver.find_element(By.ID, "rightClickBtn")
        click_me_btn = driver.find_element(By.XPATH, "//button[text()='Click Me']")
        
        actions = ActionChains(driver)
        
        print("Performing double click...")
        actions.double_click(double_click_btn).perform()
        time.sleep(1)
        
        print("Performing right click...")
        actions.context_click(right_click_btn).perform()
        time.sleep(1)
        
        print("Performing single click...")
        click_me_btn.click()
        time.sleep(1)
        
        try:
            double_msg = driver.find_element(By.ID, "doubleClickMessage")
            right_msg = driver.find_element(By.ID, "rightClickMessage")
            click_msg = driver.find_element(By.ID, "dynamicClickMessage")
            
            if double_msg.is_displayed():
                print("Double click message: " + double_msg.text)
            if right_msg.is_displayed():
                print("Right click message: " + right_msg.text)
            if click_msg.is_displayed():
                print("Click message: " + click_msg.text)
                
        except:
            print("Some button messages may not have appeared")
        
        print("\nTesting Checkbox functionality...")
        driver.get("https://demoqa.com/checkbox")
        
        expand_all = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[title='Expand all']"))
        )
        expand_all.click()
        time.sleep(1)
        
        checkboxes = driver.find_elements(By.CSS_SELECTOR, "span.rct-checkbox")
        print(f"Found {len(checkboxes)} checkboxes")
        
        if len(checkboxes) >= 3:
            for i in range(min(3, len(checkboxes))):
                try:
                    driver.execute_script("arguments[0].click();", checkboxes[i])
                    time.sleep(0.5)
                except:
                    continue
        
        try:
            result_div = driver.find_element(By.ID, "result")
            if result_div.is_displayed():
                print("Checkbox selections recorded successfully")
        except:
            print("Checkbox results may not be visible")
        
        print("\nTesting Radio Buttons...")
        driver.get("https://demoqa.com/radio-button")
        
        try:
            yes_radio = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='yesRadio']"))
            )
            yes_radio.click()
            time.sleep(1)
            
            impressive_radio = driver.find_element(By.CSS_SELECTOR, "label[for='impressiveRadio']")
            impressive_radio.click()
            time.sleep(1)
            
            try:
                result_span = driver.find_element(By.CSS_SELECTOR, "span.text-success")
                print(f"Radio button result: {result_span.text}")
            except:
                print("Radio button result not found")
                
        except Exception as e:
            print(f"Radio button test encountered an issue: {str(e)}")
        
        print("\nDemo 4 completed successfully!")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    
    finally:
        if driver:
            print("Closing browser...")
            driver.quit()

if __name__ == "__main__":
    demo_multiple_elements()
