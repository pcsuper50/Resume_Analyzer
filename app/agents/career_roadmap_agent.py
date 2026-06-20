from app.utils.gemini_helper import get_gemini_response


def career_roadmap_agent(state):

    role = state.get("role", "")

    experience = state.get("experience", "")

    prompt = f"""
    Create a detailed career roadmap.

    Role: {role}
    Experience: {experience}

    Include:

    1. Skills to Learn
    2. Projects to Build
    3. Certifications
    4. Interview Preparation
    5. 3 Month Plan
    6. 6 Month Plan
    7. 12 Month Plan
    """

    roadmap = get_gemini_response(prompt)

    return {
        "career_roadmap": roadmap
    }