from typing import TypedDict

from langgraph.graph import StateGraph

from app.agents.interview_agent import interview_agent
from app.agents.resume_agent import resume_agent
from app.agents.ats_agent import ats_agent
from app.agents.skill_gap_agent import skill_gap_agent


class CareerState(TypedDict):

    resume: str

    job_description: str

    role: str

    experience: str

    resume_analysis: str

    ats_score: float

    skill_gap: dict

    interview_questions: str

    task: str

    query: str


graph = StateGraph(CareerState)

graph.add_node(
    "resume_agent",
    resume_agent
)

graph.add_node(
    "ats_agent",
    ats_agent
)

graph.add_node(
    "skill_gap_agent",
    skill_gap_agent
)

graph.add_node(
    "interview_agent",
    interview_agent
)

graph.add_edge(
    "resume_agent",
    "ats_agent"
)

graph.add_edge(
    "ats_agent",
    "skill_gap_agent"
)

graph.add_edge(
    "skill_gap_agent",
    "interview_agent"
)

graph.set_entry_point(
    "resume_agent"
)



career_graph = graph.compile()