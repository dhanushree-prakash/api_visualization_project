import requests
import matplotlib.pyplot as plt
import seaborn as sns

# Replace with your OpenWeatherMap API key
API_KEY = '605b5df909fbf8243614753bbdd4bbe8'
CITY = 'London'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

# Fetch data from the API
def fetch_weather_data(city, api_key):
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use metric units for Celsius
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code)
        return None

# Process the data
data = fetch_weather_data(CITY, API_KEY)
if data:
    temperature = data['main']['temp']
    feels_like = data['main']['feels_like']
    humidity = data['main']['humidity']
    weather_desc = data['weather'][0]['description']

    print(f"City: {CITY}")
    print(f"Temperature: {temperature}°C")
    print(f"Feels Like: {feels_like}°C")
    print(f"Humidity: {humidity}%")
    print(f"Weather: {weather_desc}")

    # Visualization
    metrics = ['Temperature', 'Feels Like', 'Humidity']
    values = [temperature, feels_like, humidity]

    sns.barplot(x=metrics, y=values, palette='coolwarm')
    plt.title(f"Weather Metrics for {CITY}")
    plt.ylabel("Value")
    plt.show()
else:
    print("Failed to fetch data.")
