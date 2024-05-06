"""
Have these endpoints:

GET / -> list[airline_name]
GET /:airline_name -> list[flight_num]
GET /:airline_name/:flight_num -> Flight

POST /:airline
PUT /:airline/:flight_num
DELETE /:airline/:flight_num

"""

import json

from fastapi import FastAPI, HTTPException

from models import Airline, Flight


app = FastAPI()


with open("airlines.json", "r") as f:
    airline_data = json.load(f)

flights: list[Flight] = []
airlines: list[Airline] = []

for airline_name, airline_flights in airline_data.items():
    airlines.append(Airline(airline_name=airline_name, flights=airline_flights))


@app.get("/")
async def get_airline_names() -> list[str]:
    return [airline.airline_name for airline in airlines]

@app.get("/{airline_name}")
async def get_flight_nums(airline_name: str) -> list[str]:
    for airline in airlines:
        if airline.airline_name == airline_name:
            return [flight.flight_num for flight in airline.flights]

@app.get("/{airline_name}/{flight_num}")
async def get_flights(airline_name: str, flight_num: str) -> Flight:
    for airline in airlines:
        if airline.airline_name == airline_name:
            for flight in airline.flights:
                if flight.flight_num == flight_num:
                    return flight

@app.post("/{airline_name}")
async def create_airline(airline_name: str) -> Airline:
    new_airline = Airline(airline_name=airline_name, flights=[])
    airlines.append(new_airline)
    return new_airline

@app.put("/{airline_name}/{flight_num}")
async def update_flight(airline_name: str, flight_num: str, updated_flight: Flight):
    for airline in airlines:
        if airline.airline_name == airline_name:
            for flight in airline.flights:
                if flight.flight_num == flight_num:
                    flight.capacity = updated_flight.capacity
                    flight.estimated_flight_duration = updated_flight.estimated_flight_duration
                    return "Flight updated successfully"
            # If the flight doesn't exist, add it
            airline.flights.append(updated_flight)
            return "Flight created successfully"
    raise HTTPException(status_code=404, detail="Airline not found")

@app.delete("/{airline_name}/{flight_num}")
async def delete_flight(airline_name: str, flight_num: str):
    for airline in airlines:
        if airline.airline_name == airline_name:
            for flight in airline.flights:
                if flight.flight_num == flight_num:
                    airline.flights.remove(flight)
                    return {"message": "Flight deleted successfully"}
    raise HTTPException(status_code=404, detail="Flight not found")
