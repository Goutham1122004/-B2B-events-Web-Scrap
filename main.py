import requests
from bs4 import BeautifulSoup
import csv
import json

events = [
    {
        'name': 'Event 1 Name',
        'url': 'https://www.event1.com',
    },
    {
        'name': 'Event 2 Name',
        'url': 'https://www.event2.com',
    },
    {
        'name': 'Event 3 Name',
        'url': 'https://www.event3.com',
    },
    {
        'name': 'Event 4 Name',
        'url': 'https://www.event4.com',
    },
    {
        'name': 'Event 5 Name',
        'url': 'https://www.event5.com',
    }
]

def scrape_event_data(event):
    url = event['url']
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    event_data = {
        'Event Name': event['name'],
        'Website URL': url,
        'Event Date(s)': '',  
        'Location': '', 
        'Description': '', 
        'Key Speakers': '',  
        'Agenda/Schedule': '',  
        'Registration Details': '', 
        'Pricing': '',  
        'Categories': '',  
        'Audience type': ''  
    }

    return event_data

scraped_data = []
for event in events:
    event_data = scrape_event_data(event)
    scraped_data.append(event_data)

keys = scraped_data[0].keys()
with open('b2b_events_data.csv', 'w', newline='', encoding='utf-8') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(scraped_data)


with open('b2b_events_data.json', 'w', encoding='utf-8') as json_output_file:
    json.dump(scraped_data, json_output_file, ensure_ascii=False, indent=4)

