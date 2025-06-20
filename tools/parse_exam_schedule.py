import re
def parse_exam(exams_info: str) -> dict:
    """
    Parses exam information to extract the subject, time left, and topics of each exam

    Args:
        exams (str): "My history exam is in 7 days and covers ww2 and ww1, my calculus exam is in 10 days and covers integration and taylors theorem

    Result:
        dict: {"History": (7, "ww1, ww2"), "Calculus": (10, "integration, taylors theorem") }
    
    """
   
    
   
    exam_schedule = {}
    pattern = r"(\w+)\s+exam\s+is\s+in\s+(\d+)\s+days\s+and\s+covers\s+(.+?)" #this pattern finds the subject word, time left, and topics covered
    matches = re.findall(pattern,exams_info)

    for subject, date_until, topics in matches:

        subject = subject.capitalize()
        date_until = int(date_until)
        topics = topics.strip()

        exam_schedule[subject] = [date_until,topics]
    

    return exam_schedule #RETURNS dict