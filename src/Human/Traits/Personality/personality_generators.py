from numpy import random

#for main big five traits
def generate_trait():
    return round(random.normal(loc=50, scale=20))

#for big five subtraits
def generate_subtrait(general):
    return round(random.normal(loc=general, scale=10))