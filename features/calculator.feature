Feature: Calculadora
    Calculadora simples com 4 operações

    Scenario Outline: Somar dois números
        Somar dois números e mostrar o resultado da soma.
        Given O primeiro operador é <op1>
        And O segundo operador é <op2>
        When Somar dois números
        Then O resultado da soma é <resultado>
    
        Examples:
        | op1 | op2 | resultado|
        | 1   | 2   | 3        |
        | 2   | 3   | 5        |
        | 3   | 4   | 7        |
        | 4   | 5   | 9        |
        | 5   | 6   | 11       |
        | 6   | 7   | 13       |
        | 7   | 8   | 15       |
    
    Scenario Outline: Subtrair dois números
        Subtrai dois números e mostrar o resultado da subtração.
        Given O primeiro operador é <op1>
        And O segundo operador é <op2>
        When Subtrair dois números
        Then O resultado da subtração é <resultado>

        Examples:
        | op1 | op2 | resultado|
        | 1   | 2   | -1       |
        | 2   | 10  | -8       |
        | 3   | 5   | -2       |
        | 4   | 1   |  3       |
        | 5   | 0   |  5       |
        | 6   | -1  |  7       |
        | 7   | -2  |  9       |
        | 8   | -3  |  11      |
    
    Scenario Outline: Multiplicar dois números
        Multiplica dois números e mostrar o resultado da multiplicação.
        Given O primeiro operador é <op1>
        And O segundo operador é <op2>
        When Multiplicar dois números
        Then O resultado da multiplicação é <resultado>

        Examples:
        | op1 | op2 | resultado|
        | 1   | 2   | 2        |
        | 2   | 3   | 6        |
        | 3   | 4   | 12       |
        | 4   | 5   | 20       |
        | 5   | 6   | 30       |
        | 6   | 7   | 42       |
        | 7   | 8   | 56       |
    
    Scenario Outline: Dividir dois números
        Divide dois números e mostrar o resultado da divisão.
        Given O primeiro operador é <op1>
        And O segundo operador é <op2>
        When Dividir dois números
        Then O resultado da divisão é <resultado>

        Examples:
        | op1 | op2 | resultado|
        | 3   | 3   | 1        |
        | 5   | 1   | 5        |
        | 10  | 5   | 2        |
        | 50  | 5   | 10       |
        | 10  | 1   | 10       |
    
    Scenario Outline: Divisão por zero
        Mostra resultado oa dividir um número por zero e virse versa.
        Given O primeiro operador é <op1>
        And O segundo operador é <op2>
        When Dividir dois números
        Then O resultado da divisão por zero é <resultado>

        Examples:
        | op1 | op2 | resultado                      |
        | 1   | 0   | Divisão por zero não é possível|
        | 2   | 0   | Divisão por zero não é possível|

    Scenario Outline: Elevar dois números
        Potencia dois números e mostrar o resultado da potencia.
        Given O primeiro operador é <op1>
        And O segundo operador é <op2>
        When Elevar dois números
        Then O resultado da potenciação é <resultado>

        Examples:
        | op1 | op2 | resultado|
        | 1   | 2   | 1        |
        | 2   | 3   | 8        |
        | 3   | 4   | 81       |
        | 4   | 5   | 1024     |
        | 5   | 6   | 15625    |
