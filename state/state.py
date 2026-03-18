from typing import TypedDict, List, Dict, Optional


class AstronautState(TypedDict):

    facial_metrics: Optional[Dict]
    speech_metrics: Optional[Dict]

    combined_metrics: Optional[Dict]

    behavior_questions: Optional[List[str]]
    behavior_answers: Optional[List[str]]

    mood: Optional[str]
    mood_confidence: Optional[float]
    mood_summary: Optional[str]

    research_suggestions: Optional[List[str]]

    support_message: Optional[str]