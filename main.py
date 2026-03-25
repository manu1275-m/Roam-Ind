from fastapi import FastAPI
from models.travel_request import TravelRequest
from services.trip_services import plan_trip_service

app = FastAPI()

@app.get("/")
def home():
    return {"message": "RoamInd Backend Running"}

@app.post("/plan-trip")
def plan_trip(request: TravelRequest):
    return plan_trip_service(request)