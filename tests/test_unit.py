"""
Simple Tests - Digital Wellness Dashboard App

"""

import os
import pandas as pd
import json

def test_data_files():
    """Check if my data files are there"""
    print("Looking for data files...")
    
    # Check if teen data exists
    if os.path.exists("data/teen_processed.csv"):
        print("  ✓ Found teen data file")
    else:
        print("  ✗ Teen data file missing!")
        return False
    
    # Check if social media data exists
    if os.path.exists("data/social_processed.csv"):
        print("  ✓ Found social media data file")
    else:
        print("  ✗ Social media data file missing!")
        return False
    
    # Check if recommendations exist
    if os.path.exists("data/recommendations.json"):
        print("  ✓ Found recommendations file")
    else:
        print("  ✗ Recommendations file missing!")
        return False
    
    return True

def test_load_data():
    """Check if I can open the data"""
    print("Trying to open data files...")
    
    try:
        # Try to open teen data
        teen_data = pd.read_csv("data/teen_processed.csv")
        if len(teen_data) > 0:
            print(f"  ✓ Teen data opened - found {len(teen_data)} users")
        else:
            print("  ✗ Teen data is empty!")
            return False
    except:
        print("  ✗ Can't open teen data!")
        return False
    
    try:
        # Try to open social media data
        social_data = pd.read_csv("data/social_processed.csv")
        if len(social_data) > 0:
            print(f"  ✓ Social data opened - found {len(social_data)} users")
        else:
            print("  ✗ Social data is empty!")
            return False
    except:
        print("  ✗ Can't open social data!")
        return False
    
    return True

def test_recommendations():
    """Check if recommendations work"""
    print("Checking recommendations...")
    
    try:
        # Try to open recommendations
        with open("data/recommendations.json", 'r') as f:
            recommendations = json.load(f)
        
        # Check if we have teen recommendations
        if "teen_dataset" in recommendations:
            print("  ✓ Found teen recommendations")
        else:
            print("  ✗ Missing teen recommendations!")
            return False
        
        # Check if we have social recommendations
        if "social_dataset" in recommendations:
            print("  ✓ Found social recommendations")
        else:
            print("  ✗ Missing social recommendations!")
            return False
        
        return True
    except:
        print("  ✗ Can't read recommendations file!")
        return False

def run_all_unit_tests():
    """Run my basic tests"""
    print("Running simple tests...")
    
    tests_passed = 0
    total_tests = 3
    
    # Test 1: Check files
    if test_data_files():
        tests_passed += 1
    
    # Test 2: Try loading data
    if test_load_data():
        tests_passed += 1
    
    # Test 3: Check recommendations
    if test_recommendations():
        tests_passed += 1
    
    if tests_passed == total_tests:
        print("✅ All basic tests work!")
        return True
    else:
        print(f"❌ Only {tests_passed} out of {total_tests} tests passed")
        return False

if __name__ == "__main__":
    run_all_unit_tests()
