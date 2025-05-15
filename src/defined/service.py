from . import sympytools
from .schemas import DefinedIntegralRequest, IntegralResponse

def resolver_integral_definida(data: DefinedIntegralRequest) -> IntegralResponse:
    resultado = sympytools.calcular_integral_definida(
        expr_str=data.expression,
        var_str=data.variable,
        a=data.lower_limit,
        b=data.upper_limit
    )
    return IntegralResponse(expression=data.expression, result=resultado)
