from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool = True
    age: int | None = None  # Optional field with default value of None
    
input_data = {
    "id": 1,
    "name": "John Doe",
    "is_active": True,
    "age": 30
}

user = User(**input_data)
print(user)