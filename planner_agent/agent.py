from google.adk.agents import Agent
from tools.parse_exam_schedule import parse_exam
from tools.planner_tool import generate_plan



root_agent = Agent(
    model='gemini-2.0-flash-001',
    name='planner_agent_v1',
    description='A guiding assistant that creates organzied study plans',
    instruction=(
         "When given the user's exam subjects, days until the exam, and topics covered, "
        "first call the 'parse_exam' tool to extract a structured schedule. "
        "Then call 'generate_plan' to produce a day-by-day study plan. "
        "Assign a color to each subject, determine a reasonable duration (e.g., 30 minutes to 1.5 hours), "
        "and list the specific topics to study each day. "
        "If the user provides actual exam dates instead of days left, calculate days until using datetime. "
        "If any tool returns an error, inform the user politely."),
    tools = [parse_exam,generate_plan]



    
)
