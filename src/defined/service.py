from sympy import symbols, sympify, integrate
from sympy.core.sympify import SympifyError

def solve_defined(expression: str, variable: str, lower: float, upper: float) -> str:
    """
    Calcula la integral definida de `expression` respecto a `variable`
    entre `lower` y `upper`, y devuelve el resultado como string.
    """
    try:
        var = symbols(variable)
        expr = sympify(expression)
        symbols_in_expr = expr.free_symbols
        invalid_symbols = [s for s in symbols_in_expr if s != var]

        if invalid_symbols:
            raise ValueError(f"Solo se permite la variable '{variable}', simbolos invalido: {invalid_symbols}")
        result = integrate(expr, (var, lower, upper))
        return str(result)
    except SympifyError as e:
        raise ValueError(f"No puede parsear la expresión: {e}")
    except Exception as e:
        raise ValueError(f"Error al calcular la integral definida: {e}")