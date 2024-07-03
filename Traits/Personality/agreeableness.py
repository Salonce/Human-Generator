from numpy import random
from Traits.Personality.config import mid, sc

def get_agreeableness():
    return random.normal(loc=mid, scale=sc, size=(1))