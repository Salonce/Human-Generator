from src.Human.Traits.Cognition.intelligence_generators import generate_general_intelligence, generate_subtype_intelligence

# Stratum III: General intelligence (g)
# Stratum II: Broad abilities, including:
# Stratum I: Narrow abilities, which are more specific cognitive tasks under each broad ability.

class Intelligence:
    def __init__(self, general_intelligence,
                 auditory_processing,
                 fluid_reasoning,
                 long_term_memory,
                 long_term_storage_retrieval,
                 processing_speed,
                 quantitative_knowledge,
                 reaction_time,
                 reading_and_writing,
                 visual_processing,
                 working_memory):
        self.general_intelligence = general_intelligence
        self.auditory_processing = auditory_processing  # (Ga)
        self.fluid_reasoning = fluid_reasoning  # (Gf)
        self.long_term_memory = long_term_memory  # (Gc)
        self.long_term_storage_retrieval = long_term_storage_retrieval  # (Glr)
        self.processing_speed = processing_speed  # (Gs)
        self.quantitative_knowledge = quantitative_knowledge  # (Gq)
        self.reaction_time = reaction_time  # (Gt)
        self.reading_and_writing = reading_and_writing  # (Grw)
        self.visual_processing = visual_processing  # (Gv)
        self.working_memory = working_memory  # (Gsm)

    @classmethod
    def generate_random(cls, sex):
        general_intelligence = generate_general_intelligence(sex)

        auditory_processing = generate_subtype_intelligence(general_intelligence)
        fluid_reasoning = generate_subtype_intelligence(general_intelligence)
        long_term_memory = generate_subtype_intelligence(general_intelligence)
        long_term_storage_retrieval = generate_subtype_intelligence(general_intelligence)
        processing_speed = generate_subtype_intelligence(general_intelligence)
        quantitative_knowledge = generate_subtype_intelligence(general_intelligence)
        reaction_time = generate_subtype_intelligence(general_intelligence)
        reading_and_writing = generate_subtype_intelligence(general_intelligence)
        visual_processing = generate_subtype_intelligence(general_intelligence)
        working_memory = generate_subtype_intelligence(general_intelligence)

        general_intelligence = round((auditory_processing
                                      + fluid_reasoning
                                      + long_term_memory
                                      + long_term_storage_retrieval
                                      + processing_speed
                                      + quantitative_knowledge
                                      + reaction_time
                                      + reading_and_writing
                                      + visual_processing
                                      + working_memory) / 10)

        return cls(general_intelligence,
                   auditory_processing,
                   fluid_reasoning,
                   long_term_memory,
                   long_term_storage_retrieval,
                   processing_speed,
                   quantitative_knowledge,
                   reaction_time,
                   reading_and_writing,
                   visual_processing,
                   working_memory)