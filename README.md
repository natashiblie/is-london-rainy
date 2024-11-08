[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/16Ytx_fz)

![London's Rainy Weather](./data/londonrain.jpg)

# Is London Really as Rainy as the Movies Make It Out to Be? 🤔

This project investigates London's rainy reputation by analysing rainfall metrics across major cities. Using data visualisation and statistical metrics, we explore whether London's weather aligns with its portrayal in popular culture.

## Description

This analysis examines rainfall data for London and other major cities to determine if London is truly as rainy as often depicted in movies. By analysing metrics such as the number of rainy days, monthly total rainfall, and average rain intensity, we gain insights into the reality of London's weather.

## Installation

To run this project, ensure you have Python installed. Install the necessary packages with:

```bash
pip install -r requirements.txt

```
## Project Structure and How to Run

The repository is organised as follows:

```
DS105A-2024-W06-SUMMATIVE-NATASHIBLIE/
├── code/                            # Folder containing Jupyter Notebooks for data collection and analysis
│   ├── NB01 - Data Collection.ipynb       # Notebook for collecting and processing rainfall data
│   └── NB02 - Simple Data Analysis.ipynb       # Notebook for analysing and visualising rainfall data
│
├── data/                            # Folder containing data files used in the analysis
│   ├── londonrain.jpg               # Image file, potentially used for visualisation or README
│   ├── multicity_historical.json    # JSON file containing historical rainfall data across multiple cities
│   └── world_cities.csv             # CSV file with metadata or coordinates of cities involved in the study
│
├── README.md                        # Documentation file explaining the project, setup, and usage
├── requirements.txt                 # List of dependencies needed to run the project
```

To run the project, open `code/NB01 - Data Collection.ipynb` in Jupyter Notebook to collect and process rainfall data, then proceed to `code/NB02 - Simple Data Analysis.ipynb` for data analysis and visualisation. The notebooks are structured to guide you through data loading, processing, visualisation, and conclusions step-by-step.

## Methodology

### Data Source
The data used in this analysis was sourced from the [Open-Meteo Historical Weather API](https://open-meteo.com/en/docs/historical-weather-api), which provides monthly rainfall metrics for various global cities, including London, Cairo, Singapore, and more.

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

#### Data Collection Scope
For each city, the following data was retrieved for 2023:
- **Daily Precipitation** (`precipitation_sum`) to measure total rainfall.
- **Precipitation Hours** (`precipitation_hours`) to capture the duration of rainfall each day.

## Metrics and Results

### Metrics Analysed
This analysis uses key rainfall metrics to evaluate London’s reputation as a rainy city and compare it with other cities:

- **Number of Rainy Days**: Evaluates the frequency of rainy days in London versus other cities.
- **Monthly Total Rainfall**: Assesses the volume of rain London receives over time.
- **Average Rain Intensity**: Gauges whether London’s rain tends to be light or heavy.

These metrics provide a balanced view of the frequency, intensity and volume of rainfall, helping to understand London's weather patterns accurately.

### Results & Visualisations
Each metric is visualised to highlight London’s rain characteristics:

- **Figure 1: Number of Rainy Days - Bar Chart**: London has frequent, light rain, contributing to its "rainy" reputation without significant downpours.
- **Figure 2: Monthly Total Rainfall - Line Graph**: London experiences a steady rainfall trend throughout the year, showing a consistent but moderate volume of rain.
- **Figure 3: Average Rain Intensity - Bar Chart**: London’s rain is generally light, which differs from the intense rain often depicted in movies.

Detailed visualisations for these findings are available in the Jupyter Notebook named 'NB02 - Simple Data Analysis.ipynb'.


## Conclusion

This analysis shows that while London does experience frequent rainy days, the rain tends to be light and less intense than often depicted in movies. London's "rainy" image is more due to the frequency of rain rather than its intensity or total volume.

## Further Exploration

Future analysis could explore additional weather metrics, like temperature and humidity, for a fuller picture of London's climate. Another option is to compare seasonal rainfall patterns or examine trends in rain intensity over the years to see if London's rainy reputation is changing.





