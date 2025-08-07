#!/usr/bin/env python3
"""
Fix All Demos Script
====================
This script updates all demos to use webdriver-manager instead of local ChromeDriver
"""

import os
import re

def fix_demo_imports(file_path):
    """Fix imports and ChromeDriver setup in a demo file"""
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        
        # Check if already uses webdriver-manager
        if 'webdriver_manager' in content:
            print(f"✅ {os.path.basename(file_path)} - Already uses webdriver-manager")
            return True
        
        # Replace import section
        import_pattern = r'(from selenium\.webdriver\.chrome\.options import Options\n)'
        replacement = r'\1from webdriver_manager.chrome import ChromeDriverManager\n'
        
        if re.search(import_pattern, content):
            content = re.sub(import_pattern, replacement, content)
        else:
            # Add import if not found
            content = content.replace(
                'from selenium.webdriver.chrome.options import Options',
                'from selenium.webdriver.chrome.options import Options\nfrom webdriver_manager.chrome import ChromeDriverManager'
            )
        
        # Replace ChromeDriver setup
        setup_pattern = r'    # Setup ChromeDriver\n    current_dir = os\.path\.dirname\(os\.path\.abspath\(__file__\)\)\n    chromedriver_path = os\.path\.join\(current_dir, "chromedriver"\)\n    \n    chrome_options = Options\(\)\n    chrome_options\.add_argument\("--no-sandbox"\)\n    chrome_options\.add_argument\("--disable-dev-shm-usage"\)\n    \n    service = Service\(chromedriver_path\)'
        
        setup_replacement = '    # Setup ChromeDriver\n    chrome_options = Options()\n    chrome_options.add_argument("--no-sandbox")\n    chrome_options.add_argument("--disable-dev-shm-usage")\n    \n    service = Service(ChromeDriverManager().install())'
        
        if re.search(setup_pattern, content):
            content = re.sub(setup_pattern, setup_replacement, content)
        else:
            # Try alternative pattern
            alt_pattern = r'    current_dir = os\.path\.dirname\(os\.path\.abspath\(__file__\)\)\n    chromedriver_path = os\.path\.join\(current_dir, "chromedriver"\)\n    \n    chrome_options = Options\(\)\n    chrome_options\.add_argument\("--no-sandbox"\)\n    chrome_options\.add_argument\("--disable-dev-shm-usage"\)\n    \n    service = Service\(chromedriver_path\)'
            
            alt_replacement = '    chrome_options = Options()\n    chrome_options.add_argument("--no-sandbox")\n    chrome_options.add_argument("--disable-dev-shm-usage")\n    \n    service = Service(ChromeDriverManager().install())'
            
            content = re.sub(alt_pattern, alt_replacement, content)
        
        # Write back the content
        with open(file_path, 'w') as f:
            f.write(content)
        
        print(f"✅ {os.path.basename(file_path)} - Updated to use webdriver-manager")
        return True
        
    except Exception as e:
        print(f"❌ {os.path.basename(file_path)} - Error: {str(e)}")
        return False

def main():
    """Main function to fix all demos"""
    print("🔧 Fixing all demos to use webdriver-manager...")
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    demos = [
        "02_find_elements.py",
        "03_search_functionality.py",
        "04_multiple_elements.py",
        "05_forms_and_inputs.py",
        "06_waits_and_timing.py",
        "07_advanced_interactions.py",
        "08_page_navigation.py",
        "09_screenshots_and_debugging.py",
        "10_final_automation.py"
    ]
    
    success_count = 0
    
    for demo in demos:
        demo_path = os.path.join(current_dir, demo)
        if os.path.exists(demo_path):
            if fix_demo_imports(demo_path):
                success_count += 1
        else:
            print(f"❌ {demo} - File not found")
    
    print(f"\n📊 Results: {success_count}/{len(demos)} demos updated successfully")
    
    if success_count == len(demos):
        print("🎉 All demos have been updated!")
        return True
    else:
        print("⚠️ Some demos need manual fixing")
        return False

if __name__ == "__main__":
    main()
