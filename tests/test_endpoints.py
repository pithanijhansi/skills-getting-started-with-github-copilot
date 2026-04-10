def test_root_redirects_to_static_index(client):
    response = client.get("/", follow_redirects=False)

    assert response.status_code == 307
    assert response.headers["location"] == "/static/index.html"


def test_get_activities_returns_seeded_activities(client):
    response = client.get("/activities")

    assert response.status_code == 200
    payload = response.json()

    assert "Chess Club" in payload
    assert "Programming Class" in payload
    assert "participants" in payload["Chess Club"]
    assert payload["Chess Club"]["max_participants"] == 12
