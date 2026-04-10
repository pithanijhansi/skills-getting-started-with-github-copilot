def test_signup_success_adds_participant(client):
    response = client.post(
        "/activities/Basketball%20Team/signup",
        params={"email": "newstudent@mergington.edu"},
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Signed up newstudent@mergington.edu for Basketball Team"

    activities = client.get("/activities").json()
    assert "newstudent@mergington.edu" in activities["Basketball Team"]["participants"]


def test_signup_unknown_activity_returns_404(client):
    response = client.post(
        "/activities/Unknown%20Club/signup",
        params={"email": "student@mergington.edu"},
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_signup_duplicate_returns_400(client):
    response = client.post(
        "/activities/Programming%20Class/signup",
        params={"email": "emma@mergington.edu"},
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Student is already signed up"


def test_signup_is_currently_case_sensitive(client):
    response = client.post(
        "/activities/Programming%20Class/signup",
        params={"email": "EMMA@mergington.edu"},
    )

    assert response.status_code == 200

    activities = client.get("/activities").json()
    assert "emma@mergington.edu" in activities["Programming Class"]["participants"]
    assert "EMMA@mergington.edu" in activities["Programming Class"]["participants"]
