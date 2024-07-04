from Traits.Personality.Personality import Personality


def describe_personality(personality: Personality) -> str:
    return ('Personality traits:'
            + '\n'
            + '\n' '-- Openness: ' + str(personality.get_openness().get_openness())
            + '\n' + '---- Imagination: ' + str(personality.get_openness().get_imagination())
            + '\n' + '---- Artistic Interests: ' + str(personality.get_openness().get_artistic_interests())
            + '\n' + '---- Emotionality: ' + str(personality.get_openness().get_emotionality())
            + '\n' + '---- Adventurousness: ' + str(personality.get_openness().get_adventurousness())
            + '\n' + '---- Intellect: ' + str(personality.get_openness().get_intellect())
            + '\n' + '---- Liberalism: ' + str(personality.get_openness().get_liberalism())
            + '\n'
            + '\n' '-- Conscientiousness: ' + str(personality.get_conscientiousness().get_conscientiousness())
            + '\n' + '---- Self-Efficacy: ' + str(personality.get_conscientiousness().get_self_efficacy())
            + '\n' + '---- Orderliness: ' + str(personality.get_conscientiousness().get_orderliness())
            + '\n' + '---- Dutifulness: ' + str(personality.get_conscientiousness().get_dutifulness())
            + '\n' + '---- Achievement-Striving: ' + str(personality.get_conscientiousness().get_achievement_striving())
            + '\n' + '---- Self-Discipline: ' + str(personality.get_conscientiousness().get_self_discipline())
            + '\n' + '---- Cautiousness: ' + str(personality.get_conscientiousness().get_cautiousness())
            + '\n'
            + '\n' '-- Extraversion: ' + str(personality.get_extraversion().get_extraversion())
            + '\n' + '---- Friendliness: ' + str(personality.get_extraversion().get_friendliness())
            + '\n' + '---- Gregariousness: ' + str(personality.get_extraversion().get_gregariousness())
            + '\n' + '---- Assertiveness: ' + str(personality.get_extraversion().get_assertiveness())
            + '\n' + '---- Activity Level: ' + str(personality.get_extraversion().get_activity_level())
            + '\n' + '---- Excitement-Seeking: ' + str(personality.get_extraversion().get_excitement_seeking())
            + '\n' + '---- Cheerfulness: ' + str(personality.get_extraversion().get_cheerfulness())
            + '\n'
            + '\n' '-- Agreeableness: ' + str(personality.get_agreeableness().get_agreeableness())
            + '\n' + '---- Trust: ' + str(personality.get_agreeableness().get_trust())
            + '\n' + '---- Morality: ' + str(personality.get_agreeableness().get_morality())
            + '\n' + '---- Altruism: ' + str(personality.get_agreeableness().get_altruism())
            + '\n' + '---- Cooperation: ' + str(personality.get_agreeableness().get_cooperation())
            + '\n' + '---- Modesty: ' + str(personality.get_agreeableness().get_modesty())
            + '\n' + '---- Sympathy: ' + str(personality.get_agreeableness().get_sympathy())
            + '\n'
            + '\n' '-- Neuroticism: ' + str(personality.get_neuroticism().get_neuroticism())
            + '\n' + '---- Anxiety: ' + str(personality.get_neuroticism().get_anxiety())
            + '\n' + '---- Anger: ' + str(personality.get_neuroticism().get_anger())
            + '\n' + '---- Depression: ' + str(personality.get_neuroticism().get_depression())
            + '\n' + '---- Self-Consciousness: ' + str(personality.get_neuroticism().get_self_consciousness())
            + '\n' + '---- Immoderation: ' + str(personality.get_neuroticism().get_immoderation())
            + '\n' + '---- Vulnerability: ' + str(personality.get_neuroticism().get_vulnerability()))


def describe_personality_main(personality: Personality) -> str:
    return ('Personality traits: \n'
            + '\n' '-- Openness: ' + str(personality.get_openness().get_openness())
            + '\n' '-- Conscientiousness: ' + str(personality.get_conscientiousness().get_conscientiousness())
            + '\n' '-- Extraversion: ' + str(personality.get_extraversion().get_extraversion())
            + '\n' '-- Agreeableness: ' + str(personality.get_agreeableness().get_agreeableness())
            + '\n' '-- Neuroticism: ' + str(personality.get_neuroticism().get_neuroticism()))
