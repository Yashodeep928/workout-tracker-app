from fastapi.testclient import TestClient

from app.main import app


# Create test client for API testing
client = TestClient(app)


# Helper function to create a user for workout tests
def create_test_user():
    response = client.post(
        "/users/",
        json={
            "name": "Workout Test User",
            "email": "workout_test_user_day5@example.com"
        },
    )

    # If user already exists, fetch all users and find it
    if response.status_code == 201:
        return response.json()["id"]

    users_response = client.get("/users/")
    users = users_response.json()

    for user in users:
        if user["email"] == "workout_test_user_day5@example.com":
            return user["id"]

    return None


# Test workout creation
def test_create_workout():
    user_id = create_test_user()

    response = client.post(
        "/workouts/",
        json={
            "title": "Leg Day",
            "description": "Squats and lunges",
            "user_id": user_id,
        },
    )

    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Leg Day"
    assert data["description"] == "Squats and lunges"
    assert data["user_id"] == user_id


# Test get all workouts
def test_get_all_workouts():
    response = client.get("/workouts/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


# Test get workouts by user
def test_get_workouts_by_user():
    user_id = create_test_user()

    response = client.get(f"/workouts/user/{user_id}")

    assert response.status_code == 200
    assert isinstance(response.json(), list)