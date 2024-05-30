from pydantic import BaseModel
from datetime import date

class ExpenseDetails(BaseModel):
    food : float
    shopping: float
    medical : float
    bills : float
    date : date
    user : str


class Income(BaseModel):
    date: date
    income : float
    user: str