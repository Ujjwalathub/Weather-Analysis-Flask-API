import uuid
# Generate a fixed API key instead of using environment variables
API_KEY = "f47ac10b-58cc-4372-a567-0e02b2c3d479"  # Fixed API key for authentication
import os
from flask import Flask, request, jsonify, render_template, send_file
from dotenv import load_dotenv
from weather_analysis import analyze_weather

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Use the hardcoded API key
SECRET_API_KEY = API_KEY

# This is an unprotected endpoint
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the API. Use /public for public endpoint and /protected for protected endpoint. Try /weather for weather analysis."})

@app.route('/public')
def public_endpoint():
    return jsonify({"message": "This is a public endpoint. Anyone can see this."})

# This is a protected endpoint
@app.route('/protected')
def protected_endpoint():
    # 1. Get the API key from the request headers
    provided_key = request.headers.get('X-API-Key')

    # 2. Check if the key is missing or incorrect
    if not provided_key or provided_key != SECRET_API_KEY:
        # 3. If invalid, return an error
        return jsonify({"error": "Unauthorized. Invalid or missing API Key."}), 401

    # 4. If the key is valid, proceed with the function
    return jsonify({"message": "Success! You are authorized to see this secret data."})

# Add a weather analysis endpoint
@app.route('/weather')
def weather_analysis():
    try:
        # Run the weather analysis
        results = analyze_weather()
        
        # Return the results as JSON
        return jsonify({
            "message": "Weather analysis completed successfully",
            "statistics": results.get('statistics', {}),
            "monthly_averages": results.get('monthly_average', {}),
            "plot_base64": results.get('plot', "")
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)