
## Table of Contents

1. [Run Instructions](#run-instructions)
2. [Approach](#approach)
3. [Solution](#solution)
4. [Resources Used](#resources-used)
5. [Future Considerations](#future-considerations)

## Summary

This web application allows users to visualize the rate of revisions on selected Wikipedia pages during a time interval related to an event in solar history. It initially plots data over a 21-month period, but users can customize the interval and time units and regenerate plots accordingly. Additional features include hover details on plot points that display specific date ranges.

<img width="1432" alt="Screenshot 2024-04-19 at 2 47 39 PM" src="https://github.com/SofiaWongg/SwiftSolarTakehome/assets/69434698/71159414-8050-4b99-805e-cab5581e14d8">


## Run Instructions

1. Clone the repository.
2. Navigate to the project directory.
3. Install the required dependencies:

  `pip install -r requirements.txt`

4. Run the Django server:

 `python manage.py runserver`

5. Open a web browser and go to http://localhost:8000 to access the application.
**Does take some time to load 

**For running tests (on mac):** <br>
In your terminal navigate to the folder where manage.py is located and run:

`python3 manage.py test`
## Approach

Given a limited timeframe for a large project I started by listing my essentials, and working on them in that order:

I separated features I wanted into scope and reach goals:

**Scope:**
-  :sunny: Retrieve revision data from API for particular time range
-  :sunny: Sort data by event
-  :sunny: Create a chart with given data
-  :sunny: Good documentation

**Reach Goals:**
-  :sunny: Adjustable event input (CSV)
-  :cloud: Basic testing
- Data saving capability for future reference
- Improved user interface

I started this project by retrieving the correct data from the API. After getting the correct data, I decided on how I wanted to hold that data and settled on a dictionary to easily add to the arrays and reference them by event name. After storing my information from the API in a dictionary, I used it to generate plots for each event. Once plots were generated with hard-coded values, I created spaces for user inputs and created a method call that allowed me to re-generate plots with user-specified values. Once I completed these tasks, I worked on smaller features to help a user visually understand the plots - this includes features like the text when a user hovers over the points or descriptions of the user's current query at the top. 

Although this was a small project, I focused on making the functionalities scalable, for example, reading in the CSV rather than hard coding events or going through each wiki page in a for loop. I also focused on separating code in a way that would be useful for a larger project—for example, separating the API call into a separate function and creating smaller functions that could be reused for different tasks.

## Solution

<img width="691" alt="Screenshot 2024-04-19 at 11 17 41 AM" src="https://github.com/SofiaWongg/SwiftSolarTakehome/assets/69434698/c625a1a5-e8f1-4c5e-93b4-adddeb682b0f">

**load_solar_events:** This function reads data from a CSV file containing information about solar energy events. It uses Pandas to load the CSV file into a DataFrame and returns the DataFrame.

**create_dictionary** This function calls get_num_revisions from wiki_api.py for each event and stores information in a dictionary with event names mapped to arrays of revisions.It returns this dictionary along with an array of event dates. 

**get_num_revisions:** This function makes GET requests to the Wikipedia API to retrieve revision data for a specified event within a given time interval. It iterates over each month within the interval, making API requests to fetch revision data. The number of revisions for each month is stored in a list (revisions_array), which is returned after all months have been processed.

**process_form** This function is called whenever a user presses "Generate Plots" and uses user input to generate new plots. Renders the HTML file: frequency_plots.html.

**frequency_plots** This is the function called to generate plots on initial load. Similar to process_form, but uses default values '20' and 'months' to generate plots. Renders the HTML file: frequency_plots.html.


## Future Considerations

Here are some features I would have liked to include in this project, given extra time:

- **Testing & Error Handling** - There is a lot that could be added to testing. Currently, only the API call and CSV reader are tested, but there should be multiple tests for each function. There are also better ways to test API's and endpoints outside of the unit testing django.test functionality.
  
- **Data saving capability for future reference (Django Caching)** - One of the most significant downsides to this tool is the loading time. Since data generally remains the same from query to query, having a data-saving capability could be incredibly useful. It would also allow me to hold larger amounts of data since I would not need to load data every time, and it could lead to more detailed and effective plots. 

- **Improved user interface** - The plots currently have most of the basic information a user could need, but there is a lot that could be added to help users understand the graph, such as more dates, averages, or comparisons. There are also some features that would help usability, such as font size, loading signs, or descriptive error messages. 

- **More flexible selections** - Currently, users have limited choices regarding what they can see and how they can adjust their query. Some flexibility I imagine adding is the ability to select events to plot, the ability to add or remove wiki pages, and more flexible time range options. These changes would help provide more effective graphs for users and potentially help loading times since users could only load data they need to see. 



