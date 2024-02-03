import requests
import pytest

API_URL = 'http://localhost:5000'

def test_get_data_successful():
    response = requests.get(f'{API_URL}/api/data')
    assert response.status_code == 200
    assert response.json()["message"] == "Hello, API!"

@pytest.mark.parametrize("endpoint, expected_status", [("/api/data", 200), ("/api/nonexistent", 200)])
def test_api_endpoints(endpoint, expected_status):
    response = requests.get(f'{API_URL}{endpoint}')
    assert response.status_code == expected_status