import json, math
import Queue
import csv
from pprint import pprint

c = csv.writer(open("data.csv", "wb"))

def writer():
    """converts the json file to a csv file with relevant attributes for
    all businesses"""
    with open("yelp_academic_dataset_business.json") as json_data:
        counter = 0
        for line in json_data:
            counter = counter + 1
            data = json.loads(line)     #make it into a dictionary
            latitude = float(data['latitude'])  #get lat
            longitude = float(data['longitude'])
            stars = float(data['stars'])
            cats = data['categories']
            c.writerow([latitude, longitude, cats, stars])
        print(counter)

writer()
