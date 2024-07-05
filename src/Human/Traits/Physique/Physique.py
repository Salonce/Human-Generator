from . import physique_generators


class Physique:
    def __init__(self, gender, height, weight, skin_color):
        self.gender = gender
        self.height = height
        self.weight = weight
        self.skin_color = skin_color

    @classmethod
    def generate_random(cls):
        rand_gender = physique_generators.get_gender()
        rand_skin_color = physique_generators.get_skin_color()
        rand_height = physique_generators.get_height(rand_gender)
        rand_weight = physique_generators.get_weight(rand_gender, rand_height)
        return cls(rand_gender, rand_height, rand_weight, rand_skin_color)