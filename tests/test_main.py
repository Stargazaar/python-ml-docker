from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the ML-Docker API"}

def test_predict_endpoint():
    # Sample data for prediction (one from each Iris class)
    test_data = {
        "data": [
            [5.1, 3.5, 1.4, 0.2],  # Setosa
            [6.7, 3.1, 4.7, 1.5],  # Versicolor
            [6.3, 3.3, 6.0, 2.5]   # Virginica
        ]
    }
    response = client.post("/predict", json=test_data)
    assert response.status_code == 200
    response_data = response.json()
    assert "predictions" in response_data
    assert isinstance(response_data["predictions"], list)
    assert len(response_data["predictions"]) == 3
    assert response_data["predictions"] == ["setosa", "versicolor", "virginica"]