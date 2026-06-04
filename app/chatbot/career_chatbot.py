from app.utils.gemini_helper import get_gemini_response


def career_chat(user_query):

    prompt = f"""
    You are an expert AI Career Coach.

    Help users with:

    - Career guidance
    - Resume improvement
    - Interview preparation
    - Learning roadmap
    - Job search strategy
    - GenAI career advice

    User Question:

    {user_query}
    """

    return get_gemini_response(prompt)