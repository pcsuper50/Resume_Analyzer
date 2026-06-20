from typing import TypedDict


class CareerState(TypedDict):

    query: str

    task: str

    resume: str

    job_description: str

    role: str

    experience: str

    resume_analysis: str

    ats_score: float

    skill_gap: dict

    interview_questions: str

    vectorstore: object

    question: str

    rag_answer: str
    
    career_roadmap: str