from .Personality import Personality


def describe_personality(personality: Personality) -> str:
    openness = personality.openness
    consc = personality.conscientiousness
    extraversion = personality.extraversion
    agreeableness = personality.agreeableness
    neuroticism = personality.neuroticism

    return (
            'Personality traits:'
            + '\n'
            + '\n' '-- Openness: [' + str(openness.openness) + ']'
            + '\n' + '---- Imagination: [' + str(openness.imagination) + ']'
            + '\n' + '---- Artistic Interests: [' + str(openness.artistic_interests) + ']'
            + '\n' + '---- Emotionality: [' + str(openness.emotionality) + ']'
            + '\n' + '---- Adventurousness: [' + str(openness.adventurousness) + ']'
            + '\n' + '---- Intellect: [' + str(openness.intellect) + ']'
            + '\n' + '---- Liberalism: [' + str(openness.liberalism) + ']'
            + '\n'
            + '\n' '-- Conscientiousness: [' + str(consc.conscientiousness) + ']'
            + '\n' + '---- Self-Efficacy: [' + str(consc.self_efficacy) + ']'
            + '\n' + '---- Orderliness: [' + str(consc.orderliness) + ']'
            + '\n' + '---- Dutifulness: [' + str(consc.dutifulness) + ']'
            + '\n' + '---- Achievement-Striving: [' + str(consc.achievement_striving) + ']'
            + '\n' + '---- Self-Discipline: [' + str(consc.self_discipline) + ']'
            + '\n' + '---- Cautiousness: [' + str(consc.cautiousness) + ']'
            + '\n'
            + '\n' '-- Extraversion: [' + str(extraversion.extraversion) + ']'
            + '\n' + '---- Friendliness: [' + str(extraversion.friendliness) + ']'
            + '\n' + '---- Gregariousness: [' + str(extraversion.gregariousness) + ']'
            + '\n' + '---- Assertiveness: [' + str(extraversion.assertiveness) + ']'
            + '\n' + '---- Activity Level: [' + str(extraversion.activity_level) + ']'
            + '\n' + '---- Excitement-Seeking: [' + str(extraversion.excitement_seeking) + ']'
            + '\n' + '---- Cheerfulness: [' + str(extraversion.cheerfulness) + ']'
            + '\n'
            + '\n' '-- Agreeableness: [' + str(agreeableness.agreeableness) + ']'
            + '\n' + '---- Trust: [' + str(agreeableness.trust) + ']'
            + '\n' + '---- Morality: [' + str(agreeableness.morality) + ']'
            + '\n' + '---- Altruism: [' + str(agreeableness.altruism) + ']'
            + '\n' + '---- Cooperation: [' + str(agreeableness.cooperation) + ']'
            + '\n' + '---- Modesty: [' + str(agreeableness.modesty) + ']'
            + '\n' + '---- Sympathy: [' + str(agreeableness.sympathy) + ']'
            + '\n'
            + '\n' '-- Neuroticism: [' + str(neuroticism.neuroticism) + ']'
            + '\n' + '---- Anxiety: [' + str(neuroticism.anxiety) + ']'
            + '\n' + '---- Anger: [' + str(neuroticism.anger) + ']'
            + '\n' + '---- Depression: [' + str(neuroticism.depression) + ']'
            + '\n' + '---- Self-Consciousness: [' + str(neuroticism.self_consciousness) + ']'
            + '\n' + '---- Immoderation: [' + str(neuroticism.immoderation) + ']'
            + '\n' + '---- Vulnerability: [' + str(neuroticism.vulnerability) + ']'
    )


def describe_personality_main(personality: Personality) -> str:
    return ('Personality traits: \n'
            + '\n' '-- Openness: [' + str(personality.openness.openness) + ']'
            + '\n' '-- Conscientiousness: [' + str(personality.conscientiousness.conscientiousness) + ']'
            + '\n' '-- Extraversion: [' + str(personality.extraversion.extraversion) + ']'
            + '\n' '-- Agreeableness: [' + str(personality.agreeableness.agreeableness) + ']'
            + '\n' '-- Neuroticism: [' + str(personality.neuroticism.neuroticism) + ']')