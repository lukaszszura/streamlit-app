"""
Integration Tests - Digital Wellness Dashboard  
Testing how different parts work together
"""

import pandas as pd
import json
import pickle

def test_data_works_together():
    """Check if teen and social data work together"""
    print("Testing data integration...")
    
    # Load both datasets
    teen_data = pd.read_csv("data/teen_processed.csv")
    social_data = pd.read_csv("data/social_processed.csv")
    
    # Check they both have data
    assert len(teen_data) > 0, "No teen data"
    assert len(social_data) > 0, "No social data"
    print(f"  ✓ Both datasets have data (Teen: {len(teen_data)}, Social: {len(social_data)})")
    
    # Check they both have cluster assignments
    assert 'cluster' in teen_data.columns, "Teen data missing cluster column"
    assert 'cluster' in social_data.columns, "Social data missing cluster column"
    print("  ✓ Both datasets have cluster assignments")
    
    # Check cluster values are valid
    teen_clusters = set(teen_data['cluster'].unique())
    social_clusters = set(social_data['cluster'].unique())
    assert teen_clusters == {0, 1}, f"Invalid teen clusters: {teen_clusters}"
    assert social_clusters == {0, 1}, f"Invalid social clusters: {social_clusters}"
    print("  ✓ All cluster assignments are valid")

def test_recommendations_work():
    """Check if recommendations match our data"""
    print("Testing recommendations integration...")
    
    with open("data/recommendations.json", "r") as f:
        recommendations = json.load(f)
    
    # Check we have recommendations for different datasets
    assert "teen_dataset" in recommendations, "Missing teen dataset recommendations"
    assert "social_dataset" in recommendations, "Missing social dataset recommendations"
    
    # Check teen clusters
    teen_clusters = recommendations["teen_dataset"]
    assert len(teen_clusters) > 0, "No teen cluster recommendations"
    
    # Check social clusters
    social_clusters = recommendations["social_dataset"]
    assert len(social_clusters) > 0, "No social cluster recommendations"
    
    # Verify each cluster has recommendations
    for cluster_name, cluster_data in teen_clusters.items():
        assert "recommendations" in cluster_data, f"Missing recommendations in teen {cluster_name}"
        assert len(cluster_data["recommendations"]) > 0, f"Empty recommendations in teen {cluster_name}"
    
    for cluster_name, cluster_data in social_clusters.items():
        assert "recommendations" in cluster_data, f"Missing recommendations in social {cluster_name}"
        assert len(cluster_data["recommendations"]) > 0, f"Empty recommendations in social {cluster_name}"
    
    print(f"  ✓ Recommendations work for both datasets (Teen: {len(teen_clusters)}, Social: {len(social_clusters)} clusters)")

def test_models_work_with_data():
    """Check if models can process our data"""
    print("Testing model-data integration...")
    
    # Load data
    teen_data = pd.read_csv("data/teen_processed.csv")
    social_data = pd.read_csv("data/social_processed.csv")
    
    # Load models
    with open("models/teen_kmeans_model.pkl", "rb") as f:
        teen_model = pickle.load(f)
    with open("models/teen_scaler.pkl", "rb") as f:
        teen_scaler = pickle.load(f)
    with open("models/social_hierarchical_model.pkl", "rb") as f:
        social_model = pickle.load(f)
    with open("models/social_scaler.pkl", "rb") as f:
        social_scaler = pickle.load(f)
    
    # Test teen model with teen data (sample)
    teen_features = ['Sleep_Hours', 'Screen_Time_Before_Bed', 'Time_on_Social_Media', 'Daily_Usage_Hours', 'Age']
    teen_sample = teen_data[teen_features].head(10)
    teen_scaled = teen_scaler.transform(teen_sample)
    teen_predictions = teen_model.predict(teen_scaled)
    
    assert len(teen_predictions) == 10, "Teen model prediction failed"
    assert all(p in [0, 1] for p in teen_predictions), "Invalid teen predictions"
    print("  ✓ Teen model works with teen data")
    
    # Test social model with social data (sample)  
    social_features = [' Sleep Duration ', 'Social Media Usage (hrs)', 'Screen.Time(hrs)', 'Exercise Time (hrs)', 'Age']
    social_sample = social_data[social_features].head(10)
    social_scaled = social_scaler.transform(social_sample)
    
    # Note: Hierarchical clustering doesn't have predict method, but we can check if it fits
    # The model was already trained and saved, so we just verify the scaler works
    assert social_scaled.shape[0] == 10, "Social scaling failed"
    assert social_scaled.shape[1] == 5, "Social features scaling failed"
    print("  ✓ Social model components work with social data")

def test_metrics_consistency():
    """Check if metrics are consistent across files"""
    print("Testing metrics consistency...")
    
    # Load metrics
    with open("data/model_metrics.json", "r") as f:
        metrics = json.load(f)
    
    # Load actual data to verify
    teen_data = pd.read_csv("data/teen_processed.csv")
    social_data = pd.read_csv("data/social_processed.csv")
    
    # Check dataset sizes match
    assert metrics["teen_dataset"]["final_size"] == len(teen_data), "Teen size mismatch"
    assert metrics["social_dataset"]["final_size"] == len(social_data), "Social size mismatch"
    
    # Check total users
    expected_total = len(teen_data) + len(social_data)
    assert metrics["project_info"]["total_users"] == expected_total, "Total users mismatch"
    
    print(f"  ✓ Metrics consistent (Total: {expected_total} users)")

def test_performance_data():
    """Check if performance data is valid"""
    print("Testing performance data...")
    
    performance = pd.read_csv("data/algorithm_performance.csv")
    
    # Check structure
    expected_cols = ['Algorithm', 'Dataset', 'Silhouette_Score', 'Davies_Bouldin_Score', 'Best_Model']
    for col in expected_cols:
        assert col in performance.columns, f"Missing performance column: {col}"
    
    # Check we have data for both datasets
    datasets = set(performance['Dataset'].unique())
    assert 'Teen' in datasets, "Missing teen performance data"
    assert 'Social Media' in datasets, "Missing social performance data"
    
    # Check we have data for all algorithms
    algorithms = set(performance['Algorithm'].unique())
    expected_algs = {'K-Means', 'DBSCAN', 'Hierarchical'}
    assert algorithms == expected_algs, f"Algorithm mismatch: {algorithms} vs {expected_algs}"
    
    print(f"  ✓ Performance data complete ({len(performance)} records)")

def test_cluster_statistics():
    """Check if cluster statistics are valid"""
    print("Testing cluster statistics...")
    
    # Load cluster data
    teen_clusters = pd.read_csv("data/teen_clusters.csv")
    social_clusters = pd.read_csv("data/social_clusters.csv")
    
    # Load actual data
    teen_data = pd.read_csv("data/teen_processed.csv")
    social_data = pd.read_csv("data/social_processed.csv")
    
    # Verify teen cluster stats
    teen_actual_counts = teen_data['cluster'].value_counts().sort_index()
    for i, row in teen_clusters.iterrows():
        cluster_id = row['cluster']
        expected_count = teen_actual_counts[cluster_id]
        assert row['count'] == expected_count, f"Teen cluster {cluster_id} count mismatch"
    
    # Verify social cluster stats
    social_actual_counts = social_data['cluster'].value_counts().sort_index()
    for i, row in social_clusters.iterrows():
        cluster_id = row['cluster']
        expected_count = social_actual_counts[cluster_id]
        assert row['count'] == expected_count, f"Social cluster {cluster_id} count mismatch"
    
    print("  ✓ Cluster statistics match actual data")

def run_all_integration_tests():
    """Run all integration tests and return success status"""
    try:
        print("Running integration tests...")
        test_data_works_together()
        test_recommendations_work()
        test_models_work_with_data()
        test_metrics_consistency()
        test_performance_data()
        test_cluster_statistics()
        print("✅ All integration tests passed!")
        return True
    except Exception as e:
        print(f"❌ Integration tests failed: {e}")
        return False

if __name__ == "__main__":
    print("Running integration tests...")
    success = run_all_integration_tests()
    if not success:
        exit(1)
