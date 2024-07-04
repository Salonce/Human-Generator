from numpy import random

def getDefault():
    return random.normal(loc=50, scale=20, size=(1))

def getAdjusted(general):
    return random.normal(loc=general, scale=10, size=(1))