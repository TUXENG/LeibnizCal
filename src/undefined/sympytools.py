from sympy import symbols, integrate, sympify, SympifyError
from .utils import simplify_expr
from .constants import INVALID_EXPR_MESSAGE

def compute_undefined_integral(expression: str, variable: str) -> str:
    try:
        x = symbols(variable)
        expr = sympify(expression)
        result = integrate(expr, x)
        return simplify_expr(result)
    except SympifyError:
        return INVALID_EXPR_MESSAGE
