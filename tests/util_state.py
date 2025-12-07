def get_participants(activity_name):
    from src.app import get_activity
    activity = get_activity(activity_name)
    return activity["participants"] if activity else []
