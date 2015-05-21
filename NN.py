#Samantha Trippy - Northwestern University

import json, math
import Queue
from pprint import pprint

def NearestNeighbor(iLat, iLon, iCats):
    with open("yelp_academic_dataset_business.json") as json_data:
        shortestDistance = [float("inf")] * 10
        closestBusinesses = [None] * 10
        for line in json_data:          #for each business
            data = json.loads(line)     #make it into a dictionary
            latitude = float(data['latitude'])  #get lat
            longitude = float(data['longitude'])    #get long
            distance = math.sqrt(math.pow((latitude - iLat),2) + math.pow((longitude - iLon),2))
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
        sharedCats = [] 
        ret = []    #list of businesses we'll finally return
        for item in closestBusinesses:
            allCats = item["categories"]
            for cat in allCats:
                if cat in iCats and cat not in sharedCats:
                    sharedCats.append(item)
                else:
                    pass
            sim = len(sharedCats)
            if sim >= 1:
                final = float(1 - (sim/((len(iCats))+(len(allCats)))))
                print(final)
                ret.append(item)
                sharedCats = []
        for x in ret:
            print(x["name"])

NearestNeighbor(33.499313000000001, -111.98375799999999,["Food"])
