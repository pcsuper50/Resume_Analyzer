from app.agents.resume_agent import resume_agent

sample_state = {
    "resume": """
    Python
    Machine Learning
    Deep Learning
    TensorFlow
    """
}

result = resume_agent(sample_state)

print(result)