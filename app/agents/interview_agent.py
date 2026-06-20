from app.interview.interview_generator import (
    generate_interview_questions
)

from app.interview.resume_interview import (
    generate_resume_based_questions
)


def interview_agent(state):

    if state.get("resume"):

        questions = generate_resume_based_questions(
            state["resume"]
        )

    else:

        questions = generate_interview_questions(
            state["role"],
            state["experience"]
        )

    return {
        "interview_questions": questions
    }