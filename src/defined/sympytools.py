from sympy import symbols, sympify, integrate
from sympy.core.sympify import SympifyError

def calcular_integral_definida(expr_str: str, var_str: str, a: float, b: float) -> str:
    try:
        variable = symbols(var_str)
        expr = sympify(expr_str)
        resultado = integrate(expr, (variable, a, b))
        return str(resultado)
    except (SympifyError, Exception) as e:
        raise ValueError(f"Error al calcular la integral definida: {e}")
