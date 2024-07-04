from Traits.Personality.personality_generators import generate_subtrait, generate_trait

class Conscientiousness:

    def __init__(self, conscientiousness, self_efficacy, orderliness, dutifulness, achievement_striving, self_discipline, cautiousness):
        self.conscientiousness = conscientiousness
        self.self_efficacy = self_efficacy
        self.orderliness = orderliness
        self.dutifulness = dutifulness
        self.achievement_striving = achievement_striving
        self.self_discipline = self_discipline
        self.cautiousness = cautiousness

    @classmethod
    def generate_random(cls):
        conscientiousness = generate_trait()
        self_efficacy = generate_subtrait(conscientiousness)
        orderliness = generate_subtrait(conscientiousness)
        dutifulness = generate_subtrait(conscientiousness)
        achievement_striving = generate_subtrait(conscientiousness)
        self_discipline = generate_subtrait(conscientiousness)
        cautiousness = generate_subtrait(conscientiousness)
        conscientiousness = round((self_efficacy + orderliness + dutifulness + achievement_striving + self_discipline + cautiousness) / 6)

        return cls(conscientiousness, self_efficacy, orderliness, dutifulness, achievement_striving, self_discipline, cautiousness)

    def get_conscientiousness(self):
        return self.conscientiousness

    def get_self_efficacy(self):
        return self.self_efficacy

    def get_orderliness(self):
        return self.orderliness

    def get_dutifulness(self):
        return self.dutifulness

    def get_achievement_striving(self):
        return self.achievement_striving

    def get_self_discipline(self):
        return self.self_discipline

    def get_cautiousness(self):
        return self.cautiousness