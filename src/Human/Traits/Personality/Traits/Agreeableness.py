from ..personality_generators import generate_subtrait, generate_trait

class Agreeableness:

    def __init__(self, agreeableness, trust, morality, altruism, cooperation, modesty, sympathy):
        self.agreeableness = agreeableness
        self.trust = trust
        self.morality = morality
        self.altruism = altruism
        self.cooperation = cooperation
        self.modesty = modesty
        self.sympathy = sympathy

    @classmethod
    def generate_random(cls):
        agreeableness = generate_trait()
        trust = generate_subtrait(agreeableness)
        morality = generate_subtrait(agreeableness)
        altruism = generate_subtrait(agreeableness)
        cooperation = generate_subtrait(agreeableness)
        modesty = generate_subtrait(agreeableness)
        sympathy = generate_subtrait(agreeableness)
        agreeableness = round((trust + morality + altruism + cooperation + modesty + sympathy) / 6)

        return cls(agreeableness, trust, morality, altruism, cooperation, modesty, sympathy)

    def get_agreeableness(self):
        return self.agreeableness

    def get_trust(self):
        return self.trust

    def get_morality(self):
        return self.morality

    def get_altruism(self):
        return self.altruism

    def get_cooperation(self):
        return self.cooperation

    def get_modesty(self):
        return self.modesty

    def get_sympathy(self):
        return self.sympathy
