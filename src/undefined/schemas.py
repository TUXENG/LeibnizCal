from pydantic import BaseModel, Field
from .config import DEFAULT_VARIABLE

class IntegralRequest(BaseModel):
    expression: str = Field(..., description="Expresión a integrar")
    variable: str = Field(default=DEFAULT_VARIABLE, description="Variable de integración")

class IntegralResponse(BaseModel):
    expression: str
    result: str
