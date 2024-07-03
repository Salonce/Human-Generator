from numpy import random

from Person import Person
from Traits.Physical.height import getHeight
from Traits.Cognition import IntelligenceFactory
from Traits.Physical.weight import getWeight
from Traits.Personality.PersonalityFactory import create_Personality

def create_Person():
    gender = random.choice(['male', 'female'])
    height = getHeight(gender)
    weight = getWeight(height, gender)
    personality = create_Personality()
    intelligence = IntelligenceFactory.create_intelligence()

    return Person(gender, height, weight, personality, intelligence)