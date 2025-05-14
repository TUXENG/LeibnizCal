from .sympytools import compute_undefined_integral
from .schemas import IntegralRequest, IntegralResponse

def solve_undefined_integral(data: IntegralRequest) -> IntegralResponse:
    result = compute_undefined_integral(data.expression, data.variable)
    return IntegralResponse(expression=data.expression, result=result)
