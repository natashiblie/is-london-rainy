[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/16Ytx_fz)

![London's Rainy Weather](./data/londonrain.jpg)

# Is London Really as Rainy as the Movies Make It Out to Be? 🤔

This project investigates London's rainy reputation by analysing rainfall metrics across major cities. Using data visualisation and statistical metrics, we explore whether London's weather aligns with its portrayal in popular culture. By analysing metrics such as the number of rainy days, monthly total rainfall, and average rain intensity, we gain insights into the reality of London's weather.

## Project Structure

The repository is organised as follows:

```
DS105A-2024-W06-SUMMATIVE-NATASHIBLIE/
├── code/                                     # Folder containing Jupyter Notebooks 
│   └── NB01 - Simple Data Analysis.ipynb     # Notebook for analysing and visualising rainfall data
├── data/                                     # Folder containing data files used in the analysis
│   ├── londonrain.jpg                        # Image file of London rainy weather, used for README
│   └── world_cities.csv                      # CSV file with latitude and longitude of cities involved in the study
│
├── scripts/                                  # Folder containing Python scripts for data collection
│   ├── data_collection_script.py             # Script to collect rainfall data for a specified city and date range
│   └── data_collection_utils.py              # Contains reusable functions for data collection (e.g., get_lat_lon, build_url)
│
├── README.md                                 # Documentation file explaining the project, setup, and usage
└── requirements.txt                          # List of dependencies needed to run the project

```

## Python Scripts

The project includes Python scripts located in the `scripts/` folder. These scripts streamline the data collection process by organising reusable functions and enabling data collection through command-line execution.

1. **data_collection_utils.py**: This script contains reusable functions that support data collection, including:
   - `get_lat_lon(country_code, city_name)`: Retrieves latitude and longitude for a given city.
   - `build_url(latitude, longitude, start_date, end_date)`: Constructs the API URL for retrieving weather data based on city coordinates and date range.
   - `get_historical_data(country_code, city_name, start_date, end_date)`: Fetches historical rainfall data for a specified city and date range.

   These functions make it easier to keep the data collection process organized and simple to manage.

2. **data_collection_script.py**: This is a standalone script designed to collect rainfall data for a specified city and date range. It can be run directly from the terminal and uses command-line arguments to specify parameters, making it flexible for different cities and timeframes. (shown below)

## How to Set Up and Run the Project

This guide provides a step-by-step walkthrough on setting up and running the project, from installation to data analysis and visualisation.

---

1. **Clone the Repository**  
   Begin by cloning this repository to your Nuvolos environment. Open a terminal in Nuvolos, then enter the command: `git clone <repository_url>`
   The repository_url is 'git@github.com:lse-ds105/ds105a-2024-w06-summative-natashiblie.git'

2. **Install Python and Dependencies**  
   In the terminal, check if Python is installed by running: `python --version`  
   If Python is installed, the terminal should show a version number like Python 3.x.x. If it’s not installed, you’ll need to install Python by searching online for installation instructions.
   Then, navigate to the project directory and install the required packages in  terminal by typing: `pip install -r requirements.txt`

3. **Data Collection with Scripts**  
   To collect rainfall data for a specific city and date range, open terminal and run the following command in the project directory:  
   `python scripts/data_collection_script.py <country_code> <city_name> --start_date <start_date> --end_date <end_date> --output_file <output_file>`  
   Replace each placeholder with specific values:  
   - `<country_code>`: The country code for the city (e.g., "GB" for the United Kingdom).  
   - `<city_name>`: The name of the city (e.g., "London").  
   - `<start_date>`: Start date in `YYYY-MM-DD` format. Defaults to `2023-01-01`.  
   - `<end_date>`: End date in `YYYY-MM-DD` format. Defaults to `2023-12-31`.  
   - `<output_file>`: (Optional) Path to save the data as a JSON file. Defaults to `../data/multicity_historical.json`. You should replace it with a similar format, like data/xx_2023.json, where xx represents the city name for easy reference.

   **All terminal commands needed for this project can be found in the Jupyter Notebook under the header 'Data Collection Prerequisite' for easy reference.**

4. **Run Jupyter Notebooks for Visualiations & Results**  
   Use the Nuvolos interface to open the Jupyter Notebook `NB01 - Simple Data Analysis.ipynb` for visualising and analysing the collected data. Click Run at the top of the notebook. These visualisations include metrics like the number of rainy days, monthly rainfall totals, and average rain intensity, providing insights into London's rain patterns relative to other cities.


## Methodology

### Data Source
The data used in this analysis was sourced from the [Open-Meteo Historical Weather API](https://open-meteo.com/en/docs/historical-weather-api), which provides weather-related metrics for various global cities, including London, Cairo, Singapore, and more.

### Data Collection Strategy
In this project, we used the **Historical Weather Data** endpoint from the Open-Meteo API:

| Endpoint         | URL starts with                                      |
|------------------|------------------------------------------------------|
| [Historical Weather Data](https://open-meteo.com/en/docs/historical-weather-api) | `https://archive-api.open-meteo.com/v1/archive` |

The objective is to assess the raininess of **London, UK** relative to other cities with varied climates. We collected historical precipitation data for the entire year of 2023 to enable a detailed comparison of annual rain patterns.

- The `data_collection_script.py` script uses functions from `data_collection_utils.py` to automate data collection. By specifying a city and date range, the script retrieves historical weather data and saves it to a JSON file.


#### Cities Selected for Comparison:
1. **London, UK** – The main city of interest, often portrayed as rainy.
2. **Singapore** – Known for its tropical climate with high annual rainfall.
3. **Cairo, Egypt** – Represents a dry climate with very low annual rainfall.
4. **Buenos Aires, Argentina** – A moderate climate with regular seasonal rainfall.
5. **Mumbai, India** – Known for very high rainfall, particularly during the monsoon season.

These cities offer a range of climates, from dry (Cairo) to tropical (Singapore, Mumbai) and moderate (Buenos Aires), providing a balanced comparison to assess if London's raininess is as prominent as often portrayed.

#### Data Collection Scope
For each city, the following data was retrieved for 2023:
- **Daily Precipitation** (`precipitation_sum`) to measure total rainfall.

## Metrics and Results

### Metrics Analysed
This analysis uses key rainfall metrics to evaluate London’s reputation as a rainy city and compare it with other cities:

- **Number of Rainy Days**: Evaluates the frequency of rainy days in London versus other cities.
- **Monthly Total Rainfall**: Assesses the volume of rain London receives over time.
- **Average Rain Intensity**: Gauges whether London’s rain tends to be light or heavy.

These metrics provide a balanced view of the **frequency, volume and intensity of rainfall**, helping to understand London's weather patterns accurately.

### Results & Visualisations
Each metric is visualised to highlight London’s rain characteristics:

- **Figure 1: Number of Rainy Days - Bar Chart**: London has frequent, light rain, contributing to its "rainy" reputation without significant downpours.
- **Figure 2: Monthly Total Rainfall - Line Graph**: London experiences a steady rainfall trend throughout the year, showing a consistent but moderate volume of rain.
- **Figure 3: Average Rain Intensity - Bar Chart**: London’s rain is generally light, which differs from the intense rain often depicted in movies.

Detailed visualisations for these findings are available in the Jupyter Notebook named 'NB01 - Simple Data Analysis.ipynb'.


## Conclusion

The analysis shows that London experiences frequent rain, with rainfall on 62.4% of the days in 2023. While London’s rain is generally lighter and less intense compared to tropical cities, its consistent, moderate rainfall supports its reputation as a rainy city. 

Overall, we conclude that London’s rainy image is justified based on the **frequency and consistency** of rainfall, though it is not as **heavy** as often depicted in movies.


## Further Exploration

Future analysis could explore additional weather metrics, like temperature and humidity, for a fuller picture of London's climate. Another option is to compare seasonal rainfall patterns or examine trends in rain intensity over the years to see if London's rainy reputation is changing.





