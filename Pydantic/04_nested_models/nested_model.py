from pydantic import BaseModel, Field
from typing import List, Dict, Optional


class Address(BaseModel):
    street: str
    city: str
    postel_code: str


class User(BaseModel):
    id: int
    name: str
    address: Address


class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List["Comment"]] = None


Comment.model_rebuild()

# example
user = User(
    id=1,
    name="John Doe",
    address=Address(street="123 Main St", city="New York", postel_code="12345"),
)

print(user)

comment = Comment(
    id=1,
    content="This is a comment",
    replies=[
        Comment(
            id=2,
            content="This is a reply",
            replies=[Comment(id=3, content="This is another reply", replies=[])],
        ),
        Comment(
            id=4,
            content="This is another reply",
            replies=[Comment(id=5, content="This is another reply", replies=[])],
        ),
        Comment(id=6, content="This is another reply", replies=[]),
    ],
)

print(comment)
