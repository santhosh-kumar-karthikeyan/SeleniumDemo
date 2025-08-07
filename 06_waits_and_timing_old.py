#!/usr/bin/env python3
"""
Demo 6: Waits and Timing - Mastering Synchronization
====================================================

This program demonstrates:
- Implicit waits vs Explicit waits
- WebDriverWait with various conditions
- Handling dynamic content loading
- Time-based waits vs condition-based waits
- Custom wait conditions

Learning Objectives:
- Understand different types of waits
- Handle AJAX and dynamic content
- Avoid race conditions
- Optimize test execution time
- Handle loading states properly
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import os

def demo_waits_and_timing():
    print("⏰ Demo 6: Waits and Timing")
    print("=" * 35)
    
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
        
        print("\n1️⃣ Implicit Wait Demonstration")
        print("Setting implicit wait to 10 seconds...")
        # Implicit wait - applies to all find_element operations
        driver.implicitly_wait(10)
        
        # Navigate to DemoQA
        driver.get("https://demoqa.com/dynamic-properties")
        print("✅ Page loaded (with implicit wait protection)")
        
        print("\n2️⃣ Explicit Wait Demonstrations")
        
        # Create WebDriverWait instance
        wait = WebDriverWait(driver, 15)  # 15 second timeout
        
        # Wait for page to be ready
        print("Waiting for page elements to be present...")
        start_time = time.time()
        page_heading = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".main-header")))
        end_time = time.time()
        print(f"✅ Page elements found in {end_time - start_time:.2f} seconds")
        
        # Wait for dynamic button to become enabled
        print("Waiting for 'Enable After 5 Seconds' button...")
        start_time = time.time()
        try:
            enable_button = wait.until(EC.element_to_be_clickable((By.ID, "enableAfter")))
            end_time = time.time()
            print(f"✅ Button became enabled in {end_time - start_time:.2f} seconds")
        except TimeoutException:
            end_time = time.time()
            print(f"❌ Button not enabled after {end_time - start_time:.2f} seconds")
        
        # Wait for color change button
        print("Waiting for color change button...")
        try:
            color_button = driver.find_element(By.ID, "colorChange")
            initial_class = color_button.get_attribute("class")
            print(f"   Initial button class: {initial_class}")
            
            start_time = time.time()
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#colorChange.text-success")))
            end_time = time.time()
            final_class = color_button.get_attribute("class")
            print(f"✅ Button color changed in {end_time - start_time:.2f} seconds")
            print(f"   Final button class: {final_class}")
        except TimeoutException:
            print("❌ Button color did not change within timeout")
        
        print("\n3️⃣ Waiting for Progress Bar Completion")
        
        # Navigate to progress bar page
        driver.get("https://demoqa.com/progress-bar")
        print("Navigated to progress bar demo...")
        
        # Start progress bar
        start_button = wait.until(EC.element_to_be_clickable((By.ID, "startStopButton")))
        start_button.click()
        print("Started progress bar...")
        
        # Wait for progress bar to complete
        start_time = time.time()
        try:
            wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".progress-bar"), "100%"))
            end_time = time.time()
            print(f"✅ Progress bar completed in {end_time - start_time:.2f} seconds")
        except TimeoutException:
            end_time = time.time()
            progress_element = driver.find_element(By.CSS_SELECTOR, ".progress-bar")
            current_progress = progress_element.text
            print(f"❌ Progress bar did not complete in {end_time - start_time:.2f} seconds")
            print(f"   Current progress: {current_progress}")
        
        print("\n4️⃣ Advanced Wait Conditions with Alerts")
        
        # Navigate to alerts page
        driver.get("https://demoqa.com/alerts")
        
        # Test timer alert
        try:
            timer_alert_button = wait.until(EC.element_to_be_clickable((By.ID, "timerAlertButton")))
            timer_alert_button.click()
            print("Clicked timer alert button...")
            
            start_time = time.time()
            alert = wait.until(EC.alert_is_present())
            end_time = time.time()
            alert_text = alert.text
            print(f"✅ Alert appeared in {end_time - start_time:.2f} seconds")
            print(f"   Alert text: '{alert_text}'")
            alert.accept()
            
        except TimeoutException:
            print("❌ Alert did not appear within timeout")
        
        print("\n5️⃣ Custom Wait Conditions")
        
        # Navigate to form page for custom conditions
        driver.get("https://demoqa.com/text-box")
        
        # Custom condition: wait for form to be ready (all required fields present)
        def form_ready(driver):
            """Custom condition: returns True when form has all required fields"""
            try:
                required_fields = ["userName", "userEmail", "currentAddress", "permanentAddress"]
                for field_id in required_fields:
                    driver.find_element(By.ID, field_id)
                return True
            except:
                return False
        
        print("Waiting for form to be fully ready...")
        try:
            start_time = time.time()
            wait.until(form_ready)
            end_time = time.time()
            print(f"✅ Form ready in {end_time - start_time:.2f} seconds")
        except TimeoutException:
            print("❌ Form not ready within timeout")
        
        # Test form interaction with waits
        try:
            name_field = wait.until(EC.element_to_be_clickable((By.ID, "userName")))
            name_field.clear()
            name_field.send_keys("Test User")
            
            email_field = wait.until(EC.element_to_be_clickable((By.ID, "userEmail")))
            email_field.clear()
            email_field.send_keys("test@example.com")
            
            submit_button = wait.until(EC.element_to_be_clickable((By.ID, "submit")))
            submit_button.click()
            
            # Wait for output to appear
            output_section = wait.until(EC.visibility_of_element_located((By.ID, "output")))
            print("✅ Form submitted and output appeared!")
            
        except (TimeoutException, Exception) as e:
            print(f"❌ Form interaction failed: {str(e)}")
        
        print("\n6️⃣ Wait Condition Comparisons")
        
        # Test different wait strategies on the same element
        test_element_id = "userName"
        wait_strategies = [
            ("presence_of_element_located", EC.presence_of_element_located((By.ID, test_element_id))),
            ("visibility_of_element_located", EC.visibility_of_element_located((By.ID, test_element_id))),
            ("element_to_be_clickable", EC.element_to_be_clickable((By.ID, test_element_id)))
        ]
        
        for strategy_name, condition in wait_strategies:
            try:
                start_time = time.time()
                element = wait.until(condition)
                end_time = time.time()
                print(f"✅ {strategy_name}: {end_time - start_time:.3f}s")
            except TimeoutException:
                print(f"❌ {strategy_name}: Timeout")
        
        print("\n7️⃣ Handling Timeout Exceptions")
        
        # Demonstrate timeout handling
        try:
            print("Attempting to find non-existent element (will timeout)...")
            short_wait = WebDriverWait(driver, 2)  # Very short timeout
            start_time = time.time()
            short_wait.until(EC.presence_of_element_located((By.ID, "non-existent-element")))
        except TimeoutException as e:
            end_time = time.time()
            print(f"✅ Caught TimeoutException after {end_time - start_time:.2f} seconds")
            print(f"   Exception message: {str(e)}")
        
        print("\n8️⃣ Performance Comparison: Sleep vs Wait")
        
        # Bad practice: using sleep
        print("Using time.sleep(2) - Always waits full duration...")
        start_time = time.time()
        time.sleep(2)
        end_time = time.time()
        print(f"   Time.sleep(2) took exactly {end_time - start_time:.2f} seconds")
        
        # Good practice: using WebDriverWait
        print("Using WebDriverWait - Returns as soon as condition is met...")
        start_time = time.time()
        wait.until(EC.presence_of_element_located((By.NAME, "q")))
        end_time = time.time()
        print(f"   WebDriverWait took only {end_time - start_time:.3f} seconds")
        
        print("\n📊 Wait Strategy Summary:")
        print("   ✅ Implicit Wait: Global timeout for all find operations")
        print("   ✅ Explicit Wait: Condition-based waiting with custom timeout")
        print("   ✅ WebDriverWait: Most flexible and reliable")
        print("   ❌ time.sleep(): Inefficient, always waits full duration")
        
        print("\n⏳ Final pause to observe results...")
        time.sleep(3)
        
        print("\n✅ Demo 6 completed successfully!")
        
    except Exception as e:
        print(f"❌ An error occurred: {str(e)}")
        import traceback
        print(f"   Traceback: {traceback.format_exc()}")
    
    finally:
        if driver:
            print("🔒 Closing browser...")
            driver.quit()

if __name__ == "__main__":
    demo_waits_and_timing()
