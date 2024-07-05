from src.Human.Traits.Personality.personality_generators import generate_subtrait, generate_trait

class Neuroticism:

    def __init__(self, neuroticism, anxiety, anger, depression, self_consciousness, immoderation, vulnerability):
        self.neuroticism = neuroticism
        self.anxiety = anxiety
        self.anger = anger
        self.depression = depression
        self.self_consciousness = self_consciousness
        self.immoderation = immoderation
        self.vulnerability = vulnerability

    @classmethod
    def generate_random(cls):
        neuroticism = generate_trait()
        anxiety = generate_subtrait(neuroticism)
        anger = generate_subtrait(neuroticism)
        depression = generate_subtrait(neuroticism)
        self_consciousness = generate_subtrait(neuroticism)
        immoderation = generate_subtrait(neuroticism)
        vulnerability = generate_subtrait(neuroticism)
        neuroticism = round((anxiety + anger + depression + self_consciousness + immoderation + vulnerability) / 6)

        return cls(neuroticism, anxiety, anger, depression, self_consciousness, immoderation, vulnerability)

    def get_neuroticism(self):
        return self.neuroticism

    def get_anxiety(self):
        return self.anxiety

    def get_anger(self):
        return self.anger

    def get_depression(self):
        return self.depression

    def get_self_consciousness(self):
        return self.self_consciousness

    def get_immoderation(self):
        return self.immoderation

    def get_vulnerability(self):
        return self.vulnerability