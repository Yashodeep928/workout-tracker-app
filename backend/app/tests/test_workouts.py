# Helper function to create a user for workout-related tests
def create_test_user(client):
    response = client.post(
        "/users/",
        json={
            "name": "Workout User",
            "email": "workoutuser@example.com",
        },
    )

    return response.json()


# Test creating a workout successfully
def test_create_workout(client):
    # First create a user because workout needs a valid user_id
    user = create_test_user(client)

    response = client.post(
        "/workouts/",
        json={
            "title": "Leg Day",
            "description": "Squats and lunges",
            "user_id": user["id"],
        },
    )

    assert response.status_code == 201

    data = response.json()
    assert data["title"] == "Leg Day"
    assert data["description"] == "Squats and lunges"
    assert data["user_id"] == user["id"]
    assert "id" in data


# Test creating workout with invalid user_id should fail
def test_create_workout_user_not_found(client):
    response = client.post(
        "/workouts/",
        json={
            "title": "Chest Day",
            "description": "Bench press",
            "user_id": 9999,
        },
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"


# Test getting all workouts
def test_get_all_workouts(client):
    # Create user
    user = create_test_user(client)

    # Create a workout
    client.post(
        "/workouts/",
        json={
            "title": "Back Day",
            "description": "Rows and pull-downs",
            "user_id": user["id"],
        },
    )

    response = client.get("/workouts/")

    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["title"] == "Back Day"


# Test getting workouts for a specific user
def test_get_workouts_by_user(client):
    # Create user
    user = create_test_user(client)

    # Create workouts for that user
    client.post(
        "/workouts/",
        json={
            "title": "Push Day",
            "description": "Pushups and dips",
            "user_id": user["id"],
        },
    )

    client.post(
        "/workouts/",
        json={
            "title": "Pull Day",
            "description": "Pullups and curls",
            "user_id": user["id"],
        },
    )

    response = client.get(f"/workouts/user/{user['id']}")

    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 2


# Test getting workouts for non-existing user should fail
def test_get_workouts_by_user_not_found(client):
    response = client.get("/workouts/user/9999")

    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"