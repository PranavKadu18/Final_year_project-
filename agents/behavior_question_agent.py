from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
import re

from config.settings import GROQ_API_KEY


llm = ChatOpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1",
    model="llama-3.1-8b-instant",
    temperature=0.3
)


QUESTION_PROMPT = """
You are a psychological monitoring assistant for astronauts.

Based on the behavioral metrics below, generate 3 short questions
to better understand the astronaut's mental state.

Metrics:
{metrics}

Guidelines:
- Ask questions related to stress, fatigue, focus, or emotional wellbeing.
- If fatigue_indicator is high → ask about tiredness.
- If voice_stress is high → ask about stress or pressure.
- If eye_focus is low → ask about concentration.
- Questions must be simple.
- Maximum 3 questions.

Return ONLY the questions as a numbered list.
Example:

1. Are you feeling mentally overwhelmed right now?
2. Do you feel physically tired from recent tasks?
3. Are you having difficulty concentrating on your work?
"""


def behavior_question_agent(state):

    metrics = state["combined_metrics"]

    prompt = PromptTemplate.from_template(QUESTION_PROMPT)

    chain = prompt | llm

    response = chain.invoke(
        {
            "metrics": metrics
        }
    )

    raw_lines = response.content.split("\n")

    questions = []
    answers = []

    print("\nBehavioral Questions:")

    for line in raw_lines:

        q = line.strip()

        if len(q) < 5:
            continue

        # remove numbering like "1." or "2)"
        q_clean = re.sub(r"^\d+[\).\s]*", "", q)

        if not q_clean.endswith("?"):
            continue

        print(q_clean)

        ans = input("Your answer: ")

        questions.append(q_clean)
        answers.append(ans)

        # ensure maximum 3
        if len(questions) == 3:
            break

    state["behavior_questions"] = questions
    state["behavior_answers"] = answers

    return state