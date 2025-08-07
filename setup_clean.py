#!/usr/bin/env python3

import subprocess
import sys
import os

def run_command(command, description):
    """Run a command and return success status"""
    print(f"{description}...")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"   Success")
            return True
        else:
            print(f"   Failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"   Error: {str(e)}")
        return False

def check_python_version():
    """Check if Python version is adequate"""
    print("Checking Python version...")
    version = sys.version_info
    print(f"   Python {version.major}.{version.minor}.{version.micro}")
    
    if version.major >= 3 and version.minor >= 7:
        print("   Python version is adequate")
        return True
    else:
        print("   Python 3.7+ required")
        return False

def setup_virtual_environment():
    """Create and activate virtual environment"""
    print("Setting up virtual environment...")
    
    if os.path.exists(".venv"):
        print("   Virtual environment already exists")
        return True
    
    if run_command("python -m venv .venv", "Creating virtual environment"):
        print("   Virtual environment created successfully")
        return True
    else:
        return False

def install_requirements():
    """Install required packages"""
    print("Installing required packages...")
    
    packages = [
        "selenium>=4.0.0",
        "webdriver-manager>=4.0.0", 
        "requests>=2.31.0"
    ]
    
    venv_python = ".venv/bin/python" if os.name != 'nt' else ".venv\\Scripts\\python.exe"
    
    for package in packages:
        if not run_command(f"{venv_python} -m pip install {package}", f"Installing {package}"):
            return False
    
    print("   All packages installed successfully")
    return True

def test_selenium_setup():
    """Test basic Selenium functionality"""
    print("Testing Selenium setup...")
    
    test_script = '''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import sys

try:
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    driver.get("https://www.google.com")
    title = driver.title
    driver.quit()
    
    print(f"Test successful! Page title: {title}")
    sys.exit(0)
    
except Exception as e:
    print(f"Test failed: {str(e)}")
    sys.exit(1)
'''
    
    venv_python = ".venv/bin/python" if os.name != 'nt' else ".venv\\Scripts\\python.exe"
    
    with open("test_setup.py", "w") as f:
        f.write(test_script)
    
    try:
        result = subprocess.run([venv_python, "test_setup.py"], 
                              capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            print("   Selenium setup test passed")
            return True
        else:
            print(f"   Selenium setup test failed: {result.stderr}")
            return False
    except subprocess.TimeoutExpired:
        print("   Selenium setup test timed out")
        return False
    except Exception as e:
        print(f"   Selenium setup test error: {str(e)}")
        return False
    finally:
        if os.path.exists("test_setup.py"):
            os.remove("test_setup.py")

def main():
    """Main setup function"""
    print("Selenium Demo Environment Setup")
    print("=" * 40)
    
    steps = [
        ("Python Version Check", check_python_version),
        ("Virtual Environment", setup_virtual_environment),
        ("Package Installation", install_requirements),
        ("Selenium Test", test_selenium_setup)
    ]
    
    for step_name, step_function in steps:
        print(f"\n{step_name}:")
        if not step_function():
            print(f"\nSetup failed at: {step_name}")
            return False
    
    print("\n" + "=" * 40)
    print("Setup completed successfully!")
    print("\nNext steps:")
    print("1. Activate virtual environment: source .venv/bin/activate")
    print("2. Run a demo: python 01_basic_browser_launch.py")
    print("3. Or run all demos: python run_all_demos.py")
    print("4. Or test all demos: python test_all_demos.py")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
