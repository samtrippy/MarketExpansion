Download yelp dataset at:
http://www.yelp.com/dataset_challenge
** FILE USED IS "yelp_academic_dataset_business.json" **
Place in directory to run python code


**********************

Code optimized for Python 2.7


**********************

NN.py file contains:

NearestNeighbor function:
"""takes proportion of busiensses you should look at (e.g. .9 for 10%
    cross-validation)takes the latitude, longitude, and categories
    for a proposed business as well as a value
    k to generate a k-Nearest Neighbot classifier, identifying the most similar existing
    businesses and using their info to predict the success of a future venture""
inputs: proposed latitude, proposed longitude, proposed categories, k value, proportion for cross-validation
prints/returns expected star value

getTestData function:
    """takes proportion for cross-validation and returns the last prop of data to test it"""

validation function:
"""takes proportion of last 10% of businesses and runs a k-NN on first
    90% of businesses"""
inputs: businesses from getTestData and k value
prints/returns the average difference from the real businesses


**********************

ZeroR.py file contains:

zeroR function:
"""computes avg of all star ratings"""
prints/returns average

variance function:
""" finds the variance """


**********************

data.csv file contains:
longitude, latitude, and stars data for businesses


writeToCSV.py file contains:
function to write this data.csv file

**********************

IGNORE: oldFunctions.py, data.arff

**********************