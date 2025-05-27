from pydantic import BaseModel, Field
from typing import Optional


class Employee(BaseModel):
    id: int
    name: str = Field(..., min_length=3, max_length=100, description="Employee Name")
    department: Optional[str] = "General"
    salary: float = Field(
        ..., ge=10000.0, description="Employee Salary must be at least 10000.0"
    )  # Salary must be at least 10000.0


# Example usage
employee = Employee(id=1, name="John Doe", salary=50000.0)
print(employee)
