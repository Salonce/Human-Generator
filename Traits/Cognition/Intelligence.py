class Intelligence:
    def __init__(self, general_intelligence, auditory_processing, fluid_reasoning, long_term_memory, long_term_storage_retrieval,
                 processing_speed, quantitative_knowledge, reaction_time, reading_and_writing,
                 visual_processing, working_memory):
        self.general_intelligence = general_intelligence  # Auditory Processing (Ga)
        self.auditory_processing = auditory_processing  # Auditory Processing (Ga)
        self.fluid_reasoning = fluid_reasoning  # Fluid Reasoning (Gf)
        self.long_term_memory = long_term_memory  # Comprehension-Knowledge (Gc)
        self.long_term_storage_retrieval = long_term_storage_retrieval  # Long-Term Storage and Retrieval (Glr)
        self.processing_speed = processing_speed  # Processing Speed (Gs)
        self.quantitative_knowledge = quantitative_knowledge  # Quantitative Knowledge (Gq)
        self.reaction_time = reaction_time  # Decision/Reaction Time/Speed (Gt)
        self.reading_and_writing = reading_and_writing  # Reading & Writing Ability (Grw)
        self.visual_processing = visual_processing  # Visual Processing (Gv)
        self.working_memory = working_memory  # Short-Term Memory (Gsm)

    def get_general_intelligence(self):
        return self.general_intelligence

    def get_auditory_processing(self):
        return self.auditory_processing

    def get_fluid_reasoning(self):
        return self.fluid_reasoning

    def get_long_term_memory(self):
        return self.long_term_memory

    def get_long_term_storage_retrieval(self):
        return self.long_term_storage_retrieval

    def get_processing_speed(self):
        return self.processing_speed

    def get_quantitative_knowledge(self):
        return self.quantitative_knowledge

    def get_reaction_time(self):
        return self.reaction_time

    def get_reading_and_writing(self):
        return self.reading_and_writing

    def get_visual_processing(self):
        return self.visual_processing

    def get_working_memory(self):
        return self.working_memory