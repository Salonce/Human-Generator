from src.Human.Traits.Physique import physique_generators


class Physicality:
    def __init__(self, gender, height, weight):
        self.gender = gender
        self.height = height
        self.weight = weight

    @classmethod
    def generate_random(cls):
        rand_gender = physique_generators.get_gender()
        rand_height = physique_generators.get_height(rand_gender)
        rand_weight = physique_generators.get_weight(rand_gender, rand_height)
        return cls(rand_gender, rand_height, rand_weight)

    def get_gender(self):
        return self.gender

    def get_height(self):
        return self.height

    def get_weight(self):
        return self.weight
