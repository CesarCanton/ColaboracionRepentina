import resta
import suma
from .ColaboracionRepentina.multiplicacion import multiplicacin as m

menu = """

Menu
1) Resta
2) multiplicacion
3) Suma

Seleccione uno

"""

operacion = input(menu)
num1 = int(input())
num2 = int(input())

match operacion:
    case "1":
        print(resta.resta(num1, num2))
    case "2":
        m(num1, num2)
    case "3":
        print(suma.suma(num1, num2))
    case _:
        print("No seleccion ninguno")