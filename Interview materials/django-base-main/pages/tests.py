from django.test import TestCase
from .views import *
import requests

class Functional(TestCase):
    def test_CSV_read(self):
        #checks to see if csv data is being properly read in - hard coded
        file_path = "/Users/sofiawong/Downloads/Interview materials/events_data.csv"
        csv_data = load_solar_events(file_path)

        self.assertIsNotNone(csv_data)

        first_event_name = csv_data.iloc[0]["Event name"]
        self.assertEqual(first_event_name, "First perovskite solar cell reported")

        last_tag = csv_data.iloc[-1]['Tags']
        self.assertEqual(last_tag, "policy, climate change")
 
    
    def test_api(self):
        #checks to ensure that api is functioning
        expected_data = {
            'batchcomplete': True,
            'query': {
                'pages': [
                    {
                        'pageid': 2352910,
                        'ns': 0,
                        'title': 'Solar cell',
                        'revisions': [
                            {'timestamp': '2016-07-17T19:35:49Z'},
                            {'timestamp': '2016-07-29T15:08:06Z'},
                            {'timestamp': '2016-08-02T14:43:54Z'}
                        ]
                    }
                ]
            },
            'limits': {'revisions': 500}
        }

        session = requests.Session()
        URL = "https://en.wikipedia.org/w/api.php"

        PARAMS = {
                "action": "query",
                "prop": "revisions",
                "titles": 'Solar cell',
                "rvprop": "timestamp",
                "rvlimit": "max",
                "rvslots": "main",
                "formatversion": "2",
                "format": "json",
                "rvstart" : '2016-07-17T19:35:49Z',
                "rvend": '2016-08-02T14:43:54Z',
                "rvdir":"newer",
            }
        
        response = session.get(url=URL, params=PARAMS)
        data = response.json()

        self.assertEqual(data, expected_data)


    



