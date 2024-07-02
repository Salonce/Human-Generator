from numpy import random
from Traits.Personality.config import mid, sc

def getOpeness():
    return random.normal(loc=mid, scale=sc, size=(1))