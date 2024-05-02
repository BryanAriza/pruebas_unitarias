import pytest
from main import suma,resta,multiplicacion,division

def test_Sum1():
    assert suma(2,5) == 7
    print("La función suma trabaja correctamente")

def test_Sum2():
    assert suma(3,4) == 8
    print("La función suma trabaja incorrectamente")

def test_Rest1():
    assert resta(10,2) == 8
    print("La función resta trabaja correctamente")
    
def test_Rest2():
    assert resta(10,3) == 8
    print("La función resta trabaja incorrectamente")
    
def test_Multi1():
    assert multiplicacion(3,4) == 12
    print("La función multiplicación trabaja correctamente")
    
def test_Multi2():
    assert multiplicacion(3,4) == 15
    print("La función multiplicación trabaja incorrectamente")
    
def test_Divi1():
    assert division(10,2) == 5
    print("La función división trabaja correctamente")
    
def test_Divi2():
    assert division(2,0) == 10
    print("La función división trabaja incorrectamente")

# @pytest.mark.parametrize(
#     "inX, inY, esperado",
#     [
#         (3,4,7),
#         (2,8,10),
#         (100,200,300)
#     ]
# )
# def test_SumParam(inX, inY, esperado):
#     assert suma(inX, inY)== esperado
#     print("Las funciones parametrizadas trabajan correctamente")
    
if __name__ == '__main__':
    test_Sum1()
    test_Sum2()
    test_Rest1()
    test_Rest2()
    test_Multi1()
    test_Multi2()
    test_Divi1()
    test_Divi2()
    
    