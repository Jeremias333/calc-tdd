try:
    import sys
    import os
    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__), '../..'
            )
        )
    )
except:
    raise
from behave import *
from pyparsing import And
from src.calculator import Calculator

@given("O primeiro operador é {op1}")
def set_op1(context, op1):
    context.op1 = int(op1)
    
@step("O segundo operador é {op2}")
def set_op2(context, op2):
    context.op2 = int(op2)

@then("O resultado da soma é {resultado}")
def result_soma(context, resultado):
    """
    :type context: behave.runner.Context
    """
    assert context.resultado == int(resultado)

@then("O resultado da subtração é {resultado}")
def result_sub(context, resultado):
    assert context.resultado == int(resultado)

@then("O resultado da multiplicação é {resultado}")
def result_multi(context, resultado):
    assert context.resultado == int(resultado)

@then("O resultado da divisão é {resultado}")
def result_div(context, resultado):
    assert context.resultado == int(resultado)

@then("O resultado da divisão por zero é {resultado}")
def result_div(context, resultado):
    assert context.resultado == str(resultado)

@then("O resultado da potenciação é {resultado}")
def result_pot(context, resultado):
    assert context.resultado == int(resultado)

@when("Somar dois números")
def soma(context):
    calculadora = Calculator()
    context.resultado = calculadora.soma(context.op1, context.op2)

@when("Subtrair dois números")
def sub(context):
    calculadora = Calculator()
    context.resultado = calculadora.sub(context.op1, context.op2)

@when("Multiplicar dois números")
def multi(context):
    calculadora = Calculator()
    context.resultado = calculadora.multi(context.op1, context.op2)

@when("Dividir dois números")
def div(context):
    calculadora = Calculator()
    context.resultado = calculadora.div(context.op1, context.op2)

@when("Elevar dois números")
def pot(context):
    calculadora = Calculator()
    context.resultado = calculadora.pot(context.op1, context.op2)