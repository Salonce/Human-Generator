from Person import Person
from Traits.Cognition.util.describe_int import describe_int


def describe(person: Person):

    int = person.getIntelligence()
    intdesc = describe_int(int)

    print(
        '\n'
        + 'Physical traits: \n'
        + 'Gender: ' + str(person.getGender()) + '\n'
        + 'Height : ' + str(person.getHeight()) + '\n'
        + 'Weight : ' + str(person.getWeight()) + '\n'
        + '\n'
        + 'Cognitive traits: \n'
        + '\n'
        + intdesc
        + '\n'
        + '\n' + 'Personality traits (Big five): \n'
        + 'Openess: ' + str(person.getPersonality().getOpeness()) + '\n'
        + 'Conscientiousness: ' + str(person.getPersonality().getConscientiousness()) + '\n'
        + 'Extraversion: ' + str(person.getPersonality().getExtraversion()) + '\n'
        + 'Agreeableness: ' + str(person.getPersonality().getAgreeableness()) + '\n'
        + 'Neuroticism: ' + str(person.getPersonality().getNeuroticism()))
