from Traits.Cognition.Intelligence import Intelligence


def describe_int(intelligence: Intelligence) -> str:
    return ('-- General intelligence: ' + str(intelligence.get_general_intelligence())
            + '\n' + '---- Auditory processing: ' + str(intelligence.get_auditory_processing())
            + '\n' + '---- Fluid reasoning: ' + str(intelligence.get_fluid_reasoning())
            + '\n' + '---- Long term memory: ' + str(intelligence.get_long_term_memory())
            + '\n' + '---- Long term storage retrieval: ' + str(intelligence.get_long_term_storage_retrieval())
            + '\n' + '---- Processing speed: ' + str(intelligence.get_processing_speed())
            + '\n' + '---- Quantitative knowledge: ' + str(intelligence.get_quantitative_knowledge())
            + '\n' + '---- Reaction time: ' + str(intelligence.get_reaction_time())
            + '\n' + '---- Reading and writing: ' + str(intelligence.get_reading_and_writing())
            + '\n' + '---- Visual processing: ' + str(intelligence.get_visual_processing())
            + '\n' + '---- Working memory: ' + str(intelligence.get_working_memory()))

    # auditory_processing = getDefault()
    # fluid_reasoning = getDefault()
    # long_term_memory = getDefault()
    # long_term_storage_retrieval = getDefault()
    # processing_speed = getDefault()
    # quantitative_knowledge = getDefault()
    # reaction_time = getDefault()
    # reading_and_writing = getDefault()
    # visual_processing = getDefault()
    # working_memory = getDefault()
