#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def demo_page_navigation():
    print("Demo 8: Page Navigation and Browser Controls")
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
        
        print("Starting navigation tests...")
        driver.get("https://demoqa.com/")
        print(f"Initial page: {driver.title}")
        
        print("\nNavigating to Elements section...")
        driver.get("https://demoqa.com/elements")
        print(f"Current page: {driver.title}")
        
        print("Navigating to Forms section...")
        driver.get("https://demoqa.com/automation-practice-form")
        print(f"Current page: {driver.title}")
        
        print("Testing browser back navigation...")
        driver.back()
        print(f"After back: {driver.current_url}")
        
        print("Testing browser forward navigation...")
        driver.forward()
        print(f"After forward: {driver.current_url}")
        
        print("Testing page refresh...")
        driver.refresh()
        print("Page refreshed successfully")
        
        print("\nTesting window management...")
        original_window = driver.current_window_handle
        print(f"Original window handle: {original_window}")
        
        print("Opening new tab...")
        driver.get("https://demoqa.com/browser-windows")
        
        new_tab_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "tabButton"))
        )
        new_tab_button.click()
        
        WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
        windows = driver.window_handles
        print(f"Total windows: {len(windows)}")
        
        for window in windows:
            if window != original_window:
                driver.switch_to.window(window)
                print(f"Switched to new window: {driver.current_url}")
                break
        
        try:
            sample_text = driver.find_element(By.ID, "sampleHeading")
            print(f"New window content: {sample_text.text}")
        except:
            print("Could not find expected content in new window")
        
        driver.close()
        driver.switch_to.window(original_window)
        print("Returned to original window")
        
        print("\nTesting new window functionality...")
        new_window_button = driver.find_element(By.ID, "windowButton")
        new_window_button.click()
        
        WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
        windows = driver.window_handles
        
        for window in windows:
            if window != original_window:
                driver.switch_to.window(window)
                print("Opened new window successfully")
                break
        
        driver.close()
        driver.switch_to.window(original_window)
        
        print("\nTesting performance and page metrics...")
        start_time = time.time()
        driver.get("https://demoqa.com/text-box")
        load_time = time.time() - start_time
        print(f"Page load time: {load_time:.2f} seconds")
        
        page_size = len(driver.page_source)
        print(f"Page source size: {page_size} characters")
        
        window_size = driver.get_window_size()
        print(f"Window size: {window_size['width']}x{window_size['height']}")
        
        print("Maximizing window...")
        driver.maximize_window()
        time.sleep(1)
        
        maximized_size = driver.get_window_size()
        print(f"Maximized size: {maximized_size['width']}x{maximized_size['height']}")
        
        print("Setting custom window size...")
        driver.set_window_size(1280, 720)
        time.sleep(1)
        
        custom_size = driver.get_window_size()
        print(f"Custom size: {custom_size['width']}x{custom_size['height']}")
        
        print("\nTesting cookies...")
        cookies_before = len(driver.get_cookies())
        print(f"Cookies before: {cookies_before}")
        
        driver.add_cookie({"name": "test_cookie", "value": "selenium_demo"})
        
        cookies_after = len(driver.get_cookies())
        print(f"Cookies after adding: {cookies_after}")
        
        test_cookie = driver.get_cookie("test_cookie")
        if test_cookie:
            print(f"Test cookie value: {test_cookie['value']}")
        
        driver.delete_cookie("test_cookie")
        cookies_final = len(driver.get_cookies())
        print(f"Cookies after deletion: {cookies_final}")
        
        print("\nDemo 8 completed successfully!")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    
    finally:
        if driver:
            print("Closing browser...")
            driver.quit()

if __name__ == "__main__":
    demo_page_navigation()
