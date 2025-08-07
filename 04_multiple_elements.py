#!/usr/bin/env python3
"""
Demo 4: Working with Multiple Elements and Lists
================================================

This program demonstrates:
- Finding multiple elements at once
- Iterating through element lists
- Different ways to locate similar elements
- Handling dynamic content
- Working with element collections

Learning Objectives:
- Use find_elements() vs find_element()
- Iterate through element collections
- Handle cases where elements might not exist
- Work with lists and dynamic content
- Filter and process multiple elements
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

def demo_multiple_elements():
    print("📋 Demo 4: Working with Multiple Elements")
    print("=" * 45)
    
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
        
        # Navigate to DemoQA
        driver.get("https://demoqa.com/books")
        print("🌐 Navigated to DemoQA Books Store")
        
        print("\n🎯 Working with multiple elements...")
        
        # Example 1: Find all book titles
        print("\n1️⃣ Finding all book titles:")
        try:
            book_titles = driver.find_elements(By.CSS_SELECTOR, ".mr-2 a")
            print(f"   Total book titles found: {len(book_titles)}")
            
            # Show first 5 book titles
            for i, title in enumerate(book_titles[:5]):
                if title.text.strip():
                    print(f"   Book {i+1}: {title.text}")
        except Exception as e:
            print(f"   Could not find book titles: {str(e)}")
        
        # Example 2: Find all images
        print("\n2️⃣ Finding book cover images:")
        images = driver.find_elements(By.TAG_NAME, "img")
        print(f"   Total images found: {len(images)}")
        
        # Count visible images
        visible_images = 0
        for img in images:
            if img.is_displayed():
                visible_images += 1
        print(f"   Visible images: {visible_images}")
        
        # Example 3: Find all clickable elements
        print("\n3️⃣ Finding clickable elements:")
        clickable_elements = driver.find_elements(By.CSS_SELECTOR, "a, button, input[type='button'], input[type='submit']")
        print(f"   Total clickable elements: {len(clickable_elements)}")
        
        # Count enabled vs disabled elements
        enabled_count = 0
        for element in clickable_elements:
            if element.is_enabled():
                enabled_count += 1
        
        print(f"   Enabled elements: {enabled_count}")
        print(f"   Disabled elements: {len(clickable_elements) - enabled_count}")
        
        # Example 4: Navigate to a form page for more element testing
        print("\n4️⃣ Navigating to form page for more element testing...")
        driver.get("https://demoqa.com/automation-practice-form")
        
        # Find all input elements
        input_elements = driver.find_elements(By.TAG_NAME, "input")
        print(f"   Input elements found: {len(input_elements)}")
        
        # Categorize input types
        input_types = {}
        for input_elem in input_elements:
            input_type = input_elem.get_attribute("type") or "text"
            input_types[input_type] = input_types.get(input_type, 0) + 1
        
        print("   Input types breakdown:")
        for input_type, count in input_types.items():
            print(f"     {input_type}: {count}")
        
        # Example 5: Find all labels
        print("\n5️⃣ Finding form labels:")
        labels = driver.find_elements(By.TAG_NAME, "label")
        print(f"   Labels found: {len(labels)}")
        
        # Show first few labels with text
        label_count = 0
        for label in labels:
            if label.text.strip() and label_count < 5:
                label_count += 1
                print(f"   Label {label_count}: '{label.text}'")
        
        # Example 6: Check for required fields
        print("\n6️⃣ Checking for required fields:")
        required_fields = driver.find_elements(By.CSS_SELECTOR, "[required], .required")
        print(f"   Required fields found: {len(required_fields)}")
        
        for i, field in enumerate(required_fields[:3]):
            field_id = field.get_attribute("id") or f"field_{i+1}"
            field_type = field.get_attribute("type") or field.tag_name
            print(f"   Required field {i+1}: {field_id} ({field_type})")
        
        print("\n⏳ Pausing to observe results...")
        time.sleep(3)
        
        print("\n✅ Demo 4 completed successfully!")
        
    except Exception as e:
        print(f"❌ An error occurred: {str(e)}")
    
    finally:
        if driver:
            print("🔒 Closing browser...")
            driver.quit()

if __name__ == "__main__":
    demo_multiple_elements()
