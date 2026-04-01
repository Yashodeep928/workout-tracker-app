# Test root endpoint
def test_root(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Workout Tracker API is running"}


# Test health endpoint
def test_health(client):
    response = client.get("/health/")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}