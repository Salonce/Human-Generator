from Person import Person
from Traits.Cognition.describe_int import describe_int
from Traits.Personality.describe_personality import describe_personality
from Traits.Physique.describe_physicality import describe_physicality


def describe(person: Person):
    print('\n'
          + '[Person\'s name]'
          + '\n'
          + '\n'
          + '\n' + describe_physicality(person.get_physicality())
          + '\n'
          + '\n' + describe_int(person.get_intelligence())
          + '\n'
          + '\n' + describe_personality(person.get_personality())
          )
