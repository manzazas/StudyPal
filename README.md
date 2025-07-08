# StudyPal 🧠📚  
An AI-powered study assistant that helps you **summarize notes, generate quizzes, create flashcards, and build day-by-day study plans**—all in one place.

---

## 🚀 Features

| Agent             | Functionality                                           |
|------------------|---------------------------------------------------------|
| **Summarizer**    | Summarizes long notes or textbook excerpts             |
| **Quiz Maker**    | Creates multiple-choice questions with answers         |
| **Flashcard Maker**| Generates simple Q&A flashcards for memorization     |
| **Planner**        | Builds a personalized study schedule leading to exams |
| **Root Agent**     | Routes requests to the correct tool-based agent       |

---

## 🗂️ Project Structure
StudyPal/
├── agents/ # Each agent folder contains its own ADK setup
│ ├── summarizer_agent/
│ ├── quiz_agent/
│ ├── flashcard_agent/
│ ├── planner_agent/
│ └── studypal_root/ (WOrk in Progress)
├── tools/ # Reusable logic used by agents
│ ├── summarizer_tool.py
│ ├── quiz_tool.py
│ ├── flashcard_maker_tool.py
│ ├── parse_exam_schedule.py
│ └── planner_tool.py
├── tests/ # Unit tests for individual tools
├── requirements.txt
└── README.md


---

## 💻 Getting Started

### 1. Clone and set up virtual environment

```bash
git clone https://github.com/manzazas/StudyPal.git
cd StudyPal
python -m venv .venv

# For Windows (PowerShell)
.\\.venv\\Scripts\\Activate.ps1

# For macOS/Linux
source .venv/bin/activate
