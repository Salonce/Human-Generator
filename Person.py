from Traits.Cognition.Intelligence import Intelligence
from Traits.Personality.Personality import Personality
from Traits.Physique.Physique import Physicality


class Person:
    def __init__(self, physicality: Physicality,
                 personality: Personality,
                 intelligence: Intelligence):
        self.physicality = physicality
        self.personality = personality
        self.intelligence = intelligence

    @classmethod
    def generate_random(cls):
        return cls(Physicality.generate_random(),
                   Personality.generate_random(),
                   Intelligence.generate_random())

    def get_physicality(self):
        return self.physicality

    def get_personality(self):
        return self.personality

    def get_intelligence(self):
        return self.intelligence
