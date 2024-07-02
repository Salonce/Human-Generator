from Person import Person

def describe(person:Person):
    print(
        '\n'
        + 'Physical traits: \n'
        + 'Gender: ' + str(person.getGender()) + '\n'
        + 'Height : ' + str(person.getHeight()) + '\n'
        + 'Weight : ' + str(person.getWeight()) + '\n'
        + '\n'
        + 'Cognitive traits: \n'
        + 'Intelligence: ' + str(person.getIntelligence()) + '\n'
        + '\n'
        + 'Personality traits (Big five): \n'
        + 'Openess: ' + str(person.getOpen()) + '\n'
        + 'Conscientiousness: ' + str(person.getConsc()) + '\n'
        + 'Extraversion: ' + str(person.getExtra()) + '\n'
        + 'Agreeableness: ' + str(person.getAgreea()) + '\n'
        + 'Neuroticism: ' + str(person.getNeurot()))
