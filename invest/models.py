from pydantic import BaseModel, Field
from typing import List
from schemas import AccountType, AccountStatus, AccessLevel

"""
переделать принятие с фронта, например на форнте переменная называется по другому, а принять ее нужно по своему, зто было в видео диджитал
"""


class Account(BaseModel):
    id: int
    type: AccountType
    name: str
    status: AccountStatus
    opened_date: str = Field(alias='openedDate')
    closed_date: str = Field(alias='closedDate')
    access_level: AccessLevel = Field(alias='accessLevel')


class GetAccountsResponse(BaseModel):
    accounts: List[Account]
