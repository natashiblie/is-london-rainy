[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/16Ytx_fz)

## Time Period: 2024
## Cities:
```
London, UK (main city)
Seattle, USA (similar climate to London)
Cairo, Egypt (very dry)
New York, USA (moderate rainfall)
Singapore (tropical, high rainfall)
```

## Raininess
1. Total Rainfall - Aggregate the total precipitation for each city over the chosen time period (2024)
$$\text{Total Rainfall} = \sum (\text{daily precipitation values over the year})$$
Why --> This provides an overall measure of how much rain a city received during the period.

2. Rain Frequency (Number of Rainy Days) - My definition of a rainy day is any day with a measurable precipitation, precipitation_sum > 0.
$$\text{Number of Rainy Days} = \text{count of days where } \text{precipitation\_sum} > 0$$
Why --> This provides insight into how frequently it rains in each city.


3. Rain Intensity - I will calculate average rainfall per rainy day by using the formula (Total Rainfall / Number of Rainy Days).
**Intensity**:
$$\text{Intensity} = \frac{\text{Total Rainfall}}{\text{Number of Rainy Days}}$$
Why --> This measures the intensity of rain on rainy days, which helps differentiate cities with frequent light rain from those with occasional heavy rain.

## Raininess Index
To make the comparison between the countries even stronger, I will create a raininess index. This index combines rain frequency & rain intensity into a single metric to quantify the overall "raininess" of each city.
