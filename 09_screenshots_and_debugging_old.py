#!/usr/bin/env python3
"""
Demo 9: Screenshots and Debugging Techniques
============================================

This program demonstrates:
- Taking screenshots for debugging
- Element-specific screenshots
- Console log capture
- Network activity monitoring
- Error handling and debugging
- Performance metrics

Learning Objectives:
- Capture screenshots for debugging
- Extract browser logs for troubleshooting
- Handle JavaScript errors
- Monitor page performance
- Debug failing tests effectively
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import os
import base64
from datetime import datetime

def demo_screenshots_and_debugging():
    print("🐛 Demo 9: Screenshots and Debugging")
    print("=" * 40)
    
    # Setup ChromeDriver with debugging options
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--enable-logging")
    chrome_options.add_argument("--v=1")
    # Enable performance logging
    chrome_options.set_capability("goog:loggingPrefs", {"performance": "ALL", "browser": "ALL"})
    
    service = Service(ChromeDriverManager().install())
    driver = None
    
    try:
        # Launch browser
        print("🚀 Launching browser with debugging enabled...")
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.implicitly_wait(10)
        
        # Create screenshots directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        screenshots_dir = os.path.join(current_dir, "screenshots")
        os.makedirs(screenshots_dir, exist_ok=True)
        
        print("\n1️⃣ Basic Screenshot Capture")
        
        # Navigate to DemoQA
        driver.get("https://demoqa.com/text-box")
        print("📸 Taking full page screenshot...")
        
        # Take full page screenshot
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = os.path.join(screenshots_dir, f"demoqa_textbox_{timestamp}.png")
        driver.save_screenshot(screenshot_path)
        print(f"   ✅ Screenshot saved: {screenshot_path}")
        
        # Get screenshot as base64 (for embedding in reports)
        screenshot_base64 = driver.get_screenshot_as_base64()
        print(f"   📊 Screenshot size (base64): {len(screenshot_base64)} characters")
        
        print("\n2️⃣ Element-Specific Screenshots")
        
        # Find and screenshot the form
        try:
            form_element = driver.find_element(By.ID, "userForm")
            print("📸 Taking element-specific screenshot...")
            
            # Take screenshot of specific element
            element_screenshot = form_element.screenshot_as_png
            element_path = os.path.join(screenshots_dir, f"form_element_{timestamp}.png")
            
            with open(element_path, "wb") as f:
                f.write(element_screenshot)
            
            print(f"   ✅ Element screenshot saved: {element_path}")
            
        except Exception as e:
            print(f"   ❌ Failed to capture element screenshot: {str(e)}")
        
        print("\n3️⃣ Browser Console Logs")
        
        # Navigate to a page that might have console messages
        driver.get("https://demoqa.com/broken")
        print("🌐 Loaded broken images/links page for console log testing")
        
        # Capture initial console logs
        print("📋 Capturing initial console logs...")
        initial_logs = driver.get_log('browser')
        
        print(f"   Initial browser logs: {len(initial_logs)} entries")
        for log_entry in initial_logs[:3]:  # Show first 3 entries
            level = log_entry['level']
            message = log_entry['message']
            print(f"   [{level}] {message}")
        
        print("\n4️⃣ Testing Form Interaction with Screenshots")
        
        # Go to text box form for testing
        driver.get("https://demoqa.com/text-box")
        
        # Fill form to test interactions and capture screenshots
        print("🔥 Testing form interaction with screenshots...")
        
        try:
            # Fill form fields
            name_field = driver.find_element(By.ID, "userName")
            name_field.clear()
            name_field.send_keys("Debug Test User")
            
            email_field = driver.find_element(By.ID, "userEmail")
            email_field.clear()
            email_field.send_keys("debug@test.com")
            
            # Take screenshot after filling form
            form_filled_screenshot = os.path.join(screenshots_dir, f"form_filled_{timestamp}.png")
            driver.save_screenshot(form_filled_screenshot)
            print(f"   📸 Form filled screenshot saved: {form_filled_screenshot}")
            
            # Submit form
            submit_button = driver.find_element(By.ID, "submit")
            submit_button.click()
            
            # Wait for output and capture
            time.sleep(2)
            output_screenshot = os.path.join(screenshots_dir, f"form_output_{timestamp}.png")
            driver.save_screenshot(output_screenshot)
            print(f"   📸 Form output screenshot saved: {output_screenshot}")
            
        except Exception as e:
            print(f"   ❌ Form interaction failed: {str(e)}")
            error_screenshot = os.path.join(screenshots_dir, f"form_error_{timestamp}.png")
            driver.save_screenshot(error_screenshot)
        
        # Capture logs after form interaction
        form_logs = driver.get_log('browser')
        print(f"   Form interaction logs: {len(form_logs)} entries")
        for log_entry in form_logs[-3:]:  # Show last 3 entries
            level = log_entry['level']
            message = log_entry['message']
            print(f"   [{level}] {message}")
        
        print("\n5️⃣ Testing Dynamic Content and Screenshots")
        
        # Navigate to dynamic properties page
        driver.get("https://demoqa.com/dynamic-properties")
        print("🌐 Loaded dynamic properties page")
        
        # Take screenshot before changes
        before_dynamic_screenshot = os.path.join(screenshots_dir, f"before_dynamic_{timestamp}.png")
        driver.save_screenshot(before_dynamic_screenshot)
        print(f"   📸 Before dynamic changes: {before_dynamic_screenshot}")
        
        # Wait for dynamic button to become enabled
        print("⏰ Waiting for dynamic button to become enabled...")
        try:
            wait = WebDriverWait(driver, 10)
            enable_button = wait.until(EC.element_to_be_clickable((By.ID, "enableAfter")))
            
            # Take screenshot after button becomes enabled
            after_enabled_screenshot = os.path.join(screenshots_dir, f"button_enabled_{timestamp}.png")
            driver.save_screenshot(after_enabled_screenshot)
            print(f"   📸 Button enabled screenshot: {after_enabled_screenshot}")
            
            enable_button.click()
            print("   ✅ Successfully clicked enabled button")
            
        except TimeoutException:
            print("   ❌ Button did not become enabled in time")
            timeout_screenshot = os.path.join(screenshots_dir, f"timeout_button_{timestamp}.png")
            driver.save_screenshot(timeout_screenshot)
        
        print("\n6️⃣ Testing Broken Elements and Error Handling")
        
        # Navigate to broken images/links page for error demonstration
        driver.get("https://demoqa.com/broken")
        print("🌐 Testing broken links and images page")
        
        # Take screenshot of broken elements page
        broken_page_screenshot = os.path.join(screenshots_dir, f"broken_page_{timestamp}.png")
        driver.save_screenshot(broken_page_screenshot)
        print(f"   📸 Broken page screenshot: {broken_page_screenshot}")
        
        # Try to interact with potentially broken elements
        try:
            broken_links = driver.find_elements(By.XPATH, "//a[contains(@href, 'http')]")
            print(f"   Found {len(broken_links)} external links to test")
            
            # Test first broken link if available
            if broken_links:
                first_link = broken_links[0]
                link_href = first_link.get_attribute("href")
                print(f"   Testing link: {link_href}")
                
                # Take screenshot before clicking potentially broken link
                before_click_screenshot = os.path.join(screenshots_dir, f"before_broken_link_{timestamp}.png")
                driver.save_screenshot(before_click_screenshot)
                
                try:
                    first_link.click()
                    time.sleep(3)  # Wait to see if page loads or breaks
                    
                    # Take screenshot after clicking
                    after_click_screenshot = os.path.join(screenshots_dir, f"after_broken_link_{timestamp}.png")
                    driver.save_screenshot(after_click_screenshot)
                    print(f"   📸 After broken link click: {after_click_screenshot}")
                    
                except Exception as link_error:
                    print(f"   ❌ Link click failed: {str(link_error)}")
                    link_error_screenshot = os.path.join(screenshots_dir, f"link_error_{timestamp}.png")
                    driver.save_screenshot(link_error_screenshot)
                    
        except Exception as e:
            print(f"   ❌ Error testing broken elements: {str(e)}")
        
        print("\n7️⃣ Performance Monitoring")
        
        # Get performance logs
        try:
            print("📊 Capturing performance logs...")
            performance_logs = driver.get_log('performance')
            
            print(f"   Performance log entries: {len(performance_logs)}")
            
            # Analyze performance data
            navigation_events = []
            resource_events = []
            
            for log_entry in performance_logs:
                message = log_entry.get('message', '')
                if 'Navigation' in message:
                    navigation_events.append(log_entry)
                elif 'Resource' in message:
                    resource_events.append(log_entry)
            
            print(f"   Navigation events: {len(navigation_events)}")
            print(f"   Resource events: {len(resource_events)}")
            
        except Exception as e:
            print(f"   ⚠️ Performance logs not available: {str(e)}")
        
        # Get page timing information using JavaScript
        print("⏱️ Getting page timing information...")
        timing_script = """
        var timing = performance.timing;
        return {
            'navigationStart': timing.navigationStart,
            'loadEventEnd': timing.loadEventEnd,
            'domContentLoaded': timing.domContentLoadedEventEnd - timing.navigationStart,
            'pageLoad': timing.loadEventEnd - timing.navigationStart
        };
        """
        
        try:
            timing_data = driver.execute_script(timing_script)
            print("   Page timing data:")
            for key, value in timing_data.items():
                if isinstance(value, (int, float)) and value > 0:
                    if key in ['domContentLoaded', 'pageLoad']:
                        print(f"   {key}: {value}ms")
                    else:
                        print(f"   {key}: {value}")
        except Exception as e:
            print(f"   ⚠️ Could not get timing data: {str(e)}")
        
        print("\n8️⃣ Error Handling and Debugging Scenarios")
        
        # Return to a stable page for testing
        driver.get("https://demoqa.com/elements")
        
        # Demonstrate handling missing elements
        print("🔍 Testing element finding scenarios...")
        
        # Try to find existing element
        try:
            existing_element = driver.find_element(By.XPATH, "//span[text()='Text Box']")
            print("   ✅ Found existing element: Text Box")
        except NoSuchElementException as e:
            print(f"   ❌ Could not find element: {str(e)}")
            # Take screenshot when element not found
            debug_screenshot = os.path.join(screenshots_dir, f"element_not_found_{timestamp}.png")
            driver.save_screenshot(debug_screenshot)
        
        # Try to find non-existing element
        try:
            print("   🔎 Searching for non-existent element...")
            non_existent = driver.find_element(By.ID, "nonExistentElement")
        except NoSuchElementException as e:
            print(f"   ✅ Correctly caught NoSuchElementException")
            # Take screenshot for debugging
            no_element_screenshot = os.path.join(screenshots_dir, f"no_element_debug_{timestamp}.png")
            driver.save_screenshot(no_element_screenshot)
            print(f"   📸 Debug screenshot saved: {no_element_screenshot}")
        
        # Test timeout scenario
        print("⏰ Testing timeout scenario...")
        try:
            short_wait = WebDriverWait(driver, 2)  # Very short timeout
            short_wait.until(EC.presence_of_element_located((By.ID, "willNeverExist")))
        except TimeoutException as e:
            print("   ✅ Correctly caught TimeoutException")
            timeout_screenshot = os.path.join(screenshots_dir, f"timeout_debug_{timestamp}.png")
            driver.save_screenshot(timeout_screenshot)
            print(f"   📸 Timeout debug screenshot saved: {timeout_screenshot}")
        
        print("\n9️⃣ Final Debug Information Summary")
        
        # Take final screenshot
        final_screenshot = os.path.join(screenshots_dir, f"final_state_{timestamp}.png")
        driver.save_screenshot(final_screenshot)
        print(f"   📸 Final screenshot saved: {final_screenshot}")
        
        # Get final browser logs
        all_logs = driver.get_log('browser')
        print(f"📋 Total browser log entries: {len(all_logs)}")
        
        # Categorize logs
        log_levels = {}
        for log_entry in all_logs:
            level = log_entry['level']
            log_levels[level] = log_levels.get(level, 0) + 1
        
        print("   Log level summary:")
        for level, count in log_levels.items():
            print(f"   {level}: {count} entries")
        
        # Page information
        print(f"📄 Final page title: {driver.title}")
        print(f"🔗 Final URL: {driver.current_url}")
        
        # Browser information
        user_agent = driver.execute_script("return navigator.userAgent;")
        print(f"🌐 User Agent: {user_agent}")
        
        print("\n📊 Debugging and Screenshots Summary:")
        print("   ✅ Full page screenshots")
        print("   ✅ Element-specific screenshots")
        print("   ✅ Browser console log capture")
        print("   ✅ Performance monitoring")
        print("   ✅ Error handling demonstrations")
        print("   ✅ Dynamic content testing")
        print("   ✅ Debug information extraction")
        
        print(f"\n📁 All screenshots saved in: {screenshots_dir}")
        
        print("\n⏳ Final pause to observe results...")
        time.sleep(3)
        
        print("\n✅ Demo 9 completed successfully!")
        
    except Exception as e:
        print(f"❌ An error occurred: {str(e)}")
        import traceback
        print(f"   Traceback: {traceback.format_exc()}")
        
        # Take error screenshot if possible
        try:
            if driver and 'timestamp' in locals() and 'screenshots_dir' in locals():
                error_screenshot = os.path.join(screenshots_dir, f"error_debug_{timestamp}.png")
                driver.save_screenshot(error_screenshot)
                print(f"   📸 Error debug screenshot saved: {error_screenshot}")
        except:
            pass
    
    finally:
        if driver:
            print("🔒 Closing browser...")
            driver.quit()

if __name__ == "__main__":
    demo_screenshots_and_debugging()
