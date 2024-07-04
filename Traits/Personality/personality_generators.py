from numpy import random

#for main big five traits
def generate_trait():
    return random.normal(loc=50, scale=20, size=(1))

#for big five subtraits
def generate_subtrait(general):
    return random.normal(loc=general, scale=10, size=(1))