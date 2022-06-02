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
from src import calculator

import pytest

from src.calculator import CalcError


def test_existe_instancia():
    calc = calculator.Calculator()
    assert type(calc) is type(calculator.Calculator())


# ----------------------soma-------------------------
@pytest.mark.parametrize("x, y, res",
                         [(7, 2, 9),
                          (3, 2, 5),
                          (1, 2, 3)])
def test_funcao_soma(x, y, res):
    calc = calculator.Calculator()
    res_func = calc.soma(x, y)
    assert res_func == res


@pytest.mark.parametrize("x, y",
                         [("7", 2),
                          (3, "2"),
                          ("1", 2)])
def test_nao_numeros_soma(x, y):
    calc = calculator.Calculator()
    with pytest.raises(CalcError):
        calc.soma(x, y)


@pytest.mark.parametrize("x, y",
                         [(-0.5, 2),
                          (0.3, 2),
                          (-1, 2)])
def test_nao_naturais_soma(x, y):
    calc = calculator.Calculator()
    with pytest.raises(CalcError):
        calc.soma(x, y)


# -----------------------subtracao--------------------------
@pytest.mark.parametrize("x, y, res",
                         [(7, 2, 5),
                          (3, 2, 1),
                          (2, 1, 1)])
def test_funcao_sub(x, y, res):
    calc = calculator.Calculator()
    res_func = calc.sub(x, y)
    assert res_func == res


@pytest.mark.parametrize("x, y",
                         [("7", 2),
                          (3, "2"),
                          ("1", 2)])
def test_nao_numeros_sub(x, y):
    calc = calculator.Calculator()
    with pytest.raises(CalcError):
        calc.sub(x, y)


@pytest.mark.parametrize("x, y",
                         [(-0.5, 2),
                          (0.3, 2),
                          (-1, 2)])
def test_nao_naturais_sub(x, y):
    calc = calculator.Calculator()
    with pytest.raises(CalcError):
        calc.sub(x, y)


@pytest.mark.parametrize("x, y",
                         [(2, 7),
                          (3, 5),
                          (1, 2)])
def test_return_nao_natural_sub(x, y):
    calc = calculator.Calculator()
    with pytest.raises(CalcError):
        calc.sub(x, y)


# -------------------multiplicação----------------------
@pytest.mark.parametrize("x, y, res",
                         [(7, 2, 14),
                          (3, 2, 6),
                          (2, 1, 2)])
def test_funcao_multi(x, y, res):
    calc = calculator.Calculator()
    res_func = calc.multi(x, y)
    assert res_func == res


@pytest.mark.parametrize("x, y",
                         [("7", 2),
                          (3, "2"),
                          ("1", 2)])
def test_nao_numeros_multi(x, y):
    calc = calculator.Calculator()
    with pytest.raises(CalcError):
        calc.multi(x, y)


@pytest.mark.parametrize("x, y",
                         [(-0.5, 2),
                          (0.3, 2),
                          (-1, 2)])
def test_nao_naturais_multi(x, y):
    calc = calculator.Calculator()
    with pytest.raises(CalcError):
        calc.multi(x, y)


# -----------------------divisão-------------------------
@pytest.mark.parametrize("x, y, res",
                         [(5, 5, 1),
                          (4, 2, 2),
                          (10, 1, 10)])
def test_funcao_div(x, y, res):
    calc = calculator.Calculator()
    res_func = calc.div(x, y)
    assert res_func == res


@pytest.mark.parametrize("x, y",
                         [("7", 2),
                          (3, "2"),
                          ("1", 2)])
def test_nao_numeros_div(x, y):
    calc = calculator.Calculator()
    with pytest.raises(CalcError):
        calc.div(x, y)


@pytest.mark.parametrize("x, y",
                         [(-0.5, 2),
                          (0.3, 2),
                          (-1, 2)])
def test_nao_naturais_div(x, y):
    calc = calculator.Calculator()
    with pytest.raises(CalcError):
        calc.div(x, y)


@pytest.mark.parametrize("x, y",
                         [(2, 7),
                          (3, 5),
                          (1, 2)])
def test_return_nao_natural_div(x, y):
    calc = calculator.Calculator()
    with pytest.raises(CalcError):
        calc.div(x, y)


#-----------------------potência---------------------
@pytest.mark.parametrize("x, y, res",
                         [(2, 0, 1),
                          (2, 1, 2),
                          (3, 3, 27)])
def test_funcao_pot(x, y, res):
    calc = calculator.Calculator()
    res_func = calc.pot(x, y)
    assert res_func == res


@pytest.mark.parametrize("x, y",
                         [("7", 2),
                          (3, "2"),
                          ("1", 2)])
def test_nao_numeros_pot(x, y):
    calc = calculator.Calculator()
    with pytest.raises(CalcError):
        calc.pot(x, y)


@pytest.mark.parametrize("x, y",
                         [(-0.5, 2),
                          (0.3, 2),
                          (-1, 2)])
def test_nao_naturais_pot(x, y):
    calc = calculator.Calculator()
    with pytest.raises(CalcError):
        calc.pot(x, y)