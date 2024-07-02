from numpy import random

from Person import Person
from Traits.Personality.agreeableness import getAgreeableness
from Traits.Personality.coscientiousness import getConscientiousness
from Traits.Personality.extraversion import getExtraversion
from Traits.Personality.neuroticism import getNeuroticism
from Traits.Personality.openess import getOpeness
from Traits.height import getHeight
from Traits.intelligence import getIntelligence
from Traits.weight import getWeight


def create_Person():
    gender = random.choice(['male', 'female'])
    height = getHeight(gender)
    weight = getWeight(height, gender)
    openness = getOpeness()
    conscientiousness = getConscientiousness()
    extraversion = getExtraversion()
    agreeableness = getAgreeableness()
    neuroticism = getNeuroticism()
    intelligence = getIntelligence()

    return Person(gender, height, weight, openness, conscientiousness, extraversion, agreeableness, neuroticism, intelligence)