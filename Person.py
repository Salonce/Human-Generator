from numpy import random
from Traits.Personality.openess import getOpeness
from Traits.Personality.coscientiousness import getConscientiousness
from Traits.Personality.neuroticism import getNeuroticism
from Traits.Personality.extraversion import getExtraversion
from Traits.Personality.agreeableness import getAgreeableness
from Traits.height import getHeight
from Traits.intelligence import getIntelligence
from Traits.weight import getWeight


class Person:
    def __init__(self, gender=None, height=None, weight=None, openness=None, conscientiousness=None, extraversion=None,
                 agreeableness=None, neuroticism=None, intelligence=None):
        self.gender = gender
        self.height = height
        self.weight = weight
        self.openness = openness
        self.conscientiousness = conscientiousness
        self.extraversion = extraversion
        self.agreeableness = agreeableness
        self.neuroticism = neuroticism
        self.intelligence = intelligence

    def getGender(self):
        return self.gender
    def getHeight(self):
        return self.height
    def getWeight(self):
        return self.weight
    def getOpen(self):
        return self.openness
    def getConsc(self):
        return self.conscientiousness
    def getExtra(self):
        return self.extraversion
    def getAgreea(self):
        return self.agreeableness
    def getNeurot(self):
        return self.neuroticism
    def getIntelligence(self):
        return self.intelligence
