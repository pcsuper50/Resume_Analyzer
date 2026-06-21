def planner_agent(state):

    query = state["query"].lower()

    if "resume" in query:
        task = "resume"

    elif "ats" in query:
        task = "ats"

    elif "skill" in query:
        task = "skill_gap"

    elif "interview" in query:
        task = "interview"

    elif "roadmap" in query:
        task = "roadmap"

    else:
        task = "career"

    return {"task": task}