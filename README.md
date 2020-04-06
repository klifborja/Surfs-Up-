# Surfs-Up!

![surfs-up.jpeg](Static/Images/surfs-up.png)

Looking to take that long-deserved trip to Hawaii but don’t want the weather to get in your way? Surfs Up is able to analyze past weather patterns to help you plan your vacation around inclement weather. This app is a climate analysis tool that gives you a look at the precipitation frequency, average rainfall, and average temperature by date and location. 

## Climate Analysis and Exploration
Hawaii Climate Database exploration with Python and SQLAlchemy. Analysis completed using SQLAlchemy ORM Queries, Pandas, and Matplotlib.

### Precipitation Analysis

* Designed a query to retrieve the last 12 months of precipitation data using only the `date` and `prcp` values. Loaded the query results into a Pandas DataFrame and set the index to the date column and sorted the DataFrame values by `date` and ploted the results using the DataFrame `plot` method.

![precipitation](Static/Images/precipitation.png)

### Station Analysis

* Designed a query to calculate the total number of stations and to find the most active stations. Listed the stations and observation counts in descending order. Discovered which station has the highest number of observations using functions such as `func.min`, `func.max`, `func.avg`, and `func.count` in the queries.

* Design a query to retrieve the last 12 months of temperature observation data (tobs). Filtered by the station with the highest number of observations and plotted the results as a histogram with `bins=12`.

    ![station-histogram](Static/Images/station-histogram.png)

## Climate App

Designed a Flask API based on the developed queries using FLASK to create the routes.

### Routes

* `/`

  * Home page.

  * List of all routes that are available.

* `/api/v1.0/precipitation`

  * Converted the query results to a Dictionary using `date` as the key and `prcp` as the value.
  * Returned the JSON representation of the dictionary.

* `/api/v1.0/stations`

  * Returned a JSON list of stations from the dataset.

* `/api/v1.0/tobs`
  * query for the dates and temperature observations from a year from the last data point.
  * Returned a JSON list of Temperature Observations (tobs) for the previous year.

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

  * Returned a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
  * Start only, calculates `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.
  * Start and the end date, calculates the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.
  * Joined the station and measurement tables for some of the analysis queries.
  * Useed Flask `jsonify` to convert the API data into a valid JSON response object.

### Temperature Analysis

* Used the `calc_temps` function to calculate the min, avg, and max temperatures for matching dates from the previous year (i.e., use "2017-01-01" if start date was "2018-01-01").
* Ploted the min, avg, and max temperature from your previous query as a bar chart.

  * Use the average temperature as the bar height.

  * Use the peak-to-peak (tmax-tmin) value as the y error bar (yerr).

    ![temperature](Images/temperature.png)

### Daily Rainfall Average.

* Calculated the rainfall per weather station using the previous year's matching dates.
* Calculated the daily normals. Normals are the averages for the min, avg, and max temperatures.
* Created a list of dates in the format `%m-%d`. Used the `daily_normals` function to calculate the normals for each date string and append the results to a list.
* Loaded the list of daily normals into a Pandas DataFrame and set the index equal to the date.
* Used Pandas to plot an area plot (`stacked=False`) for the daily normals.

  ![daily-normals](Static/Images/daily-normals.png)