from pydantic import BaseModel


class Flight(BaseModel):
    flight_num: str
    capacity: int
    estimated_flight_duration: int

class Airline(BaseModel):
    airline_name: str
    flights: list[Flight]
