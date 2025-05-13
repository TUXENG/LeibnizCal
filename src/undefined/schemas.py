from pydantic import BaseModel
from typing import Dict, Any

class UndefinedRequest(BaseModel):
    expression: str        # La función a integrar, p.ej. "e**x"
    variable: str = "x"    # Variable de integración por defecto

class IntegralResponse(BaseModel):
    input: Dict[str, Any]  # Echo de los datos recibidos
    result: str            # Resultado de la integral (como string)
