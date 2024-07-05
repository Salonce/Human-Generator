from src.Human.Traits.Cognition.Intelligence import Intelligence


def describe_int(intelligence: Intelligence) -> str:
    return ('Cognitive traits: \n'
            + '\n' '-- General intelligence: [' + str(intelligence.general_intelligence) + ']'
            + '\n' + '---- Auditory processing: [' + str(intelligence.auditory_processing) + ']'
            + '\n' + '---- Fluid reasoning: [' + str(intelligence.fluid_reasoning) + ']'
            + '\n' + '---- Long term memory: [' + str(intelligence.long_term_memory) + ']'
            + '\n' + '---- Long term storage retrieval: [' + str(intelligence.long_term_storage_retrieval) + ']'
            + '\n' + '---- Processing speed: [' + str(intelligence.processing_speed) + ']'
            + '\n' + '---- Quantitative knowledge: [' + str(intelligence.quantitative_knowledge) + ']'
            + '\n' + '---- Reaction time: [' + str(intelligence.reaction_time) + ']'
            + '\n' + '---- Reading and writing: [' + str(intelligence.reading_and_writing) + ']'
            + '\n' + '---- Visual processing: [' + str(intelligence.visual_processing) + ']'
            + '\n' + '---- Working memory: [' + str(intelligence.working_memory) + ']')

def describe_int_main(intelligence: Intelligence) -> str:
    return ('Cognitive traits: \n'
            + '\n' '-- General intelligence: [' + str(intelligence.general_intelligence) + ']')
