
from typing import Optional
from datetime import datetime
from enum import Enum
from pydantic import BaseModel, ConfigDict, Field, EmailStr, field_validator


class RoleEnum(str, Enum):
    admin = "admin"
    staff = "staff"

class Item(BaseModel):
    id: int
    username: str = Field(
        ...,
        min_length=6,
        max_length=15,
        pattern=r'^[a-z0-9]+$',
        title='Username',
        description='must be alpha-numeric',
        example='johndoe777'
    )

    email: EmailStr = Field(..., description="Valid email address", example="user@email.com")

    password: str = Field(
        ...,
        min_length=8,
        max_length=20,
        title='Password',
        description='8-20 chars, min 1 uppercase, 1 lowercase, 1 digit, 1 special (! or @)',
        example='Password1!'
    )
    @field_validator('password')
    @classmethod
    def validate_password(cls, v):
        import re
        if not (8 <= len(v) <= 20):
            raise ValueError('Password must be 8-20 characters long')
        if not re.search(r'[A-Z]', v):
            raise ValueError('Password must contain at least one uppercase letter')
        if not re.search(r'[a-z]', v):
            raise ValueError('Password must contain at least one lowercase letter')
        if not re.search(r'\d', v):
            raise ValueError('Password must contain at least one digit')
        if not re.search(r'[!@]', v):
            raise ValueError('Password must contain at least one special character (! or @)')
        if not re.fullmatch(r'[A-Za-z\d!@]+', v):
            raise ValueError('Password may only contain letters, digits, !, and @')
        return v

    role: RoleEnum = Field(..., description="Role must be 'admin' or 'staff'", example="admin")

    created_at: Optional[datetime] = Field(default=None, description="Waktu pembuatan user (jika tidak diisi, isi otomatis di backend)")
    updated_at: Optional[datetime] = Field(default=None, description="Waktu update terakhir user (jika tidak diisi, isi otomatis di backend)")
    model_config = ConfigDict(extra="forbid")


class ItemResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    password: str
    role: RoleEnum
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

class ResponseModel(BaseModel):
  success: bool
  message: str
  data: ItemResponse