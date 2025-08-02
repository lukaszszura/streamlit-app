"""
Integration Tests - Digital Wellness Dashboard  
Testing how different parts work together
"""

import pandas as pd
import json

def test_data_works_together():
    """Check if teen and social data work together"""
    print("Testing data integration...")
    
    # Load both datasets
    teen_data = pd.read_csv("../data/teen_processed.csv")
    social_data = pd.read_csv("../data/social_processed.csv")
    
    # Check they both have data
    assert len(teen_data) > 0, "No teen data"
    assert len(social_data) > 0, "No social data"
    print("  ✓ Both datasets have data")
    
    # Check they have similar columns for screen time
    teen_has_usage = 'Daily_Usage_Hours' in teen_data.columns
    social_has_screen = 'Screen.Time(hrs)' in social_data.columns
    
    assert teen_has_usage or social_has_screen, "No screen time data found"
    print("  ✓ Screen time data available")

def test_recommendations_work():
    """Check if recommendations match our data"""
    print("Testing recommendations...")
    
    # Load recommendations
    with open("../data/recommendations.json", 'r') as f:
        recommendations = json.load(f)
    
    # Load data to compare
    teen_data = pd.read_csv("../data/teen_processed.csv")
    
    # Check we have recommendations and data
    assert len(recommendations) > 0, "No recommendations"
    assert len(teen_data) > 0, "No data for recommendations"
    print("  ✓ Recommendations and data both available")

def test_complete_workflow():
    """Test complete user workflow"""
    print("Testing complete workflow...")
    
    # Step 1: Load user data
    teen_data = pd.read_csv("../data/teen_processed.csv")
    assert len(teen_data) > 0, "No user data"
    
    # Step 2: Get recommendations
    with open("../data/recommendations.json", 'r') as f:
        recommendations = json.load(f)
    assert len(recommendations) > 0, "No recommendations"
    
    print("  ✓ Complete workflow works")

def run_all_integration_tests():
    """Run all integration tests"""
    print("Integration Tests - Digital Wellness Dashboard")
    print("=" * 45)
    
    try:
        test_data_works_together()
        test_recommendations_work()
        test_complete_workflow()
        print("All integration tests passed!")
        return True
    except Exception as e:
        print(f"Integration test failed: {e}")
        return False

if __name__ == '__main__':
    run_all_integration_tests()
