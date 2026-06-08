import requests
from typing import Dict, Optional, List
from datetime import datetime
from config import Config

class WeatherService:
    """Service for fetching weather data from OpenWeatherMap API"""
    
    def __init__(self):
        self.api_key = Config.OPENWEATHER_API_KEY
        self.base_url = Config.OPENWEATHER_BASE_URL
    
    def get_current_weather(self, city: str, units: str = 'metric') -> Optional[Dict]:
        """
        Fetch current weather for a specific city
        
        Args:
            city: City name
            units: Temperature units ('metric' for Celsius, 'imperial' for Fahrenheit)
            
        Returns:
            Dictionary with weather data or None if request fails
        """
        try:
            endpoint = f"{self.base_url}/weather"
            params = {
                'q': city,
                'appid': self.api_key,
                'units': units
            }
            
            response = requests.get(endpoint, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            return self._parse_current_weather(data)
        
        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather data: {e}")
            return None
    
    def get_forecast(self, city: str, units: str = 'metric') -> Optional[Dict]:
        """
        Fetch 5-day weather forecast for a specific city
        
        Args:
            city: City name
            units: Temperature units ('metric' for Celsius, 'imperial' for Fahrenheit)
            
        Returns:
            Dictionary with forecast data or None if request fails
        """
        try:
            endpoint = f"{self.base_url}/forecast"
            params = {
                'q': city,
                'appid': self.api_key,
                'units': units
            }
            
            response = requests.get(endpoint, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            return self._parse_forecast(data)
        
        except requests.exceptions.RequestException as e:
            print(f"Error fetching forecast data: {e}")
            return None
    
    def get_weather_by_coordinates(self, lat: float, lon: float, units: str = 'metric') -> Optional[Dict]:
        """
        Fetch current weather by geographical coordinates
        
        Args:
            lat: Latitude
            lon: Longitude
            units: Temperature units
            
        Returns:
            Dictionary with weather data or None if request fails
        """
        try:
            endpoint = f"{self.base_url}/weather"
            params = {
                'lat': lat,
                'lon': lon,
                'appid': self.api_key,
                'units': units
            }
            
            response = requests.get(endpoint, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            return self._parse_current_weather(data)
        
        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather data: {e}")
            return None
    
    def _parse_current_weather(self, data: Dict) -> Dict:
        """Parse current weather data from API response"""
        return {
            'city': data['name'],
            'country': data['sys']['country'],
            'temperature': data['main']['temp'],
            'feels_like': data['main']['feels_like'],
            'temp_min': data['main']['temp_min'],
            'temp_max': data['main']['temp_max'],
            'pressure': data['main']['pressure'],
            'humidity': data['main']['humidity'],
            'description': data['weather'][0]['description'],
            'main': data['weather'][0]['main'],
            'icon': data['weather'][0]['icon'],
            'wind_speed': data['wind']['speed'],
            'wind_deg': data['wind'].get('deg', 0),
            'clouds': data['clouds']['all'],
            'visibility': data.get('visibility', 0),
            'sunrise': datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M:%S'),
            'sunset': datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M:%S'),
            'timestamp': datetime.fromtimestamp(data['dt']).isoformat()
        }
    
    def _parse_forecast(self, data: Dict) -> Dict:
        """Parse forecast data from API response"""
        forecasts = []
        
        for item in data['list']:
            forecasts.append({
                'timestamp': datetime.fromtimestamp(item['dt']).isoformat(),
                'temperature': item['main']['temp'],
                'feels_like': item['main']['feels_like'],
                'temp_min': item['main']['temp_min'],
                'temp_max': item['main']['temp_max'],
                'humidity': item['main']['humidity'],
                'pressure': item['main']['pressure'],
                'description': item['weather'][0]['description'],
                'main': item['weather'][0]['main'],
                'icon': item['weather'][0]['icon'],
                'wind_speed': item['wind']['speed'],
                'clouds': item['clouds']['all'],
                'rain': item.get('rain', {}).get('3h', 0),
                'snow': item.get('snow', {}).get('3h', 0)
            })
        
        return {
            'city': data['city']['name'],
            'country': data['city']['country'],
            'forecasts': forecasts
        }
