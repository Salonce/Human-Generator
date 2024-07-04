from Traits.Personality.default import getAdjusted, getDefault

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
        neuroticism = getDefault()
        anxiety = getAdjusted(neuroticism)
        anger = getAdjusted(neuroticism)
        depression = getAdjusted(neuroticism)
        self_consciousness = getAdjusted(neuroticism)
        immoderation = getAdjusted(neuroticism)
        vulnerability = getAdjusted(neuroticism)
        neuroticism = (anxiety + anger + depression + self_consciousness + immoderation + vulnerability) / 6

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