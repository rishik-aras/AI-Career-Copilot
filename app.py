import re
import streamlit as st
from dotenv import load_dotenv
from pypdf import PdfReader

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

# Load API Key
load_dotenv()

# Gemini Model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.3
)

st.set_page_config(page_title="AI Career Copilot", page_icon="🚀")

st.title("AI Career Copilot")

# Upload Resume
uploaded_file = st.file_uploader(
    " Upload Your Resume",
    type="pdf"
)

# Choose Career Goal
career_goal = st.selectbox(
    " Target Role",
    [
        "AI Engineer",
        "ML Engineer",
        "Data Scientist",
        "Generative AI Engineer",
        "Python Developer"
    ]
)

# Generate Report
if uploaded_file and st.button("Analyze Resume"):

    # Read PDF
    reader = PdfReader(uploaded_file)

    resume_text = ""

    for page in reader.pages:
        text = page.extract_text()

        if text:
            resume_text += text

    st.success("Resume Uploaded Successfully")

    prompt = PromptTemplate(
        input_variables=["resume", "career_goal"],
        template="""
You are a Senior HR Recruiter and AI Career Mentor.

Analyze the following resume.

Resume:
{resume}

Target Role:
{career_goal}

Return ONLY in this format.

# ATS Score
(Give score out of 100)

# Strengths
(Bullet points)

# Weaknesses
(Bullet points)

# Missing Skills
(Bullet points)

# Personalized Learning Roadmap
(4-week roadmap)

# Suggested AI Projects
(3 projects)

# Interview Questions
(5 questions)

# Resume Summary
(Rewrite professionally)
"""
    )

    final_prompt = prompt.format(
        resume=resume_text,
        career_goal=career_goal
    )

    response = llm.invoke(final_prompt)

    st.divider()

    st.header(" AI Career Report")

    st.markdown(response.content)