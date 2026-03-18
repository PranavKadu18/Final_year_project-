from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

from prompts.prompts import SUPPORT_PROMPT
from config.settings import GROQ_API_KEY


llm = ChatOpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1",
    model="llama-3.1-8b-instant",
    temperature=0.7
)


def support_agent(state):

    mood = state["mood"]
    summary = state["mood_summary"]
    solutions = state["research_suggestions"]

    prompt = PromptTemplate.from_template(SUPPORT_PROMPT)

    chain = prompt | llm

    response = chain.invoke(
        {
            "mood": mood,
            "summary": summary,
            "solutions": solutions
        }
    )

    message = response.content

    print("\nSupport Message:\n")
    print(message)

    state["support_message"] = message

    return state