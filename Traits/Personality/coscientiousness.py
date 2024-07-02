from numpy import random
from Traits.Personality.config import mid, sc

def getConscientiousness():
    return random.normal(loc=mid, scale=sc, size=(1))