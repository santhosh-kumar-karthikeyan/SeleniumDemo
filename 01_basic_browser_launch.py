#!/usr/bin/env python3
"""
Demo 1: Basic Browser Launch and Google Navigation
==================================================

This is the most basic Selenium program. It demonstrates:
- Setting up ChromeDriver
- Launching Chrome browser
- Navigating to Google.com
- Basic browser controls

Learning Objectives:
- Understand WebDriver basics
- Learn how to launch a browser
- Navigate to a webpage
- Close the browser properly
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

def demo_basic_browser():
    print("🚀 Demo 1: Basic Browser Launch")
    print("=" * 40)
    
    # Configure Chrome options
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Uncomment for headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    # Create Chrome service with automatic driver management
    service = Service(ChromeDriverManager().install())
    
    try:
        # Create WebDriver instance
        print("📂 Setting up ChromeDriver...")
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        # Configure implicit wait
        driver.implicitly_wait(10)
        
        # Navigate to DemoQA test site
        print("🌐 Opening DemoQA test site...")
        driver.get("https://demoqa.com/books")
        
        # Get page title
        page_title = driver.title
        print(f"📄 Page title: {page_title}")
        
        # Get current URL
        current_url = driver.current_url
        print(f"🔗 Current URL: {current_url}")
        
        # Wait for 3 seconds to see the page
        print("⏳ Waiting 3 seconds...")
        time.sleep(3)
        
        # Get page source length (basic info)
        page_source_length = len(driver.page_source)
        print(f"📏 Page source length: {page_source_length} characters")
        
        print("✅ Demo 1 completed successfully!")
        
    except Exception as e:
        print(f"❌ An error occurred: {str(e)}")
    
    finally:
        # Always close the browser
        if 'driver' in locals():
            print("🔒 Closing browser...")
            driver.quit()

if __name__ == "__main__":
    demo_basic_browser()
