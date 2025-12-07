from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field, EmailStr
from typing import Optional


class Student(BaseModel):
    name: str = 'Gyan Prakash'
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10, default= 5, description= 'A Decimal')
    
stud = Student(**{
    'email': 'hey@g.com',
    'cgpa': 2,
    'age': 3
})

print(stud)