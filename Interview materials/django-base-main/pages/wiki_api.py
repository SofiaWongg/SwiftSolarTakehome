import requests
import pandas as pd

class WikiAPI:
    def __init__(self):
        self.session = requests.Session()
        self.URL = "https://en.wikipedia.org/w/api.php"

    # Make a GET request to the Wikipedia API to retrieve revisions for the specified event
    def get_num_revisions(self, wiki_title, start_date, end_date, unit):
        
        #holds number of revisions
        revisions_array = []

        # Calculate the end date for the current interval - Determine the offset based on the unit
        if unit == 'days':
            offset = pd.DateOffset(days=1)
        elif unit == 'weeks':
            offset = pd.DateOffset(weeks=1)
        elif unit == 'months':
            offset = pd.DateOffset(months=1)
        else:
            raise ValueError("Invalid unit value")

        current_date = start_date

        while current_date <= end_date:
           
            interval_end_date = current_date + offset

            PARAMS = {
                "action": "query",
                "prop": "revisions",
                "titles": wiki_title,
                "rvprop": "timestamp",
                "rvlimit": "max",
                "rvslots": "main",
                "formatversion": "2",
                "format": "json",
                "rvstart" :current_date.strftime('%Y-%m-%dT%H:%M:%SZ'),
                "rvend": interval_end_date.strftime('%Y-%m-%dT%H:%M:%SZ'),
                "rvdir":"newer",
            }

            response = self.session.get(url=self.URL, params=PARAMS)
            data = response.json()
            
            # Extract the number of revisions
            pages = data.get("query", {}).get("pages", [])
            num_revisions = sum(len(page.get("revisions", [])) for page in pages)
            revisions_array.append(num_revisions)

            # Move to the next interval (increment current_date by one unit)
            current_date += offset

        return revisions_array