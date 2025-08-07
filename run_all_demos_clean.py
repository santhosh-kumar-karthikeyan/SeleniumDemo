#!/usr/bin/env python3

import os
import sys
import subprocess
import time
from datetime import datetime

def run_demo(demo_file):
    """Run a single demo and return success status"""
    print(f"\n{'='*60}")
    print(f"Running {demo_file}")
    print(f"{'='*60}")
    
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        python_path = os.path.join(current_dir, ".venv", "bin", "python")
        demo_path = os.path.join(current_dir, demo_file)
        
        if not os.path.exists(python_path):
            python_path = "python"
            print(f"Using system python (virtual env not found)")
        
        if not os.path.exists(demo_path):
            print(f"Demo file not found: {demo_path}")
            return False
        
        result = subprocess.run([python_path, demo_path], 
                              cwd=current_dir,
                              capture_output=False)
        
        if result.returncode == 0:
            print(f"\nDemo {demo_file} completed successfully!")
            return True
        else:
            print(f"\nDemo {demo_file} failed with return code {result.returncode}")
            return False
            
    except Exception as e:
        print(f"Error running {demo_file}: {e}")
        return False

def wait_for_user(demo_num, total_demos, pause_seconds=3):
    """Wait between demos with countdown"""
    if demo_num < total_demos:
        print(f"\nPausing for {pause_seconds} seconds before next demo...")
        for i in range(pause_seconds, 0, -1):
            print(f"Next demo starts in {i} seconds...", end="\r", flush=True)
            time.sleep(1)
        print(" " * 30, end="\r")

def main():
    """Run all Selenium demos in sequence"""
    
    print("Selenium WebDriver Demonstration Suite")
    print("=" * 60)
    print("This will run all 10 demos in sequence")
    print("Total estimated time: 15-20 minutes")
    print("=" * 60)
    
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
    
    start_time = datetime.now()
    successful_demos = []
    failed_demos = []
    
    for i, demo in enumerate(demos, 1):
        print(f"\nDemo {i} of {len(demos)}")
        
        if run_demo(demo):
            successful_demos.append(demo)
        else:
            failed_demos.append(demo)
        
        wait_for_user(i, len(demos))
    
    end_time = datetime.now()
    duration = end_time - start_time
    
    print(f"\n{'='*60}")
    print("DEMONSTRATION COMPLETE")
    print(f"{'='*60}")
    
    print(f"Start time: {start_time.strftime('%H:%M:%S')}")
    print(f"End time: {end_time.strftime('%H:%M:%S')}")
    print(f"Total duration: {duration}")
    
    print(f"\nSuccessful demos: {len(successful_demos)}/{len(demos)}")
    print(f"Failed demos: {len(failed_demos)}/{len(demos)}")
    
    if successful_demos:
        print(f"\nSuccessful:")
        for demo in successful_demos:
            print(f"  - {demo}")
    
    if failed_demos:
        print(f"\nFailed:")
        for demo in failed_demos:
            print(f"  - {demo}")
        print("\nSome demos failed. Check error messages above.")
        return 1
    else:
        print(f"\nAll demos completed successfully!")
        print("Selenium WebDriver demonstration complete!")
        return 0

if __name__ == "__main__":
    try:
        result = main()
        sys.exit(result)
    except KeyboardInterrupt:
        print("\n\nDemonstration interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        sys.exit(1)
