import sys


cadena_arn = sys.argv[1].upper() #aqui obligamos a que la cadena la coja en mayúsculas para hacerme la vida un poco más facil xD
cadena_adn = []

for x in cadena_arn:
    if x not in 'AUGC':
            print(f"Error: La cadena que has escrito: '{cadena_arn}' contiene un carácter no válido: '{x}'.")
            print("Asegúrate de que la cadena solo contenga las letras A, U, G o C.")
            #print(cadena_arn) esta linea es de prueba
            sys.exit(1)  #Sale del programa
    if x == "U":
        x = "T"
        cadena_adn.append(x) #reemplazamos las U por las T
    else:
        cadena_adn.append(x)
    



#cadena_adn.pop(0)
print(cadena_arn)
print(cadena_adn)
