from bson import ObjectId

# Sample test data for the octofit_db database

def get_test_data():
    return {
        "users": [
            {"_id": ObjectId(), "username": "john_doe", "email": "john_doe@example.com", "password": "password123"},
            {"_id": ObjectId(), "username": "jane_smith", "email": "jane_smith@example.com", "password": "password123"},
        ],
        "teams": [
            {"_id": ObjectId(), "name": "Team Alpha", "members": ["john_doe"]},
            {"_id": ObjectId(), "name": "Team Beta", "members": ["jane_smith"]},
        ],
        "activities": [
            {"_id": ObjectId(), "user": "john_doe", "activity": "Running", "duration": 30, "calories_burned": 300},
            {"_id": ObjectId(), "user": "jane_smith", "activity": "Cycling", "duration": 45, "calories_burned": 400},
        ],
        "leaderboard": [
            {"_id": ObjectId(), "user": "jane_smith", "points": 100},
            {"_id": ObjectId(), "user": "john_doe", "points": 80},
        ],
        "workouts": [
            {"_id": ObjectId(), "name": "Morning Run", "description": "A quick 5km run to start the day."},
            {"_id": ObjectId(), "name": "Evening Yoga", "description": "Relaxing yoga session to wind down."},
        ],
    }
