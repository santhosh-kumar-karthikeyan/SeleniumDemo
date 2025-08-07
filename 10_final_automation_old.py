#!/usr/bin/env python3
"""
Demo 10: Complete Automation Workflow
=====================================

This final program demonstrates:
- End-to-end automation workflow
- Combining all previous concepts
- Real-world automation scenario
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
        self.headless = headless
        
        # Setup paths
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.chromedriver_path = os.path.join(self.current_dir, "chromedriver")
        self.reports_dir = os.path.join(self.current_dir, "reports")
        self.screenshots_dir = os.path.join(self.current_dir, "screenshots")
        
        # Create directories
        os.makedirs(self.reports_dir, exist_ok=True)
        os.makedirs(self.screenshots_dir, exist_ok=True)
    
    def setup_driver(self):
        """Initialize WebDriver with optimal settings"""
        print("🚀 Setting up WebDriver with optimal configuration...")
        
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        
        if self.headless:
            chrome_options.add_argument("--headless")
        
        # Performance optimizations
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-plugins")
        chrome_options.add_argument("--disable-images")
        
        service = Service(ChromeDriverManager().install())
        
        try:
            self.driver = webdriver.Chrome(service=service, options=chrome_options)
            self.driver.implicitly_wait(10)
            self.wait = WebDriverWait(self.driver, 15)
            print("   ✅ WebDriver initialized successfully")
            return True
        except Exception as e:
            print(f"   ❌ Failed to initialize WebDriver: {str(e)}")
            return False
    
    def take_screenshot(self, test_name, description=""):
        """Take screenshot with proper naming and error handling"""
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{test_name}_{timestamp}.png"
            screenshot_path = os.path.join(self.screenshots_dir, filename)
            
            self.driver.save_screenshot(screenshot_path)
            
            screenshot_info = {
                'test_name': test_name,
                'filename': filename,
                'path': screenshot_path,
                'description': description,
                'timestamp': timestamp
            }
            
            self.results['screenshots'].append(screenshot_info)
            return screenshot_path
            
        except Exception as e:
            print(f"   ⚠️ Failed to take screenshot: {str(e)}")
            return None
    
    def log_test_result(self, test_name, status, details="", duration=0):
        """Log test results for reporting"""
        result = {
            'test_name': test_name,
            'status': status,
            'details': details,
            'duration': duration,
            'timestamp': datetime.now().isoformat()
        }
        
        self.results['test_results'].append(result)
        self.results['total_tests'] += 1
        
        if status == 'PASSED':
            self.results['passed_tests'] += 1
            print(f"   ✅ {test_name}: PASSED")
        else:
            self.results['failed_tests'] += 1
            print(f"   ❌ {test_name}: FAILED - {details}")
    
    def test_google_search_workflow(self):
        """Test 1: Complete Google search workflow"""
        test_name = "Google Search Workflow"
        print(f"\n1️⃣ Running {test_name}")
        start_time = time.time()
        
        try:
            # Navigate to Google
            self.driver.get("https://www.google.com")
            self.take_screenshot("google_homepage", "Google homepage loaded")
            
            # Find and interact with search box
            search_box = self.wait.until(EC.presence_of_element_located((By.NAME, "q")))
            
            # Perform search
            search_term = "Selenium WebDriver Python tutorial"
            search_box.clear()
            search_box.send_keys(search_term)
            self.take_screenshot("search_entered", f"Entered search term: {search_term}")
            
            # Submit search
            search_box.send_keys(Keys.RETURN)
            
            # Wait for results and verify
            self.wait.until(EC.presence_of_element_located((By.ID, "search")))
            
            # Verify results
            page_title = self.driver.title
            if search_term.lower().replace(" ", "") in page_title.lower().replace(" ", ""):
                result_titles = self.driver.find_elements(By.CSS_SELECTOR, "h3")
                
                if len(result_titles) >= 5:
                    self.take_screenshot("search_results", f"Found {len(result_titles)} search results")
                    
                    # Click on first result
                    first_result = result_titles[0]
                    result_text = first_result.text
                    first_result.click()
                    
                    # Wait for page load
                    time.sleep(3)
                    self.take_screenshot("first_result", f"Clicked on: {result_text}")
                    
                    duration = time.time() - start_time
                    self.log_test_result(test_name, "PASSED", f"Successfully searched and clicked first result", duration)
                    return True
                else:
                    raise Exception(f"Expected at least 5 results, got {len(result_titles)}")
            else:
                raise Exception(f"Search term not found in page title: {page_title}")
                
        except Exception as e:
            duration = time.time() - start_time
            self.take_screenshot("google_search_error", f"Error during Google search: {str(e)}")
            self.log_test_result(test_name, "FAILED", str(e), duration)
            return False
    
    def test_form_automation(self):
        """Test 2: Form filling automation"""
        test_name = "Form Automation"
        print(f"\n2️⃣ Running {test_name}")
        start_time = time.time()
        
        try:
            # Create test form
            form_html = """
            <!DOCTYPE html>
            <html>
            <head><title>Test Form</title></head>
            <body>
                <h1>Automation Test Form</h1>
                <form id="testForm">
                    <input type="text" id="name" placeholder="Full Name" required>
                    <input type="email" id="email" placeholder="Email" required>
                    <select id="country">
                        <option value="">Select Country</option>
                        <option value="us">United States</option>
                        <option value="uk">United Kingdom</option>
                        <option value="ca">Canada</option>
                    </select>
                    <input type="checkbox" id="newsletter"> Newsletter
                    <input type="radio" id="exp1" name="experience" value="beginner"> Beginner
                    <input type="radio" id="exp2" name="experience" value="expert"> Expert
                    <textarea id="comments" placeholder="Comments"></textarea>
                    <button type="submit" id="submit">Submit</button>
                </form>
                <div id="result" style="display:none;">Form submitted successfully!</div>
                <script>
                    document.getElementById('testForm').onsubmit = function(e) {
                        e.preventDefault();
                        document.getElementById('result').style.display = 'block';
                    };
                </script>
            </body>
            </html>
            """
            
            # Save and load form
            form_path = os.path.join(self.current_dir, "test_form.html")
            with open(form_path, "w") as f:
                f.write(form_html)
            
            self.driver.get(f"file://{form_path}")
            self.take_screenshot("form_loaded", "Test form loaded")
            
            # Fill form fields
            form_data = {
                'name': 'John Doe',
                'email': 'john.doe@example.com',
                'country': 'us',
                'comments': 'This is an automated test comment.'
            }
            
            # Fill text inputs
            name_field = self.driver.find_element(By.ID, "name")
            name_field.send_keys(form_data['name'])
            
            email_field = self.driver.find_element(By.ID, "email")
            email_field.send_keys(form_data['email'])
            
            # Handle dropdown
            country_dropdown = Select(self.driver.find_element(By.ID, "country"))
            country_dropdown.select_by_value(form_data['country'])
            
            # Handle checkbox
            newsletter_checkbox = self.driver.find_element(By.ID, "newsletter")
            newsletter_checkbox.click()
            
            # Handle radio button
            expert_radio = self.driver.find_element(By.ID, "exp2")
            expert_radio.click()
            
            # Fill textarea
            comments_field = self.driver.find_element(By.ID, "comments")
            comments_field.send_keys(form_data['comments'])
            
            self.take_screenshot("form_filled", "All form fields filled")
            
            # Submit form
            submit_button = self.driver.find_element(By.ID, "submit")
            submit_button.click()
            
            # Verify submission
            result_element = self.wait.until(EC.visibility_of_element_located((By.ID, "result")))
            if "successfully" in result_element.text.lower():
                self.take_screenshot("form_submitted", "Form submission successful")
                
                # Clean up
                os.remove(form_path)
                
                duration = time.time() - start_time
                self.log_test_result(test_name, "PASSED", "Form automation completed successfully", duration)
                return True
            else:
                raise Exception("Form submission not confirmed")
                
        except Exception as e:
            duration = time.time() - start_time
            self.take_screenshot("form_error", f"Form automation error: {str(e)}")
            self.log_test_result(test_name, "FAILED", str(e), duration)
            
            # Clean up on error
            try:
                form_path = os.path.join(self.current_dir, "test_form.html")
                if os.path.exists(form_path):
                    os.remove(form_path)
            except:
                pass
            
            return False
    
    def test_multi_tab_navigation(self):
        """Test 3: Multi-tab navigation and management"""
        test_name = "Multi-tab Navigation"
        print(f"\n3️⃣ Running {test_name}")
        start_time = time.time()
        
        try:
            # Start with Google
            self.driver.get("https://www.google.com")
            original_window = self.driver.current_window_handle
            
            # Open new tabs
            sites_to_visit = [
                ("https://github.com", "GitHub"),
                ("https://stackoverflow.com", "Stack Overflow"),
                ("https://www.python.org", "Python.org")
            ]
            
            opened_tabs = [original_window]
            
            for url, name in sites_to_visit:
                # Open new tab
                self.driver.execute_script(f"window.open('{url}', '_blank');")
                
                # Wait for new tab and switch to it
                self.wait.until(lambda d: len(d.window_handles) > len(opened_tabs))
                
                new_window = [w for w in self.driver.window_handles if w not in opened_tabs][0]
                opened_tabs.append(new_window)
                
                self.driver.switch_to.window(new_window)
                
                # Wait for page load and verify
                self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
                
                page_title = self.driver.title
                if name.lower() in page_title.lower():
                    self.take_screenshot(f"tab_{name.lower().replace('.', '_')}", f"Loaded {name}")
                else:
                    print(f"   ⚠️ {name} title verification failed: {page_title}")
            
            # Switch between tabs and verify
            for i, window_handle in enumerate(opened_tabs):
                self.driver.switch_to.window(window_handle)
                current_title = self.driver.title
                print(f"   Tab {i+1}: {current_title}")
                time.sleep(1)
            
            # Close additional tabs
            for window_handle in opened_tabs[1:]:
                self.driver.switch_to.window(window_handle)
                self.driver.close()
            
            # Switch back to original
            self.driver.switch_to.window(original_window)
            
            duration = time.time() - start_time
            self.log_test_result(test_name, "PASSED", f"Successfully managed {len(sites_to_visit)} additional tabs", duration)
            return True
            
        except Exception as e:
            duration = time.time() - start_time
            self.take_screenshot("multi_tab_error", f"Multi-tab error: {str(e)}")
            self.log_test_result(test_name, "FAILED", str(e), duration)
            return False
    
    def test_advanced_interactions(self):
        """Test 4: Advanced mouse and keyboard interactions"""
        test_name = "Advanced Interactions"
        print(f"\n4️⃣ Running {test_name}")
        start_time = time.time()
        
        try:
            # Go to Google for interaction testing
            self.driver.get("https://www.google.com")
            
            # Test ActionChains
            actions = ActionChains(self.driver)
            search_box = self.driver.find_element(By.NAME, "q")
            
            # Complex interaction sequence
            actions.move_to_element(search_box).click().perform()
            time.sleep(0.5)
            
            # Type with pauses
            text_to_type = "Advanced Selenium interactions"
            for char in text_to_type:
                actions.send_keys(char).perform()
                time.sleep(0.05)
            
            self.take_screenshot("typing_demo", "Demonstration of advanced typing")
            
            # Select all text using Ctrl+A
            actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
            time.sleep(0.5)
            
            # Replace with new text
            actions.send_keys("Selenium automation framework").perform()
            self.take_screenshot("text_replaced", "Text replacement demo")
            
            # Test hover effect (simulate hover over Google logo if visible)
            try:
                google_logo = self.driver.find_element(By.CSS_SELECTOR, "img[alt*='Google']")
                actions.move_to_element(google_logo).perform()
                time.sleep(1)
            except:
                print("   ℹ️ Google logo not found for hover test")
            
            duration = time.time() - start_time
            self.log_test_result(test_name, "PASSED", "Advanced interactions completed successfully", duration)
            return True
            
        except Exception as e:
            duration = time.time() - start_time
            self.take_screenshot("interactions_error", f"Interactions error: {str(e)}")
            self.log_test_result(test_name, "FAILED", str(e), duration)
            return False
    
    def test_error_handling_recovery(self):
        """Test 5: Error handling and recovery scenarios"""
        test_name = "Error Handling and Recovery"
        print(f"\n5️⃣ Running {test_name}")
        start_time = time.time()
        
        recovery_attempts = 0
        max_attempts = 3
        
        try:
            # Test scenario: handling timeouts and missing elements
            test_cases = [
                ("existing_element", By.NAME, "q", True),
                ("non_existent_element", By.ID, "non-existent-id", False),
                ("timeout_scenario", By.CLASS_NAME, "will-never-exist", False)
            ]
            
            for case_name, by_method, locator, should_exist in test_cases:
                print(f"   Testing: {case_name}")
                
                try:
                    if should_exist:
                        element = self.wait.until(EC.presence_of_element_located((by_method, locator)))
                        print(f"     ✅ Found expected element: {locator}")
                    else:
                        # Use shorter timeout for negative tests
                        short_wait = WebDriverWait(self.driver, 2)
                        short_wait.until(EC.presence_of_element_located((by_method, locator)))
                        print(f"     ❌ Unexpectedly found element: {locator}")
                        
                except TimeoutException:
                    if not should_exist:
                        print(f"     ✅ Correctly handled missing element: {locator}")
                    else:
                        print(f"     ⚠️ Timeout for expected element: {locator}")
                        recovery_attempts += 1
                        
                        if recovery_attempts < max_attempts:
                            print(f"     🔄 Recovery attempt {recovery_attempts}")
                            self.driver.refresh()
                            time.sleep(2)
                        
                except NoSuchElementException:
                    if not should_exist:
                        print(f"     ✅ Correctly handled NoSuchElementException: {locator}")
                    else:
                        print(f"     ❌ Unexpected NoSuchElementException: {locator}")
            
            self.take_screenshot("error_handling", "Error handling test completed")
            
            duration = time.time() - start_time
            self.log_test_result(test_name, "PASSED", f"Error handling tested with {recovery_attempts} recovery attempts", duration)
            return True
            
        except Exception as e:
            duration = time.time() - start_time
            self.take_screenshot("error_handling_failed", f"Error handling test failed: {str(e)}")
            self.log_test_result(test_name, "FAILED", str(e), duration)
            return False
    
    def generate_report(self):
        """Generate comprehensive test report"""
        print("\n📊 Generating comprehensive test report...")
        
        self.results['end_time'] = datetime.now().isoformat()
        
        # Calculate success rate
        if self.results['total_tests'] > 0:
            success_rate = (self.results['passed_tests'] / self.results['total_tests']) * 100
        else:
            success_rate = 0
        
        self.results['success_rate'] = success_rate
        
        # Create detailed report
        report_content = f"""
# Selenium Automation Framework - Test Report

## Test Execution Summary
- **Total Tests:** {self.results['total_tests']}
- **Passed:** {self.results['passed_tests']} ✅
- **Failed:** {self.results['failed_tests']} ❌
- **Success Rate:** {success_rate:.1f}%
- **Start Time:** {self.results['start_time']}
- **End Time:** {self.results['end_time']}

## Test Results Details

"""
        
        for test in self.results['test_results']:
            status_emoji = "✅" if test['status'] == 'PASSED' else "❌"
            report_content += f"""
### {test['test_name']} {status_emoji}
- **Status:** {test['status']}
- **Duration:** {test['duration']:.2f} seconds
- **Details:** {test['details']}
- **Timestamp:** {test['timestamp']}

"""
        
        if self.results['screenshots']:
            report_content += "\n## Screenshots Captured\n\n"
            for screenshot in self.results['screenshots']:
                report_content += f"- **{screenshot['test_name']}:** {screenshot['description']} ({screenshot['filename']})\n"
        
        # Save JSON report
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        json_report_path = os.path.join(self.reports_dir, f"test_report_{timestamp}.json")
        
        with open(json_report_path, "w") as f:
            json.dump(self.results, f, indent=2)
        
        # Save markdown report
        md_report_path = os.path.join(self.reports_dir, f"test_report_{timestamp}.md")
        
        with open(md_report_path, "w") as f:
            f.write(report_content)
        
        print(f"   ✅ JSON Report saved: {json_report_path}")
        print(f"   ✅ Markdown Report saved: {md_report_path}")
        
        return json_report_path, md_report_path
    
    def run_complete_automation_suite(self):
        """Execute the complete automation test suite"""
        print("🎯 Demo 10: Complete Automation Workflow")
        print("=" * 50)
        
        if not self.setup_driver():
            print("❌ Failed to setup WebDriver. Exiting.")
            return False
        
        try:
            print("\n🧪 Starting comprehensive automation test suite...")
            
            # Run all test cases
            test_methods = [
                self.test_google_search_workflow,
                self.test_form_automation,
                self.test_multi_tab_navigation,
                self.test_advanced_interactions,
                self.test_error_handling_recovery
            ]
            
            for test_method in test_methods:
                try:
                    test_method()
                    time.sleep(2)  # Brief pause between tests
                except Exception as e:
                    print(f"   ❌ Test method failed: {str(e)}")
            
            # Generate comprehensive report
            json_report, md_report = self.generate_report()
            
            print("\n📈 Test Suite Summary:")
            print(f"   Total Tests: {self.results['total_tests']}")
            print(f"   Passed: {self.results['passed_tests']} ✅")
            print(f"   Failed: {self.results['failed_tests']} ❌")
            print(f"   Success Rate: {self.results['success_rate']:.1f}%")
            print(f"   Screenshots: {len(self.results['screenshots'])}")
            
            print(f"\n📁 Reports generated:")
            print(f"   JSON Report: {json_report}")
            print(f"   Markdown Report: {md_report}")
            print(f"   Screenshots Directory: {self.screenshots_dir}")
            
            print("\n✅ Complete automation workflow demonstration finished!")
            
            return self.results['success_rate'] > 80  # Consider successful if > 80% pass rate
            
        except Exception as e:
            print(f"❌ Critical error in automation suite: {str(e)}")
            return False
        
        finally:
            if self.driver:
                print("\n🔒 Cleaning up WebDriver...")
                self.driver.quit()

def demo_complete_automation():
    """Main function to run the complete automation demo"""
    print("🚀 Initializing Complete Selenium Automation Framework...")
    
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
        
        print("\n🌟 You're now ready to build robust Selenium automation!")
    else:
        print("\n⚠️ Some tests failed, but you've still learned valuable concepts!")
    
    return success

if __name__ == "__main__":
    demo_complete_automation()
