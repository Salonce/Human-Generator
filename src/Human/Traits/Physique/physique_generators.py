from numpy import random

def get_gender():
    return random.choice(['Male', 'Female'])

def get_skin_color():
    return random.choice(['Black', 'Brown', 'White', 'Yellow'])


def get_height(gender):
    if gender == "Male":
        return round(random.normal(loc=178, scale=6))
    if gender == "Female":
        return round(random.normal(loc=165, scale=6))


#Men: IBW (kgs) = 22 × (height in meters)2
#Women: IBW (kgs) = 22 × (height in meters − 10 cm)2
#
def get_weight(gender, height):
    if gender == "Male":
        return round(random.normal(loc=22 * (pow(height / 100, 2)), scale=7))
    if gender == "Female":
        return round(random.normal(loc=22 * (pow(height / 100 - 0.1, 2)), scale=7))
