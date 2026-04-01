# Test creating a new user
def test_create_user(client):
    response = client.post(
        "/users/",
        json={
            "name": "Test User",
            "email": "testuser@example.com",
        },
    )

    assert response.status_code == 201

    data = response.json()
    assert data["name"] == "Test User"
    assert data["email"] == "testuser@example.com"
    assert "id" in data


# Test fetching all users
def test_get_users(client):
    # First create one user so GET has some data
    client.post(
        "/users/",
        json={
            "name": "Another User",
            "email": "anotheruser@example.com",
        },
    )

    response = client.get("/users/")

    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["email"] == "anotheruser@example.com"


# Test duplicate email should fail
def test_create_user_duplicate_email(client):
    payload = {
        "name": "Duplicate User",
        "email": "duplicate@example.com",
    }

    # First creation should succeed
    first_response = client.post("/users/", json=payload)
    assert first_response.status_code == 201

    # Second creation with same email should fail
    second_response = client.post("/users/", json=payload)
    assert second_response.status_code == 400
    assert second_response.json()["detail"] == "Email already registered"