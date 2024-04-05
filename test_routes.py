from fastapi.testclient import TestClient
from main import app


client = TestClient(app)

def test_upload_file():
    file_path = "test_file.txt"
    with open(file_path, "rb") as file:
        files = {"file": ("test_file.txt", file)}
        response = client.post("/upload/", files=files)
        assert response.status_code == 200
        data = response.json()
        assert "filename" in data
        assert "mime_type" in data