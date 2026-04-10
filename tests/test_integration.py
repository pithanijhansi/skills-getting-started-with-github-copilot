def test_signup_then_unregister_same_participant(client):
    signup_response = client.post(
        "/activities/Science%20Club/signup",
        params={"email": "flowstudent@mergington.edu"},
    )
    assert signup_response.status_code == 200

    unregister_response = client.delete(
        "/activities/Science%20Club/participants",
        params={"email": "flowstudent@mergington.edu"},
    )
    assert unregister_response.status_code == 200

    activities = client.get("/activities").json()
    assert "flowstudent@mergington.edu" not in activities["Science Club"]["participants"]


def test_activities_state_isolated_per_test(client):
    activities = client.get("/activities").json()
    assert activities["Science Club"]["participants"] == []
