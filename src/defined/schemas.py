from pydantic import BaseModel, Field
from .config import DEFAULT_VARIABLE

class DefinedIntegralRequest(BaseModel):
    expression: str = Field(..., description="Expresión a integrar")
    variable: str = Field(default=DEFAULT_VARIABLE, description="Variable de integración")
    lower_limit: float = Field(..., description="Límite inferior de integración")
    upper_limit: float = Field(..., description="Límite superior de integración")

class IntegralResponse(BaseModel):
    expression: str
    result: str
