import pandas as pd
import requests
import json

def get_lat_lon(country_code, city_name):
    # Load the CSV file into a DataFrame
    world_cities = pd.read_csv('data/world_cities.csv')

    # Filter the DataFrame to find the specific city based on country code and city name
    city_data = world_cities[(world_cities['country'] == country_code) & 
                             (world_cities['name'] == city_name)]
    
    # Convert the filtered data to a list of dictionaries for easy access
    city_data = city_data.to_dict('records')
    
    # Raise an error if no matching record is found
    if len(city_data) == 0:
        raise ValueError(f"No records found for {city_name}, {country_code} in data/world_cities.csv")

    # Extract latitude and longitude from the first matching record
    latitude = city_data[0]['lat']
    longitude = city_data[0]['lng']

    # Return latitude and longitude as a tuple
    return latitude, longitude

def build_url(latitude: float, longitude: float, start_date: str, end_date: str):
    # Base URL for the historical weather API
    base_historical_url = "https://archive-api.open-meteo.com/v1/era5?"
    
    # Add latitude and longitude parameters to the URL
    params_lat_long = "latitude=" + str(latitude) + "&longitude=" + str(longitude)
    
    # Add start and end date parameters for the data range
    params_date = "&start_date=" + start_date + "&end_date=" + end_date

    # Specify data type (precipitation) and set timezone to auto for local adjustment
    params_others = "&daily=precipitation_sum,precipitation_hours&timezone=auto"

    # Combine all parts to form the final API URL
    final_url = base_historical_url + params_lat_long + params_date + params_others

    return final_url

def get_historical_data(country_code, city_name, start_date="2023-01-01", end_date="2023-12-31"):
    """
    Retrieves historical weather data for a specific city using default dates if none are provided.
    
    Parameters:
        country_code (str): The country code of the city.
        city_name (str): The name of the city.
        start_date (str): Start date in "YYYY-MM-DD" format. Defaults to Jan 1, 2023.
        end_date (str): End date in "YYYY-MM-DD" format. Defaults to Dec 31, 2023.
    
    Returns:
        dict: Dictionary of historical rainfall data.
    """
    
    # Get latitude and longitude for the specified city and country
    latitude, longitude = get_lat_lon(country_code, city_name)
    
    # Build the API URL using the latitude, longitude, and date range
    url = build_url(latitude, longitude, start_date, end_date)
    
    # Make an API request to retrieve historical weather data
    response = requests.get(url)
    
    # Parse the JSON response and return daily data
    data = response.json()
    
    return data.get("daily", {})
