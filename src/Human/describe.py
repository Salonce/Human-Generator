from Human import Human
from src.Human.Traits.Cognition.describe_int import describe_int, describe_int_main
from src.Human.Traits.Physique.describe_physique import describe_physique
from src.Human.Traits.Personality.describe_personality import describe_personality, describe_personality_main


def describe(person: Human):
    print('\n'
          + '[Person\'s name]'
          + '\n'
          + '\n'
          + '\n' + describe_physique(person.physique)
          + '\n'
          + '\n' + describe_int(person.intelligence)
          + '\n'
          + '\n' + describe_personality(person.personality)
          )


def describe_reduced(person: Human):
    print('\n'
          + '[Person\'s name]'
          + '\n'
          + '\n'
          + '\n' + describe_physique(person.physique)
          + '\n'
          + '\n' + describe_int_main(person.intelligence)
          + '\n'
          + '\n' + describe_personality_main(person.personality)
          )
