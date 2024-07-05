from Traits.Cognition.Intelligence import Intelligence
from Traits.Personality.Personality import Personality
from Traits.Physique.Physique import Physique


class Human:
    def __init__(self, physique: Physique,
                 personality: Personality,
                 intelligence: Intelligence):
        self.physique = physique
        self.personality = personality
        self.intelligence = intelligence

    @classmethod
    def generate_random(cls):
        physique = Physique.generate_random()
        personality = Personality.generate_random()
        gender = physique.gender
        intelligence = Intelligence.generate_random(gender)
        return cls(physique,
                   personality,
                   intelligence)