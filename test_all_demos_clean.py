#!/usr/bin/env python3

import subprocess
import sys
import os
import time
from datetime import datetime

def test_demo(demo_file, timeout=60):
    """Test a single demo with timeout"""
    print(f"Testing {demo_file}...", end=" ", flush=True)
    
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        python_path = "/home/s4ndy/Projects/SeleniumDemo/.venv/bin/python"
        demo_path = os.path.join(current_dir, demo_file)
        
        start_time = time.time()
        
        result = subprocess.run(
            [python_path, demo_path], 
            capture_output=True, 
            text=True,
            timeout=timeout,
            cwd=current_dir
        )
        
        duration = time.time() - start_time
        
        if result.returncode == 0:
            print(f"PASSED ({duration:.1f}s)")
            return True, duration, ""
        else:
            error_msg = result.stderr.strip() if result.stderr else "Unknown error"
            print(f"FAILED ({duration:.1f}s)")
            return False, duration, error_msg
            
    except subprocess.TimeoutExpired:
        duration = time.time() - start_time
        print(f"TIMEOUT (>{timeout}s)")
        return False, duration, f"Timeout exceeded {timeout}s"
    except Exception as e:
        duration = time.time() - start_time
        print(f"ERROR ({duration:.1f}s)")
        return False, duration, str(e)

def main():
    print("Selenium Demo Test Suite")
    print("=" * 50)
    
    demos = [
        "01_basic_browser_launch.py",
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
    
    print(f"Testing {len(demos)} demos...")
    print()
    
    results = []
    total_duration = 0
    
    for demo in demos:
        success, duration, error = test_demo(demo)
        results.append((demo, success, duration, error))
        total_duration += duration
    
    print("\n" + "=" * 50)
    print("TEST RESULTS SUMMARY")
    print("=" * 50)
    
    passed = sum(1 for _, success, _, _ in results if success)
    failed = len(results) - passed
    success_rate = (passed / len(results)) * 100
    
    print(f"Total Demos: {len(results)}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    print(f"Total Duration: {total_duration:.1f}s")
    print(f"Success Rate: {success_rate:.1f}%")
    
    if failed > 0:
        print()
        print("Failed Demos:")
        for demo, success, duration, error in results:
            if not success:
                print(f"   - {demo}: {error}")
        print()
        print("SOME TESTS FAILED")
        return 1
    else:
        print()
        print("ALL TESTS PASSED!")
        return 0

if __name__ == "__main__":
    sys.exit(main())
