from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
from typing import List

app = FastAPI()

# Allow all origins (for development purposes)
origins = [
    "http://localhost:8080",  # Frontend address, add more if needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class DoorEvent(BaseModel):
    timestamp: str

door_events: List[DoorEvent] = []

@app.post("/door_opened")
async def door_opened(event: DoorEvent):
    event.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    door_events.append(event)
    print(f"Door opened at {event.timestamp}")
    return {"status": "success", "timestamp": event.timestamp}

@app.get("/door_events")
async def get_door_events():
    return door_events

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
