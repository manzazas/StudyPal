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
    pattern = r"([A-Za-z ]+?) exam is in (\d+) days(?: and covers ([^\.]+))?" #this pattern finds the subject word, time left, and topics covered
    matches = re.findall(pattern, exams_info, flags=re.IGNORECASE)


    for subject, date_until, topics in matches:

        subject = subject.capitalize()
        date_until = int(date_until)
        topics = topics.strip() if topics else " "

        exam_schedule[subject] = (date_until,topics)
    

    return exam_schedule #RETURNS dict