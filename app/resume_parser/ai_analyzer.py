# import os

# from dotenv import load_dotenv

# from mistralai.client import MistralClient
# from mistralai.models.chat_completion import ChatMessage

# load_dotenv()

# api_key = os.getenv("MISTRAL_API_KEY")

# client = MistralClient(api_key=api_key)


# def analyze_resume(resume_text):

#     prompt = f"""
#     You are an expert AI Resume Analyzer.

#     Analyze this resume and provide:

#     1. Professional Summary
#     2. Technical Skills
#     3. Missing Skills
#     4. Career Suggestions
#     5. ATS Improvement Tips

#     Resume:
#     {resume_text}
#     """

#     messages = [
#         ChatMessage(
#             role="user",
#             content=prompt
#         )
#     ]

#     response = client.chat(
#         model="mistral-small-latest",
#         messages=messages
#     )

#     return response.choices[0].message.content

from app.utils.gemini_helper import get_gemini_response


def analyze_resume(resume_text):

    prompt = f"""
    Analyze this resume and provide:

    1. Professional Summary
    2. Technical Skills
    3. Missing Skills
    4. Career Suggestions
    5. ATS Improvement Tips

    Resume:
    {resume_text}
    """

    return get_gemini_response(prompt)