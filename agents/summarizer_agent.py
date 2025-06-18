from google.adk.agents import Agent
from tools.summarizer_tool import get_summary
AGENT_MODEL = "gemini-2.0-flash"

summarizer_agent = Agent(
    name = "summarizer_agent_v1",
    model = AGENT_MODEL,
    description = "Summarizes study notes and text excerpts into bullet points",
    instruction = ("You are great at breaking down complex information. "
        "When a user enters their notes, break them down and explain them clearly. "
        "When a user enters a textbook or slideshow excerpt, simplify it as if explaining to a high schooler. "
        "Use the 'get_summary' tool to generate the summary. "
        "If the tool returns an error, inform the user politely. "
        "If successful, present the summary with clear titles and bullet points."),


    tools = [get_summary], 
    
)
print(f"Agent: {summarizer_agent.name} created using model: {AGENT_MODEL}.")