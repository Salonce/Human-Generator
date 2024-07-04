from numpy import random

#https://www.medicinenet.com/how_do_you_calculate_ideal_body_weight/article.htm
#Men: IBW (kgs) = 22 × (height in meters)2
#Women: IBW (kgs) = 22 × (height in meters − 10 cm)2

def get_weight(height, gender):
    if gender == "male":
        return random.normal(loc=22*(pow(height/100, 2)), scale=7, size=(1))
    if gender == "female":
        return random.normal(loc=22*(pow(height/100 - 0.1, 2)), scale=7, size=(1))