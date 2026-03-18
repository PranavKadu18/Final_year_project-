import numpy as np
from fer import FER

from utils.video_capture import capture_video_frames


def facial_metrics_agent(state):

    frames = capture_video_frames()

    detector = FER(mtcnn=True)

    blink_counter = 0
    emotion_scores = []

    total_faces = 0

    for frame in frames:

        results = detector.detect_emotions(frame)

        if len(results) == 0:
            continue

        face = results[0]

        emotions = face["emotions"]

        emotion_scores.append(emotions)

        total_faces += 1

        # crude blink estimation
        if emotions.get("neutral", 0) > 0.7:
            blink_counter = blink_counter + 1

    if total_faces == 0:
        facial_tension = 0.0
    else:

        anger = np.mean([e["angry"] for e in emotion_scores])
        fear = np.mean([e["fear"] for e in emotion_scores])

        facial_tension = float((anger + fear) / 2)

    blink_rate = blink_counter

    fatigue_indicator = min(blink_rate / 30, 1)

    eye_focus = float(1 - fatigue_indicator)

    facial_metrics = {
        "facial_tension": facial_tension,
        "blink_rate": blink_rate,
        "eye_focus": eye_focus,
        "fatigue_indicator": fatigue_indicator,
    }

    print("\nFacial Metrics:", facial_metrics)

    state["facial_metrics"] = facial_metrics

    return state