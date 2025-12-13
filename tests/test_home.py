def test_home(client):

    response = client.get('/')

    assert response.status_code == 200
    assert response.json["status"] == "online"
    assert "msg" in response.json