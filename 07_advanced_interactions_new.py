#!/usr/bin/env python3
"""
Demo 7: Advanced Interactions - Mouse and Keyboard Actions
=========================================================

This program demonstrates:
- Mouse actions (click, double-click, right-click)
- Drag and drop operations
- Hover (mouseover) effects
- Keyboard shortcuts and combinations
- ActionChains for complex interactions
- Element resizing and sorting

Learning Objectives:
- Master ActionChains for complex interactions
- Handle drag and drop operations
- Work with hover effects and menus
- Use keyboard shortcuts effectively
- Implement advanced mouse operations
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def demo_advanced_interactions():
    print("🎮 Demo 7: Advanced Interactions")
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
        
        print("🎮 Demo 7: Advanced Interactions - Mouse and Keyboard Actions")
        
        # Navigate to DemoQA interactions page
        driver.get("https://demoqa.com/buttons")
        print("🌐 Navigated to Buttons interaction page")
        
        # Create ActionChains instance for advanced interactions
        actions = ActionChains(driver)
        
        print("\n🎯 Testing button interactions...")
        
        # Example 1: Double-click
        print("\n1️⃣ Double-click interaction:")
        try:
            double_click_btn = driver.find_element(By.ID, "doubleClickBtn")
            actions.double_click(double_click_btn).perform()
            print("   ✅ Performed double-click on button")
            
            # Check for success message
            try:
                double_click_msg = driver.find_element(By.ID, "doubleClickMessage")
                if double_click_msg.text:
                    print(f"   Message: {double_click_msg.text}")
            except:
                print("   ❌ No double-click message found")
        except Exception as e:
            print(f"   ❌ Double-click failed: {str(e)}")
        
        # Example 2: Right-click (context menu)
        print("\n2️⃣ Right-click interaction:")
        try:
            right_click_btn = driver.find_element(By.ID, "rightClickBtn")
            actions.context_click(right_click_btn).perform()
            print("   ✅ Performed right-click on button")
            
            # Check for success message
            try:
                right_click_msg = driver.find_element(By.ID, "rightClickMessage")
                if right_click_msg.text:
                    print(f"   Message: {right_click_msg.text}")
            except:
                print("   ❌ No right-click message found")
        except Exception as e:
            print(f"   ❌ Right-click failed: {str(e)}")
        
        # Example 3: Regular click with dynamic ID
        print("\n3️⃣ Dynamic click interaction:")
        try:
            # This button has a dynamic ID but can be found by xpath
            click_me_btn = driver.find_element(By.XPATH, "//button[text()='Click Me']")
            click_me_btn.click()
            print("   ✅ Performed click on dynamic button")
            
            # Check for success message
            try:
                click_msg = driver.find_element(By.ID, "dynamicClickMessage")
                if click_msg.text:
                    print(f"   Message: {click_msg.text}")
            except:
                print("   ❌ No click message found")
        except Exception as e:
            print(f"   ❌ Dynamic click failed: {str(e)}")
        
        # Example 4: Drag and Drop interactions
        print("\n4️⃣ Drag and Drop interaction:")
        driver.get("https://demoqa.com/droppable")
        
        try:
            drag_element = driver.find_element(By.ID, "draggable")
            drop_element = driver.find_element(By.ID, "droppable")
            
            print("   Before drag and drop:")
            print(f"   Drop area text: '{drop_element.text}'")
            
            # Perform drag and drop
            actions.drag_and_drop(drag_element, drop_element).perform()
            print("   ✅ Performed drag and drop")
            
            # Check if drop was successful
            time.sleep(1)
            drop_text_after = drop_element.text
            print(f"   Drop area text after: '{drop_text_after}'")
            
            if "Dropped!" in drop_text_after:
                print("   ✅ Drag and drop was successful!")
            else:
                print("   ❌ Drag and drop may not have worked")
                
        except Exception as e:
            print(f"   ❌ Drag and drop failed: {str(e)}")
        
        # Example 5: Hover interactions
        print("\n5️⃣ Hover (mouseover) interactions:")
        driver.get("https://demoqa.com/menu")
        
        try:
            # Hover over main menu item
            main_item = driver.find_element(By.XPATH, "//a[text()='Main Item 2']")
            actions.move_to_element(main_item).perform()
            print("   ✅ Hovered over 'Main Item 2'")
            
            time.sleep(1)
            
            # Try to hover over submenu item
            try:
                sub_item = driver.find_element(By.XPATH, "//a[text()='Sub Item']")
                actions.move_to_element(sub_item).perform()
                print("   ✅ Hovered over sub-item")
                
                # Click the sub item
                sub_item.click()
                print("   ✅ Clicked sub-item")
            except:
                print("   ❌ Could not interact with sub-menu")
                
        except Exception as e:
            print(f"   ❌ Hover interaction failed: {str(e)}")
        
        # Example 6: Keyboard interactions
        print("\n6️⃣ Keyboard interactions:")
        driver.get("https://demoqa.com/text-box")
        
        try:
            name_field = driver.find_element(By.ID, "userName")
            name_field.clear()
            
            # Type using ActionChains
            actions.click(name_field).perform()
            actions.send_keys("John Doe").perform()
            print("   ✅ Typed name using ActionChains")
            
            # Use keyboard shortcuts
            actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
            print("   ✅ Selected all text with Ctrl+A")
            
            actions.send_keys("Jane Smith").perform()
            print("   ✅ Replaced text with new name")
            
            # Tab to next field
            actions.send_keys(Keys.TAB).perform()
            print("   ✅ Tabbed to next field")
            
            # Type email
            actions.send_keys("jane.smith@example.com").perform()
            print("   ✅ Typed email using Tab navigation")
            
        except Exception as e:
            print(f"   ❌ Keyboard interactions failed: {str(e)}")
        
        # Example 7: Resizable interactions
        print("\n7️⃣ Resizable element interactions:")
        driver.get("https://demoqa.com/resizable")
        
        try:
            # Find resizable element and its handle
            resizable_box = driver.find_element(By.ID, "resizableBoxWithRestriction")
            resize_handle = driver.find_element(By.CSS_SELECTOR, "#resizableBoxWithRestriction .react-resizable-handle")
            
            print("   Initial size of resizable box:")
            initial_size = resizable_box.size
            print(f"   Width: {initial_size['width']}, Height: {initial_size['height']}")
            
            # Drag the resize handle
            actions.click_and_hold(resize_handle).move_by_offset(50, 30).release().perform()
            print("   ✅ Resized the box")
            
            # Check new size
            time.sleep(1)
            new_size = resizable_box.size
            print(f"   New size - Width: {new_size['width']}, Height: {new_size['height']}")
            
            if new_size['width'] > initial_size['width'] or new_size['height'] > initial_size['height']:
                print("   ✅ Box was successfully resized!")
            else:
                print("   ❌ Box may not have been resized")
                
        except Exception as e:
            print(f"   ❌ Resize interaction failed: {str(e)}")
        
        # Example 8: Sortable interactions
        print("\n8️⃣ Sortable list interactions:")
        driver.get("https://demoqa.com/sortable")
        
        try:
            # Get the sortable items
            sortable_items = driver.find_elements(By.CSS_SELECTOR, ".vertical-list-container .list-group-item")
            
            if len(sortable_items) >= 2:
                print(f"   Found {len(sortable_items)} sortable items")
                
                # Get initial order
                initial_order = [item.text for item in sortable_items]
                print(f"   Initial order: {initial_order}")
                
                # Move first item to second position
                first_item = sortable_items[0]
                second_item = sortable_items[1]
                
                actions.drag_and_drop(first_item, second_item).perform()
                print("   ✅ Moved first item to second position")
                
                # Check new order
                time.sleep(1)
                new_items = driver.find_elements(By.CSS_SELECTOR, ".vertical-list-container .list-group-item")
                new_order = [item.text for item in new_items]
                print(f"   New order: {new_order}")
                
                if new_order != initial_order:
                    print("   ✅ List order was changed!")
                else:
                    print("   ❌ List order was not changed")
            else:
                print("   ❌ Not enough sortable items found")
                
        except Exception as e:
            print(f"   ❌ Sortable interaction failed: {str(e)}")
        
        print("\n✅ Advanced interactions demo completed!")
        
    except Exception as e:
        print(f"❌ An error occurred: {str(e)}")
    
    finally:
        if driver:
            print("🔒 Closing browser...")
            driver.quit()

if __name__ == "__main__":
    demo_advanced_interactions()
