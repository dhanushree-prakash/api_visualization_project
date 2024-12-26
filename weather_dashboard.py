import streamlit as st  # Importing Streamlit for creating the web application
import requests         # Importing requests library to make API calls
import matplotlib.pyplot as plt  # Importing Matplotlib for creating visualizations
import seaborn as sns    # Importing Seaborn for styling the visualizations

# Replace with your OpenWeatherMap API key
API_KEY = '605b5df909fbf8243614753bbdd4bbe8'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'  # OpenWeatherMap API endpoint for weather data

# Function to fetch weather data from the OpenWeatherMap API
def fetch_weather_data(city, api_key):
    """
    Fetch weather data for a given city using the OpenWeatherMap API.
    Args:
        city (str): Name of the city to fetch data for.
        api_key (str): API key for authentication.
    Returns:
        dict: Parsed JSON data if successful, None otherwise.
    """
    params = {
        'q': city,          # City name to search for
        'appid': api_key,   # API key for authentication
        'units': 'metric'   # Units of measurement (metric system for Celsius)
    }
    response = requests.get(BASE_URL, params=params)  # Sending GET request to the API
    if response.status_code == 200:  # Check if the API request was successful
        return response.json()  # Return the JSON data
    else:
        return None  # Return None if the request fails

# Streamlit App
st.title("Weather Dashboard with Visualization")  # Title of the dashboard

# Input field for city name
city = st.text_input("Enter City Name", "London")  # Default city is set to 'London'

# Button to trigger the weather data fetch
if st.button("Get Weather"):
    data = fetch_weather_data(city, API_KEY)  # Fetch data for the input city
    if data:
        # Extract key weather metrics from the API response
        temperature = data['main']['temp']  # Current temperature
        feels_like = data['main']['feels_like']  # Feels like temperature
        humidity = data['main']['humidity']  # Humidity percentage
        weather_desc = data['weather'][0]['description']  # Weather description

        # Display the fetched weather data on the dashboard
        st.subheader(f"Weather in {city}")  # Subheader for the city
        st.write(f"**Temperature:** {temperature}°C")  # Display temperature
        st.write(f"**Feels Like:** {feels_like}°C")  # Display feels like temperature
        st.write(f"**Humidity:** {humidity}%")  # Display humidity
        st.write(f"**Weather Description:** {weather_desc.capitalize()}")  # Display weather description

        # Create data for the bar graph
        metrics = ['Temperature', 'Feels Like', 'Humidity']  # Labels for the graph
        values = [temperature, feels_like, humidity]  # Corresponding values for the graph

        # Create a bar graph using Matplotlib and Seaborn
        fig, ax = plt.subplots()  # Create a new figure and axes
        sns.barplot(x=metrics, y=values, palette='coolwarm', ax=ax)  # Plot the bar graph
        ax.set_title(f"Weather Metrics for {city}")  # Set graph title
        ax.set_ylabel("Value")  # Set label for the y-axis
        ax.set_xlabel("Metrics")  # Set label for the x-axis

        # Display the graph on the Streamlit dashboard
        st.pyplot(fig)
    else:
        # Display an error message if the API call fails
        st.error("Could not fetch data. Please check the city name or API key.")
