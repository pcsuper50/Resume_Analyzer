from app.utils.gemini_helper import get_gemini_response

def planner_agent(state):

    query = state["query"]

    prompt = f"""
You are an AI Career Planner.

User Query:
{query}

Available Agents:

resume
ats
skill_gap
interview
roadmap
career

Return ONLY a comma separated list of required agents.
"""

    task = get_gemini_response(prompt)

    return {
        "task": task.strip().lower()
    }