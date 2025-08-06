"""
Unit Tests - Digital Wellness Dashboard
Testing individual parts of the app
"""

import os
import pandas as pd
import json
import pickle

def test_data_files():
    """Check if data files exist"""
    print("Checking data files...")
    
    # Check teen data
    assert os.path.exists("data/teen_processed.csv"), "Teen data file missing"
    print("  ✓ Teen data file found")
    
    # Check social data  
    assert os.path.exists("data/social_processed.csv"), "Social data file missing"
    print("  ✓ Social data file found")
    
    # Check cluster data
    assert os.path.exists("data/teen_clusters.csv"), "Teen clusters file missing"
    assert os.path.exists("data/social_clusters.csv"), "Social clusters file missing"
    print("  ✓ Cluster data files found")
    
    # Check recommendations
    assert os.path.exists("data/recommendations.json"), "Recommendations file missing"
    print("  ✓ Recommendations file found")
    
    # Check model metrics
    assert os.path.exists("data/model_metrics.json"), "Model metrics file missing"
    print("  ✓ Model metrics file found")

def test_load_data():
    """Check if we can load the data"""
    print("Testing data loading...")
    
    # Load teen data
    teen_data = pd.read_csv("data/teen_processed.csv")
    assert len(teen_data) > 0, "Teen data is empty"
    assert len(teen_data) == 3000, f"Expected 3000 teen users, got {len(teen_data)}"
    print(f"  ✓ Teen data loads correctly ({len(teen_data)} users)")
    
    # Load social data
    social_data = pd.read_csv("data/social_processed.csv") 
    assert len(social_data) > 0, "Social data is empty"
    assert len(social_data) == 4299, f"Expected 4299 social users, got {len(social_data)}"
    print(f"  ✓ Social data loads correctly ({len(social_data)} users)")

def test_data_columns():
    """Check if data has required columns"""
    print("Checking data columns...")
    
    teen_data = pd.read_csv("data/teen_processed.csv")
    social_data = pd.read_csv("data/social_processed.csv")
    
    # Check teen data columns
    required_teen_cols = ['Age', 'Sleep_Hours', 'Screen_Time_Before_Bed', 'Time_on_Social_Media', 'Daily_Usage_Hours', 'cluster']
    for col in required_teen_cols:
        assert col in teen_data.columns, f"Missing teen column: {col}"
    print(f"  ✓ Teen data has all required columns ({len(teen_data.columns)} total)")
    
    # Check social data columns  
    required_social_cols = ['Age', ' Sleep Duration ', 'Social Media Usage (hrs)', 'Screen.Time(hrs)', 'cluster']
    for col in required_social_cols:
        assert col in social_data.columns, f"Missing social column: {col}"
    print(f"  ✓ Social data has all required columns ({len(social_data.columns)} total)")

def test_cluster_assignments():
    """Check if cluster assignments are valid"""
    print("Testing cluster assignments...")
    
    teen_data = pd.read_csv("data/teen_processed.csv")
    social_data = pd.read_csv("data/social_processed.csv")
    
    # Check teen clusters
    teen_clusters = teen_data['cluster'].unique()
    assert len(teen_clusters) == 2, f"Expected 2 teen clusters, got {len(teen_clusters)}"
    assert set(teen_clusters) == {0, 1}, f"Expected clusters [0,1], got {teen_clusters}"
    print(f"  ✓ Teen clusters valid: {sorted(teen_clusters)}")
    
    # Check social clusters
    social_clusters = social_data['cluster'].unique()
    assert len(social_clusters) == 2, f"Expected 2 social clusters, got {len(social_clusters)}"
    assert set(social_clusters) == {0, 1}, f"Expected clusters [0,1], got {social_clusters}"
    print(f"  ✓ Social clusters valid: {sorted(social_clusters)}")

def test_models_exist():
    """Check if model files exist"""
    print("Checking model files...")
    
    # Check teen models
    assert os.path.exists("models/teen_kmeans_model.pkl"), "Teen K-Means model missing"
    assert os.path.exists("models/teen_scaler.pkl"), "Teen scaler missing"
    print("  ✓ Teen K-Means model and scaler found")
    
    # Check social models
    assert os.path.exists("models/social_hierarchical_model.pkl"), "Social Hierarchical model missing"
    assert os.path.exists("models/social_scaler.pkl"), "Social scaler missing"
    print("  ✓ Social Hierarchical model and scaler found")

def test_model_loading():
    """Check if models can be loaded"""
    print("Testing model loading...")
    
    try:
        # Load teen models
        with open("models/teen_kmeans_model.pkl", "rb") as f:
            teen_model = pickle.load(f)
        with open("models/teen_scaler.pkl", "rb") as f:
            teen_scaler = pickle.load(f)
        print("  ✓ Teen models load successfully")
        
        # Load social models
        with open("models/social_hierarchical_model.pkl", "rb") as f:
            social_model = pickle.load(f)
        with open("models/social_scaler.pkl", "rb") as f:
            social_scaler = pickle.load(f)
        print("  ✓ Social models load successfully")
        
    except Exception as e:
        raise AssertionError(f"Model loading failed: {e}")

def test_recommendations_structure():
    """Check if recommendations have correct structure"""
    print("Testing recommendations structure...")
    
    with open("data/recommendations.json", "r") as f:
        recommendations = json.load(f)
    
    # Check main structure
    assert "teen_dataset" in recommendations, "Missing teen dataset recommendations"
    assert "social_dataset" in recommendations, "Missing social dataset recommendations"
    
    # Check teen recommendations
    teen_recs = recommendations["teen_dataset"]
    for cluster_name, cluster_data in teen_recs.items():
        assert "recommendations" in cluster_data, f"Missing recommendations in {cluster_name}"
        assert isinstance(cluster_data["recommendations"], list), f"Recommendations should be a list in {cluster_name}"
        assert len(cluster_data["recommendations"]) > 0, f"Empty recommendations in {cluster_name}"
    
    # Check social recommendations
    social_recs = recommendations["social_dataset"]
    for cluster_name, cluster_data in social_recs.items():
        assert "recommendations" in cluster_data, f"Missing recommendations in {cluster_name}"
        assert isinstance(cluster_data["recommendations"], list), f"Recommendations should be a list in {cluster_name}"
        assert len(cluster_data["recommendations"]) > 0, f"Empty recommendations in {cluster_name}"
    
    print(f"  ✓ Recommendations structure is valid")
    
    print(f"  ✓ Recommendations structure valid ({len(recommendations)} groups)")

def run_all_unit_tests():
    """Run all unit tests and return success status"""
    try:
        print("Running unit tests...")
        test_data_files()
        test_load_data() 
        test_data_columns()
        test_cluster_assignments()
        test_models_exist()
        test_model_loading()
        test_recommendations_structure()
        print("✅ All unit tests passed!")
        return True
    except Exception as e:
        print(f"❌ Unit tests failed: {e}")
        return False

if __name__ == "__main__":
    print("Running unit tests...")
    success = run_all_unit_tests()
    if not success:
        exit(1)
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
