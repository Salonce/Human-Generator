from numpy import random

from Person import Person
from Traits.height import getHeight
from Traits.intelligence import getIntelligence
from Traits.weight import getWeight
from Traits.Personality.PersonalityFactory import create_Personality

def create_Person():
    gender = random.choice(['male', 'female'])
    height = getHeight(gender)
    weight = getWeight(height, gender)
    personality = create_Personality()
    intelligence = getIntelligence()

    return Person(gender, height, weight, personality, intelligence)