try:
    import sys
    import os
    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__), '..'
            )
        )
    )
except:
    raise
from unittest import TestCase, main
import pytest
from src import calculator

import pytest

from src.calculator import Calculator, CalcError

def test_existe_instancia():
    calc = calculator.Calculator()
    assert type(calc) is type(calculator.Calculator())

@pytest.mark.parametrize("x, y, res",
                         [(7, 2, 9),
                          (3, 2, 5),
                          (1, 2, 3)])
def test_funcao_soma(x, y, res):
    calc = calculator.Calculator()
    res_func = calc.soma(x,y)
    assert res_func == res

@pytest.mark.parametrize("x, y",
                         [("7", 2),
                          (3, "2"),
                          ("1", 2)])
def test_nao_numeros(x,y):
    calc = calculator.Calculator()
    with pytest.raises(CalcError):
        calc.soma(x, y)



# @pytest.mark.parametrize("a, b, res",
#                          [(7, 2, 9),
#                           (3, 2, 5),
#                           (-1, 2, 1)])
# def test_soma(a, b, res):
#     calculator = Calculator()
#     res_calc = calculator.soma(a, b)
#     assert res == res_calc


# @pytest.mark.parametrize("a, b, res",
#                          [("7", 2, 9),
#                           (3, "2", 5),
#                           (-1, "2", 1)])
# def test_soma_type(a, b, res):
#     calculator = Calculator()
#     with pytest.raises(CalcError):
#         res_calc = calculator.soma(a, b)


# @pytest.mark.parametrize("a, b, res",
#                          [(7, 2, 5),
#                           (3, 2, 1),
#                           (-1, 2, -3)])
# def test_sub(a, b, res):
#     calculator = Calculator()
#     res_calc = calculator.sub(a, b)
#     assert res == res_calc


# @pytest.mark.parametrize("a, b, res",
#                          [("7", 2, 5),
#                           (3, "2", 1),
#                           (-1, "2", -3)])
# def test_sub(a, b, res):
#     calculator = Calculator()
#     with pytest.raises(CalcError):
#         res_calc = calculator.sub(a, b)

