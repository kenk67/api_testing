from fastapi import FastAPI, HTTPException
from models import ItemOutput
from settings import get_settings

app = FastAPI()

settings = get_settings()

# Fruit descriptions
fruits_info = {
    "apple": "Apples are sweet and crunchy fruits that come in a variety of colors including red, green, and yellow.",
    "banana": "Bananas are elongated, yellow fruits that are soft and sweet when ripe.",
    "orange": "Oranges are citrus fruits known for their tangy and sweet flavor, packed with vitamin C.",
    "grape": "Grapes are small, juicy fruits that can be eaten fresh or used to make wine, jams, and juice.",
    "mango": "Mangoes are tropical fruits with a sweet and tangy flavor, known for their juicy, orange flesh.",
    "watermelon": "Its freaking good"
}

# Vehicle descriptions
vehicles_info = {
    "car": "A car is a road vehicle with four wheels, typically powered by an internal combustion engine or an electric motor.",
    "motorcycle": "A motorcycle is a two-wheeled vehicle powered by an engine, designed for speed and agility.",
    "truck": "A truck is a motor vehicle designed to transport cargo, often larger and heavier than cars.",
    "bicycle": "A bicycle is a human-powered vehicle with two wheels, driven by pedals and used for transportation or recreation.",
    "bus": "A bus is a large motor vehicle designed to carry passengers, usually along a fixed route."
}

@app.get("/fruits", response_model=ItemOutput)
def get_fruit_description(fruit: str):
    fruit_lower = fruit.lower()
    if fruit_lower in fruits_info:
        return ItemOutput(name=fruit, description=fruits_info[fruit_lower])
    else:
        raise HTTPException(status_code=404, detail="Fruit not found")

@app.get("/vehicles", response_model=ItemOutput)
def get_vehicle_description(vehicle: str):
    vehicle_lower = vehicle.lower()
    if vehicle_lower in vehicles_info:
        return ItemOutput(name=vehicle, description=vehicles_info[vehicle_lower])
    else:
        raise HTTPException(status_code=404, detail="Vehicle not found")

@app.get("/config")
def get_config():
    return {
        "api_version": settings.api_version,
        "fruit_limit": settings.fruit_limit,
        "vehicle_limit": settings.vehicle_limit
    }