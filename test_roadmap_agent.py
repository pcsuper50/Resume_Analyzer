from app.graph.agentic_graph import agentic_graph

result = agentic_graph.invoke({
    "query": "roadmap",
    "role": "AI ML Engineer",
    "skill_gap": {
        "missing_skills": [
            "langgraph",
            "docker",
            "aws"
        ]
    }
})

print(result)