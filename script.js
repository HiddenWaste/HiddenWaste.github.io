document.addEventListener('DOMContentLoaded', function () {
    // Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
    const apiKey = 'YOUR_API_KEY';
    const city = 'YOUR_CITY_NAME'; // Replace with the city name you want to get the forecast for

    const apiUrl = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}`;

    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            const weatherInfo = document.getElementById('weather-info');
            const temperature = Math.round(data.main.temp - 273.15); // Convert temperature to Celsius
            const description = data.weather[0].description;

            weatherInfo.innerHTML = `Temperature: ${temperature}°C, Description: ${description}`;
        })
        .catch(error => {
            console.error('Error fetching weather data:', error);
            document.getElementById('weather-info').innerHTML = 'Unable to fetch weather data';
        });
});
