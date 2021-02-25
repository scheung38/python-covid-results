import main


def test_1():
    client = main.app.test_client()
    response = client.get('/')
    assert b"hello world" in response.data
