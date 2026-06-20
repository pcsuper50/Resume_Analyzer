from app.graph.agentic_graph import agentic_graph

result = agentic_graph.invoke({

    "query": "Generate interview questions for AI Engineer",

    "role": "AI Engineer",

    "experience": "4 Years"
})

print(result)