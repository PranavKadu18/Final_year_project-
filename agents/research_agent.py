from duckduckgo_search import DDGS
import time


def research_agent(state):

    mood = state["mood"]
    summary = state["mood_summary"]

    query = f"astronaut mental health coping strategies for {mood}"

    print("\nSearching solutions...")

    suggestions = []

    try:
        # small delay helps avoid rate limits
        time.sleep(1)

        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=5))

            for r in results:
                if "title" in r:
                    suggestions.append(r["title"])

    except Exception as e:

        print("DuckDuckGo search failed:", e)

        # fallback suggestions (system continues working)
        suggestions = [
            "practice slow breathing exercises",
            "take short cognitive rest breaks",
            "perform guided mindfulness",
            "communicate regularly with crew members",
            "maintain structured daily routines",
        ]

    print("\nResearch Suggestions:", suggestions)

    state["research_suggestions"] = suggestions

    return state