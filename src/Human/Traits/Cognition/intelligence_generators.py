from numpy import random

#for general intelligence - g-factor
def generate_general_intelligence(sex):
    if sex == "Male":
        sd = 15
    if sex == "Female":
        sd = 14
    return round(random.normal(loc=100, scale=sd))


#for subtypes of intelligence, the higher general intelligence, the bigger subtrait sd (standard deviation)
def generate_subtype_intelligence(general_intelligence):
    sd = (general_intelligence - 100)/10 + 6
    return round(random.normal(loc=general_intelligence, scale=sd))


#note - females score on average ~0.5sd on verbal ability
#note - men score on average ~0.7sd better on visual-spatial ability, slightly on memory (perhaps)
#note - men have higher variance

# Sex differences are
# smaller for visual-spatial working memory (d = 0.09 to 0.22; Voyer, Voyer, & Saint-
# Aubin, 2016), spatial perception (d = 0.04 to 0.84), and spatial visualization (d = 0.24
# to 0.50) than for mental rotation (d = 0.50 to 0.96; Linn & Petersen, 1985)