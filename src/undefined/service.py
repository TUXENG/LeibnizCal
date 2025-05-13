from sympy import symbols, sympify, integrate
from sympy.core.sympify import SympifyError

def solve_undefined(expression: str, variable: str) -> str:
    """
    Calcula la integral indefinida de `expression` respecto a `variable`
    y devuelve el resultado (con + C) como string.
    """
    try:
        var = symbols(variable)
        expr = sympify(expression)
        symbols_in_expr = expr.free_symbols
        invalid_symbols = [s for s in symbols_in_expr if s != var]

        if invalid_symbols:
            raise ValueError(f"Solo se permite la variable '{variable}', simbolos invalidos: {invalid_symbols}") 
        result = integrate(expr, var)
        # Añadimos manualmente la constante de integración
        return f"{result} + C"
    except SympifyError as e:
        raise ValueError(f"No pude parsear la expresión: {e}")
    except Exception as e:
        raise ValueError(f"Error al calcular la integral indefinida: {e}")
