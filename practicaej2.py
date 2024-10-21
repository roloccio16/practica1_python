cadena = input(" dime el texto que quieres que codifique: ")


'''
O -> 0
I -> 1
E -> 3
A -> 4
S -> 5
G -> 6
T -> 7
B -> 8
g -> 9

'''
cadena = cadena.upper() #aprovecho como el script anterior este método para no tener que poner todas las variantes
cadena = cadena.replace("O","0")
cadena = cadena.replace("o","0")
cadena = cadena.replace("I","1")
cadena = cadena.replace("i","1")
cadena = cadena.replace("E","3")
cadena = cadena.replace("e","3")
cadena = cadena.replace("A","4")
cadena = cadena.replace("S","5")
cadena = cadena.replace("a","4")
cadena = cadena.replace("G","6")
cadena = cadena.replace("T","7")
cadena = cadena.replace("B","8")
cadena = cadena.replace("g","9")
print(cadena)
