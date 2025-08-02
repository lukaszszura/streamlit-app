"""
Security Tests - Digital Wellness Dashboard
Testing for safety and bad inputs
"""

import os
import pandas as pd

def test_file_safety():
    """Check if files are safe to use"""
    print("Testing file safety...")
    
    files = ["../data/teen_processed.csv", "../data/social_processed.csv"]
    
    for file_path in files:
        # Check file exists
        assert os.path.exists(file_path), f"File missing: {file_path}"
        
        # Check file can be read
        data = pd.read_csv(file_path)
        assert len(data) > 0, f"File empty: {file_path}"
        
    print("  ✓ Files are safe to use")

def test_data_values():
    """Check data values are reasonable"""
    print("Testing data values...")
    
    teen_data = pd.read_csv("../data/teen_processed.csv")
    
    if 'Daily_Usage_Hours' in teen_data.columns:
        usage = teen_data['Daily_Usage_Hours']
        
        # Check for bad values
        bad_negative = usage[usage < 0]
        bad_too_high = usage[usage > 24]
        
        assert len(bad_negative) == 0, "Found negative usage hours"
        assert len(bad_too_high) == 0, "Found usage over 24 hours"
        
    print("  ✓ Data values look good")

def test_age_values():
    """Check age values make sense"""
    print("Testing age values...")
    
    teen_data = pd.read_csv("../data/teen_processed.csv")
    
    if 'Age' in teen_data.columns:
        ages = teen_data['Age']
        
        # Check for weird ages
        bad_ages = ages[(ages < 0) | (ages > 100)]
        assert len(bad_ages) == 0, "Found weird age values"
        
    print("  ✓ Age values make sense")

def run_all_security_tests():
    """Run all security tests"""
    print("Security Tests - Digital Wellness Dashboard")
    print("=" * 40)
    
    try:
        test_file_safety()
        test_data_values()
        test_age_values()
        print("All security tests passed!")
        return True
    except Exception as e:
        print(f"Security test failed: {e}")
        return False

if __name__ == '__main__':
    run_all_security_tests()
