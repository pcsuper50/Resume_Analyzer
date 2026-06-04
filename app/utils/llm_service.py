from app.utils.gemini_helper import get_gemini_response


def analyze_resume(resume_text):

    prompt = f"""
    Analyze this resume and provide:

    1. Professional Summary
    2. Technical Skills
    3. Missing Skills
    4. ATS Improvement Suggestions

    Resume:
    {resume_text}
    """

    return get_gemini_response(prompt)


def generate_interview_questions(role, experience):

    prompt = f"""
    Generate:

    - 30 Technical Questions
    - 10 Scenario Questions
    - 5 HR Questions
    - Detailed Answers

    Role: {role}
    Experience: {experience}
    """

    return get_gemini_response(prompt)


def career_chat(query):

    prompt = f"""
    You are an AI Career Coach.

    User Query:
    {query}
    """

    return get_gemini_response(prompt)