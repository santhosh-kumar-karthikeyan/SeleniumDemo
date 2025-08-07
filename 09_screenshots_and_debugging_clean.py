#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import os

def demo_screenshots_and_debugging():
    print("Demo 9: Screenshots and Debugging Techniques")
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
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        screenshots_dir = os.path.join(current_dir, "screenshots")
        os.makedirs(screenshots_dir, exist_ok=True)
        
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        
        print("Taking initial screenshot...")
        driver.get("https://demoqa.com/text-box")
        
        screenshot_path = os.path.join(screenshots_dir, f"demoqa_textbox_{timestamp}.png")
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved: {screenshot_path}")
        
        print("\nDemonstrating successful form interaction...")
        name_field = driver.find_element(By.ID, "userName")
        name_field.send_keys("Debug Test User")
        
        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("debug@test.com")
        
        before_submit_path = os.path.join(screenshots_dir, f"form_filled_{timestamp}.png")
        driver.save_screenshot(before_submit_path)
        print(f"Form filled screenshot: {before_submit_path}")
        
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()
        
        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.ID, "output"))
            )
            
            success_path = os.path.join(screenshots_dir, f"form_submitted_{timestamp}.png")
            driver.save_screenshot(success_path)
            print(f"Success screenshot: {success_path}")
            
        except TimeoutException:
            timeout_path = os.path.join(screenshots_dir, f"timeout_debug_{timestamp}.png")
            driver.save_screenshot(timeout_path)
            print(f"Timeout debug screenshot: {timeout_path}")
        
        print("\nDemonstrating error handling...")
        try:
            nonexistent_element = driver.find_element(By.ID, "nonexistent")
        except NoSuchElementException:
            print("Element not found (expected behavior)")
            error_path = os.path.join(screenshots_dir, f"no_element_debug_{timestamp}.png")
            driver.save_screenshot(error_path)
            print(f"Error debug screenshot: {error_path}")
        
        print("\nTesting dynamic properties page...")
        driver.get("https://demoqa.com/dynamic-properties")
        
        before_dynamic_path = os.path.join(screenshots_dir, f"before_dynamic_{timestamp}.png")
        driver.save_screenshot(before_dynamic_path)
        print(f"Before dynamic changes: {before_dynamic_path}")
        
        print("Waiting for dynamic button to become enabled...")
        try:
            WebDriverWait(driver, 8).until(
                EC.element_to_be_clickable((By.ID, "enableAfter"))
            )
            
            enabled_path = os.path.join(screenshots_dir, f"button_enabled_{timestamp}.png")
            driver.save_screenshot(enabled_path)
            print(f"Button enabled screenshot: {enabled_path}")
            
        except TimeoutException:
            print("Button did not become enabled in time")
        
        print("\nTesting broken links page...")
        driver.get("https://demoqa.com/broken")
        
        before_broken_path = os.path.join(screenshots_dir, f"before_broken_link_{timestamp}.png")
        driver.save_screenshot(before_broken_path)
        print(f"Before clicking broken link: {before_broken_path}")
        
        try:
            broken_link = driver.find_element(By.XPATH, "//a[text()='Click Here for Broken Link']")
            broken_link.click()
            time.sleep(3)
            
            after_broken_path = os.path.join(screenshots_dir, f"after_broken_link_{timestamp}.png")
            driver.save_screenshot(after_broken_path)
            print(f"After broken link click: {after_broken_path}")
            
        except Exception as e:
            print(f"Broken link test issue: {e}")
        
        print("\nTesting elements page for debugging...")
        driver.get("https://demoqa.com/elements")
        
        elements_path = os.path.join(screenshots_dir, f"elements_page_{timestamp}.png")
        driver.save_screenshot(elements_path)
        print(f"Elements page screenshot: {elements_path}")
        
        try:
            text_box_link = driver.find_element(By.XPATH, "//span[text()='Text Box']")
            text_box_link.click()
            
            element_clicked_path = os.path.join(screenshots_dir, f"form_element_{timestamp}.png")
            driver.save_screenshot(element_clicked_path)
            print(f"Form element clicked: {element_clicked_path}")
            
        except Exception as e:
            print(f"Element click issue: {e}")
            error_element_path = os.path.join(screenshots_dir, f"form_error_{timestamp}.png")
            driver.save_screenshot(error_element_path)
            print(f"Form error screenshot: {error_element_path}")
        
        print("\nGenerating final debug report...")
        final_path = os.path.join(screenshots_dir, f"final_state_{timestamp}.png")
        driver.save_screenshot(final_path)
        print(f"Final state screenshot: {final_path}")
        
        print("\nDebug information:")
        print(f"Current URL: {driver.current_url}")
        print(f"Page title: {driver.title}")
        print(f"Window size: {driver.get_window_size()}")
        print(f"Cookies count: {len(driver.get_cookies())}")
        
        all_screenshots = [f for f in os.listdir(screenshots_dir) if f.endswith('.png') and timestamp in f]
        print(f"\nGenerated {len(all_screenshots)} screenshots for debugging")
        
        print("\nDemo 9 completed successfully!")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        
        if driver:
            error_final_path = os.path.join(screenshots_dir, f"error_final_{timestamp}.png")
            try:
                driver.save_screenshot(error_final_path)
                print(f"Error final screenshot: {error_final_path}")
            except:
                print("Could not capture error screenshot")
    
    finally:
        if driver:
            print("Closing browser...")
            driver.quit()

if __name__ == "__main__":
    demo_screenshots_and_debugging()
