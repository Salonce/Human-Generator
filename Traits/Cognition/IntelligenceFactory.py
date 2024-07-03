from Traits.Cognition.Stratum2.Default import getDefault
from Traits.Cognition.Stratum2.Default import getAdjusted
from Traits.Cognition.Intelligence import Intelligence

def create_intelligence():
    general_intelligence = getDefault()

    auditory_processing = getAdjusted(general_intelligence)
    fluid_reasoning = getAdjusted(general_intelligence)
    long_term_memory = getAdjusted(general_intelligence)
    long_term_storage_retrieval = getAdjusted(general_intelligence)
    processing_speed = getAdjusted(general_intelligence)
    quantitative_knowledge = getAdjusted(general_intelligence)
    reaction_time = getAdjusted(general_intelligence)
    reading_and_writing = getAdjusted(general_intelligence)
    visual_processing = getAdjusted(general_intelligence)
    working_memory = getAdjusted(general_intelligence)

    general_intelligence = (auditory_processing + fluid_reasoning + long_term_memory + long_term_storage_retrieval + processing_speed
    + quantitative_knowledge + reaction_time + reading_and_writing + visual_processing + working_memory)/10

    return Intelligence(general_intelligence, auditory_processing, fluid_reasoning, long_term_memory, long_term_storage_retrieval, processing_speed,
                        quantitative_knowledge, reaction_time, reading_and_writing, visual_processing, working_memory)