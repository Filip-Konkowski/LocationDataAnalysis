# Location Data Analysis

This algorithm scrutinizes geolocation metadata harvested from Google Maps, abstracting particulars about designated locales, and supplements information if the said position was within the United Kingdom's territories. The purpose behind devising this algorithm was to determine instances wherein my presence was recorded beyond the boundaries of the United Kingdom. The necessity for this data compilation arose in the context of fulfilling the stipulations required for my UK naturalisation application. The objective was to ascertain and document the precise dates of my non-residential status within the UK. In order to realize this, I executed an export of pertinent data from Google Maps, following which, I activated the script within the confines of the /Takeout/Location History directory. The outcome of this algorithmic operation is a CSV file, ready for seamless integration with Google Sheets.

It takes JSON data as input and generates a CSV file with relevant information.

## Requirements
Python 3.x
geopy library
csv library
Usage
Install the required libraries by running the following command:

### Copy code
`pip install geopy`
Prepare your location data JSON file. Ensure it is in the correct format and contains the necessary data fields.

Update the script with the appropriate file paths:

Modify the file_path variable in the script to point to your location data JSON file.
Set the desired output CSV file name in the csv_file variable.
Run the script:

### Copy code
`python location_analysis.py`
The script will process the JSON data, analyze the locations, and create a CSV file with the extracted information.

Script Details
The script uses the Nominatim geocoder from the geopy library to perform reverse geocoding and retrieve the address information.
It checks if the address contains keywords such as "United Kingdom" or "London" to determine if the location is in the UK.
The extracted information, including the address, timestamp, and whether it's in the UK, is stored in a CSV file.
If the output CSV file already exists, the script will append the data to it. Otherwise, it will create a new CSV file.
License
This script is licensed under the MIT License.
