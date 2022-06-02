class Calculator(object):
    def __init__(self):
        pass

    def _check_integer(self, op):
        if not isinstance(op, int):
            raise CalcError(f"{op} não é número inteiro!")

    def _check_return_div(self, x, y):
        if (x % y) != 0:
            raise CalcError("valor de resposta não é um inteiro")
    
    def _check_is_zero(self, op):
        if op == 0:
            raise CalcError("Divisão por zero não é possível")

    def soma(self, x, y):
        self._check_integer(x)
        self._check_integer(y)
        return x + y

    def sub(self, x, y):
        self._check_integer(x)
        self._check_integer(y)
        return x - y

    def multi(self, x, y):
        self._check_integer(x)
        self._check_integer(y)
        return x * y

    def div(self, x, y):
        try:
            self._check_integer(x)
            self._check_integer(y)
            self._check_is_zero(y)
            self._check_return_div(x, y)
            return x / y
        except:
            return "Divisão por zero não é possível"

    def pot(self, x, y):
        self._check_integer(x)
        self._check_integer(y)
        return x ** y

class CalcError(Exception):
    pass
