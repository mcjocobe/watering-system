import pytest
import time
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn
import requests
import threading

@pytest.fixture
def mock_pi_pico():
    app = FastAPI()

    @app.get("/check")
    def check():
        print("CHECKED")

    @app.post("/relay1/{state}")
    async def relay(state: str):
        return HTMLResponse(
            content=f"<body>Relay Status: {state}</body>"
        )
    config = uvicorn.Config(app, host="0.0.0.0", port=8765, log_level="error", ws="wsproto")
    server = uvicorn.Server(config)

    thread = threading.Thread(target=server.run, daemon=True)
    thread.start()

    for _ in range(20):
        try:
            requests.get("http://localhost:8765/check", timeout=0.5)
            break
        except requests.exceptions.ConnectionError:
            time.sleep(0.1)
    yield

    server.should_exit = True
    thread.join(timeout=5)

def test_set_state(mock_pi_pico):
    response = requests.post("http://localhost:8765/relay1/on")
    assert response.status_code == 200
    assert "on" in response.text