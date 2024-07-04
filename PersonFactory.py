from numpy import random

from Person import Person
from Traits.Physical.height import get_height
from Traits.Physical.gender import get_gender
from Traits.Cognition import IntelligenceFactory
from Traits.Physical.weight import get_weight
from Traits.Personality.Personality import Personality

def create_Person():
    gender = get_gender()
    height = get_height(gender)
    weight = get_weight(height, gender)
    personality = Personality.generate_random()
    intelligence = IntelligenceFactory.create_intelligence()

    return Person(gender, height, weight, personality, intelligence)