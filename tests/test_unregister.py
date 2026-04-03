import src.app as app_module
from fastapi.testclient import TestClient


def test_unregister_returns_200_and_confirmation_message(client: TestClient):
    # Arrange
    activity_name = "Chess Club"
    email = "michael@mergington.edu"  # pre-seeded participant

    # Act
    response = client.delete(f"/activities/{activity_name}/participants", params={"email": email})

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": f"Unregistered {email} from {activity_name}"}


def test_unregister_removes_participant_from_activity(client: TestClient):
    # Arrange
    activity_name = "Chess Club"
    email = "michael@mergington.edu"  # pre-seeded participant

    # Act
    client.delete(f"/activities/{activity_name}/participants", params={"email": email})

    # Assert
    assert email not in app_module.activities[activity_name]["participants"]


def test_unregister_returns_404_for_unknown_activity(client: TestClient):
    # Arrange
    activity_name = "Underwater Basket Weaving"
    email = "michael@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity_name}/participants", params={"email": email})

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_returns_404_when_participant_not_in_activity(client: TestClient):
    # Arrange
    activity_name = "Chess Club"
    email = "notamember@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity_name}/participants", params={"email": email})

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Participant not found in this activity"
