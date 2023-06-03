x= 4 * (3 ** 2 - 2 * (5 * 4 - 3 ** 3))
print(x)

"""
- and(&): Nos regresará True siempre que las componentes
      involucradas sean todas verdaderas (&)
-or (|): Nos regresará True siempre que en las componentes
      haya al menos un True (|)
-not (!): True-->False, False-->True (not)
"""

print("Tabla de verdad del operador AND")
print("True and True =", True & True)
print("True and False =", True & False)
print("False and True =", False & True)
print("False and False =", False & False)
print("-" * 40)
print("Tabla de verdad del operador OR")
print("True or True =", True | True)
print("True or False =", True | False)
print("False or True =", False | True)
print("False or False =", False | False)

# False | False ---> False
# not (False | False) ---> True
# True & True--->True
True & ( not (False | False) )