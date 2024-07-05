from src.Human.Traits.Physique.Physique import Physique


def describe_physique(physique: Physique) -> str:
    return ('Physique traits: \n'
            + '\n' '-- Skin: ' + str(physique.get_skin_color())
            + '\n' '-- Gender: ' + str(physique.get_gender())
            + '\n' '-- Height: ' + str(physique.get_height()) + " cm"
            + '\n' '-- Weight: ' + str(physique.get_weight())) + " kg"
