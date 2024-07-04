from Person import Person
from Traits.Cognition.util.describe_int import describe_int
from Traits.Personality.util.describe_personality import describe_personality


def describe(person: Person):

    print(
        '\n'
        + 'Physical traits:'
        + '\n'
        + '\n' + '-- Gender: ' + str(person.getGender())
        + '\n' + '-- Height : ' + str(person.getHeight())
        + '\n' + '-- Weight : ' + str(person.getWeight())
        + '\n'
        + '\n' + describe_int(person.getIntelligence())
        + '\n'
        + '\n'
        + describe_personality(person.getPersonality()))
