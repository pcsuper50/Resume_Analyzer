from app.resume_parser.ats_score import calculate_ats_score

def ats_agent(state):

    resume = state["resume"]

    job_description = state["job_description"]

    ats_score = calculate_ats_score(
        resume,
        job_description
    )

    return {
        "ats_score": float(ats_score)
    }