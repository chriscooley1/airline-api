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

from fastapi import FastAPI

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
    pass

@app.get("/{airline_name}/{flight_num}")
async def get_flights(airline_name: str, flight_num: str) -> Flight:
    pass

@app.post("/{airline_name}")
async def create_airline(airline: Airline) -> None:
    pass

@app.put("/{airline_name}/{flight_num}")
async def update_flights(airline_name: str, flight_num: str, updated_flight: Flight) -> None:
    pass
        
@app.delete("/{airline_name}/{flight_num}")
async def delete_flights(airline_name: str, flight_num: str) -> None:
    pass