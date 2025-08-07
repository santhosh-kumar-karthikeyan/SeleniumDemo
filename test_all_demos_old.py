#!/usr/bin/env python3
"""
Test Runner - Quick Validation of All Demos
===========================================

This script quickly tests each demo to ensure they work correctly.
It runs each demo with minimal output to verify functionality.
"""

import subprocess
import sys
import os
import time
from datetime import datetime

def test_demo(demo_file, timeout=60):
    """Test a single demo with timeout"""
    print(f"🧪 Testing {demo_file}...", end=" ", flush=True)
    
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        python_path = "/home/s4ndy/Projects/SeleniumDemo/.venv/bin/python"
        demo_path = os.path.join(current_dir, demo_file)
        
        start_time = time.time()
        
        # Run the demo with timeout
        result = subprocess.run(
            [python_path, demo_path], 
            capture_output=True, 
            text=True, 
            timeout=timeout,
            cwd=current_dir
        )
        
        end_time = time.time()
        duration = end_time - start_time
        
        if result.returncode == 0:
            print(f"✅ PASSED ({duration:.1f}s)")
            return True, duration, ""
        else:
            print(f"❌ FAILED ({duration:.1f}s)")
            error_msg = result.stderr[:200] + "..." if len(result.stderr) > 200 else result.stderr
            print(f"   Error: {error_msg}")
            return False, duration, result.stderr
            
    except subprocess.TimeoutExpired:
        print(f"⏰ TIMEOUT (>{timeout}s)")
        return False, timeout, "Timeout exceeded"
    except Exception as e:
        print(f"💥 ERROR: {str(e)}")
        return False, 0, str(e)

def main():
    """Main test function"""
    print("🔧 Selenium Demo Test Suite")
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
    
    print(f"Testing {len(demos)} demos...\n")
    
    results = []
    total_duration = 0
    
    for demo in demos:
        success, duration, error = test_demo(demo)
        results.append((demo, success, duration, error))
        total_duration += duration
        
        # Small delay between tests
        time.sleep(1)
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 TEST RESULTS SUMMARY")
    print("=" * 50)
    
    passed = sum(1 for _, success, _, _ in results if success)
    failed = len(results) - passed
    
    print(f"Total Demos: {len(results)}")
    print(f"✅ Passed: {passed}")
    print(f"❌ Failed: {failed}")
    print(f"⏱️  Total Duration: {total_duration:.1f}s")
    print(f"📈 Success Rate: {(passed/len(results)*100):.1f}%")
    
    if failed > 0:
        print(f"\n❌ Failed Demos:")
        for demo, success, duration, error in results:
            if not success:
                print(f"   - {demo}: {error[:100]}...")
    
    print(f"\n{'🎉 ALL TESTS PASSED!' if failed == 0 else '⚠️ SOME TESTS FAILED'}")
    
    return failed == 0

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
