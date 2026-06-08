# StockAnalyticsPro - Weather Dashboard

A modern, responsive weather dashboard built with Flask and OpenWeatherMap API. Get real-time weather data, forecasts, and beautiful visualizations.

## Features

- 🌍 **Search by City** - Search weather information for any city worldwide
- 📍 **Geolocation** - Get weather for your current location automatically
- 📊 **Current Weather** - View detailed current weather conditions
- 📅 **5-Day Forecast** - See upcoming weather predictions
- 🌡️ **Temperature Units** - Toggle between Celsius and Fahrenheit
- 📱 **Responsive Design** - Works seamlessly on desktop, tablet, and mobile devices
- 🎨 **Modern UI** - Beautiful gradient backgrounds and smooth animations
- ⚡ **Real-time Data** - Always up-to-date weather information

## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **API**: OpenWeatherMap API
- **Styling**: Modern CSS with gradients and animations

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- An OpenWeatherMap API key (free tier available)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/babu961/StockAnalyticsPro.git
   cd StockAnalyticsPro/weather_dashboard
   ```

2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Get your OpenWeatherMap API key**
   - Visit [OpenWeatherMap](https://openweathermap.org/api)
   - Sign up for a free account
   - Copy your API key

5. **Create environment configuration**
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your OpenWeatherMap API key:
   ```
   OPENWEATHER_API_KEY=your_api_key_here
   FLASK_ENV=development
   FLASK_DEBUG=True
   ```

6. **Run the application**
   ```bash
   python app.py
   ```

7. **Open in browser**
   Navigate to `http://localhost:5000`

## Project Structure

```
weather_dashboard/
├── app.py                 # Main Flask application
├── config.py             # Configuration management
├── weather_service.py    # Weather API service layer
├── requirements.txt      # Project dependencies
├── .env.example          # Environment variables template
├── templates/
│   └── dashboard.html    # Main HTML template
└── static/
    ├── css/
    │   └── style.css     # Application styles
    └── js/
        └── app.js        # Frontend JavaScript
```

## API Endpoints

### Current Weather
- **Endpoint**: `/api/weather/current`
- **Method**: GET
- **Parameters**:
  - `city` (required): City name (e.g., "London")
  - `units` (optional): "metric" (default) or "imperial"
- **Example**: `/api/weather/current?city=London&units=metric`

### 5-Day Forecast
- **Endpoint**: `/api/weather/forecast`
- **Method**: GET
- **Parameters**:
  - `city` (required): City name
  - `units` (optional): "metric" (default) or "imperial"
- **Example**: `/api/weather/forecast?city=London&units=metric`

### Weather by Coordinates
- **Endpoint**: `/api/weather/coordinates`
- **Method**: GET
- **Parameters**:
  - `lat` (required): Latitude
  - `lon` (required): Longitude
  - `units` (optional): "metric" (default) or "imperial"
- **Example**: `/api/weather/coordinates?lat=51.5074&lon=-0.1278&units=metric`

### Health Check
- **Endpoint**: `/api/health`
- **Method**: GET
- **Response**: API health status and configuration check

## Configuration

### Environment Variables

- `OPENWEATHER_API_KEY`: Your OpenWeatherMap API key (required)
- `FLASK_ENV`: Environment mode ("development" or "production")
- `FLASK_DEBUG`: Enable Flask debug mode (True or False)

## Features Explained

### Current Weather Display
- City name and country
- Current temperature with "feels like" temperature
- Weather description with icon
- Min/Max temperatures
- Humidity percentage
- Wind speed and direction
- Atmospheric pressure
- Visibility
- Cloud coverage
- Sunrise and sunset times

### 5-Day Forecast
- Hourly/Daily forecasts for the next 5 days
- Temperature trends
- Weather conditions
- Humidity and wind data
- Precipitation forecasts
- Cloud coverage

### User Interface
- Clean, modern design with gradient backgrounds
- Smooth animations and transitions
- Responsive grid layouts
- Interactive hover effects
- Real-time error handling
- Loading states
- Welcome screen with feature highlights

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Troubleshooting

### API Key Issues
- Ensure you have a valid OpenWeatherMap API key
- Check that the API key is correctly set in the `.env` file
- The free tier may have rate limits (60 calls/min)

### CORS Issues
- CORS is enabled for all origins by default
- Modify `CORS(app)` in `app.py` for production use

### Location Access Denied
- Check browser location permissions
- Some browsers block geolocation on non-HTTPS sites
- Use HTTPS in production

### Temperature Not Showing
- Verify your API key is valid
- Check that you're using the correct city name
- Some cities may require disambiguation (e.g., "Springfield, USA")

## Performance Tips

- Use browser caching for static files
- Implement request debouncing for search
- Consider adding Redis caching for API responses
- Use CDN for static assets in production

## Future Enhancements

- [ ] Save favorite cities
- [ ] Weather alerts and notifications
- [ ] Historical weather data
- [ ] Weather charts and graphs
- [ ] Air quality information
- [ ] UV index data
- [ ] Pollen count information
- [ ] Multiple language support
- [ ] Dark mode toggle
- [ ] Weather comparison between cities

## API Rate Limits

OpenWeatherMap Free Tier:
- 60 calls/minute
- 1,000,000 calls/month
- 5-day forecast with 3-hour step

## License

Apache License 2.0 - See LICENSE file for details

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

For issues, questions, or suggestions, please open an issue on GitHub.

## Acknowledgments

- [OpenWeatherMap](https://openweathermap.org/) - Weather data provider
- [Font Awesome](https://fontawesome.com/) - Icons
- [Flask](https://flask.palletsprojects.com/) - Web framework

## Contact

**Author**: babu961  
**Repository**: https://github.com/babu961/StockAnalyticsPro

---

**Happy weather checking! 🌤️**
