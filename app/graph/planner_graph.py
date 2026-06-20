from langgraph.graph import StateGraph

from app.graph.state import CareerState

from app.agents.planner_agent import planner_agent
from app.agents.rag_agent import rag_agent

graph = StateGraph(CareerState)

graph.add_node(
    "planner",
    planner_agent
)

graph.add_node(
    "rag",
    rag_agent
)

graph.set_entry_point("planner")

graph.add_edge(
    "planner",
    "rag"
)

planner_graph = graph.compile()