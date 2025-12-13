def test_register_sucess(client):

    payload = {
        "username" : "novo",
        "password" : "123456"
    }

    response = client.post(
        "/api/v1/auth/register",
        json=payload
    )

    print(response.json)

    assert response.status_code == 201
    assert response.is_json

    data = response.json

    assert "msg" in data
    #assert "user_name" in data
    #assert isinstance(data['user_name'], str)