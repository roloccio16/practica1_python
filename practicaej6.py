import requests

def get_usuarios(api_url):
    try:
        #hacemos la petición GET al endpoint
        respuesta = requests.get(api_url)

        #si el status code que recibimos es 200 pasamos la respuesta a JSON y y hacemos que la funcion lo returnee dentro de la variable con nombre usuarios
        if respuesta.status_code == 200:
            usuarios = respuesta.json()
            return usuarios
        else:
            print(f"Error no hay nada: {respuesta.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def showsave_nombres(usuarios, archivo_salida):
    try:
        with open(archivo_salida, 'w') as archivo:
            for usuario in usuarios:
                nombre = usuario['name']
                print(nombre)  #mostramos el nombre en la consola
                archivo.write(nombre + '\n')  #guardamos el nombre en el archivo
        print(f"Nombres guardados en el archivo '{archivo_salida}'.")

    except IOError as e:
        print(f"Error al escribir en el archivo: {e}")

    #definimos la URL de la API
    url_api = "https://jsonplaceholder.typicode.com/users"

    #hacemos la petición a la API para obtener los usuarios
    usuarios = get_usuarios(url_api)

    if usuarios:
        #mostramos los nombres y los guardamos en un archivo
        showsave_nombres(usuarios, 'nombres_usuarios.txt')
