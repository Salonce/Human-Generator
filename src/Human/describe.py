from Human import Human
from src.Human.Traits.Cognition.describe_int import describe_int, describe_int_main
from src.Human.Traits.Physique.describe_physique import describe_physique
from src.Human.Traits.Personality.describe_personality import describe_personality, describe_personality_main

def describe(person: Human):
    print('\n'
          + '[Person\'s name]'
          + '\n'
          + '\n'
          + '\n' + describe_physique(person.get_physicality())
          + '\n'
          + '\n' + describe_int(person.get_intelligence())
          + '\n'
          + '\n' + describe_personality(person.get_personality())
          )

def describe_reduced(person: Human):
    print('\n'
          + '[Person\'s name]'
          + '\n'
          + '\n'
          + '\n' + describe_physique(person.get_physicality())
          + '\n'
          + '\n' + describe_int_main(person.get_intelligence())
          + '\n'
          + '\n' + describe_personality_main( person.get_personality())
          )
