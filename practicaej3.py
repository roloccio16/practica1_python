chars= "┌┐┘└│─"
chars2="╔╗╝╚║═"
numero = 0 
tipo = int(input("Si quieres lineas simples escribe 1 si las quieres dobles escribe 2: "))
ancho = int(input("Como de ancho quieres que sea la forma?: "))
anchura = ancho - 2
alto = int(input("Como de alto quieres la forma?: "))
altura = alto - 1
# print(chars[0],end="",flush="true") este es el print que use la primera vez que hicimos este ejercicio para que al hacerlo no hiciese un salto de línea, por si lo querías ver
if tipo == 1:
    for x in range(0,altura):
        if (numero == 0):
            print(chars[0] + chars[5] * anchura + chars[1])
            numero +=1
        if (numero > 0 and numero < altura):
            print(chars[4] + " " * anchura + chars[4])
            numero += 1
        if (numero == altura):
            print(chars[3] + chars[5] * anchura + chars[2])
            numero += 1
else:
    for x in range(0,altura):
        if (numero == 0):
            print(chars2[0] + chars2[5] * anchura + chars2[1])
            numero +=1
        if (numero > 0 and numero < altura):
            print(chars2[4] + " " * anchura + chars2[4])
            numero += 1
        if (numero == altura):
            print(chars2[3] + chars2[5] * anchura + chars2[2])
            numero += 1
# print("fin")

