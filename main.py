from graph.workflow import build_graph


def main():

    graph = build_graph()

    print("\n=== Astronaut Wellbeing Monitoring System ===")

    while True:

        print("\nStarting wellbeing evaluation...\n")

        result = graph.invoke(
            {
                "facial_metrics": None,
                "speech_metrics": None,
                "combined_metrics": None,
                "behavior_questions": None,
                "behavior_answers": None,
                "mood": None,
                "mood_confidence": None,
                "mood_summary": None,
                "research_suggestions": None,
                "support_message": None,
            }
        )

        print("\nMonitoring cycle complete.")

        again = input("\nRun another health check? (yes/no): ")

        if again.lower() not in ["yes", "y"]:
            print("\nSystem shutting down. Stay safe astronaut.")
            break


if __name__ == "__main__":
    main()