class WeatherDashboard {
    constructor() {
        this.currentUnits = 'metric';
        this.currentCity = null;
        this.initElements();
        this.attachEventListeners();
    }

    initElements() {
        // Search elements
        this.cityInput = document.getElementById('cityInput');
        this.searchBtn = document.getElementById('searchBtn');
        this.locationBtn = document.getElementById('locationBtn');
        this.unitsRadios = document.querySelectorAll('input[name="units"]');

        // State elements
        this.loading = document.getElementById('loading');
        this.errorMessage = document.getElementById('error');
        this.welcome = document.getElementById('welcome');
        this.currentWeather = document.getElementById('currentWeather');
        this.forecastSection = document.getElementById('forecastSection');
        this.forecastContainer = document.getElementById('forecastContainer');
    }

    attachEventListeners() {
        this.searchBtn.addEventListener('click', () => this.searchCity());
        this.cityInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') this.searchCity();
        });
        this.locationBtn.addEventListener('click', () => this.useUserLocation());
        this.unitsRadios.forEach(radio => {
            radio.addEventListener('change', (e) => this.onUnitsChange(e));
        });
    }

    async searchCity() {
        const city = this.cityInput.value.trim();
        if (!city) {
            this.showError('Please enter a city name');
            return;
        }

        this.currentCity = city;
        await this.fetchWeatherData();
    }

    async useUserLocation() {
        if (!navigator.geolocation) {
            this.showError('Geolocation is not supported by your browser');
            return;
        }

        this.showLoading();
        navigator.geolocation.getCurrentPosition(
            async (position) => {
                const { latitude, longitude } = position.coords;
                await this.fetchWeatherByCoordinates(latitude, longitude);
            },
            (error) => {
                this.hideLoading();
                let errorMsg = 'Unable to get your location';
                if (error.code === error.PERMISSION_DENIED) {
                    errorMsg = 'Location permission denied. Please enable it in your browser settings.';
                }
                this.showError(errorMsg);
            }
        );
    }

    async fetchWeatherData() {
        this.showLoading();
        try {
            const [currentData, forecastData] = await Promise.all([
                this.fetchCurrentWeather(),
                this.fetchForecast()
            ]);

            if (currentData) {
                this.displayCurrentWeather(currentData);
                this.hideWelcome();
            }

            if (forecastData) {
                this.displayForecast(forecastData);
            }
        } catch (error) {
            this.showError('Failed to fetch weather data. Please try again.');
            console.error('Error:', error);
        } finally {
            this.hideLoading();
        }
    }

    async fetchWeatherByCoordinates(lat, lon) {
        this.showLoading();
        try {
            const response = await fetch(
                `/api/weather/coordinates?lat=${lat}&lon=${lon}&units=${this.currentUnits}`
            );
            const data = await response.json();

            if (response.ok) {
                this.currentCity = data.city;
                this.cityInput.value = data.city;
                this.displayCurrentWeather(data);
                
                // Fetch forecast after getting current data
                const forecastData = await this.fetchForecast();
                if (forecastData) {
                    this.displayForecast(forecastData);
                }
                this.hideWelcome();
            } else {
                this.showError(data.error || 'Failed to fetch weather data');
            }
        } catch (error) {
            this.showError('Failed to fetch weather data');
            console.error('Error:', error);
        } finally {
            this.hideLoading();
        }
    }

    async fetchCurrentWeather() {
        try {
            const response = await fetch(
                `/api/weather/current?city=${this.currentCity}&units=${this.currentUnits}`
            );
            const data = await response.json();

            if (!response.ok) {
                this.showError(data.error || 'City not found');
                return null;
            }

            return data;
        } catch (error) {
            console.error('Error fetching current weather:', error);
            return null;
        }
    }

    async fetchForecast() {
        try {
            const response = await fetch(
                `/api/weather/forecast?city=${this.currentCity}&units=${this.currentUnits}`
            );
            const data = await response.json();

            if (!response.ok) {
                return null;
            }

            return data;
        } catch (error) {
            console.error('Error fetching forecast:', error);
            return null;
        }
    }

    displayCurrentWeather(data) {
        const unit = this.currentUnits === 'metric' ? '°C' : '°F';
        const windUnit = this.currentUnits === 'metric' ? 'm/s' : 'mph';
        const visibilityUnit = this.currentUnits === 'metric' ? 'km' : 'mi';

        document.getElementById('cityName').textContent = `${data.city}, ${data.country}`;
        document.getElementById('timestamp').textContent = new Date(data.timestamp).toLocaleString();
        document.getElementById('temperature').textContent = Math.round(data.temperature);
        document.getElementById('feelsLike').textContent = `Feels like: ${Math.round(data.feels_like)}${unit}`;
        document.getElementById('description').textContent = data.description;
        document.getElementById('minMax').textContent = 
            `${Math.round(data.temp_min)}${unit} / ${Math.round(data.temp_max)}${unit}`;
        document.getElementById('humidity').textContent = `${data.humidity}%`;
        document.getElementById('windSpeed').textContent = `${data.wind_speed.toFixed(1)} ${windUnit}`;
        document.getElementById('pressure').textContent = `${data.pressure} hPa`;
        document.getElementById('visibility').textContent = `${(data.visibility / 1000).toFixed(1)} ${visibilityUnit}`;
        document.getElementById('clouds').textContent = `${data.clouds}%`;
        document.getElementById('sunrise').textContent = data.sunrise;
        document.getElementById('sunset').textContent = data.sunset;

        // Update weather icon
        const iconUrl = `https://openweathermap.org/img/wn/${data.icon}@4x.png`;
        document.getElementById('weatherIcon').src = iconUrl;
        document.getElementById('weatherIcon').alt = data.description;

        // Update temp unit display
        document.querySelectorAll('.temp-unit').forEach(el => {
            el.textContent = unit;
        });

        this.currentWeather.style.display = 'block';
    }

    displayForecast(data) {
        this.forecastContainer.innerHTML = '';

        // Group forecasts by day and take one per day (every 24 hours approximately)
        const groupedForecasts = this.groupForecastsByDay(data.forecasts);

        groupedForecasts.forEach(forecast => {
            const card = this.createForecastCard(forecast);
            this.forecastContainer.appendChild(card);
        });

        this.forecastSection.style.display = 'block';
    }

    groupForecastsByDay(forecasts) {
        const grouped = {};
        const unit = this.currentUnits === 'metric' ? '°C' : '°F';

        forecasts.forEach(forecast => {
            const date = new Date(forecast.timestamp);
            const day = date.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });

            if (!grouped[day]) {
                grouped[day] = forecast;
            }
        });

        return Object.values(grouped).slice(0, 5);
    }

    createForecastCard(forecast) {
        const card = document.createElement('div');
        card.className = 'forecast-card';

        const date = new Date(forecast.timestamp);
        const dayName = date.toLocaleDateString('en-US', { weekday: 'short' });
        const dayDate = date.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
        const time = date.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit' });

        const unit = this.currentUnits === 'metric' ? '°C' : '°F';
        const iconUrl = `https://openweathermap.org/img/wn/${forecast.icon}@3x.png`;

        card.innerHTML = `
            <div class="forecast-time">${dayName}, ${dayDate} ${time}</div>
            <img src="${iconUrl}" alt="${forecast.description}" class="forecast-icon">
            <div class="forecast-temp">${Math.round(forecast.temperature)}${unit}</div>
            <div class="forecast-description">${forecast.description}</div>
            <div class="forecast-details">
                <div class="forecast-details-item">
                    <span>💧 Humidity:</span>
                    <span>${forecast.humidity}%</span>
                </div>
                <div class="forecast-details-item">
                    <span>💨 Wind:</span>
                    <span>${forecast.wind_speed.toFixed(1)} ${this.currentUnits === 'metric' ? 'm/s' : 'mph'}</span>
                </div>
                <div class="forecast-details-item">
                    <span>☁️ Clouds:</span>
                    <span>${forecast.clouds}%</span>
                </div>
                ${forecast.rain > 0 ? `
                <div class="forecast-details-item">
                    <span>🌧️ Rain:</span>
                    <span>${forecast.rain.toFixed(1)} mm</span>
                </div>
                ` : ''}
            </div>
        `;

        return card;
    }

    onUnitsChange(event) {
        this.currentUnits = event.target.value;

        if (this.currentCity) {
            this.fetchWeatherData();
        }
    }

    showLoading() {
        this.loading.style.display = 'block';
        this.errorMessage.style.display = 'none';
    }

    hideLoading() {
        this.loading.style.display = 'none';
    }

    showError(message) {
        this.errorMessage.textContent = message;
        this.errorMessage.style.display = 'block';
        this.currentWeather.style.display = 'none';
        this.forecastSection.style.display = 'none';
        this.hideLoading();
    }

    hideWelcome() {
        this.welcome.style.display = 'none';
    }
}

// Initialize dashboard when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    new WeatherDashboard();
});
