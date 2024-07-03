from Person import Person
from Traits.Cognition.util.describe_int import describe_int


def describe(person: Person):

    print(
        '\n'
        + 'Physical traits: \n'
        + 'Gender: ' + str(person.getGender()) + '\n'
        + 'Height : ' + str(person.getHeight()) + '\n'
        + 'Weight : ' + str(person.getWeight()) + '\n'
        + '\n' + describe_int(person.getIntelligence())
        + '\n'
        + '\n' + 'Personality traits (Big five): \n'
        + 'Openess: ' + str(person.getPersonality().get_openess()) + '\n'
        + 'Conscientiousness: ' + str(person.getPersonality().get_conscientiousness()) + '\n'
        + 'Extraversion: ' + str(person.getPersonality().get_extraversion()) + '\n'
        + 'Agreeableness: ' + str(person.getPersonality().get_agreeableness()) + '\n'
        + 'Neuroticism: ' + str(person.getPersonality().get_neuroticism()))
