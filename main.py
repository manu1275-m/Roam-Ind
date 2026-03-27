from fastapi import FastAPI
from api.trip_routes import router as trip_router
from models.travel_request import TravelRequest
from services.trip_services import plan_trip_service

app = FastAPI()

app.include_router(trip_router)

@app.get("/")
def home():
    return {"message": "RoamInd Backend Running"}

@app.post("/plan-trip")
def plan_trip(request: TravelRequest):
    return plan_trip_service(request)
import webbrowser

@app.on_event("startup")
def open_docs():
    webbrowser.open("http://127.0.0.1:8000/docs")