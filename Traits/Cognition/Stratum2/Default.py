from numpy import random

def getDefault():
    return random.normal(loc=100, scale=15, size=(1))

def getAdjusted(general_intelligence):
    return random.normal(loc=general_intelligence, scale=6, size=(1))
