## Surfs Up!

## Background

climate_analysis takes two csv files as a data source 
- hawaii_stations.csv
- hawaii_measurements.csv
cleans the data where there is any null value, and use the clensed data to plot

1) precipitation analysis

precipitation during last year.

![bar.png](https://github.com/EmilySakata/climate_analysis/blob/master/img/percipitation.png)

2) station analysis

![histogram.png](https://github.com/EmilySakata/climate_analysis/blob/master/img/histogram.png)

3) temperature analysis

![bar.png](https://github.com/EmilySakata/climate_analysis/blob/master/img/bar.png)


then design a Flask api based on the query to share the analysis in JSON format. 

users can run the app.py file to create a server to run the API.


## technology used

- Python
- Sqlalchemy
- Flask
- Sqlite database
- csv

