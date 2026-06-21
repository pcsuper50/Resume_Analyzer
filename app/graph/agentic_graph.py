from langgraph.graph import StateGraph, END

from app.graph.state import CareerState
from app.graph.router import route_task

from app.agents.planner_agent import planner_agent
from app.agents.resume_agent import resume_agent
from app.agents.ats_agent import ats_agent
from app.agents.skill_gap_agent import skill_gap_agent
from app.agents.interview_agent import interview_agent
from app.agents.rag_agent import rag_agent
#from app.agents.career_roadmap_agent import career_roadmap_agent
from app.agents.roadmap_agent import roadmap_agent

graph = StateGraph(CareerState)

# Nodes
graph.add_node("planner", planner_agent)

graph.add_node("resume_agent", resume_agent)

graph.add_node("ats_agent", ats_agent)

graph.add_node("skill_gap_agent", skill_gap_agent)

graph.add_node("interview_agent", interview_agent)

# graph.add_node(
#     "career_roadmap_agent",
#     career_roadmap_agent
# )

graph.add_node(
    "roadmap_agent",
    roadmap_agent
)

graph.add_node("rag_agent", rag_agent)

# Entry
graph.set_entry_point("planner")

# Conditional Routing
graph.add_conditional_edges(
    "planner",
    route_task,
    {
        "resume_agent": "resume_agent",
        "ats_agent": "ats_agent",
        "skill_gap_agent": "skill_gap_agent",
        "interview_agent": "interview_agent",
        "roadmap_agent": "roadmap_agent",
        "rag_agent": "rag_agent",
        
    }
)

# End Nodes
graph.add_edge("resume_agent", END)

graph.add_edge("ats_agent", END)

graph.add_edge("skill_gap_agent", END)

graph.add_edge("interview_agent", END)

# graph.add_edge(
#     "career_roadmap_agent",
#     END
# )

graph.add_edge("rag_agent", END)

graph.add_edge(
    "roadmap_agent",
    END
)

agentic_graph = graph.compile()