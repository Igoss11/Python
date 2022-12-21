# Модуль для выполнения операций


import sympy


def execute_expr(expr: str) -> str:
    """Принимает на вход строку-пример.
    Возвращает результат примера."""
    return str(eval(expr))


def solve_eq(expr: str) -> str:
    """Принимает на вход уравнение в виде строки.
    Возвращает список корней уравнения в строку с разделителем."""
    x = sympy.Symbol('x')
    a = expr
    return sympy.solve(a, x)


def simpify_pol(expr: str) -> str:
    """Упрощает введенный многочлен"""
    return str(sympy.simplify(expr))
