import pytest
from httpx import ASGITransport, AsyncClient

from main import app


@pytest.mark.asyncio
async def test_read_root():
    # Arrange
    transport = ASGITransport(app=app)

    # Act
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get("/")

    # Assert
    assert response.status_code == 200
    payload = response.json()
    assert payload["success"] is True
    assert payload["data"] == {"message": "Hello World"}
    assert "x-request-id" in response.headers
    assert payload["meta"]["request_id"] == response.headers["x-request-id"]
