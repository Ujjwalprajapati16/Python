from pydantic import BaseModel, Field, ConfigDict
from typing import List, Dict, Optional
from datetime import datetime


class Address(BaseModel):
    street: str
    city: str
    postel_code: str


class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    created_at: datetime
    address: Address
    tags: List[str] = []

    model_config = ConfigDict(
        json_encoders={
            datetime: lambda v: v.strftime("%d-%m-%Y %H:%M:%S %Z"),
        }
    )


# create a user instance

user = User(
    id=1,
    name="John Doe",
    email="H2H4M@example.com",
    address=Address(street="123 Main St", city="New York", postel_code="12345"),
    created_at=datetime.now(),
    tags=["premium", "vip"],
)

# Using model_dump() -> dict

python_dict = user.model_dump()

print(python_dict)

# Using model_dump_json() -> json

json_string = user.model_dump_json()

print(json_string)
