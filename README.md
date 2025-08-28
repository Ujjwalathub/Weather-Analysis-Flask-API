Weather Analysis Flask APIA simple and secure Flask-based API that provides weather data analysis. It features public and protected endpoints, including a route that performs a statistical analysis of weather data and returns the results along with a visualized plot.FeaturesPublic Endpoint: An open endpoint for basic API information.Protected Endpoint: Requires an API key for access to protected data.Weather Analysis Endpoint:Analyzes historical weather data (Temperature, Humidity, Pressure).If no data file is provided, it generates sample data for the past year.Returns key statistics (mean, max, min, standard deviation).Generates and returns a base64-encoded PNG image of the monthly average temperature.Technologies UsedBackend: Python, FlaskData Analysis: Pandas, NumPyData Visualization: MatplotlibInstallationClone the repository:git clone https://github.com/your-username/weather-analysis-api.git
cd weather-analysis-api
Create and activate a virtual environment (recommended):python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required dependencies:pip install -r requirements.txt
Running the ApplicationTo run the Flask development server, use the following command:flask run
The application will be running at http://127.0.0.1:5000.API Endpoints1. HomeURL: /Method: GETDescription: Welcome message for the API.Response:{
  "message": "Welcome to the API. Use /public for public endpoint and /protected for protected endpoint. Try /weather for weather analysis."
}
2. Public EndpointURL: /publicMethod: GETDescription: A public endpoint that does not require authentication.Response:{
  "message": "This is a public endpoint. Anyone can see this."
}
3. Protected EndpointURL: /protectedMethod: GETDescription: A protected endpoint that requires API key authentication.Headers:X-API-Key: f47ac10b-58cc-4372-a567-0e02b2c3d479Success Response:{
  "message": "Success! You are authorized to see this secret data."
}
Error Response (if key is missing or invalid):{
  "error": "Unauthorized. Invalid or missing API Key."
}
4. Weather AnalysisURL: /weatherMethod: GETDescription: Performs weather analysis and returns statistics and a plot.Success Response:{
    "message": "Weather analysis completed successfully",
    "monthly_averages": {
        "2023-10-31T00:00:00.000Z": 15.123,
        "...": "..."
    },
    "plot_base64": "iVBORw0KGgoAAAANSUhEUgAABAAAA...",
    "statistics": {
        "max": 25.8,
        "mean": 14.9,
        "min": 3.2,
        "std": 5.7
    }
}
