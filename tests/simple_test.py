import os
import pandas as pd

print("Testing from tests directory...")
print("Current directory:", os.getcwd())

# Test relative paths
data_files = [
    "../data/teen_processed.csv",
    "../data/social_processed.csv", 
    "../data/recommendations.json"
]

for file_path in data_files:
    if os.path.exists(file_path):
        print(f"✅ Found: {file_path}")
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
            print(f"   Rows: {len(df)}, Columns: {len(df.columns)}")
    else:
        print(f"❌ Missing: {file_path}")

print("Test complete!")
