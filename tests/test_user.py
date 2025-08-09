"""
User Tests - Digital Wellness Dashboard App

"""

import pandas as pd
import json

def test_user_can_see_data():
    """Check if users can see their data"""
    print("Testing if users can see data...")
    
    try:
        teen_data = pd.read_csv("data/teen_processed.csv")
        social_data = pd.read_csv("data/social_processed.csv")
        
        if len(teen_data) > 0 and len(social_data) > 0:
            print("  ✓ Users can see their data")
            return True
        else:
            print("  ✗ No data for users to see!")
            return False
    except:
        print("  ✗ Can't load data for users!")
        return False

def test_recommendations_helpful():
    """Check if recommendations are helpful"""
    print("Testing if recommendations are helpful...")
    
    try:
        with open("data/recommendations.json", 'r') as f:
            recommendations = json.load(f)
        
        if len(recommendations) > 0:
            print("  ✓ Recommendations are available for users")
            return True
        else:
            print("  ✗ No recommendations for users!")
            return False
    except:
        print("  ✗ Can't load recommendations for users!")
        return False

def test_app_makes_sense():
    """Check if the app makes sense to users"""
    print("Testing if app makes sense...")
    
    try:
        # Check if data has alues
        teen_data = pd.read_csv("data/teen_processed.csv")
        
        # Check sleep hours 
        if 'Sleep_Hours' in teen_data.columns:
            avg_sleep = teen_data['Sleep_Hours'].mean()
            if avg_sleep > 0 and avg_sleep < 15:
                print(f"  ✓ Sleep data looks reasonable (avg: {avg_sleep:.1f} hours)")
                return True
            else:
                print(f"  ✗ Sleep data looks weird (avg: {avg_sleep:.1f} hours)")
                return False
        else:
            print("  ✓ Data structure looks fine")
            return True
    except:
        print("  ✗ Can't check if data makes sense!")
        return False

def run_all_user_tests():
    """Run all user tests"""
    print("Running user tests...")
    
    tests_passed = 0
    total_tests = 3
    
    # Test 1: Users can see data
    if test_user_can_see_data():
        tests_passed += 1
    
    # Test 2: Recommendations are helpful
    if test_recommendations_helpful():
        tests_passed += 1
    
    # Test 3: App makes sense
    if test_app_makes_sense():
        tests_passed += 1
    
    if tests_passed == total_tests:
        print("✅ All user tests work!")
        return True
    else:
        print(f"❌ Only {tests_passed} out of {total_tests} tests passed")
        return False

if __name__ == "__main__":
    run_all_user_tests()
