# 🚀 AI Career Copilot

> An AI-powered resume analysis application that helps students and job seekers evaluate their resumes, improve ATS compatibility, identify skill gaps, and prepare for interviews using Google Gemini.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red)
![Gemini](https://img.shields.io/badge/Google-Gemini%202.5%20Flash-4285F4)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📖 Overview

AI Career Copilot is an intelligent career assistant that analyzes uploaded resumes and generates a personalized career report using Google's Gemini Large Language Model.

The application helps users understand how their resume aligns with their desired career path by providing ATS evaluation, strengths, weaknesses, missing skills, interview preparation, and a personalized learning roadmap.

---

## ✨ Features

- 📄 Upload Resume (PDF)
- 🤖 AI Resume Analysis
- 📊 ATS Score Evaluation
- 💪 Resume Strength Analysis
- ⚠️ Weakness Identification
- 🧠 Missing Skill Detection
- 🗺️ Personalized 4-Week Learning Roadmap
- 💡 AI Project Recommendations
- 🎤 Interview Question Generation
- 📝 Professional Resume Summary
- 🎯 Career-Specific Feedback

---

## 🖥️ Demo Workflow

```text
Upload Resume (PDF)
        │
        ▼
Extract Resume Text
        │
        ▼
Choose Target Role
        │
        ▼
Google Gemini Analysis
        │
        ▼
Generate AI Career Report
```

---

## 🛠 Tech Stack

| Category | Technologies |
|----------|--------------|
| Frontend | Streamlit |
| Language | Python |
| AI Model | Google Gemini 2.5 Flash |
| Prompt Engineering | LangChain |
| PDF Processing | PyPDF |
| Environment | python-dotenv |

---

## 📂 Project Structure

```
AI-Career-Copilot/
│
├── app.py
├── .env
├── requirements.txt
├── README.md
└── assets/
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/AI-Career-Copilot.git

cd AI-Career-Copilot
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Mac/Linux

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file.

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

The application will launch in your browser.

---

## 📄 Generated Career Report

After uploading a resume, the application generates:

- ATS Score
- Resume Strengths
- Weaknesses
- Missing Skills
- Personalized Learning Roadmap
- AI Project Suggestions
- Interview Questions
- Professional Resume Summary

---

## 🎯 Supported Career Roles

- AI Engineer
- Machine Learning Engineer
- Data Scientist
- Generative AI Engineer
- Python Developer

---

## 🚀 Future Enhancements

- Resume ATS visualization dashboard
- Resume keyword highlighting
- Cover letter generation
- LinkedIn profile analysis
- AI Mock Interview
- Voice Interview Assistant
- Multi-resume comparison
- Resume version history
- Job recommendation system
- Resume improvement tracker

---

## 📚 Libraries Used

- Streamlit
- LangChain
- Google Generative AI
- PyPDF
- python-dotenv

---

## 👨‍💻 Author

**Rishik Raje Urs K S**

Artificial Intelligence & Machine Learning Undergraduate

---

## ⭐ If you found this project useful

Consider giving this repository a ⭐ on GitHub.
