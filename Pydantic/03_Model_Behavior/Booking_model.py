from pydantic import BaseModel, Field, computed_field

class Booking(BaseModel):
    user_id: int
    room_id: int
    nights: int = Field(..., ge=1, description="Number of nights for the booking")
    rate_per_night: float
    
    @computed_field
    @property
    def total_amount(self) -> float:
        return self.nights * self.rate_per_night
    
hotel = Booking(
    user_id = 1,
    room_id = 1,
    nights = 2,
    rate_per_night = 100
)

print(hotel.total_amount)