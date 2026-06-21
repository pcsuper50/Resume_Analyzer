import streamlit as st
from app.resume_parser.parser import extract_resume_text
from app.resume_parser.ai_analyzer import analyze_resume
from app.resume_parser.ats_score import calculate_ats_score
from app.resume_parser.skill_gap import skill_gap_analysis
from app.interview.interview_generator import generate_interview_questions
from app.interview.resume_interview import generate_resume_based_questions
#from app.utils.llm_service import analyze_resume
from app.chatbot.career_chatbot import career_chat
from app.utils.pdf_utils import extract_text_from_pdf
from app.rag.rag_engine import (
    create_vectorstore,
    ask_rag
)
from app.graph.career_workflow import career_workflow
from app.utils.pdf_report import generate_pdf_report
import re

# Common technical skills database
# SKILLS_DB = [

#     # Programming
#     "python",
#     "java",
#     "c++",
#     "javascript",
#     "sql",

#     # ML / AI
#     "machine learning",
#     "deep learning",
#     "tensorflow",
#     "pytorch",
#     "nlp",
#     "transformers",
#     "llm",
#     "genai",

#     # Data
#     "pandas",
#     "numpy",
#     "matplotlib",
#     "seaborn",

#     # Backend
#     "fastapi",
#     "flask",
#     "django",

#     # Cloud / DevOps
#     "aws",
#     "docker",
#     "kubernetes",
#     "jenkins",
#     "ansible",
#     "linux",

#     # Databases
#     "mysql",
#     "mongodb",
#     "postgresql",

#     # GenAI Tools
#     "langchain",
#     "langgraph",
#     "chromadb",
#     "faiss",
#     "rag"
# ]


def extract_skills(text):

    text = text.lower()

    found_skills = []

    # for skill in SKILLS_DB:

    #     pattern = r"\b" + re.escape(skill) + r"\b"

    #     if re.search(pattern, text):

    #         found_skills.append(skill)

    # return list(set(found_skills))


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

st.set_page_config(
    page_title="AI Career Copilot",
    page_icon="🚀",
    layout="wide"
)

# st.title("🚀 AI Career Copilot")

# st.write("Your AI-powered career assistant")

st.title("🚀 AI Career Copilot")

st.markdown("""
Your Personal AI Career Assistant

✅ Resume Analysis

✅ ATS Optimization

✅ Skill Gap Detection

✅ Interview Preparation

✅ Career Roadmap Generation

✅ AI Career Chatbot

✅ RAG Knowledge Base
""")

st.sidebar.title("🚀 AI Career Copilot")

st.sidebar.markdown("---")

menu = st.sidebar.selectbox(
    "Select Feature",
    [
        "Home",
        "Resume Analyzer",
        "Interview Prep",
        "Career Chatbot",
        "RAG Knowledge Base",
        "Career Report (LangGraph)"
    ]
)

st.sidebar.markdown("---")

st.sidebar.success(
    "Built with LangGraph + Gemini + FAISS"
)

if menu == "🏠 Home":
    st.header("🚀 Welcome to AI Career Copilot")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Resume Analysis",
            "AI Powered"
        )

    with col2:
        st.metric(
            "ATS Scoring",
            "Semantic Matching"
        )

    with col3:
        st.metric(
            "Interview Prep",
            "GenAI Based"
        )

    st.markdown("---")

    st.info("""
    🎯 Upload your resume

    🎯 Check ATS compatibility

    🎯 Find missing skills

    🎯 Generate interview questions

    🎯 Chat with AI

    🎯 Build your AI career roadmap
    """)

elif menu == "📄 Resume Analyzer":
    st.header("📄 Resume Analyzer")

    uploaded_file = st.file_uploader(
        "Upload Your Resume (PDF)",
        type=["pdf"]
    )

    if uploaded_file is not None:

        st.success("Resume Uploaded Successfully ✅")

        # Extract Resume Text
        resume_text = extract_resume_text(uploaded_file)

        st.subheader("Extracted Resume Text")

        st.text_area(
            "Resume Content",
            resume_text,
            height=300
        )

        # =====================================
        # AI Resume Analysis
        # =====================================

        if st.button("Analyze Resume"):

            with st.spinner("Analyzing Resume..."):

                analysis = analyze_resume(resume_text)

                st.subheader("🤖 AI Resume Analysis")

                st.write(analysis)

        # =====================================
        # JOB DESCRIPTION INPUT
        # =====================================

        st.subheader("📌 Paste Job Description")

        job_description = st.text_area(
            "Enter Job Description",
            height=250
        )
        
        if st.button("Generate Resume-Based Interview Questions"):
            with st.spinner("Generating Personalized Questions..."):
                result = generate_resume_based_questions(
                    resume_text
                    )
                st.subheader("🎯 Resume-Based Interview Questions"
                    )
                st.write(result)
        # =====================================
        # ATS SCORE
        # =====================================

        if st.button("Calculate ATS Score"):
            

            if job_description.strip() == "":

                st.warning("Please Enter Job Description")

            else:

                with st.spinner("Calculating ATS Score..."):

                    ats_score = calculate_ats_score(
                        resume_text,
                        job_description
                    )

                    st.subheader("🎯 ATS Match Score")

                    st.metric(
                        label="ATS Score",
                        value=f"{ats_score}%"
                    )

                    # Score Feedback

                    if ats_score >= 80:

                        st.success("Excellent Resume Match 🚀")

                    elif ats_score >= 60:

                        st.warning("Good Match 👍")

                    else:

                        st.error("Low Match ❌ Improve Resume")
            # =====================================
            result = skill_gap_analysis(
                        resume_text,
                        job_description
                    )

            st.subheader("✅ Matched Skills")

            if result["matched_skills"]:

                        st.success(
                            ", ".join(result["matched_skills"])
                        )

            else:

                st.warning("No matching skills found")

                st.subheader("❌ Missing Skills")

                if result["missing_skills"]:

                        st.error(
                            ", ".join(result["missing_skills"])
                        )

                else:

                        st.success("No missing skills 🎉")



elif menu == "💼 Job Search":
    st.header("Job Search")

elif menu == "🎯 Interview Prep":
    st.header("🎯 AI Interview Preparation")

    role = st.text_input(
        "Target Role",
        placeholder="AI Engineer"
    )

    experience = st.selectbox(
        "Experience",
        [
            "Fresher",
            "1 Year",
            "2 Years",
            "3+ Years",
            "5+ Years"
        ]
    )

    if st.button("Generate Questions"):

        if role.strip() == "":

            st.warning("Please enter a role")

        else:

            with st.spinner("Generating Interview Questions..."):

                result = generate_interview_questions(
                    role,
                    experience
                )

                st.write(result)
    

elif menu == "🤖 Career Chatbot":

    st.title("🤖 AI Career Coach")

    st.caption(
        "Ask anything about AI, ML, Resume, Interview, Career Growth."
    )

    user_query = st.text_area(
        "Ask your career question"
    )

    if st.button("Ask AI"):

        with st.spinner("Thinking..."):

            response = career_chat(user_query)

            st.write(response)
elif menu == "📚 RAG Knowledge Base":

    st.title("📚 RAG Knowledge Base")

    pdf = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )

    if pdf:

        text = extract_text_from_pdf(pdf)

        vectorstore = create_vectorstore(text)
        st.success(
        "Knowledge Base Created Successfully ✅"
            )

        question = st.text_input(
            "Ask a question"
        )

        if st.button("Ask"):

            answer = ask_rag(
                vectorstore,
                question
            )

            st.write(answer)

elif menu == "Career Report (LangGraph)":

    st.title("🚀 AI Career Report")

    uploaded_file = st.file_uploader(
        "Upload Resume",
        type=["pdf"]
    )

    job_description = st.text_area(
        "Paste Job Description"
    )

    role = st.text_input(
        "Target Role",
        value="AI ML Engineer"
    )

    experience = st.selectbox(
        "Experience",
        [
            "Fresher",
            "1 Year",
            "2 Years",
            "3 Years",
            "5+ Years"
        ]
    )

    if st.button("Generate Complete Career Report"):

        if uploaded_file is None:

            st.warning("Please upload resume")

        elif job_description.strip() == "":

            st.warning("Please enter job description")

        else:

            with st.spinner(
                "Generating Career Report..."
            ):

                resume_text = extract_resume_text(
                    uploaded_file
                )

                result = career_workflow.invoke({

                    "resume": resume_text,

                    "job_description":
                    job_description,

                    "role": role,

                    "experience":
                    experience

                })

                st.success(
                    "Career Report Generated"
                )

                st.subheader(
                    "📄 Resume Analysis"
                )

                st.write(
                    result["resume_analysis"]
                )

                st.subheader(
                    "🎯 ATS Score"
                )

                st.metric(
                    "ATS Score",
                    f"{result['ats_score']}%"
                )

                st.subheader(
                    "📌 Skill Gap Analysis"
                )

                st.write(
                    result["skill_gap"]
                )

                st.subheader(
                    "🗺️ Learning Roadmap"
                )

                st.write(
                    result["roadmap"]
                )

                st.subheader(
                    "🎤 Interview Questions"
                )

                st.write(
                    result["interview_questions"]
                )

                st.subheader(
                    "📋 Final Career Report"
                )

                st.write(
                    result["final_report"]
                )

                pdf_file = generate_pdf_report(
                result,
                "career_report.pdf"
                )

                with open(
                    pdf_file,
                    "rb"
                ) as file:

                   st.download_button(
                        label="📥 Download PDF Report",
                        data=file,
                        file_name="career_report.pdf",
                        mime="application/pdf"
                    )