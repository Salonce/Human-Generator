from .Physique import Physique


def describe_physique(physique: Physique) -> str:
    return ('Physique traits: \n'
            + '\n' '-- Skin: ' + str(physique.skin_color)
            + '\n' '-- Gender: ' + str(physique.gender)
            + '\n' '-- Height: ' + str(physique.height) + " cm"
            + '\n' '-- Weight: ' + str(physique.weight)) + " kg"
