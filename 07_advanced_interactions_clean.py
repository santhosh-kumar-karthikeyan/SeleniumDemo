#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def demo_advanced_interactions():
    print("Demo 7: Advanced Interactions")
    print("=" * 35)
    
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    service = Service(ChromeDriverManager().install())
    driver = None
    
    try:
        print("Launching browser...")
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.implicitly_wait(10)
        
        actions = ActionChains(driver)
        wait = WebDriverWait(driver, 10)
        
        print("Testing button interactions...")
        driver.get("https://demoqa.com/buttons")
        
        double_click_btn = wait.until(EC.element_to_be_clickable((By.ID, "doubleClickBtn")))
        actions.double_click(double_click_btn).perform()
        print("Double click performed")
        
        right_click_btn = driver.find_element(By.ID, "rightClickBtn")
        actions.context_click(right_click_btn).perform()
        print("Right click performed")
        
        click_me_btn = driver.find_element(By.XPATH, "//button[text()='Click Me']")
        click_me_btn.click()
        print("Regular click performed")
        
        print("\nTesting drag and drop...")
        driver.get("https://demoqa.com/droppable")
        
        try:
            draggable = wait.until(EC.presence_of_element_located((By.ID, "draggable")))
            droppable = driver.find_element(By.ID, "droppable")
            
            actions.drag_and_drop(draggable, droppable).perform()
            print("Drag and drop completed")
            
            drop_text = droppable.text
            if "Dropped!" in drop_text:
                print("Drag and drop was successful")
            else:
                print("Drag and drop may not have worked as expected")
        except Exception as e:
            print(f"Drag and drop encountered an issue: {e}")
        
        print("\nTesting menu hover interactions...")
        driver.get("https://demoqa.com/menu")
        
        try:
            main_item = wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()='Main Item 2']")))
            actions.move_to_element(main_item).perform()
            time.sleep(1)
            print("Hovered over main menu item")
            
            sub_item = driver.find_element(By.XPATH, "//a[text()='Sub Item']")
            actions.move_to_element(sub_item).perform()
            time.sleep(1)
            print("Hovered over sub menu item")
        except Exception as e:
            print(f"Menu hover test encountered an issue: {e}")
        
        print("\nTesting text input with advanced actions...")
        driver.get("https://demoqa.com/text-box")
        
        name_field = wait.until(EC.presence_of_element_located((By.ID, "userName")))
        
        actions.click(name_field).perform()
        actions.send_keys("Advanced").perform()
        actions.key_down(Keys.SHIFT).send_keys(" interactions").key_up(Keys.SHIFT).perform()
        actions.send_keys(" test").perform()
        print("Advanced text input completed")
        
        actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
        actions.send_keys("Replaced text").perform()
        print("Text selection and replacement completed")
        
        print("\nTesting resizable interactions...")
        driver.get("https://demoqa.com/resizable")
        
        try:
            resizable_handle = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#resizableBoxWithRestriction .react-resizable-handle")))
            
            original_size = driver.find_element(By.ID, "resizableBoxWithRestriction").size
            print(f"Original size: {original_size}")
            
            actions.click_and_hold(resizable_handle).move_by_offset(50, 30).release().perform()
            print("Resizable element interaction completed")
            
            time.sleep(1)
            new_size = driver.find_element(By.ID, "resizableBoxWithRestriction").size
            print(f"New size: {new_size}")
        except Exception as e:
            print(f"Resizable test encountered an issue: {e}")
        
        print("\nTesting sortable interactions...")
        driver.get("https://demoqa.com/sortable")
        
        try:
            sortable_items = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".list-group-item")))
            
            if len(sortable_items) >= 2:
                first_item = sortable_items[0]
                second_item = sortable_items[1]
                
                first_text = first_item.text
                second_text = second_item.text
                print(f"Before sort: First='{first_text}', Second='{second_text}'")
                
                actions.drag_and_drop(first_item, second_item).perform()
                time.sleep(1)
                print("Sortable items reordered")
        except Exception as e:
            print(f"Sortable test encountered an issue: {e}")
        
        print("\nDemo 7 completed successfully!")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    
    finally:
        if driver:
            print("Closing browser...")
            driver.quit()

if __name__ == "__main__":
    demo_advanced_interactions()
