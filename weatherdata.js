// Function to fetch weather data for a specific city
function fetchWeather(city) {
    const apiKey = '4b1a6ebf5a0e9f3e6197c542169d12eb';
    const apiUrl = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}`;

    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            const weatherInfo = document.getElementById('weather-info');
            const temperature = Math.round(data.main.temp - 273.15); // Convert temperature to Celsius
            const description = data.weather[0].description;

            weatherInfo.innerHTML = `${weatherInfo.innerHTML} ${city} - Temperature: ${temperature}°C, Description: ${description}<br><br>`;
        })
        .catch(error => {
            console.error('Error fetching weather data:', error);
            document.getElementById('weather-info').innerHTML = 'Unable to fetch weather data';
        });
}

// Call fetchWeather function with the desired city name
fetchWeather('Madison'); 
fetchWeather('Sioux Falls');
fetchWeather('Bangkok'); 