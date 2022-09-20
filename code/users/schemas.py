from pydantic import BaseModel, constr, EmailStr


class RegisterSchema(BaseModel):
    email: EmailStr
    password: constr(min_length=8)
