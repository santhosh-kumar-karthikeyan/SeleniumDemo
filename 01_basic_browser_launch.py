#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def demo_basic_browser():
    print("Demo 1: Basic Browser Launch and Navigation")
    print("=" * 50)
    
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    service = Service(ChromeDriverManager().install())
    
    try:
        print("Setting up ChromeDriver...")
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        driver.implicitly_wait(10)
        
        print("Opening DemoQA test site...")
        driver.get("https://demoqa.com/books")
        
        page_title = driver.title
        print(f"Page title: {page_title}")
        
        current_url = driver.current_url
        print(f"Current URL: {current_url}")
        
        print("Waiting 3 seconds...")
        time.sleep(3)
        
        page_source_length = len(driver.page_source)
        print(f"Page source length: {page_source_length} characters")
        
        print("Demo 1 completed successfully!")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    
    finally:
        if 'driver' in locals():
            print("Closing browser...")
            driver.quit()

if __name__ == "__main__":
    demo_basic_browser()
