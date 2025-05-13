from pydantic import BaseModel
from typing import Dict, Any

class DefinedRequest(BaseModel):
    expression: str        # La función a integrar, e.g. "x**2 + sin(x)"
    variable: str = "x"    # La variable de integración por defecto
    lower_limit: float     # Límite inferior de la integral
    upper_limit: float     # Límite superior de la integral

class IntegralResponse(BaseModel):
    input: Dict[str, Any]  # Repetimos lo recibido (útil para debug)
    result: str            # El resultado de la integral, serializado como texto
