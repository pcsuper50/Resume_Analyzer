from app.agents.planner_agent import planner_agent

state = {
    "query": "Prepare me for AI Engineer interview"
}

result = planner_agent(state)

print(result)