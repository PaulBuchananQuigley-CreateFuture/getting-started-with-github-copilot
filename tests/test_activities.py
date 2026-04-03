from fastapi.testclient import TestClient


EXPECTED_ACTIVITIES = [
    "Chess Club",
    "Programming Class",
    "Gym Class",
    "Basketball",
    "Soccer",
    "Art Workshop",
    "Music Ensemble",
    "Science Club",
    "Debate Team",
]


def test_get_activities_returns_200(client: TestClient):
    # Arrange
    # (no special setup — seeded activities are restored by reset_activities fixture)

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200


def test_get_activities_returns_all_seeded_activities(client: TestClient):
    # Arrange
    # (no special setup — seeded activities are restored by reset_activities fixture)

    # Act
    response = client.get("/activities")

    # Assert
    data = response.json()
    for name in EXPECTED_ACTIVITIES:
        assert name in data, f"Expected activity '{name}' not found in response"


def test_get_activities_each_has_required_fields(client: TestClient):
    # Arrange
    required_fields = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")

    # Assert
    data = response.json()
    for name, activity in data.items():
        missing = required_fields - activity.keys()
        assert not missing, f"Activity '{name}' is missing fields: {missing}"
