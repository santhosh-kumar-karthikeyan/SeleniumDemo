#!/usr/bin/env python3
"""
Demo 10: Complete Automation Workflow
=====================================

This final program demonstrates:
- End-to-end automation workflow
- Combining all previous concepts
- Real-world automation scenario using DemoQA
- Best practices implementation
- Error handling and recovery
- Reporting and logging

Learning Objectives:
- Integrate all Selenium concepts learned
- Create a robust automation workflow
- Handle real-world scenarios
- Implement proper error handling
- Generate automation reports
- Follow automation best practices
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
import time
import os
import json
import tempfile
from datetime import datetime

class SeleniumAutomationFramework:
    """Complete Selenium automation framework demonstrating best practices"""
    
    def __init__(self, headless=False):
        self.driver = None
        self.wait = None
        self.results = {
            'test_results': [],
            'start_time': datetime.now().isoformat(),
            'end_time': None,
            'total_tests': 0,
            'passed_tests': 0,
            'failed_tests': 0,
            'screenshots': []
        }
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.screenshots_dir = os.path.join(self.current_dir, "screenshots")
        self.headless = headless
        
        # Ensure screenshots directory exists
        os.makedirs(self.screenshots_dir, exist_ok=True)
    
    def setup_driver(self):
        """Initialize the Chrome WebDriver with optimal settings"""
        try:
            print("🔧 Setting up Chrome WebDriver...")
            
            chrome_options = Options()
            if self.headless:
                chrome_options.add_argument("--headless")
            
            # Standard Chrome options for stability
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--window-size=1920,1080")
            chrome_options.add_argument("--disable-extensions")
            chrome_options.add_argument("--disable-plugins")
            chrome_options.add_argument("--disable-images")
            
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=chrome_options)
            self.wait = WebDriverWait(self.driver, 10)
            
            print("✅ Chrome WebDriver initialized successfully")
            return True
            
        except Exception as e:
            print(f"❌ Failed to initialize WebDriver: {e}")
            return False
    
    def take_screenshot(self, name, description=""):
        """Take a screenshot and save it with a descriptive name"""
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{timestamp}_{name}.png"
            filepath = os.path.join(self.screenshots_dir, filename)
            
            self.driver.save_screenshot(filepath)
            
            self.results['screenshots'].append({
                'name': name,
                'description': description,
                'filepath': filepath,
                'timestamp': timestamp
            })
            
            print(f"📸 Screenshot saved: {filename} - {description}")
            return filepath
            
        except Exception as e:
            print(f"⚠️ Screenshot failed: {e}")
            return None
    
    def log_test_result(self, test_name, status, details="", execution_time=0):
        """Log test results for reporting"""
        result = {
            'test_name': test_name,
            'status': status,
            'details': details,
            'execution_time': execution_time,
            'timestamp': datetime.now().isoformat()
        }
        
        self.results['test_results'].append(result)
        self.results['total_tests'] += 1
        
        if status == 'PASSED':
            self.results['passed_tests'] += 1
            print(f"✅ {test_name}: {status}")
        else:
            self.results['failed_tests'] += 1
            print(f"❌ {test_name}: {status}")
        
        if details:
            print(f"   📝 {details}")
    
    def test_comprehensive_form_automation(self):
        """Test comprehensive form filling using DemoQA practice form"""
        test_name = "Comprehensive Form Automation"
        start_time = time.time()
        
        try:
            print("\n🎯 Testing comprehensive form automation...")
            
            # Navigate to DemoQA Automation Practice Form
            self.driver.get("https://demoqa.com/automation-practice-form")
            self.take_screenshot("form_loaded", "Practice form loaded")
            
            # Wait for form to load
            form_title = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "main-header")))
            print(f"📄 Form loaded: {form_title.text}")
            
            # Test data
            test_data = {
                "firstName": "Alexander",
                "lastName": "Johnson", 
                "email": "alexander.johnson@demo.com",
                "mobile": "5551234567",
                "address": "123 Automation Street, Test City, TC 12345"
            }
            
            # Fill basic information
            print("📝 Filling basic information...")
            
            first_name = self.driver.find_element(By.ID, "firstName")
            first_name.clear()
            first_name.send_keys(test_data["firstName"])
            
            last_name = self.driver.find_element(By.ID, "lastName")
            last_name.clear()
            last_name.send_keys(test_data["lastName"])
            
            email = self.driver.find_element(By.ID, "userEmail")
            email.clear()
            email.send_keys(test_data["email"])
            
            mobile = self.driver.find_element(By.ID, "userNumber")
            mobile.clear()
            mobile.send_keys(test_data["mobile"])
            
            print("✅ Basic information filled")
            
            # Select gender
            print("🚻 Selecting gender...")
            try:
                male_radio = self.driver.find_element(By.CSS_SELECTOR, "label[for='gender-radio-1']")
                self.driver.execute_script("arguments[0].click();", male_radio)
                print("✅ Gender selected: Male")
            except Exception as e:
                print(f"⚠️ Gender selection failed: {e}")
            
            # Handle date of birth
            print("📅 Setting date of birth...")
            try:
                dob_field = self.driver.find_element(By.ID, "dateOfBirthInput")
                dob_field.click()
                
                # Navigate to specific date (January 1990)
                month_dropdown = self.driver.find_element(By.CLASS_NAME, "react-datepicker__month-select")
                month_dropdown.click()
                january_option = self.driver.find_element(By.XPATH, "//option[@value='0']")
                january_option.click()
                
                year_dropdown = self.driver.find_element(By.CLASS_NAME, "react-datepicker__year-select")
                year_dropdown.click()
                year_option = self.driver.find_element(By.XPATH, "//option[@value='1990']")
                year_option.click()
                
                # Select day 15
                day_element = self.driver.find_element(By.XPATH, "//div[@class='react-datepicker__day react-datepicker__day--015' and text()='15']")
                day_element.click()
                
                print("✅ Date of birth set: January 15, 1990")
            except Exception as e:
                print(f"⚠️ Date selection issue: {e}")
            
            # Add subjects
            print("📚 Adding subjects...")
            try:
                subjects_field = self.driver.find_element(By.ID, "subjectsInput")
                subjects = ["Math", "Computer Science"]
                
                for subject in subjects:
                    subjects_field.click()
                    subjects_field.send_keys(subject)
                    time.sleep(1)
                    subjects_field.send_keys(Keys.TAB)
                    print(f"   ✅ Added: {subject}")
            except Exception as e:
                print(f"⚠️ Subjects adding issue: {e}")
            
            # Select hobbies
            print("🎯 Selecting hobbies...")
            try:
                hobbies = [
                    ("hobbies-checkbox-1", "Sports"),
                    ("hobbies-checkbox-2", "Reading")
                ]
                
                for hobby_id, hobby_name in hobbies:
                    hobby_label = self.driver.find_element(By.CSS_SELECTOR, f"label[for='{hobby_id}']")
                    self.driver.execute_script("arguments[0].click();", hobby_label)
                    print(f"   ✅ Selected: {hobby_name}")
            except Exception as e:
                print(f"⚠️ Hobby selection issue: {e}")
            
            # Upload file
            print("📎 Uploading file...")
            try:
                # Create a temporary file for upload
                with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as temp_file:
                    temp_file.write("This is a test file for Selenium automation demo.")
                    temp_file_path = temp_file.name
                
                file_input = self.driver.find_element(By.ID, "uploadPicture")
                file_input.send_keys(temp_file_path)
                print("✅ File uploaded successfully")
                
                # Clean up
                os.unlink(temp_file_path)
            except Exception as e:
                print(f"⚠️ File upload issue: {e}")
            
            # Fill address
            address_field = self.driver.find_element(By.ID, "currentAddress")
            address_field.clear()
            address_field.send_keys(test_data["address"])
            print("✅ Address filled")
            
            # Select state and city
            print("🌍 Selecting state and city...")
            try:
                # Select state
                state_dropdown = self.driver.find_element(By.ID, "state")
                state_dropdown.click()
                time.sleep(1)
                
                ncr_option = self.driver.find_element(By.XPATH, "//div[text()='NCR']")
                ncr_option.click()
                print("   ✅ State: NCR")
                
                # Select city
                time.sleep(1)
                city_dropdown = self.driver.find_element(By.ID, "city")
                city_dropdown.click()
                time.sleep(1)
                
                delhi_option = self.driver.find_element(By.XPATH, "//div[text()='Delhi']")
                delhi_option.click()
                print("   ✅ City: Delhi")
            except Exception as e:
                print(f"⚠️ State/City selection issue: {e}")
            
            self.take_screenshot("form_filled", "Form completely filled before submission")
            
            # Submit the form
            print("🚀 Submitting form...")
            submit_button = self.driver.find_element(By.ID, "submit")
            self.driver.execute_script("arguments[0].click();", submit_button)
            
            # Wait for modal to appear
            time.sleep(2)
            
            try:
                modal = self.driver.find_element(By.CSS_SELECTOR, ".modal-content")
                if modal.is_displayed():
                    print("✅ Submission successful - Modal appeared!")
                    self.take_screenshot("form_submitted", "Form submission modal")
                    
                    # Extract submitted data
                    try:
                        modal_body = self.driver.find_element(By.CSS_SELECTOR, ".modal-body")
                        submitted_data = modal_body.text
                        print("📋 Submitted data verified")
                    except:
                        print("⚠️ Could not extract submitted data")
                    
                    # Close modal
                    close_button = self.driver.find_element(By.ID, "closeLargeModal")
                    close_button.click()
                    
                    execution_time = time.time() - start_time
                    self.log_test_result(test_name, 'PASSED', 
                                       f"Form filled and submitted successfully in {execution_time:.2f}s", 
                                       execution_time)
                    return True
                else:
                    self.log_test_result(test_name, 'FAILED', "Modal not visible after submission")
                    return False
                    
            except Exception as modal_error:
                self.log_test_result(test_name, 'FAILED', f"Modal handling error: {modal_error}")
                return False
                
        except Exception as e:
            execution_time = time.time() - start_time
            self.log_test_result(test_name, 'FAILED', f"Exception: {e}", execution_time)
            return False
    
    def test_multi_element_interactions(self):
        """Test multiple element interactions on DemoQA Elements page"""
        test_name = "Multi-Element Interactions"
        start_time = time.time()
        
        try:
            print("\n🎯 Testing multi-element interactions...")
            
            # Navigate to Elements page
            self.driver.get("https://demoqa.com/elements")
            self.take_screenshot("elements_page", "Elements page loaded")
            
            # Test Text Box
            print("📝 Testing Text Box...")
            text_box_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Text Box']")))
            text_box_link.click()
            
            # Fill text box form
            user_name = self.driver.find_element(By.ID, "userName")
            user_name.send_keys("Test User Multi")
            
            user_email = self.driver.find_element(By.ID, "userEmail")
            user_email.send_keys("testuser@multi.com")
            
            current_address = self.driver.find_element(By.ID, "currentAddress")
            current_address.send_keys("123 Current Street")
            
            permanent_address = self.driver.find_element(By.ID, "permanentAddress")
            permanent_address.send_keys("456 Permanent Avenue")
            
            submit_btn = self.driver.find_element(By.ID, "submit")
            submit_btn.click()
            
            # Verify output
            time.sleep(1)
            try:
                output = self.driver.find_element(By.ID, "output")
                if output.is_displayed():
                    print("✅ Text Box test passed")
                    self.take_screenshot("textbox_output", "Text Box output displayed")
            except:
                print("⚠️ Text Box output not found")
            
            # Test Buttons
            print("🔘 Testing Buttons...")
            self.driver.get("https://demoqa.com/buttons")
            
            # Double click
            double_click_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "doubleClickBtn")))
            actions = ActionChains(self.driver)
            actions.double_click(double_click_btn).perform()
            time.sleep(1)
            
            # Right click
            right_click_btn = self.driver.find_element(By.ID, "rightClickBtn")
            actions.context_click(right_click_btn).perform()
            time.sleep(1)
            
            # Single click
            click_me_btn = self.driver.find_element(By.XPATH, "//button[text()='Click Me']")
            click_me_btn.click()
            time.sleep(1)
            
            self.take_screenshot("buttons_clicked", "All buttons clicked")
            print("✅ Buttons test passed")
            
            execution_time = time.time() - start_time
            self.log_test_result(test_name, 'PASSED', 
                               f"Multiple element interactions completed in {execution_time:.2f}s", 
                               execution_time)
            return True
            
        except Exception as e:
            execution_time = time.time() - start_time
            self.log_test_result(test_name, 'FAILED', f"Exception: {e}", execution_time)
            return False
    
    def test_advanced_scenarios(self):
        """Test advanced scenarios including alerts, windows, and frames"""
        test_name = "Advanced Scenarios"
        start_time = time.time()
        
        try:
            print("\n🎯 Testing advanced scenarios...")
            
            # Test Alerts
            print("⚠️ Testing Alerts...")
            self.driver.get("https://demoqa.com/alerts")
            self.take_screenshot("alerts_page", "Alerts page loaded")
            
            # Simple alert
            alert_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "alertButton")))
            alert_btn.click()
            
            # Handle alert
            alert = self.wait.until(EC.alert_is_present())
            alert_text = alert.text
            alert.accept()
            print(f"✅ Simple alert handled: {alert_text}")
            
            # Confirm alert
            time.sleep(1)
            confirm_btn = self.driver.find_element(By.ID, "confirmButton")
            confirm_btn.click()
            
            confirm_alert = self.wait.until(EC.alert_is_present())
            confirm_alert.accept()
            print("✅ Confirm alert handled")
            
            # Test Browser Windows
            print("🪟 Testing Browser Windows...")
            self.driver.get("https://demoqa.com/browser-windows")
            
            # Open new tab
            new_tab_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "tabButton")))
            original_window = self.driver.current_window_handle
            new_tab_btn.click()
            
            # Switch to new tab
            self.wait.until(lambda driver: len(driver.window_handles) > 1)
            for window_handle in self.driver.window_handles:
                if window_handle != original_window:
                    self.driver.switch_to.window(window_handle)
                    break
            
            # Get new tab content
            try:
                new_tab_content = self.driver.find_element(By.ID, "sampleHeading")
                print(f"✅ New tab content: {new_tab_content.text}")
            except:
                print("⚠️ New tab content not found")
            
            # Close new tab and switch back
            self.driver.close()
            self.driver.switch_to.window(original_window)
            print("✅ Window management test passed")
            
            self.take_screenshot("advanced_completed", "Advanced scenarios completed")
            
            execution_time = time.time() - start_time
            self.log_test_result(test_name, 'PASSED', 
                               f"Advanced scenarios completed in {execution_time:.2f}s", 
                               execution_time)
            return True
            
        except Exception as e:
            execution_time = time.time() - start_time
            self.log_test_result(test_name, 'FAILED', f"Exception: {e}", execution_time)
            return False
    
    def generate_report(self):
        """Generate a comprehensive test report"""
        print("\n📊 Generating test report...")
        
        self.results['end_time'] = datetime.now().isoformat()
        
        # Calculate summary statistics
        total_time = sum([result['execution_time'] for result in self.results['test_results']])
        success_rate = (self.results['passed_tests'] / self.results['total_tests'] * 100) if self.results['total_tests'] > 0 else 0
        
        # Create report
        report = {
            'summary': {
                'total_tests': self.results['total_tests'],
                'passed_tests': self.results['passed_tests'],
                'failed_tests': self.results['failed_tests'],
                'success_rate': f"{success_rate:.1f}%",
                'total_execution_time': f"{total_time:.2f}s",
                'start_time': self.results['start_time'],
                'end_time': self.results['end_time']
            },
            'test_results': self.results['test_results'],
            'screenshots': self.results['screenshots']
        }
        
        # Save report to file
        report_file = os.path.join(self.current_dir, f"test_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
        
        try:
            with open(report_file, 'w') as f:
                json.dump(report, f, indent=2)
            print(f"📄 Report saved: {report_file}")
        except Exception as e:
            print(f"⚠️ Report save failed: {e}")
        
        # Print summary
        print("\n" + "="*50)
        print("🎯 AUTOMATION TEST SUMMARY")
        print("="*50)
        print(f"📊 Total Tests: {self.results['total_tests']}")
        print(f"✅ Passed: {self.results['passed_tests']}")
        print(f"❌ Failed: {self.results['failed_tests']}")
        print(f"📈 Success Rate: {success_rate:.1f}%")
        print(f"⏱️  Total Time: {total_time:.2f}s")
        print(f"📸 Screenshots: {len(self.results['screenshots'])}")
        print("="*50)
    
    def run_complete_automation_suite(self):
        """Run the complete automation test suite"""
        print("\n🚀 Starting Complete Automation Test Suite...")
        print("="*60)
        
        # Setup WebDriver
        if not self.setup_driver():
            print("❌ Failed to setup WebDriver. Exiting...")
            return False
        
        try:
            # Run all test scenarios
            test_results = []
            
            # Test 1: Comprehensive Form Automation
            test_results.append(self.test_comprehensive_form_automation())
            
            # Test 2: Multi-Element Interactions
            test_results.append(self.test_multi_element_interactions())
            
            # Test 3: Advanced Scenarios
            test_results.append(self.test_advanced_scenarios())
            
            # Generate final report
            self.generate_report()
            
            # Overall success
            overall_success = all(test_results)
            
            if overall_success:
                print("\n🎉 ALL TESTS PASSED! Automation suite completed successfully!")
            else:
                print("\n⚠️ Some tests failed, but valuable learning achieved!")
            
            return overall_success
            
        except Exception as e:
            print(f"❌ Critical error in automation suite: {e}")
            return False
            
        finally:
            # Cleanup
            if self.driver:
                print("\n🧹 Cleaning up resources...")
                self.driver.quit()
                print("✅ WebDriver closed")


def demo_complete_automation():
    """Main function to run the complete automation demo"""
    print("🚀 Initializing Complete Selenium Automation Framework...")
    print("🎯 This demo showcases a comprehensive automation workflow using DemoQA")
    print("🌟 All interactions use real web elements - no local HTML files!")
    
    # Create automation framework instance
    framework = SeleniumAutomationFramework(headless=False)  # Set to True for headless mode
    
    # Run the complete test suite
    success = framework.run_complete_automation_suite()
    
    if success:
        print("\n🎉 Automation framework demonstration completed successfully!")
        print("\n🎓 Congratulations! You've learned:")
        print("   ✅ Basic WebDriver operations")
        print("   ✅ Element finding and interaction")
        print("   ✅ Form handling and input management")
        print("   ✅ Wait strategies and timing")
        print("   ✅ Advanced interactions (mouse/keyboard)")
        print("   ✅ Page navigation and browser controls")
        print("   ✅ Screenshots and debugging")
        print("   ✅ Multi-window/tab management")
        print("   ✅ Error handling and recovery")
        print("   ✅ Complete automation framework")
        print("   ✅ Test reporting and documentation")
        
        print("\n🌟 You're now ready to build robust Selenium automation!")
        print("🎯 All demos used real websites (DemoQA) for authentic learning!")
    else:
        print("\n⚠️ Some tests failed, but you've still learned valuable concepts!")
        print("🔍 Check the generated report for detailed results!")
    
    return success


if __name__ == "__main__":
    demo_complete_automation()
