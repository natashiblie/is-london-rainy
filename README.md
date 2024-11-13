[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/16Ytx_fz)

# Is London Really as Rainy as the Movies Make It Out to Be? 🤔 


<img src="./data/londonrain.jpg" alt="Is London Really as Rainy as the Movies Make It Out to Be?" width="1000"/>

This project investigates London's rainy reputation by analysing rainfall metrics across major cities. Using data visualisation and statistical metrics, we explore whether London's weather aligns with its portrayal in popular culture. By analysing metrics such as the number of rainy days, monthly total rainfall, and average rain intensity, we gain insights into the reality of London's weather.

## Contents

- [Project Structure](#project-structure)
- [How to Set Up and Run the Project](#how-to-set-up-and-run-the-project)
- [Methodology](#methodology)
  - [Data Source](#data-source)
  - [Data Collection Strategy](#data-collection-strategy)
  - [Cities Selected for Comparison](#cities-selected-for-comparison)
  - [Data Collection Scope](#data-collection-scope)
- [Metrics] (#metrics)
- [Conclusion](#conclusion)
- [Further Exploration](#further-exploration)


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

## How to Set Up and Run the Project

Follow these steps to set up and run the project, from installation to data analysis and visualisation.

1. **Clone the Repository in Terminal**  
   ```bash
   git clone git@github.com:lse-ds105/ds105a-2024-w06-summative-natashiblie.git 
   ```

2. **Install Python and Dependencies**  
- Check if Python is installed in terminal by running the following code:
   ```bash
   python --version
   ```  
   If Python is installed, the terminal should show a version number like Python 3.x.x. If it’s not installed, you’ll need to install Python by searching online for installation instructions.

- Then, navigate to the project directory and install the required packages in  terminal by typing: 
   ```bash 
   pip install -r requirements.txt
   ```

3. **Data Collection with Scripts in Terminal**  
   To collect rainfall data for a city and date range, run:
   ```bash
   python scripts/data_collection_script.py <country_code> <city_name> --start_date <start_date> --end_date <end_date> --output_file <output_file>
   ```

   Replace placeholders:
- `<country_code>`: e.g., "GB" for the UK
- `<city_name>`: e.g., "London"
- `<start_date>` & `<end_date>`: Dates in `YYYY-MM-DD` format (default `2023-01-01` to `2023-12-31`)
- `<output_file>`: Output path (default `../data/multicity_historical.json`; use format `data/xx_2023.json` for clarity)

4. **Run Jupyter Notebooks for Visualisations & Results**  
   Open `NB01 - Simple Data Analysis.ipynb` in Nuvolos and click Run to visualise and analyse data. Metrics like rainy days, monthly rainfall, and average rain intensity provide insights into London's rain patterns compared to other cities.



## Methodology

### Data Source
The data used in this analysis was sourced from the [Open-Meteo Historical Weather API](https://open-meteo.com/en/docs/historical-weather-api), which provides weather-related metrics for various global cities, including London, Cairo, Singapore, and more.

### Data Collection Strategy
In this project, we used the **Historical Weather Data** endpoint from the Open-Meteo API:

| Endpoint         | URL starts with                                      |
|------------------|------------------------------------------------------|
| [Historical Weather Data](https://open-meteo.com/en/docs/historical-weather-api) | `https://archive-api.open-meteo.com/v1/archive` |

The objective is to assess the raininess of **London, UK** relative to other cities with varied climates. We collected historical precipitation data for the entire year of 2023 to enable a detailed comparison of annual rain patterns.

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

## Metrics
This analysis evaluates London’s reputation as a rainy city by comparing key rainfall metrics with those of other cities. Here’s how raininess is defined:

- **Number of Rainy Days**: Measures the frequency of rain in London compared to other cities.
- **Monthly Total Rainfall**: Shows the volume of rain London receives over time.
- **Average Rain Intensity**: Indicates if London’s rain is typically light or heavy.

## Conclusion

The analysis shows that London experiences frequent rain, with rainfall on 62.4% of the days in 2023. While London’s rain is generally lighter and less intense compared to tropical cities, its consistent, moderate rainfall supports its reputation as a rainy city. 

Overall, we conclude that London’s rainy image is justified based on the **frequency and consistency** of rainfall, though it is not as **heavy** as often depicted in movies.


## Further Exploration

Future analysis could explore additional weather metrics, like temperature and humidity, for a fuller picture of London's climate. Another option is to compare seasonal rainfall patterns or examine trends in rain intensity over the years to see if London's rainy reputation is changing.





