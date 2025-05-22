events = []

def create_event(name, category):
    # Simple creation logic
    event = {
        "name": name,
        "category": category,
        "participants": []
    }
    events.append(event)
