from Traits.Personality.personality_generators import generate_subtrait, generate_trait


class Openness:

    def __init__(self, openness, imagination, artistic_interests, emotionality, adventurousness, intellect, liberalism):
        self.openness = openness
        self.imagination = imagination
        self.artistic_interests = artistic_interests
        self.emotionality = emotionality
        self.adventurousness = adventurousness
        self.intellect = intellect
        self.liberalism = liberalism

    @classmethod
    def generate_random(cls):
        openness = generate_trait()
        imagination = generate_subtrait(openness)
        artistic_interests = generate_subtrait(openness)
        emotionality = generate_subtrait(openness)
        adventurousness = generate_subtrait(openness)
        intellect = generate_subtrait(openness)
        liberalism = generate_subtrait(openness)
        openness = round((imagination + artistic_interests + emotionality + adventurousness + intellect + liberalism) / 6)

        return cls(openness, imagination, artistic_interests, emotionality, adventurousness, intellect, liberalism)

    def get_openness(self):
        return self.openness

    def get_imagination(self):
        return self.imagination

    def get_artistic_interests(self):
        return self.artistic_interests

    def get_emotionality(self):
        return self.emotionality

    def get_adventurousness(self):
        return self.adventurousness

    def get_intellect(self):
        return self.intellect

    def get_liberalism(self):
        return self.liberalism

# Imagination: Creative and inventive.
# Artistic Interests: Appreciation for art and beauty.
# Emotionality: Awareness of one's own feelings.
# Adventurousness: Willingness to try new activities.
# Intellect: Intellectual curiosity and preference for complex ideas.
# Liberalism: Openness to new values and experiences.
