import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(r"C:\Users\thesi\OneDrive\Documents\weather_forecast_data.csv", parse_dates=['Pressure'], index_col='Pressure')
print("File loaded successfully. Here are the first 5 rows:")
print(df.head())
print("\nData Information:")
df.info()

num_rows = len(df)
df.index = pd.to_datetime(pd.date_range(start='2022-01-01', periods=num_rows, freq='D'))

if 'Rain' in df.columns:
    df.drop(columns=['Rain'], inplace=True)
    print("\n'Rain' column dropped.")

plot_col = 'Temperature' 

if plot_col in df.columns:
    monthly_mean_temp = df[plot_col].resample('ME').mean()

    print("\nMonthly Average Temperature:")
    print(monthly_mean_temp.head())

    plt.style.use('seaborn-v0_8-whitegrid')
    fig, ax = plt.subplots(figsize=(14, 7))

    monthly_mean_temp.plot(ax=ax, marker='o', linestyle='-', color='b')

    ax.set_title('Monthly Average Temperature Over Time', fontsize=16)
    ax.set_ylabel('Average Temperature (°C)', fontsize=12)
    ax.set_xlabel('Month', fontsize=12)
    
    ax.tick_params(axis='x', rotation=45)
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)
    
    plt.tight_layout()

    plt.savefig('monthly_weather_forecast.png')
    print("\nPlot saved as 'monthly_weather_forecast.png'")

    plt.show()
else:
    print(f"\nError: Column '{plot_col}' not found in the DataFrame.")
    print("Available columns:", df.columns.tolist())
