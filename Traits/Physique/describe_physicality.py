from Traits.Physique.Physique import Physicality


def describe_physicality(physicality: Physicality) -> str:
    return ('Physique traits: \n'
            + '\n' '-- Gender: ' + str(physicality.get_gender())
            + '\n' '-- Height: ' + str(physicality.get_height()) + " cm"
            + '\n' '-- Weight: ' + str(physicality.get_weight())) + " kg"
