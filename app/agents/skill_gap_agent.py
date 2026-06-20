from app.resume_parser.skill_gap import skill_gap_analysis


def skill_gap_agent(state):

    resume = state["resume"]

    job_description = state["job_description"]

    result = skill_gap_analysis(
        resume,
        job_description
    )

    return {
        "skill_gap": result
    }