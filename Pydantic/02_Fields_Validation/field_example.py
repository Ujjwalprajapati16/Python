from pydantic import BaseModel
from typing import List, Dict, Optional

class Cart(BaseModel):
    user_id: int
    items: List[str] 
    quantities: Dict[str, int]  # Dictionary with item names as keys and quantities as values
    
class BlogPost(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None  # Optional field for image URL