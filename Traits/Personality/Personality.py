class Personality:
    def __init__(self, openness=None, conscientiousness=None, extraversion=None, agreeableness=None, neuroticism=None):
        self.openness = openness
        self.conscientiousness = conscientiousness
        self.extraversion = extraversion
        self.agreeableness = agreeableness
        self.neuroticism = neuroticism

    def get_openess(self):
        return self.openness
    def get_conscientiousness(self):
        return self.conscientiousness
    def get_extraversion(self):
        return self.extraversion
    def get_agreeableness(self):
        return self.agreeableness
    def get_neuroticism(self):
        return self.neuroticism