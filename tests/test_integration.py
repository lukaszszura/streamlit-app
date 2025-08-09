"""
Integration Tests - Digital Wellness Dashboard App

"""

import pandas as pd
import json

def test_data_works_together():
    """Check if teen and social data can be used together"""
    print("Testing if data works together...")
    
    # Load both datasets
    teen_data = pd.read_csv("data/teen_processed.csv")
    social_data = pd.read_csv("data/social_processed.csv")
    
    # Make sure both have data
    if len(teen_data) == 0:
        print("  ✗ Teen data is empty!")
        return False
    if len(social_data) == 0:
        print("  ✗ Social data is empty!")
        return False
    
    print(f"  ✓ Both datasets have data (Teen: {len(teen_data)}, Social: {len(social_data)})")
    
    # Check if both have clusters
    if 'cluster' not in teen_data.columns:
        print("  ✗ Teen data missing cluster column!")
        return False
    if 'cluster' not in social_data.columns:
        print("  ✗ Social data missing cluster column!")
        return False
    
    print("  ✓ Both datasets have cluster assignments")
    
    return True

def test_recommendations_work():
    """Check if recommendations match our data"""
    print("Testing recommendations...")
    
    try:
        with open("data/recommendations.json", "r") as f:
            recommendations = json.load(f)
    except:
        print("  ✗ Can't open recommendations file!")
        return False
    
    # Check if we have teen and social recommendations
    if "teen_dataset" not in recommendations:
        print("  ✗ Missing teen recommendations!")
        return False
    if "social_dataset" not in recommendations:
        print("  ✗ Missing social recommendations!")
        return False
    
    print(f"  ✓ Recommendations work for both datasets")
    
    return True

def test_everything_connects():
    """Test if all parts work together"""
    print("Testing if everything connects...")
    
    # Load data
    try:
        teen_data = pd.read_csv("data/teen_processed.csv")
        social_data = pd.read_csv("data/social_processed.csv")
    except:
        print("  ✗ Can't load data files!")
        return False
    
    # Load recommendations
    try:
        with open("data/recommendations.json", "r") as f:
            recommendations = json.load(f)
    except:
        print("  ✗ Can't load recommendations!")
        return False
    
    # Check if teen data has the right number of clusters
    teen_clusters = teen_data['cluster'].unique()
    if len(teen_clusters) != 2:
        print(f"  ✗ Teen data should have 2 clusters, found {len(teen_clusters)}")
        return False
    
    # Check if social data has the right number of clusters
    social_clusters = social_data['cluster'].unique()
    if len(social_clusters) != 2:
        print(f"  ✗ Social data should have 2 clusters, found {len(social_clusters)}")
        return False
    
    print("  ✓ Everything connects properly")
    return True

def run_all_integration_tests():
    """Run all my integration tests"""
    print("Running integration tests...")
    
    tests_passed = 0
    total_tests = 3
    
    # Test 1: Data works together
    if test_data_works_together():
        tests_passed += 1
    
    # Test 2: Recommendations work
    if test_recommendations_work():
        tests_passed += 1
    
    # Test 3: Everything connects
    if test_everything_connects():
        tests_passed += 1
    
    if tests_passed == total_tests:
        print("✅ All integration tests work!")
        return True
    else:
        print(f"❌ Only {tests_passed} out of {total_tests} tests passed")
        return False

if __name__ == "__main__":
    run_all_integration_tests()
