from pydantic import BaseModel, Field

# Create Product model with id, name, price and in_stock

class Product(BaseModel):
    id: int
    name: str
    price: float = 0  # Price must be greater than 0
    in_stock: bool = True  # Default value is True
    
cloth = Product(id=1, name="T-shirt", price=19.99, in_stock=True)
print(cloth)