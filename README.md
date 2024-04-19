
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
-  :sunny: Retrieve revision data from API for particular time range
-  :sunny: Sort data by event
-  :sunny: Create a chart with given data
-  :sunny: Good documentation

**Wants:**
-  :sunny: Adjustable event input (CSV)
-  :cloud: Basic testing
- Data saving capability for future reference
- Improved user interface

I started this project by retrieving the correct data from the API. After getting the correct data, I decided on how I wanted to hold that data and settled on a dictionary to easily add to the arrays and reference them by event name. After storing my information from the API in a dictionary, I used it to generate plots for each event. Once plots were generated with hard-coded values, I created spaces for user inputs and created a method call that allowed me to re-generate plots with user-specified values. Once I completed these tasks, I worked on smaller features to help a user visually understand the plots - this includes features like the text when a user hovers over the points or descriptions of the user's current query at the top. 

Although this was a small project, I focused on making the functionalities scalable, for example, reading in the CSV rather than hard coding events or going through each wiki page in a for loop. I also focused on separating code in a way that would be useful for a larger project—for example, separating the API call into a separate function and creating smaller functions that could be reused for different tasks.

## Solution

<img width="691" alt="Screenshot 2024-04-19 at 11 17 41 AM" src="https://github.com/SofiaWongg/SwiftSolarTakehome/assets/69434698/c625a1a5-e8f1-4c5e-93b4-adddeb682b0f">

**load_solar_events:** This function reads data from a CSV file containing information about solar energy events. It uses Pandas to load the CSV file into a DataFrame and returns the DataFrame.

**create_dictionary** This function calls get_num_revisions from wiki_api.py for each event and stores information in a dictionary with event names mapped to arrays of revisions. Returns this dictionary along with an array of event dates. 

**get_num_revisions:** This function makes GET requests to the Wikipedia API to retrieve revision data for a specified event within a given time interval. It iterates over each month within the interval, making API requests to fetch revision data. The number of revisions for each month is stored in a list (revisions_array), which is returned after all months have been processed.

**process_form** This function is called whenever a user presses "Generate Plots" and uses user input to generate new plots. Renders the HTML file: frequency_plots.html.

**frequency_plots** This is the function called to generate plots on initial load. Similar to process_form, but uses default values '20' and 'months' to generate plots. Renders the HTML file: frequency_plots.html.

## Resources Used

**Pandas:** A Python library used for data manipulation and analysis, particularly for loading data from CSV files.
**Plotly:** A Python graphing library used for creating interactive plots and visualizations.
**Requests:** A Python HTTP library used for making HTTP requests to the Wikipedia API.
**Wikipedia API:** The API used to retrieve revision data for Wikipedia pages related to solar energy events.
**NumPy:** A Python library used for numerical computing, though it's not explicitly used in this project.
**datetime:** A Python module used for manipulating dates and times.
**CSV file:** A local file containing data about solar energy events, accessed using Python's built-in file reading capabilities.


## Future Considerations

- Data saving capability for future reference
- Improved user interface (loading signs, )
- Ability to choose event to plot
- Ability to add or remove wiki-pages
- More flexible time range options
