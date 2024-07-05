from .Traits.Openness import Openness
from .Traits.Neuroticism import Neuroticism
from .Traits.Extraversion import Extraversion
from .Traits.Conscientiousness import Conscientiousness
from .Traits.Agreeableness import Agreeableness


class Personality:
    def __init__(self, openness: Openness,
                 conscientiousness: Conscientiousness,
                 extraversion: Extraversion,
                 agreeableness: Agreeableness,
                 neuroticism: Neuroticism):
        self.openness = openness
        self.conscientiousness = conscientiousness
        self.extraversion = extraversion
        self.agreeableness = agreeableness
        self.neuroticism = neuroticism

    @classmethod
    def generate_random(cls):
        return cls(Openness.generate_random(),
                   Conscientiousness.generate_random(),
                   Extraversion.generate_random(),
                   Agreeableness.generate_random(),
                   Neuroticism.generate_random(),
                   )