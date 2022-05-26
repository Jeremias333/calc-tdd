# try:
#     import sys
#     import os
#     sys.path.append(
#         os.path.abspath(
#             os.path.join(
#                 os.path.dirname(__file__), '..'
#             )
#         )
#     )
# except:
#     raise
# from unittest import TestCase, main
# import pytest
# from src import calculator

# pytestmark = pytest.mark.parametrize("x, y, res", [(7,2,9), (3,5,8), (12, 12, 24)])

# class TestCalculadora(TestCase):
#     def setUp(self):
#        self.calc = calculator.Calculator()

#     def test_instancia_existe(self):
#         calc = calculator.Calculator()
#         self.assertIsInstance(calc, type(calculator.Calculator()))

#     @pytest.mark.parametrize("x, y, res", [(7,2,9), (3,5,8), (12, 12, 24)])
#     def test_funcao_soma_exist(self, x, y, res):
#         res_func = self.calc.soma(x, y)
#         self.assertEqual(res_func, res)
    
#     def test_soma_parametro_x_negativo(self):
#         pass

# if __name__ == '__main__':
#     main(verbosity=2)

