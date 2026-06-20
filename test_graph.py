from app.graph.career_graph import career_graph

state = {

    "resume": """
    Python
    TensorFlow
    LangChain
    Deep Learning
    """,

    "job_description": """
    Looking for AI Engineer
    with LangGraph
    Docker
    AWS
    TensorFlow
    """
}

result = career_graph.invoke(state)

print(result.keys())