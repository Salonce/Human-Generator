from numpy import random

from Person import Person
from Traits.Physical.Height import get_height
from Traits.Physical.Gender import get_gender
from Traits.Cognition.Intelligence import Intelligence
from Traits.Physical.Weight import get_weight
from Traits.Personality.Personality import Personality

def create_Person():
    gender = get_gender()
    height = get_height(gender)
    weight = get_weight(height, gender)
    personality = Personality.generate_random()
    intelligence = Intelligence.generate_random()

    return Person(gender, height, weight, personality, intelligence)