#!/usr/bin/env python3
"""
Selenium Demo Runner
===================

This script runs all the Selenium demos in sequence for a complete
20-minute demonstration of Selenium WebDriver capabilities.

Usage:
    python run_all_demos.py
    
Or run individual demos:
    python 01_basic_browser_launch.py
    python 02_find_elements.py
    ... etc
"""

import os
import sys
import subprocess
import time
from datetime import datetime

def run_demo(demo_file):
    """Run a single demo and return success status"""
    print(f"\n{'='*60}")
    print(f"🚀 Running {demo_file}")
    print(f"{'='*60}")
    
    try:
        # Get the current directory and Python executable
        current_dir = os.path.dirname(os.path.abspath(__file__))
        python_path = "/home/s4ndy/Projects/SeleniumDemo/.venv/bin/python"
        demo_path = os.path.join(current_dir, demo_file)
        
        # Run the demo
        result = subprocess.run([python_path, demo_path], 
                              capture_output=False, 
                              text=True, 
                              cwd=current_dir)
        
        if result.returncode == 0:
            print(f"✅ {demo_file} completed successfully!")
            return True
        else:
            print(f"❌ {demo_file} failed with return code: {result.returncode}")
            return False
            
    except Exception as e:
        print(f"❌ Error running {demo_file}: {str(e)}")
        return False

def main():
    """Main function to run all demos"""
    print("🎯 Selenium WebDriver Demo Suite")
    print("================================")
    print("Welcome to the comprehensive Selenium learning experience!")
    print("This will run 10 progressive demos to teach you Selenium WebDriver.\n")
    
    # List of all demo files in order
    demo_files = [
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
    
    # Check if all demo files exist
    current_dir = os.path.dirname(os.path.abspath(__file__))
    missing_files = []
    
    for demo_file in demo_files:
        demo_path = os.path.join(current_dir, demo_file)
        if not os.path.exists(demo_path):
            missing_files.append(demo_file)
    
    if missing_files:
        print("❌ Missing demo files:")
        for missing_file in missing_files:
            print(f"   - {missing_file}")
        print("\nPlease make sure all demo files are present.")
        return False
    
    # Ask user if they want to run all demos
    print("Available demos:")
    for i, demo_file in enumerate(demo_files, 1):
        print(f"   {i:2d}. {demo_file}")
    
    print("\nOptions:")
    print("   1. Run all demos in sequence (recommended for full 20-min presentation)")
    print("   2. Run individual demo (enter demo number)")
    print("   3. Exit")
    
    try:
        choice = input("\nEnter your choice (1, 2, or 3): ").strip()
        
        if choice == "1":
            # Run all demos
            print("\n🎬 Starting complete demo sequence...")
            print("⏰ Estimated time: 20 minutes")
            
            start_time = datetime.now()
            successful_demos = 0
            failed_demos = 0
            
            for i, demo_file in enumerate(demo_files, 1):
                print(f"\n📍 Demo {i}/{len(demo_files)}")
                
                if run_demo(demo_file):
                    successful_demos += 1
                else:
                    failed_demos += 1
                
                # Pause between demos (except for the last one)
                if i < len(demo_files):
                    print(f"\n⏸️  Pausing 3 seconds before next demo...")
                    time.sleep(3)
            
            end_time = datetime.now()
            duration = end_time - start_time
            
            print(f"\n{'='*60}")
            print("🏁 DEMO SEQUENCE COMPLETE!")
            print(f"{'='*60}")
            print(f"📊 Results Summary:")
            print(f"   ✅ Successful demos: {successful_demos}")
            print(f"   ❌ Failed demos: {failed_demos}")
            print(f"   ⏰ Total duration: {duration}")
            print(f"   📈 Success rate: {(successful_demos/len(demo_files)*100):.1f}%")
            
            if successful_demos == len(demo_files):
                print("\n🎉 Congratulations! All demos completed successfully!")
                print("You've mastered the fundamentals of Selenium WebDriver!")
            else:
                print("\n💪 Great job! Even with some challenges, you've learned a lot!")
            
            return successful_demos == len(demo_files)
            
        elif choice == "2":
            # Run individual demo
            try:
                demo_number = int(input(f"Enter demo number (1-{len(demo_files)}): "))
                if 1 <= demo_number <= len(demo_files):
                    demo_file = demo_files[demo_number - 1]
                    print(f"\n🎯 Running individual demo: {demo_file}")
                    return run_demo(demo_file)
                else:
                    print(f"❌ Invalid demo number. Please enter 1-{len(demo_files)}")
                    return False
            except ValueError:
                print("❌ Invalid input. Please enter a number.")
                return False
                
        elif choice == "3":
            print("👋 Thanks for using the Selenium demo suite!")
            return True
            
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")
            return False
            
    except KeyboardInterrupt:
        print("\n\n⏹️  Demo interrupted by user.")
        print("👋 Thanks for using the Selenium demo suite!")
        return False
    except Exception as e:
        print(f"\n❌ An error occurred: {str(e)}")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
