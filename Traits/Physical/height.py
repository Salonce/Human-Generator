from numpy import random

def getHeight(gender):
    if gender == "male":
        return random.normal(loc = 178, scale = 6, size=(1))
    if gender == "female":
        return random.normal(loc=165, scale=6, size=(1))