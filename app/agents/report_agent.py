from app.utils.gemini_helper import get_gemini_response

def report_agent(state):

    prompt = f"""
Create a professional career report.

Resume Analysis:
{state.get("resume_analysis", "")}

ATS Score:
{state.get("ats_score", "")}

Skill Gap:
{state.get("skill_gap", "")}

Roadmap:
{state.get("roadmap", "")}

Interview Questions:
{state.get("interview_questions", "")}

Generate a structured report.
"""

    report = get_gemini_response(prompt)

    return {
        "final_report": report
    }