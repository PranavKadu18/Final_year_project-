import numpy as np


def metric_fusion_agent(state):

    facial = state["facial_metrics"]
    speech = state["speech_metrics"]

    facial_tension = facial["facial_tension"]
    fatigue = facial["fatigue_indicator"]

    voice_stress = speech["voice_stress"]

    combined_stress_score = float(
        np.mean([facial_tension, fatigue, voice_stress])
    )

    combined_metrics = {

        "speech_rate": speech["speech_rate"],
        "pitch_variation": speech["pitch_variation"],
        "voice_stress": voice_stress,

        "blink_rate": facial["blink_rate"],
        "eye_focus": facial["eye_focus"],
        "fatigue_indicator": fatigue,

        "facial_tension": facial_tension,

        "combined_stress_score": combined_stress_score
    }

    print("\nCombined Metrics:", combined_metrics)

    state["combined_metrics"] = combined_metrics

    return state