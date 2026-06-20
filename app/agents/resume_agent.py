from app.resume_parser.ai_analyzer import analyze_resume


def resume_agent(state):

    resume_text = state["resume"]

    result = analyze_resume(resume_text)

    return {
        "resume_analysis": result
    }