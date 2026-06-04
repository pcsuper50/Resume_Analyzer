import os

from dotenv import load_dotenv
# from mistralai.client import MistralClient
# from mistralai import Mistral
# from mistralai.models.chat_completion import ChatMessage
# from app.utils.gemini_helper import get_gemini_response

# load_dotenv()

# api_key = os.getenv("MISTRAL_API_KEY")

# client = MistralClient(api_key=api_key)


# def generate_interview_questions(role, experience):

#     prompt = f"""
#     Act as a senior interviewer.

#     Generate:

#     1. Top 30 Technical Questions
#     2. Top 10 Scenario Based Questions
#     3. Top 10 HR Questions
#     4. Detailed Answers

#     Role: {role}
#     Experience: {experience}
#     """

#     response = client.chat(
#         model="mistral-small-latest",
#         messages=[
#             ChatMessage(
#                 role="user",
#                 content=prompt
#             )
#         ]
#     )

#     return response.choices[0].message.content
from app.utils.gemini_helper import get_gemini_response
def generate_interview_questions(role, experience):

    prompt = f"""
    Generate interview questions for:

    Role: {role}
    Experience: {experience}

    Include:
    - Technical Questions
    - Scenario Questions
    - HR Questions
    - Detailed Answers
    """

    return get_gemini_response(prompt)