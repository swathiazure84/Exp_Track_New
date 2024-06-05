from fastapi import APIRouter
from models import ExpenseDetails, Income
from .common_utils import CommonUtils
import json
expence_router = APIRouter()


@expence_router.post("/create_user")
def create_user(user_name : str):
    comm_utils  = CommonUtils()
    comm_utils.writ_json(f"data/{user_name}.json",{} )
    return "created the user"

@expence_router.post("/add_income")
def create_user(income : Income):
    income_details = income.model_dump()
    year = income_details['date'].year
    month = income_details['date'].month
    user = income_details['user']
    income = income_details['income']
    common_utils = CommonUtils()
    data = common_utils.read_json(user)
    if len(data) == 0:
        income_data = common_utils.income_formater( year, month, income)
        common_utils.writ_json(user, income_data)
    
        


    #hear goes logic for updating year, month 

    #return income_details
    # comm_utils  = CommonUtils()
    # comm_utils.writ_json(f"data/{user_name}.json",{"user_name":user_name} )


@expence_router.post("/add_expences")
def add_expences(expence_details : ExpenseDetails):
    expence_details = expence_details.model_dump()
    user_name = expence_details['user']
    data.update(expence_details)
    comm_utils  = CommonUtils()
    comm_utils.writ_json(f"data/{user_name}.json", data )
    return "added expences"


@expence_router.get("/show_expences/{user_name}")
def show_expences(user_name:str):
    with open(f"data/{user_name}.json", 'r') as f:
        data = json.loads(f.read())
    return data



