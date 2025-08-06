# Digital Wellness Dashboard - Clustering Based Recommendations

A web-based dashboard that provides personalized recommendations to reduce late night social media usage and improve sleep quality. Built with Streamlit and machine learning clustering analysis.

## Project Dependencies

- Python >= 3.8
- streamlit >= 1.28.0
- pandas >= 1.5.0
- numpy >= 1.21.0
- plotly >= 5.15.0
- scikit-learn >= 1.1.0
- joblib >= 1.2.0

## Installation Steps

1. Extract the project files
   ```bash
   # Extract the ZIP file to your desired location
   # Navigate to the digital-wellness-app directory
   cd digital-wellness-app
   ```

2. Create and activate a virtual environment (recommended)
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. Install dependencies
   ```bash
   pip install streamlit pandas numpy plotly scikit-learn joblib
   ```

## How to Run the Dashboard

1. Ensure required data files are present:
   - The `data/` folder should contain all processed CSV files
   - Files are automatically generated from the main notebook analysis
   - Required files: teen_processed.csv, social_processed.csv, recommendations.json, etc.

2. Start the Streamlit dashboard
   ```bash
   streamlit run app.py
   ```

3. Access the dashboard
   - Open your web browser and go to `http://localhost:8501`
   - The dashboard will automatically load with the main interface

## How to Use the Dashboard

1. **Overview & Analytics**: View research insights and data visualizations
2. **Take Assessment**: Complete the digital wellness questionnaire 
3. **Get Recommendations**: Receive personalized advice based on your assessment
4. **Research Results**: Understand the machine learning methodology

## Features

- Interactive assessment with risk scoring
- Personalized recommendations based on clustering analysis
- Dark theme interface with professional styling
- Real-time data visualization with Plotly charts
- Mobile-friendly responsive design

## Notes

- Ensure all data files are in the `data/` directory before running
- The dashboard uses machine learning models trained on 7,299+ user records
- Assessment results are stored in session state for personalized recommendations
- No internet connection required - runs completely locally

## Troubleshooting

- If you get import errors, make sure all dependencies are installed
- If data files are missing, run the main project notebook first to generate them
- If the app won't start, check that port 8501 is not already in use
