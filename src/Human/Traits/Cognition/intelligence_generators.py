from numpy import random

#for general intelligence - g-factor
def generate_general_intelligence():
    return round(random.normal(loc=100, scale=15))


#for subtypes of intelligence, the higher general intelligence, the bigger subtrait sd (standard deviation)
def generate_subtype_intelligence(general_intelligence):
    sd = (general_intelligence - 100)/10 + 6
    return round(random.normal(loc=general_intelligence, scale=sd))
