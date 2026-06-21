from app.utils.gemini_helper import get_gemini_response

def roadmap_agent(state):

    role = state.get("role", "AI ML Engineer")

    missing_skills = state.get(
        "skill_gap",
        {}
    ).get(
        "missing_skills",
        []
    )

    prompt = f"""
    Create a 6 month learning roadmap.

    Target Role:
    {role}

    Missing Skills:
    {missing_skills}

    Include:

    1. Month-wise roadmap
    2. Courses
    3. Projects
    4. Certifications
    5. Interview preparation plan
    """

    roadmap = get_gemini_response(prompt)

    return {
        "roadmap": roadmap
    }