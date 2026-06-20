from app.agents.ats_agent import ats_agent

state = {

    "resume": """
    Python
    Machine Learning
    TensorFlow
    Deep Learning
    """,

    "job_description": """
    Looking for Python developer
    with Machine Learning and TensorFlow
    experience.
    """
}

result = ats_agent(state)

print(result)