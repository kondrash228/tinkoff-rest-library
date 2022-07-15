from pydantic import BaseModel, Field
from typing import List
from schemas import AccountType, AccountStatus, AccessLevel

# ответы запросов 

class Account(BaseModel):
    id: str
    type: AccountType
    name: str
    status: str
    opened_date: str = Field(alias='openedDate')
    closed_date: str = Field(alias='closedDate')
    access_level: str = Field(alias='accessLevel')


class GetAccountsResponse(BaseModel):
    accounts: List[Account]


class GetAccountsRequest(BaseModel):
    accounts: List[Account]