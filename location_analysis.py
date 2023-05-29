import json
from geopy.geocoders import Nominatim
import os
import csv

def locationData(geolocator, segment):
    results = []
    if 'latitudeE7' in segment['location'] and 'longitudeE7' in segment['location']:
        location = geolocator.reverse(
                            [
                                segment['location']['latitudeE7'] / 1e7, 
                                segment['location']['longitudeE7'] / 1e7
                            ],
                            exactly_one=True
                        )
        address = location.address
    elif 'address' in segment['location']:
        address = (segment['location']['address'])
    else:
        address = 'unknown'

    if address.find("United Kingdom") != -1 or address.find("London") != -1 :
        results.append({'address': address, 'time': segment['duration']['startTimestamp'], 'isUK': True})
    else:
        results.append({'address': address, 'time': segment['duration']['startTimestamp'], 'isUK': False})

    return results    

def createCSVFile(results):
    print(results)
    print('Going to create CSV')
            # Define the output CSV file
    csv_file = 'output.csv'
            
            # Define the fieldnames for the CSV
    fieldnames = ['address', 'time', 'isUK']

            # Write data to CSV file
    if os.path.exists('/Users/filipkonkowski/Downloads/Takeout/Location_History/Semantic_Location_History/output.csv'):
        with open(csv_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(results)
        print("CSV file created successfully.")   
    else:    
        with open(csv_file, 'a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(results)
        print("JSON data appended to the CSV file successfully.")


months = ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 'JULY', 'AUGUST',
            'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER']


years = [2016, 2017, 2018, 2019, 2020,2021, 2022, 2023]

full_year=[]
geolocator = Nominatim(user_agent="geoapiExercises")

for year in years: 
    for month in months:
        print(f"start for Year: {year}, {month}")
        file_path = f'/Users/filipkonkowski/Downloads/Takeout/Location_History/Semantic_Location_History/{year}/{year}_{month}.json'

        if os.path.exists(file_path):
            f = open(file_path)
            data=json.load(f)

            # Parse the JSON data
            timelineObjects = data['timelineObjects']
            results = []
            # Loop through each object in the timeline
            for obj in timelineObjects:
                if 'placeVisit' in obj:
                    current = []
                    segment = obj['placeVisit']

                    results = locationData(geolocator, segment)

            createCSVFile(results)   
  