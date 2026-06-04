from app.utils.gemini_helper import get_gemini_response


def generate_resume_based_questions(resume_text):

    prompt = f"""
    You are a Senior Technical Interviewer.

    Analyze the resume below and generate:

    1. Top 35 Technical Questions
    2. Top 30 Project-Based Questions
    3. Top 15 Scenario-Based Questions
    4. Top 10 HR Questions
    5. Detailed Sample Answers

    Resume:

    {resume_text}

    Generate questions specifically based on the candidate's skills,
    projects, tools, technologies, and experience.
    """

    return get_gemini_response(prompt)