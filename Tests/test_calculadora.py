from App.calculadora import Calculadora

def test_sumar():
    resultado = Calculadora.sumar(2, 3)
    assert resultado == 5

def test_restar():
    resultado = Calculadora.restar(2, 3)
    assert resultado == -1

def test_multiplicar():
    resultado = Calculadora.multiplicar(2, 3)
    assert resultado == 6

def test_dividir():
    resultado = Calculadora.dividir(2, 3)
    assert round(resultado, 3) == 0.667