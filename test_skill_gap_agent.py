from app.agents.skill_gap_agent import skill_gap_agent

state = {

    "resume": """
    Python
    Machine Learning
    TensorFlow
    Pandas
    NumPy
    """,

    "job_description": """
    Looking for AI Engineer with
    Python
    TensorFlow
    LangChain
    LangGraph
    Docker
    AWS
    RAG
    """
}

result = skill_gap_agent(state)

print(result)