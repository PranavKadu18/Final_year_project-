import json

from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

from prompts.prompts import MOOD_ANALYSIS_PROMPT
from config.settings import GROQ_API_KEY


llm = ChatOpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1",
    model="llama-3.1-8b-instant",
    temperature=0
)


def mood_detection_agent(state):

    metrics = state["combined_metrics"]

    questions = state.get("behavior_questions", [])
    answers = state.get("behavior_answers", [])

    qa_pairs = []

    for q, a in zip(questions, answers):
        qa_pairs.append(f"{q} -> {a}")

    qa_text = "\n".join(qa_pairs)

    prompt = PromptTemplate.from_template(MOOD_ANALYSIS_PROMPT)

    chain = prompt | llm

    response = chain.invoke(
        {
            "metrics": metrics,
            "answers": qa_text
        }
    )

    content = response.content

    try:
        data = json.loads(content)
    except:
        data = {
            "mood": "unknown",
            "confidence": 0.0,
            "summary": content
        }

    print("\nDetected Mood:", data)

    state["mood"] = data.get("mood")
    state["mood_confidence"] = data.get("confidence")
    state["mood_summary"] = data.get("summary")

    return state