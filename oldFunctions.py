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

def getClosest(lat, lon):
    """gets euclidean difference between an input's lat & lon and
    all businesses. returns list of distances and list of businesses
    as dictionaries"""
    with open("yelp_academic_dataset_business.json") as json_data:
        shortestDistance = [float("inf")] * 10
        closestBusinesses = [None] * 10
        for line in json_data:          #for each business
            data = json.loads(line)     #make it into a dictionary
            latitude = float(data['latitude'])  #get lat
            longitude = float(data['longitude'])    #get long
            distance = math.sqrt(math.pow((latitude - lat),2) + math.pow((longitude - lon),2))
            m = max(shortestDistance)   #max in list
            i = shortestDistance.index(m)   #index of the max
            if m > distance:
                shortestDistance.remove(m)  #remove the bigger distance
                closestBusinesses.pop(i)      #remove the corresponding business
                shortestDistance.append(distance)   #add new distance
                closestBusinesses.append(data)  #add corresponding business
            else:
                pass
            distance = 0
#        print(shortestDistance)
#        pprint (closestBusinesses)
        return closestBusinesses

#example case to return the list of shortest distances
#closest = getClosest(33.499313000000001, -111.98375799999999)
#should return list of closest distances and list of closest business JSON objects as dictionaries

def computeComplex(closestBusinesses, inputCategories):
    """ computing the complex figure for representing number of shared categories """
    tot1 = len(inputCategories)
    sharedCats = [] 
    ret = []    #list of businesses we'll finally return
    for item in closestBusinesses:
        allCats = item["categories"]
        tot2 = len(allCats)
        for cat in allCats:
            if cat in inputCategories and cat not in sharedCats:
                sharedCats.append(item)
            else:
                pass
        sim = len(sharedCats)
        if sim >= 1:
            final = float(1 - (sim/(tot1+tot2)))
            print(final)
            ret.append(item)
            sharedCats = []
#    for x in ret:
#        print(x["name"])
    return ret
