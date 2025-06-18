from google.adk.agents import Agent
from tools.quiz_tool import generate_quiz


root_agent = Agent(
    name='quiz_agent_v1', 
    model='gemini-2.0-flash-001',
    description="Generates practice quizes based on study notes",
    instruction= (
        "When given study notes or a text excerpt, call the quiz_tool tool"
        "Produce a list of multiple choice questions with options and answers"
        "The difficulty should vary from easy to medium to hard questions"
        "If the tool returns an error, inform the user politely. "
    
    ),
    tools = [generate_quiz],
)
