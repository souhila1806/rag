"""
Evaluation set for the RAG pipeline.

Each entry:
- question: the query to send through the pipeline
- expected_answer: key fact(s) the generated answer should contain
- expected_source: the KB filename the answer should come from (None if the
  question has no answer anywhere in the KB, used to test refusal behavior)
- type: "direct" (wording close to the doc), "paraphrase" (same fact, different
  wording), or "out_of_kb" (no answer exists in the KB)
"""

eval_set = [
    # --- ancient_wonders.md ---
    {
        "question": "Which of the Seven Wonders of the Ancient World is still standing today?",
        "expected_answer": "The Great Pyramid of Giza",
        "expected_source": "ancient_wonders.md",
        "type": "direct",
    },
    {
        "question": "Who sculpted the giant statue of Zeus at Olympia?",
        "expected_answer": "Phidias",
        "expected_source": "ancient_wonders.md",
        "type": "direct",
    },
    {
        "question": "Why do historians doubt that the Hanging Gardens were really in Babylon?",
        "expected_answer": "No archaeological evidence has been confirmed; some think they were actually in Nineveh",
        "expected_source": "ancient_wonders.md",
        "type": "paraphrase",
    },

    # --- water_cycle.md ---
    {
        "question": "What percentage of global evaporation comes from the oceans?",
        "expected_answer": "About 86%",
        "expected_source": "water_cycle.md",
        "type": "direct",
    },
    {
        "question": "How does cutting down forests affect local rainfall?",
        "expected_answer": "Deforestation reduces transpiration, which can decrease local rainfall over time",
        "expected_source": "water_cycle.md",
        "type": "paraphrase",
    },
    {
        "question": "What is the term for evaporation and transpiration combined?",
        "expected_answer": "Evapotranspiration",
        "expected_source": "water_cycle.md",
        "type": "direct",
    },

    # --- photosynthesis.md ---
    {
        "question": "Why do most plants look green?",
        "expected_answer": "Chlorophyll reflects green light while absorbing blue and red wavelengths",
        "expected_source": "photosynthesis.md",
        "type": "paraphrase",
    },
    {
        "question": "Where in the chloroplast does the Calvin cycle take place?",
        "expected_answer": "In the stroma",
        "expected_source": "photosynthesis.md",
        "type": "direct",
    },
    {
        "question": "What gas is released when water molecules are split during photosynthesis?",
        "expected_answer": "Oxygen",
        "expected_source": "photosynthesis.md",
        "type": "paraphrase",
    },

    # --- history_of_internet.md ---
    {
        "question": "Who invented the World Wide Web and when?",
        "expected_answer": "Tim Berners-Lee, in 1989",
        "expected_source": "history_of_internet.md",
        "type": "direct",
    },
    {
        "question": "When was the first message sent over ARPANET?",
        "expected_answer": "October 29, 1969",
        "expected_source": "history_of_internet.md",
        "type": "direct",
    },
    {
        "question": "Who is credited with popularizing the '@' symbol in email addresses?",
        "expected_answer": "Ray Tomlinson",
        "expected_source": "history_of_internet.md",
        "type": "paraphrase",
    },

    # --- circulatory_system.md ---
    {
        "question": "How many chambers does the human heart have?",
        "expected_answer": "Four",
        "expected_source": "circulatory_system.md",
        "type": "direct",
    },
    {
        "question": "Which blood vessel type is where oxygen and nutrients actually pass into body tissues?",
        "expected_answer": "Capillaries",
        "expected_source": "circulatory_system.md",
        "type": "paraphrase",
    },
    {
        "question": "What is considered a normal blood pressure reading?",
        "expected_answer": "Around 120/80 mmHg",
        "expected_source": "circulatory_system.md",
        "type": "direct",
    },

    # --- out-of-KB questions (no answer should exist) ---
    {
        "question": "What causes earthquakes?",
        "expected_answer": None,
        "expected_source": None,
        "type": "out_of_kb",
    },
    {
        "question": "Who won the FIFA World Cup in 2022?",
        "expected_answer": None,
        "expected_source": None,
        "type": "out_of_kb",
    },
    {
        "question": "What is the recipe for a traditional Algerian couscous?",
        "expected_answer": None,
        "expected_source": None,
        "type": "out_of_kb",
    },
]