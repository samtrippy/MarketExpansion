import json, math
import csv

def zeroR():
    """computes avg of all star ratings"""
    with open("yelp_academic_dataset_business.json") as json_data:
        counter = 0
        sum = float(0)
        avg = float(0)
        for line in json_data:
            counter = counter + 1
            data = json.loads(line)     #make it into a dictionary
            stars = float(data['stars'])
            sum = sum + stars
        avg = sum/float(counter)
        print(avg)
        return avg

#zeroR()

#the average is equal to 3.67330511245

def variance():
    """ finds the variance """
    with open("yelp_academic_dataset_business.json") as json_data:
        counter = 0
        mean = 3.67330511245
        VarX = float(0)
        allVars = float(0)
        variance = float(0)
        for line in json_data:
            counter = counter + 1
            data = json.loads(line)     #make it into a dictionary
            stars = float(data['stars'])
            VarX = math.pow((mean - stars), 2)
            allVars = allVars + VarX
        variance = allVars/float(counter)
        print(variance)
        return variance

variance()
