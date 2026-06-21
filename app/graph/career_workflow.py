from langgraph.graph import StateGraph, END

from app.graph.state import CareerState

from app.agents.resume_agent import resume_agent
from app.agents.ats_agent import ats_agent
from app.agents.skill_gap_agent import skill_gap_agent
from app.agents.roadmap_agent import roadmap_agent
from app.agents.interview_agent import interview_agent
from app.agents.report_agent import report_agent

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
    "roadmap_agent",
    roadmap_agent
)

graph.add_node(
    "interview_agent",
    interview_agent
)

graph.add_node(
    "report_agent",
    report_agent
)

graph.set_entry_point(
    "resume_agent"
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
    "roadmap_agent"
)

graph.add_edge(
    "roadmap_agent",
    "interview_agent"
)

graph.add_edge(
    "interview_agent",
    "report_agent"
)

graph.add_edge(
    "report_agent",
    END
)

career_workflow = graph.compile()