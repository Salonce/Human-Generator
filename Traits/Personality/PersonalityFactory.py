from Traits.Personality.Personality import Personality
from Traits.Personality.agreeableness import getAgreeableness
from Traits.Personality.coscientiousness import getConscientiousness
from Traits.Personality.extraversion import getExtraversion
from Traits.Personality.neuroticism import getNeuroticism
from Traits.Personality.openess import getOpeness


def create_Personality():
    openness = getOpeness()
    conscientiousness = getConscientiousness()
    extraversion = getExtraversion()
    agreeableness = getAgreeableness()
    neuroticism = getNeuroticism()

    return Personality(openness, conscientiousness, extraversion, agreeableness, neuroticism)