import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import io
import base64
import os
from datetime import datetime, timedelta

def generate_sample_data():
    """Generate sample weather data if the CSV file is not available"""
    # Create date range for the past year
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)
    dates = pd.date_range(start=start_date, end=end_date, freq='D')
    
    # Generate random temperature data with seasonal pattern
    temps = []
    for i in range(len(dates)):
        # Create seasonal pattern (higher in summer, lower in winter)
        season_factor = np.sin(2 * np.pi * i / 365)
        base_temp = 15  # Base temperature
        seasonal_variation = 10 * season_factor  # 10 degrees variation
        random_variation = np.random.normal(0, 3)  # Random daily variation
        temp = base_temp + seasonal_variation + random_variation
        temps.append(temp)
    
    # Create DataFrame
    df = pd.DataFrame({
        'Date': dates,
        'Temperature': temps,
        'Humidity': np.random.uniform(30, 90, len(dates)),
        'Pressure': np.random.uniform(990, 1030, len(dates))
    })
    
    return df

def analyze_weather(csv_path=None):
    """Analyze weather data and return results including plot"""
    try:
        if csv_path and os.path.exists(csv_path):
            df = pd.read_csv(csv_path, parse_dates=['Date'], index_col='Date')
        else:
            # Use sample data if file doesn't exist
            df = generate_sample_data()
            df = df.set_index('Date')
        
        # Process the data
        if 'Rain' in df.columns:
            df.drop(columns=['Rain'], inplace=True)
        
        plot_col = 'Temperature'
        results = {}
        
        if plot_col in df.columns:
            # Calculate monthly averages
            monthly_mean_temp = df[plot_col].resample('ME').mean()
            results['monthly_average'] = monthly_mean_temp.to_dict()
            
            # Create plot
            plt.style.use('seaborn-v0_8-whitegrid')
            fig, ax = plt.subplots(figsize=(10, 6))
            
            monthly_mean_temp.plot(ax=ax, marker='o', linestyle='-', color='b')
            
            ax.set_title('Monthly Average Temperature Over Time', fontsize=16)
            ax.set_ylabel('Average Temperature (°C)', fontsize=12)
            ax.set_xlabel('Month', fontsize=12)
            
            ax.tick_params(axis='x', rotation=45)
            ax.grid(True, which='both', linestyle='--', linewidth=0.5)
            
            plt.tight_layout()
            
            # Save plot to a bytes buffer
            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            
            # Convert plot to base64 string
            plot_data = base64.b64encode(buf.getvalue()).decode('utf-8')
            results['plot'] = plot_data
            
            plt.close()  # Close the plot to free memory
            
            # Add statistics
            results['statistics'] = {
                'mean': df[plot_col].mean(),
                'max': df[plot_col].max(),
                'min': df[plot_col].min(),
                'std': df[plot_col].std()
            }
            
            return results
        else:
            return {"error": f"Column '{plot_col}' not found in the DataFrame."}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    # For local testing
    results = analyze_weather()
    print("Analysis complete. Statistics:")
    if 'statistics' in results:
        for key, value in results['statistics'].items():
            print(f"{key}: {value}")
