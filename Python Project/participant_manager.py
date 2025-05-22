def register_student(event_list, event_name, student_name, house):
    for event in event_list:
        if event["name"] == event_name:
            participant = {
                "name": student_name,
                "house": house,
                "score": 0
            }
            event["participants"].append(participant)

def record_score(event_list, event_name, student_name, score):
    for event in event_list:
        if event["name"] == event_name:
            for p in event["participants"]:
                if p["name"] == student_name:
                    p["score"] = score
