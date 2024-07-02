class Personality:
    def __init__(self, openness=None, conscientiousness=None, extraversion=None, agreeableness=None, neuroticism=None):
        self.openness = openness
        self.conscientiousness = conscientiousness
        self.extraversion = extraversion
        self.agreeableness = agreeableness
        self.neuroticism = neuroticism

    def getOpeness(self):
        return self.openness
    def getConscientiousness(self):
        return self.conscientiousness
    def getExtraversion(self):
        return self.extraversion
    def getAgreeableness(self):
        return self.agreeableness
    def getNeuroticism(self):
        return self.neuroticism