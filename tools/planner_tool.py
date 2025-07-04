
import random
from datetime import date, timedelta
def generate_random_rgb():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)




def generate_plan(exam_schedule: dict ) -> list:
    """
    Creates a comphrensive study plan taking into account the time until the exams and the topics covered

    Args:
        exam_schedule(dict): contains the subject (str)as a key, and a list containing time left (int) and topics covered (str) as the values

   Returns:
        list: A list of dictionaries where each entry represents a day. Each dictionary has:
              - 'day' (str): the date
              - 'tasks' (list): a list of tasks, each with subject, color, study_duration, and study_details

   """
    
    planByDay = {} #Key: date, Value: list of tasks
    subject_colors = {} #Key: subject, Value: color

    for subject, [days_left, topics] in exam_schedule.items():
        subject_colors[subject] = generate_random_rgb() ##assign each subject a color to be implemented later
        for i in range(0,days_left):
            study_date= (date.today() + timedelta(days = i)).isoformat()
            task = {
                "subject": subject,
                "color": subject_colors[subject],
                "study_duration":random.choice([
                    "30 minutes", "45 minutes", "1 hour", "1.5 hours", "2 hours"
                ]),  
                "study_details": topics,

            }
            if (study_date not in planByDay):
                planByDay[study_date] = []
            planByDay[study_date].append(task)
            
            

    final_plan = []
    for dates in sorted(planByDay):
        final_plan.append({"day":dates, "tasks": planByDay[dates] })
    return final_plan

            





