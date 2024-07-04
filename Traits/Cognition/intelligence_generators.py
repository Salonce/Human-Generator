from numpy import random

#for general intelligence - g-factor
def generate_general_intelligence():
    return random.normal(loc=100, scale=15, size=(1))


#for subtypes of intelligence
def generate_subtype_intelligence(general_intelligence):
    return random.normal(loc=general_intelligence, scale=6, size=(1))
