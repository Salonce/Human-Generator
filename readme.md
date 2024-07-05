# Human (profile) generator

Generate a random human profile: physique, intelligence, and personality attributes.

### Features
1. Scientifically accepted divisions of personality and cognition:
   - Cognitive Abilities: based on the Cattell–Horn–Carroll theory.
   - Personality Traits: based on the Five-Factor Model (Big Five).
2. Randomized scores: generated using normal distribution and tweaked according to the results of the latest scientific research.

**Possible Applications:** Generate entire populations or nations for simulations or games.


## Generate a human profile and display it in the console
In the root directory:
1. `pip install -r requirements.txt`
2. `python .\src\Human\main.py` or `python .\src\Human\main_reduced.py` for shorter version


### An example of a randomly generated profile:
```
[Person's name]


Physique traits: 

-- Skin: Brown
-- Gender: Female
-- Height: 174 cm
-- Weight: 54 kg

Cognitive traits: 

-- General intelligence: [121]
---- Auditory processing: [126]
---- Fluid reasoning: [130]
---- Long term memory: [124]
---- Long term storage retrieval: [107]
---- Processing speed: [122]
---- Quantitative knowledge: [119]
---- Reaction time: [117]
---- Reading and writing: [114]
---- Visual processing: [124]
---- Working memory: [126]

Personality traits:

-- Openness: [65]
---- Imagination: [68]
---- Artistic Interests: [52]
---- Emotionality: [66]
---- Adventurousness: [72]
---- Intellect: [76]
---- Liberalism: [54]

-- Conscientiousness: [83]
---- Self-Efficacy: [104]
---- Orderliness: [95]
---- Dutifulness: [83]
---- Achievement-Striving: [66]
---- Self-Discipline: [84]
---- Cautiousness: [68]

-- Extraversion: [29]
---- Friendliness: [46]
---- Gregariousness: [25]
---- Assertiveness: [29]
---- Activity Level: [26]
---- Excitement-Seeking: [25]
---- Cheerfulness: [22]

-- Agreeableness: [60]
---- Trust: [70]
---- Morality: [64]
---- Altruism: [67]
---- Cooperation: [48]
---- Modesty: [53]
---- Sympathy: [59]

-- Neuroticism: [22]
---- Anxiety: [21]
---- Anger: [16]
---- Depression: [28]
---- Self-Consciousness: [32]
---- Immoderation: [16]
---- Vulnerability: [17]

Process finished with exit code 0
```