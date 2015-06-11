#Samantha Trippy - Northwestern University

import json, math
import Queue
from pprint import pprint

def NearestNeighbor(iLat, iLon, iCats, kNN, prop):
    """takes proportion of busiensses you should look at (e.g. .9 for 10%
    cross-validation)takes the latitude, longitude, and categories
    for a proposed business as well as a value
    k to generate a k-Nearest Neighbot classifier, identifying the most similar existing
    businesses and using their info to predict the success of a future venture"""
    with open("yelp_academic_dataset_business.json") as json_data:
        nearest = [float("inf")] * kNN
        closestBusinesses = [None] * kNN
        sharedCats = []
        ret = []    #list of businesses we'll finally return
        counter = 0
        stop = math.ceil(61184 * float(1-prop))
        for line in json_data:          #for each business
            counter = counter + 1
            if counter < stop:
                data = json.loads(line)     #make it into a dictionary
                latitude = float(data['latitude'])  #get lat
                longitude = float(data['longitude'])    #get long
                distance = math.sqrt(math.pow((latitude - iLat),2) + math.pow((longitude - iLon),2))
                allCats = data["categories"]    #a business' categoires
                for cat in allCats:
                    if cat in iCats and cat not in sharedCats:
                        sharedCats.append(data) #append shared ones
                    else:
                        pass
                sim = len(sharedCats)   # num. similar
                #need to keep smallest distance and businesses separate
                m = max(nearest)
                i = nearest.index(m)
                if sim >= 1:
                    result = 150*float(1 - (sim/float(((len(iCats))+(len(allCats))))))
                    final = distance + result
                    if final < m:       #if it's better than any in the list
                        nearest.remove(m)
                        nearest.append(final)
                        closestBusinesses.pop(i)
                        closestBusinesses.append(data)
                    else:
                        pass
                sharedCats = []
                distance = 0
                result = 0
#        pprint(closestBusinesses) #pretty prints the businesses as dictionaries
        totStars = float(0)
        for bus in closestBusinesses:
            totStars += bus["stars"]
        expectedStars = totStars/float(kNN) #calculate avg num of stars of k-Nearest Neighbors
        return expectedStars

def getTestData(prop):
    """takes proportion and returns the last prop of data to test it"""
    with open("yelp_academic_dataset_business.json") as json_data:
        counter = 0
        businesses = []
        start = 61184 * float(1-prop)
        for line in json_data:          #for each business
            counter = counter + 1
            data = json.loads(line)     #make it into a dictionary
            if counter >= start:
                businesses.append(data)
#        pprint(businesses)
        return businesses
            
g = getTestData(.0003)

def validation(businesses, knn):
    """takes proportion of last 10% of businesses and runs a k-NN on first
    90% of businesses"""
    stars = []
    avg = 0
    for bus in businesses:
        lat = float(bus['latitude'])
        lon = float(bus['longitude'])
        cat = bus['categories']
        n = NearestNeighbor(lat, lon, cat, knn, 0.0003)
        dif = math.fabs(bus['stars'] - n)
        stars.append(dif)
    avg = sum(stars) / len(stars)
    print(avg)
        
        
validation(g, 5)

#test for food in AZ
#NearestNeighbor(33.499313000000001, -111.98375799999999,["Food"], 10, 0.9)

#test for Restaurants in Las Vegas
#NearestNeighbor(36.095424000000001, -115.175922, ["Restaurants"], 5, 0.9)
