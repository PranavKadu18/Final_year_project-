from langgraph.graph import StateGraph, END

from state.state import AstronautState

from agents.facial_metrics_agent import facial_metrics_agent
from agents.speech_metrics_agent import speech_metrics_agent
from agents.metric_fusion_agent import metric_fusion_agent
from agents.mood_detection_agent import mood_detection_agent
from agents.research_agent import research_agent
from agents.support_agent import support_agent
from agents.behavior_question_agent import behavior_question_agent
from agents.conversation_agent import conversation_agent


def build_graph():

    builder = StateGraph(AstronautState)

    # Add nodes (names must NOT match state keys)
    builder.add_node("facial_metrics_agent", facial_metrics_agent)
    builder.add_node("speech_metrics_agent", speech_metrics_agent)
    builder.add_node("metric_fusion_agent", metric_fusion_agent)
    builder.add_node("mood_detection_agent", mood_detection_agent)
    builder.add_node("research_agent", research_agent)
    builder.add_node("support_agent", support_agent)
    builder.add_node("behavior_question_agent", behavior_question_agent)
    builder.add_node("conversation_agent", conversation_agent)

    # Entry point
    builder.set_entry_point("facial_metrics_agent")

    # Graph flow
    builder.add_edge("facial_metrics_agent", "speech_metrics_agent")
    builder.add_edge("speech_metrics_agent", "metric_fusion_agent")
    builder.add_edge("metric_fusion_agent", "behavior_question_agent")
    builder.add_edge("behavior_question_agent", "mood_detection_agent")
    builder.add_edge("mood_detection_agent", "research_agent")
    builder.add_edge("research_agent", "support_agent")
    builder.add_edge("support_agent", "conversation_agent")
    builder.add_edge("conversation_agent", END)


    return builder.compile()