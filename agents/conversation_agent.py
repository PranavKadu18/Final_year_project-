from langchain_openai import ChatOpenAI
from config.settings import GROQ_API_KEY
from utils.tts import speak
from utils.stt import listen

llm = ChatOpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1",
    model="llama-3.1-8b-instant",
    temperature=0.7
)


def conversation_agent(state):

    mood = state["mood"]
    summary = state["mood_summary"]
    support_message = state["support_message"]

    print("\n--- Astronaut Support Chat ---\n")

    system_context = f"""
You are an emotional support companion for astronauts on long space missions.

You behave like a caring teammate or close friend.

Astronaut emotional state:
Mood: {mood}

Summary:
{summary}

Guidelines:
- Speak warmly and naturally
- Encourage positive coping
- Ask gentle questions
- Never sound like a clinical system
- Keep responses short and supportive
"""

    history = [
        {"role": "system", "content": system_context}
    ]

    print("AI:", support_message)

    while True:

        # user_input = input("\nAstronaut: ")
        user_input = listen()

        if not user_input:
            continue

        if user_input.lower() in ["bye", "exit", "quit"]:
            print("\nAI: Alright. I'm here whenever you need support. Stay safe up there.")
            break

        history.append({"role": "user", "content": user_input})

        response = llm.invoke(history)

        reply = response.content

        print("\nAI:", reply)
        speak(reply)

        history.append({"role": "assistant", "content": reply})

    return state