# StudyPal 🧠📚  
An AI-powered study assistant that helps you **summarize notes, generate quizzes, create flashcards, and build day-by-day study plans**—all in one place.

---

##  Features

| Agent             | Functionality                                           |
|------------------|---------------------------------------------------------|
| **Summarizer**    | Summarizes long notes or textbook excerpts             |
| **Quiz Maker**    | Creates multiple-choice questions with answers         |
| **Flashcard Maker**| Generates simple Q&A flashcards for memorization     |
| **Planner**        | Builds a personalized study schedule leading to exams |
| **Root Agent**     | Routes requests to the correct tool-based agent       |


---

##  Getting Started
API Key & Environment Setup
This project uses the Google Generative AI API to power its AI agents. For security reasons, API keys are not included in this repository.

To run the project locally, follow these steps:

1. Obtain a Google API Key
Visit Google AI Studio

Sign in and generate your API key

2. Create a .env File
In the root of your project (next to your agent and tool folders), create a .env file:

bash
Copy
Edit
touch .env
Add the following to the file:

env
Copy
Edit
GOOGLE_API_KEY=your_google_api_key_here
GOOGLE_GENAI_USE_VERTEXAI=FALSE
✅ Important: Do not commit your .env file to GitHub. This project includes .env in .gitignore.

3. Activate Your Environment & Run the Project
bash
Copy
Edit
# Activate your virtual environment (adjust for your OS/shell)
source .venv/Scripts/activate  # Windows PowerShell
# or
source .venv/bin/activate      # macOS/Linux

# Run an agent directly
adk run summarizer_agent

# Or launch the web interface
adk web summarizer_agent
