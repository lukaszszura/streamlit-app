import pandas as pd
import json

def test_user_can_see_data():
    print("Testing user data access...")
    teen_data = pd.read_csv("data/teen_processed.csv")
    social_data = pd.read_csv("data/social_processed.csv")
    assert len(teen_data) > 0, "No teen data for users"
    assert len(social_data) > 0, "No social data for users"
    print("  ✓ Users can see their data")

def test_recommendations_helpful():
    print("Testing recommendations...")
    with open("data/recommendations.json", 'r') as f:
        recommendations = json.load(f)
    assert len(recommendations) > 0, "No recommendations for users"
    print("  ✓ Recommendations are helpful")

def test_data_quality():
    print("Testing data quality...")
    teen_data = pd.read_csv("data/teen_processed.csv")
    if 'Daily_Usage_Hours' in teen_data.columns:
        usage = teen_data['Daily_Usage_Hours'].mean()
        assert usage > 0, "Usage shows no activity"
        assert usage < 25, "Usage shows impossible values"
    print("  ✓ Data makes sense to users")

def run_all_user_tests():
    """Run all user tests and return success status"""
    try:
        print("Running user tests...")
        test_user_can_see_data()
        test_recommendations_helpful()
        test_data_quality()
        print("✅ All user tests passed!")
        return True
    except Exception as e:
        print(f"❌ User tests failed: {e}")
        return False

if __name__ == "__main__":
    print("Running user tests...")
    success = run_all_user_tests()
    if not success:
        exit(1)
