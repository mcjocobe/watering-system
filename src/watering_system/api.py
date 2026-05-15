from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from datetime import datetime
from typing import Optional
import uvicorn
from watering_system.gateway import set_relay

app = FastAPI()
 
# In-memory store: { device_id -> registration info }
devices: dict[str, dict] = {}
 
 
@app.post("/register")
async def register(request: Request):
    """Pico W calls this at boot to register its IP."""
    body = await request.json()
    device_id = body.get("id", "unknown")
    ip = request.client.host  # use actual source IP, not what device reports
 
    devices[device_id] = {
        "id": device_id,
        "ip": ip,
        "name": body.get("name", device_id),
        "last_seen": datetime.now().isoformat(),
        "boot_count": devices.get(device_id, {}).get("boot_count", 0) + 1,
    }
 
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Registered: {device_id} @ {ip}")
    return {"status": "ok", "ip": ip}
 
 
@app.get("/devices")
async def list_devices():
    return list(devices.values())

@app.post("/relay1/{status}")
async def set_relay_to_status(status):
    response = set_relay(target_ip=devices[1]["ip"], "on")
    print(response)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8765)