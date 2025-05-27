from pydantic import BaseModel, Field, field_validator, model_validator, computed_field

class User(BaseModel):
    username: str
    
    @field_validator('username')
    def username_length(cls, value: str) -> str:
        if len(value) < 3:
            raise ValueError('Username must be at least 3 characters long')
        return value

class SignupData(BaseModel):
    password: str
    confirm_password: str
    
    @model_validator(mode='after')
    def password_match(cls, values):
        if values['password'] != values['confirm_password']:
            raise ValueError('Passwords do not match')
        return values
    
class Product(BaseModel):
    name: str
    price: float
    
    @computed_field
    @property
    def is_expensive(self) -> bool:
        return self.price > 100.0
    
cloth = Product(name='T-Shirt', price=25.0)
print(cloth.is_expensive)  # Output: False
lv = Product(name='Leather Jacket', price=150.0)
print(lv.is_expensive)  # Output: True