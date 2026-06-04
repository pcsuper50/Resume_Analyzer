import re

# Common technical skills database
SKILLS_DB = [

    # Programming
    "python",
    "java",
    "c++",
    "javascript",
    "sql",

    # ML / AI
    "machine learning",
    "deep learning",
    "tensorflow",
    "pytorch",
    "nlp",
    "transformers",
    "llm",
    "genai",

    # Data
    "pandas",
    "numpy",
    "matplotlib",
    "seaborn",

    # Backend
    "fastapi",
    "flask",
    "django",

    # Cloud / DevOps
    "aws",
    "docker",
    "kubernetes",
    "jenkins",
    "ansible",
    "linux",

    # Databases
    "mysql",
    "mongodb",
    "postgresql",

    # GenAI Tools
    "langchain",
    "langgraph",
    "chromadb",
    "faiss",
    "rag"
]


def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in SKILLS_DB:

        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text):

            found_skills.append(skill)

    return list(set(found_skills))


def skill_gap_analysis(resume_text, jd_text):

    resume_skills = extract_skills(resume_text)

    jd_skills = extract_skills(jd_text)

    missing_skills = list(
        set(jd_skills) - set(resume_skills)
    )

    matched_skills = list(
        set(jd_skills).intersection(set(resume_skills))
    )

    return {
        "resume_skills": resume_skills,
        "jd_skills": jd_skills,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }