from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_unregister_participant():
    response = client.delete("/activities/Chess%20Club/participants/michael@mergington.edu")

    assert response.status_code == 200
    assert "Unregistered michael@mergington.edu" in response.json()["message"]

    activities_response = client.get("/activities")
    assert activities_response.status_code == 200
    assert "michael@mergington.edu" not in activities_response.json()["Chess Club"]["participants"]
