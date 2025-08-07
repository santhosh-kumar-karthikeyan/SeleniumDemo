#!/usr/bin/env python3
"""
Setup Script for Selenium Demo
==============================

This script sets up the environment for all Selenium demos by:
1. Installing required packages
2. Setting up Chrome WebDriver
3. Testing the basic configuration

Run this before running any demos.
"""

import subprocess
import sys
import os

def run_command(command, description):
    """Run a command and return success status"""
    print(f"🔧 {description}...")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"   ✅ Success")
            return True
        else:
            print(f"   ❌ Failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"   ❌ Error: {str(e)}")
        return False

def main():
    print("🚀 Selenium Demo Environment Setup")
    print("=" * 40)
    
    # Get current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    python_path = "/home/s4ndy/Projects/SeleniumDemo/.venv/bin/python"
    
    # Install webdriver-manager for automatic driver management
    success = run_command(
        f"{python_path} -m pip install webdriver-manager",
        "Installing webdriver-manager for automatic ChromeDriver management"
    )
    
    if not success:
        print("❌ Failed to install webdriver-manager")
        return False
    
    # Test basic import
    test_script = '''
try:
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    print("✅ All required packages imported successfully")
except ImportError as e:
    print(f"❌ Import error: {e}")
    exit(1)
'''
    
    print("🧪 Testing package imports...")
    result = subprocess.run([python_path, "-c", test_script], 
                          capture_output=True, text=True)
    
    if result.returncode == 0:
        print("   ✅ Package imports successful")
        print(result.stdout.strip())
    else:
        print("   ❌ Package import failed")
        print(result.stderr)
        return False
    
    print("\n🎯 Setup completed successfully!")
    print("You can now run the demos using:")
    print(f"   {python_path} 01_basic_browser_launch.py")
    print("   or")
    print(f"   {python_path} run_all_demos.py")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
