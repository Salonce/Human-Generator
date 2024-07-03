from Traits.Cognition import Intelligence
from Traits.Personality import Personality


class Person:
    def __init__(self, gender, height, weight, personality: Personality, intelligence: Intelligence):
        self.gender = gender
        self.height = height
        self.weight = weight
        self.personality = personality
        self.intelligence = intelligence

    def getGender(self):
        return self.gender

    def getHeight(self):
        return self.height

    def getWeight(self):
        return self.weight

    def getPersonality(self):
        return self.personality

    def getIntelligence(self):
        return self.intelligence
