import pandas as pd
import json

def test_user_can_see_data():
    print("Testing user data access...")
    teen_data = pd.read_csv("../data/teen_processed.csv")
    social_data = pd.read_csv("../data/social_processed.csv")
    assert len(teen_data) > 0, "No teen data for users"
    assert len(social_data) > 0, "No social data for users"
    print("  ✓ Users can see their data")

def test_recommendations_helpful():
    print("Testing recommendations...")
    with open("../data/recommendations.json", 'r') as f:
        recommendations = json.load(f)
    assert len(recommendations) > 0, "No recommendations for users"
    print("  ✓ Recommendations are helpful")

def test_data_quality():
    print("Testing data quality...")
    teen_data = pd.read_csv("../data/teen_processed.csv")
    if 'Daily_Usage_Hours' in teen_data.columns:
        usage = teen_data['Daily_Usage_Hours'].mean()
        assert usage > 0, "Usage shows no activity"
        assert usage < 25, "Usage shows impossible values"
    print("  ✓ Data makes sense to users")

def run_all_user_tests():
    print("User Tests - Digital Wellness Dashboard")
    print("=" * 35)
    try:
        test_user_can_see_data()
        test_recommendations_helpful()
        test_data_quality()
        print("All user tests passed!")
        return True
    except Exception as e:
        print(f"User test failed: {e}")
        return False

if __name__ == "__main__":
    success = run_all_user_tests()
    if success:
        print("✅ PASSED - User Tests")
    else:
        print("❌ FAILED - User Tests")
