from app.graph.career_workflow import career_workflow

result = career_workflow.invoke({

    "resume": """
    Python
    Machine Learning
    Deep Learning
    TensorFlow
    """,

    "job_description": """
    Looking for AI Engineer with
    AWS
    Docker
    LangGraph
    RAG
    """,

    "role": "AI ML Engineer",

    "experience": "1 Year"
})

print(result.keys())

print("\nATS Score:")
print(result["ats_score"])

print("\nMissing Skills:")
print(result["skill_gap"]["missing_skills"])

print("\nRoadmap Generated:")
print(result["roadmap"][:500])

print("\nFinal Report Generated:")
print(result["final_report"][:500])