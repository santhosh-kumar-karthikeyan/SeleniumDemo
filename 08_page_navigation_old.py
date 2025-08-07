#!/usr/bin/env python3
"""
Demo 8: Page Navigation and Browser Controls
============================================

This program demonstrates:
- Basic navigation (get, back, forward, refresh)
- Working with multiple tabs/windows
- Browser window management
- Navigation history
- URL manipulation
- Page load timing

Learning Objectives:
- Master browser navigation controls
- Handle multiple windows and tabs
- Manage browser window properties
- Monitor navigation performance
- Work with browser history
"""

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

def demo_page_navigation():
    print("🧭 Demo 8: Page Navigation and Browser Controls")
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
        
        print("🧭 Demo 8: Page Navigation and Browser Controls")
        
        # Start with DemoQA main page
        print("\n1️⃣ Basic navigation operations:")
        driver.get("https://demoqa.com")
        print("   ✅ Navigated to DemoQA homepage")
        print(f"   📄 Page title: {driver.title}")
        print(f"   🔗 Current URL: {driver.current_url}")
        
        # Navigate to Elements section
        print("\n2️⃣ Navigating through site sections:")
        elements_card = driver.find_element(By.XPATH, "//h5[text()='Elements']")
        elements_card.click()
        time.sleep(2)
        
        print("   ✅ Clicked Elements card")
        print(f"   📄 New title: {driver.title}")
        print(f"   🔗 New URL: {driver.current_url}")
        
        # Navigate to Text Box
        text_box_item = driver.find_element(By.XPATH, "//span[text()='Text Box']")
        text_box_item.click()
        time.sleep(2)
        
        print("   ✅ Clicked Text Box item")
        print(f"   📄 Text Box title: {driver.title}")
        print(f"   🔗 Text Box URL: {driver.current_url}")
        
        # Demonstrate back/forward navigation
        print("\n3️⃣ Browser back/forward navigation:")
        driver.back()
        time.sleep(2)
        print("   ⬅️ Navigated back")
        print(f"   📄 After back: {driver.title}")
        print(f"   🔗 After back: {driver.current_url}")
        
        driver.forward()
        time.sleep(2)
        print("   ➡️ Navigated forward")
        print(f"   📄 After forward: {driver.title}")
        print(f"   🔗 After forward: {driver.current_url}")
        
        # Refresh page
        print("\n4️⃣ Page refresh:")
        print("   🔄 Refreshing page...")
        driver.refresh()
        time.sleep(2)
        print("   ✅ Page refreshed")
        print(f"   📄 After refresh: {driver.title}")
        
        # Navigate to different sections for tab/window testing
        print("\n5️⃣ Multiple tab navigation:")
        
        # Open new tab by navigating to different pages
        driver.get("https://demoqa.com/forms")
        print("   ✅ Navigated to Forms section")
        original_window = driver.current_window_handle
        print(f"   🪟 Original window handle: {original_window}")
        
        # Open a link that might open in a new window/tab
        # (Some browsers might block this, so we'll handle it gracefully)
        try:
            # Execute JavaScript to open new window
            driver.execute_script("window.open('https://demoqa.com/widgets', '_blank');")
            time.sleep(2)
            
            # Get all window handles
            all_windows = driver.window_handles
            print(f"   🪟 Total windows/tabs: {len(all_windows)}")
            
            if len(all_windows) > 1:
                # Switch to new window
                new_window = [window for window in all_windows if window != original_window][0]
                driver.switch_to.window(new_window)
                print("   ✅ Switched to new window/tab")
                print(f"   📄 New tab title: {driver.title}")
                print(f"   🔗 New tab URL: {driver.current_url}")
                
                # Navigate in new tab
                try:
                    accordian_item = driver.find_element(By.XPATH, "//span[text()='Accordian']")
                    accordian_item.click()
                    time.sleep(2)
                    print("   ✅ Navigated in new tab")
                except:
                    print("   ⚠️ Could not find Accordian item")
                
                # Switch back to original window
                driver.switch_to.window(original_window)
                print("   ✅ Switched back to original window")
                print(f"   📄 Original tab title: {driver.title}")
                
                # Close new tab
                driver.switch_to.window(new_window)
                driver.close()
                driver.switch_to.window(original_window)
                print("   ✅ Closed new tab")
            else:
                print("   ⚠️ New tab/window was not opened (may be blocked)")
                
        except Exception as e:
            print(f"   ❌ Tab/window management failed: {str(e)}")
        
        # Navigate to different sections systematically
        print("\n6️⃣ Systematic navigation through sections:")
        
        sections = [
            ("https://demoqa.com/elements", "Elements"),
            ("https://demoqa.com/forms", "Forms"),
            ("https://demoqa.com/alerts-frame-windows", "Alerts, Frame & Windows"),
            ("https://demoqa.com/widgets", "Widgets"),
            ("https://demoqa.com/interaction", "Interactions"),
            ("https://demoqa.com/book-store-application", "Book Store")
        ]
        
        navigation_history = []
        
        for url, section_name in sections:
            try:
                print(f"   🧭 Navigating to {section_name}...")
                driver.get(url)
                time.sleep(1)
                
                # Record navigation
                current_info = {
                    'section': section_name,
                    'url': driver.current_url,
                    'title': driver.title,
                    'timestamp': time.time()
                }
                navigation_history.append(current_info)
                
                print(f"   ✅ Successfully loaded {section_name}")
                print(f"      📄 Title: {driver.title}")
                
            except Exception as e:
                print(f"   ❌ Failed to navigate to {section_name}: {str(e)}")
        
        # Display navigation history
        print("\n7️⃣ Navigation history summary:")
        for i, nav_item in enumerate(navigation_history, 1):
            print(f"   {i}. {nav_item['section']}")
            print(f"      URL: {nav_item['url']}")
            print(f"      Title: {nav_item['title']}")
        
        # Test navigation timing
        print("\n8️⃣ Navigation performance testing:")
        test_urls = [
            "https://demoqa.com/text-box",
            "https://demoqa.com/buttons",
            "https://demoqa.com/dynamic-properties"
        ]
        
        for test_url in test_urls:
            start_time = time.time()
            driver.get(test_url)
            end_time = time.time()
            
            load_time = (end_time - start_time) * 1000  # Convert to milliseconds
            print(f"   ⏱️ {test_url.split('/')[-1]}: {load_time:.2f}ms")
        
        # Window/browser management
        print("\n9️⃣ Window and browser management:")
        
        # Get window size and position
        window_size = driver.get_window_size()
        window_position = driver.get_window_position()
        
        print(f"   📐 Current window size: {window_size['width']}x{window_size['height']}")
        print(f"   📍 Current window position: ({window_position['x']}, {window_position['y']})")
        
        # Resize window
        print("   📏 Resizing window...")
        driver.set_window_size(1024, 768)
        time.sleep(1)
        
        new_size = driver.get_window_size()
        print(f"   📐 New window size: {new_size['width']}x{new_size['height']}")
        
        # Maximize window
        print("   🔍 Maximizing window...")
        driver.maximize_window()
        time.sleep(1)
        
        max_size = driver.get_window_size()
        print(f"   📐 Maximized size: {max_size['width']}x{max_size['height']}")
        
        # Final navigation test
        print("\n🔟 Final navigation verification:")
        driver.get("https://demoqa.com")
        time.sleep(2)
        
        print(f"   📄 Final page title: {driver.title}")
        print(f"   🔗 Final URL: {driver.current_url}")
        print("   ✅ Navigation test completed successfully!")
        
        print("\n✅ Demo 8 completed successfully!")
        
    except Exception as e:
        print(f"❌ An error occurred: {str(e)}")
    
    finally:
        if driver:
            print("🔒 Closing browser...")
            driver.quit()

if __name__ == "__main__":
    demo_page_navigation()
