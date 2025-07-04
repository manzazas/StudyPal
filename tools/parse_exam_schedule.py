import re
def parse_exam(exams_info: str) -> dict:
    """
    Parses exam information to extract the subject, time left, and topics of each exam
    Supports multi-word subject names and returns topics as a list.


    Args:
        exams_info (str): "My history exam is in 7 days and covers ww2 and ww1. My calculus exam is in 10 days and covers integration and taylors theorem

    Returns:
        dict: {"History": (7, ["ww1, ww2"]), "Calculus": (10, ["integration, taylors theorem"]) }
    
    """
   
    
   
    exam_schedule = {}
    pattern = r"([A-Za-z ]+?) exam is in (\d+) days(?: and covers ([^\.]+))" #this pattern finds the subject word, time left, and topics covered
    matches = re.findall(pattern, exams_info, flags=re.IGNORECASE)


    for subject, date_until, topics in matches:

        subject = subject.strip().title()
        date_until = int(date_until)
        if topics:
            parts = re.split(r'\s*(?:,|and)\s*', topics.strip())
            topics_list = [t for t in parts if t]
        else:
            topics_list = []
            exam_schedule[subject] = (date_until,topics_list)

        exam_schedule[subject] = (date_until,topics_list)
    

    return exam_schedule #RETURNS dict