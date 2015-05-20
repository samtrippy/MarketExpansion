#Samantha Trippy - Northwestern University

import json, math
import Queue
from pprint import pprint

def printOneBusiness():
    """prints the JSON object for the first business"""
    data = []
    with open("yelp_academic_dataset_business.json") as json_data:
        for line in json_data:      #each "line" in the json_data is 1 business object
            data.append(json.loads(line))       #load the data into a python dictionary and append it
            pprint(data)            #pretty print this first dictionary
            break

#printOne()

def printCategories():
    """prints the 'categories' attribute of the first business/JSON object"""
    with open("yelp_academic_dataset_business.json") as json_data:
        for line in json_data:
            data = json.loads(line)     #load the data into a python dictionary
            pprint(data['categories'])  #as a dictionary, you can index the value by business attributes
            break

#printCategories()

def getDistance(lat, lon):
    """gets euclidean difference between an input's lat & lon and
    the first business JSON object"""
    with open("yelp_academic_dataset_business.json") as json_data:
        shortestDistance = [float("inf")] * 10
        for line in json_data:          #for each business
            data = json.loads(line)     #make it into a dictionary
            latitude = float(data['latitude'])
            longitude = float(data['longitude'])
            distance = math.sqrt(math.pow((latitude - lat),2) + math.pow((longitude - lon),2))
            m = max(shortestDistance)
            if m > distance:
                shortestDistance.remove(m)
                shortestDistance.append(distance)
            else:
                pass
            distance = 0
        print(shortestDistance)
            

#example case should return a difference of 100
getDistance(133.499313000000001, -111.98375799999999)
