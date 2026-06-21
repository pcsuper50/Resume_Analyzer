def route_task(state):

    task = state["task"]

    if task == "resume":
        return "resume_agent"

    elif task == "ats":
        return "ats_agent"

    elif task == "skill_gap":
        return "skill_gap_agent"

    elif task == "interview":
        return "interview_agent"

    elif task == "roadmap":
        return "roadmap_agent"

    else:
        return "rag_agent"