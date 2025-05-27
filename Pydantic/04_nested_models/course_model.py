from pydantic import BaseModel, Field
from typing import List, Dict, Optional

class Lesson(BaseModel):
    lesson_id: int
    topic: str
    
class Module(BaseModel):
    module_id: int
    name: str
    lessons: List[Lesson]
    
class Course(BaseModel):
    course_id: int
    title: str
    modules: List[Module]
    
# example
course = Course(
    course_id=1,
    title="Python Programming",
    modules=[
        Module(
            module_id=1,
            name="Introduction to Python",
            lessons=[
                Lesson(lesson_id=1, topic="Variables and Data Types"),
                Lesson(lesson_id=2, topic="Control Flow"),
                Lesson(lesson_id=3, topic="Functions"),
            ],
        ),
        Module(
            module_id=2,
            name="Object-Oriented Programming",
            lessons=[
                Lesson(lesson_id=4, topic="Classes and Objects"),
                Lesson(lesson_id=5, topic="Inheritance"),
                Lesson(lesson_id=6, topic="Polymorphism"),
            ],
        ),
    ],
)