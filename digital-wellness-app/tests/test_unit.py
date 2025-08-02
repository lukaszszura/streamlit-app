"""
Unit Tests - Digital Wellness Dashboard
Testing individual parts of the app
"""

import os
import pandas as pd
import json

def test_data_files():
    """Check if data files exist"""
    print("Checking data files...")
    
    # Check teen data
    assert os.path.exists("../data/teen_processed.csv"), "Teen data file missing"
    print("  ✓ Teen data file found")
    
    # Check social data  
    assert os.path.exists("../data/social_processed.csv"), "Social data file missing"
    print("  ✓ Social data file found")
    
    # Check recommendations
    assert os.path.exists("../data/recommendations.json"), "Recommendations file missing"
    print("  ✓ Recommendations file found")

def test_load_data():
    """Check if we can load the data"""
    print("Testing data loading...")
    
    # Load teen data
    teen_data = pd.read_csv("../data/teen_processed.csv")
    assert len(teen_data) > 0, "Teen data is empty"
    print("  ✓ Teen data loads correctly")
    
    # Load social data
    social_data = pd.read_csv("../data/social_processed.csv") 
    assert len(social_data) > 0, "Social data is empty"
    print("  ✓ Social data loads correctly")

def test_data_columns():
    """Check if data has required columns"""
    print("Checking data columns...")
    
    teen_data = pd.read_csv("../data/teen_processed.csv")
    
    # Check for important columns
    assert 'Daily_Usage_Hours' in teen_data.columns, "Missing usage hours column"
    print("  ✓ Usage hours column found")
    
    assert 'Age' in teen_data.columns, "Missing age column"
    print("  ✓ Age column found")

def run_all_unit_tests():
    """Run all unit tests"""
    print("Unit Tests - Digital Wellness Dashboard")
    print("=" * 40)
    
    try:
        test_data_files()
        test_load_data() 
        test_data_columns()
        print("All unit tests passed!")
        return True
    except Exception as e:
        print(f"Unit test failed: {e}")
        return False

if __name__ == '__main__':
    run_all_unit_tests()
