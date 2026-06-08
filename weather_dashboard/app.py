from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from weather_service import WeatherService
from config import config
import os

# Initialize Flask app
app = Flask(__name__, template_folder='templates', static_folder='static')
env = os.getenv('FLASK_ENV', 'development')
app.config.from_object(config[env])

# Enable CORS
CORS(app)

# Initialize weather service
weather_service = WeatherService()

@app.route('/')
def index():
    """Render the main dashboard page"""
    return render_template('dashboard.html')

@app.route('/api/weather/current')
def get_current_weather():
    """API endpoint for current weather"""
    city = request.args.get('city', 'London')
    units = request.args.get('units', 'metric')
    
    if not city:
        return jsonify({'error': 'City parameter is required'}), 400
    
    weather_data = weather_service.get_current_weather(city, units)
    
    if weather_data is None:
        return jsonify({'error': f'Could not fetch weather data for {city}'}), 404
    
    return jsonify(weather_data)

@app.route('/api/weather/forecast')
def get_forecast():
    """API endpoint for weather forecast"""
    city = request.args.get('city', 'London')
    units = request.args.get('units', 'metric')
    
    if not city:
        return jsonify({'error': 'City parameter is required'}), 400
    
    forecast_data = weather_service.get_forecast(city, units)
    
    if forecast_data is None:
        return jsonify({'error': f'Could not fetch forecast data for {city}'}), 404
    
    return jsonify(forecast_data)

@app.route('/api/weather/coordinates')
def get_weather_by_coordinates():
    """API endpoint for weather by coordinates"""
    try:
        lat = float(request.args.get('lat', 0))
        lon = float(request.args.get('lon', 0))
        units = request.args.get('units', 'metric')
        
        if lat == 0 and lon == 0:
            return jsonify({'error': 'Valid latitude and longitude are required'}), 400
        
        weather_data = weather_service.get_weather_by_coordinates(lat, lon, units)
        
        if weather_data is None:
            return jsonify({'error': 'Could not fetch weather data for the given coordinates'}), 404
        
        return jsonify(weather_data)
    
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid latitude or longitude values'}), 400

@app.route('/api/health')
def health_check():
    """Health check endpoint"""
    api_key_configured = bool(app.config['OPENWEATHER_API_KEY'])
    return jsonify({
        'status': 'healthy',
        'api_configured': api_key_configured
    })

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({'error': 'Resource not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'], host='0.0.0.0', port=5000)
