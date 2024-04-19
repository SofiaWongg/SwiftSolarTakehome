
## Table of Contents

1. [Run Instructions](#run-instructions)
2. [Approach](#approach)
3. [Solution](#solution)
4. [Resources Used](#resources-used)
5. [Future Considerations](#future-considerations)

## Summary

A web app that allow us to plot the rate of revisions on chosen Wikipedia pages that relate to the data we have about solar events. The plots are initialized with the interval of 21 and time unit of months, but users are able to select their interval and unit and re-generate plots. When hovering over plots users can see the date range of a particular value, as well as the date of the event. 

## Run Instructions

1. Clone the repository.
2. Navigate to the project directory.
3. Install the required dependencies:

  `pip install -r requirements.txt`

4. Run the Django server:

 `python manage.py runserver`

5. Open a web browser and go to http://localhost:8000 to access the application.
**Does take some time to load 

**For running tests (on mac):**
In your terminal navigate to project directory and run:

`python3 manage.py test`
## Approach

Given a limited timeframe for a large project I started by listing my essentials, and working on them in that order:

I separated features I wanted into wants and needs:

**Needs:**
-   :sunny: Retrieve revision data from API for particular time range
-  :sunny: Sort data by event
-  :sunny: Create a chart with given data
-  :sunny: Good documentation

**Wants:**
-  :sunny: Adjustable event input (CSV)
-  :cloud: Basic testing
- Data saving capability for future reference
- Improved user interface

Although this was a small project I tried to focus on making the functionalities scalable, for example reading in the CSV rather than hard coding events or going through each wiki page in a for loop. I also foucused on separating code in a way that would be useful for a larger project. For example separating the network call into a separate function and creating smaller functions that could be reused for different tasks.
## Solution

<img width="691" alt="Screenshot 2024-04-19 at 11 17 41 AM" src="https://github.com/SofiaWongg/SwiftSolarTakehome/assets/69434698/c625a1a5-e8f1-4c5e-93b4-adddeb682b0f">

**Load Solar Events Function: **This function reads data from a CSV file containing information about solar energy events. It uses Pandas to load the CSV file into a DataFrame and returns the DataFrame.

**Frequency Plots Function: **This is the main function responsible for generating frequency plots of revisions for solar energy events. It first loads solar events data using the load_solar_events function. Then, it iterates over each event, calculating the start and end dates for a 20-month period relative to the event date. Within this period, it calls the get_num_revisions function to retrieve the number of revisions for each month. The revisions data is aggregated and stored in a dictionary (revisions_by_month). Finally, the dictionary is converted into a DataFrame (revisions_df) and passed as a context variable to render a template for displaying the frequency plots.

**Get Num Revisions Function:** This function makes GET requests to the Wikipedia API to retrieve revision data for a specified event within a given time interval. It iterates over each month within the interval, making API requests to fetch revision data. The number of revisions for each month is stored in a list (revisions_array), which is returned after all months have been processed.

## Resources Used

**Django: **The web framework used to build the application.
**Pandas:** A Python library used for data manipulation and analysis, particularly for loading data from CSV files.
**Plotly: **A Python graphing library used for creating interactive plots and visualizations.
**Requests:** A Python HTTP library used for making HTTP requests to the Wikipedia API.
**Wikipedia API:** The API used to retrieve revision data for Wikipedia pages related to solar energy events.
**NumPy: **A Python library used for numerical computing, though it's not explicitly used in this project.
**datetime:** A Python module used for manipulating dates and times.
**CSV file: **A local file containing data about solar energy events, accessed using Python's built-in file reading capabilities.


## Future Considerations

- Data saving capability for future reference
- Improved user interface (loading signs, )
- Ability to choose event to plot
- Ability to add or remove wiki-pages
- More flexible time range options
