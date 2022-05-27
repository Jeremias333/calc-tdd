class Calculator(object):
    def __init__(self):
        pass

    def _check_natural(self, op):
        if not isinstance(op, int) or op < 0:
            raise CalcError(f"{op} não é um natural!")

    def _check_return_sub(self, x, y):
        if (x - y) < 0:
            raise CalcError("valor de resposta não é natural")

    def _check_return_div(self, x, y):
        if (x % y) != 0:
            raise CalcError("valor de resposta não é natural")

    def soma(self, x, y):
        self._check_natural(x)
        self._check_natural(y)
        return x + y

    def sub(self, x, y):
        self._check_natural(x)
        self._check_natural(y)
        self._check_return_sub(x, y)
        return x - y

    def multi(self, x, y):
        self._check_natural(x)
        self._check_natural(y)
        return x * y

    def div(self, x, y):
        self._check_natural(x)
        self._check_natural(y)
        self._check_return_div(x, y)
        return x / y

    def pot(self, x, y):
        self._check_natural(x)
        self._check_natural(y)
        return x ** y

class CalcError(Exception):
    pass
