from google.adk.agents import Agent
from tools.flashcard_maker_tool import create_flashcards

root_agent = Agent(
    model='gemini-2.0-flash-001',
    name='flashcard_agent_v1',
    description='A helpful assistant that generates flashcards to study from',
    instruction=(
        "When given a textbook excerpt or study notes, call 'flashcard_maker_tool'. "
        "Produce flashcards with the questions and answers. "
        "The questions are a variety of fill in the blank, vocabulary, and short-answer questions. "
        "They should be simplified as much as possible, like how a flashcard would be. "
        "If the tool returns an error, politely inform the user."
    ),
    tools = [create_flashcards]
)
