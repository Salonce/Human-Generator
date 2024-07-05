from src.Human.Traits.Cognition.Intelligence import Intelligence
from src.Human.Traits.Personality.Personality import Personality
from src.Human.Traits.Physique.Physique import Physique


class Human:
    def __init__(self, physicality: Physique,
                 personality: Personality,
                 intelligence: Intelligence):
        self.physicality = physicality
        self.personality = personality
        self.intelligence = intelligence

    @classmethod
    def generate_random(cls):
        physique = Physique.generate_random()
        personality = Personality.generate_random()
        gender = physique.get_gender()
        intelligence = Intelligence.generate_random(gender)
        return cls(physique,
                   personality,
                   intelligence)

    def get_physicality(self):
        return self.physicality

    def get_personality(self):
        return self.personality

    def get_intelligence(self):
        return self.intelligence
