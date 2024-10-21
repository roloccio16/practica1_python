import sys
import subprocess

def ejecutar_ping(ip, num_peticiones, intervalo=0.1, tamaño_paquete=56, timeout=4): #ponemos parámetros default en la funcion que definimos
    try:
        comando_ping = [
            "ping", ip,
            "-i", str(intervalo),  #intervalo entre cada ping
            "-c", str(num_peticiones),  #número de pings a enviar
            "-s", str(tamaño_paquete),  #tamaño del paquete en bytes
            "-W", str(timeout)  #tiempo de espera por respuesta
        ]

        print(f"Ejecutando: {' '.join(comando_ping)}") 

        resultado = subprocess.run(comando_ping, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) #usamos el comanod subprocess como se nos pide en el ejercicio para ejecurar el ping

        if resultado.returncode == 0:
            print(f"Ping completado correctamente:\n{resultado.stdout}")
        else:
            print(f"Error durante la ejecución del ping:\n{resultado.stderr}")

    except Exception as e:
        print(f"error: {e}")


    #determinamos a que variable apunta cada valor que recibimos por parametros
    ip_servidor = sys.argv[1]
    num_peticiones = int(sys.argv[2])

    #a los parametros opcionales le volvemos a poner valores por defecto
    intervalo = float(sys.argv[3]) if len(sys.argv) > 3 else 0.1
    tamaño_paquete = int(sys.argv[4]) if len(sys.argv) > 4 else 56
    timeout = int(sys.argv[5]) if len(sys.argv) > 5 else 4
    #ya solo queda ejecutar el comando con los parámetros recibidos
    ejecutar_ping(ip_servidor, num_peticiones, intervalo, tamaño_paquete, timeout)


    #para ejecutar este archivo finalmente solo tendremos que hacer python3 practicaej4.py ip 100 0.05 100 2
