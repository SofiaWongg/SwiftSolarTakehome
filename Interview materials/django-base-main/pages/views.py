from django.shortcuts import render
import pandas as pd
from .wiki_api import WikiAPI
from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import redirect

class wikiPages:
    #list of Wikipedia pages to look at
    SOLAR_CELL = "Solar cell"
    SEMICONDUCTOR = "Semiconductor"
    PEROVSKITE_SOLAR_CELL = "Perovskite solar cell"

def home(request):
    return redirect('frequency_plots')

def random_number(request):
    return render(request, 'pages/random_number.html')

def process_form(request):   
    #Called whenever Update Plots button is pressed
    if request.method == 'POST':

        #getting values from form
        my_input_value = request.POST.get('my_input')
        unit = request.POST.get('unit')

        #stores touple response(revisionsPerMonth, dateList)
        response = create_dictionary(int(my_input_value), unit)
        revisions_by_month = response[0]
        dates_list = response[1]

        dates_list = [date.strftime('%Y-%m-%d') for date in dates_list]
        
        # Convert the dictionary to a dataframe
        revisions_df = pd.DataFrame(revisions_by_month)
        
        # Passing relevant information for creating plots through context
        context = {"revisions_df": revisions_df, "revisions_by_month": revisions_by_month, "interval": int(my_input_value), "unit": unit, "dates_list": dates_list}

        return render(request, 'pages/frequency_plots.html', context)
    else:
        return HttpResponse('Form submission method not allowed.')


def load_solar_events(file_path):
    # Function to read CSV file into a dataframe
    df = pd.read_csv(file_path)
    return df

#initial function that is called to create plots 
def frequency_plots(request, interval = 20, unit = 'months'):

    #stores touple response(revPerMon, dateList)
    response = create_dictionary(interval)
    revisions_by_month = response[0]
    dates_list = response[1]
    
    # Convert the dictionary to a dataframe
    revisions_df = pd.DataFrame(revisions_by_month)

    dates_list = [date.strftime('%Y-%m-%d') for date in dates_list]

    # Passing relevant information for creating plots through context
    context = {"revisions_df": revisions_df, "revisions_by_month": revisions_by_month, "interval": interval, "unit": unit, "dates_list": dates_list}

    return render(request, 'pages/frequency_plots.html', context)


def create_dictionary(interval = 20, unit = 'months'):
    # Retrieves the number of revisions for a Wikipedia event within a specified time interval.
    halfInt = int(interval/2)
    titles_to_check = [
        wikiPages.SOLAR_CELL,
        wikiPages.SEMICONDUCTOR,
        wikiPages.PEROVSKITE_SOLAR_CELL
    ]

    dates_list = [] #[event_date]

    file_path = "/Users/sofiawong/Downloads/Interview materials/events_data.csv"
    solar_events_df = load_solar_events(file_path)
    event_titles = solar_events_df["Event name"].unique().tolist()

    # Initialize a dictionary with event names mapped to arrays of revisions
    revisions_by_month = {title: [] for title in event_titles}
    
    # Convert the "Event date" column to datetime format
    solar_events_df['Event date'] = pd.to_datetime(solar_events_df['Event date'])
    
    # Determine the offset based on the unit
    if unit == 'days':
        offset = pd.DateOffset(days=halfInt)
    elif unit == 'weeks':
        offset = pd.DateOffset(weeks=halfInt)
    elif unit == 'months':
        offset = pd.DateOffset(months=halfInt)
    else:
        raise ValueError("Invalid unit value")
    
    # Iterate over each event
    for _, row in solar_events_df.iterrows():
        title = row["Event name"]
        date_of_event = row["Event date"]

        #adds each date of events to date list
        dates_list.append(date_of_event)

        # Calculate the start and end dates based on the unit and offset
        start_date = date_of_event - offset
        end_date = date_of_event + offset

        wiki_api = WikiAPI()

        for wikiPage in titles_to_check:
            
            # Fetch revisions for each event
            revisions = wiki_api.get_num_revisions(wikiPage, start_date, end_date, unit)

            #if first runthrough -> set them to now array / otherwise add to existing array
            if revisions_by_month[title] == []: 
                for i in range(0, len(revisions)):
                    revisions_by_month[title] = revisions
            else:
                for i in range(0, len(revisions)):
                    revisions_by_month[title][i] += revisions[i]

    return (revisions_by_month, dates_list)
