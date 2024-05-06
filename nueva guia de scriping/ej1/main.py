import pyperclip
import requests

def principal():
    try:
        url = pyperclip.paste()
        if es_url_valida(url):
            descargar_pagina(url)
    except KeyboardInterrupt:
        print("\nInterrupción de usuario. Saliendo del programa.")

def es_url_valida(url):
    patron_url = re.compile(r'https?://(www\.)?[\w.-]+\.\w+')
    return bool(patron_url.match(url))

def descargar_pagina(url):
    response = requests.get(url)
    if response.status_code == 200:
        html = response.text
        guardar_archivo(html)
    else:
        print("Error al descargar la página:", response.status_code)

def guardar_archivo(html):
    nombre_archivo = generar_nombre_archivo()
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write(html)
    print("Página descargada y guardada como:", nombre_archivo)


def generar_nombre_archivo():
    num_descargas = obtener_num_descargas()
    nombre_archivo = f"descarga_{num_descargas}.html"
    return nombre_archivo

def obtener_num_descargas():
    try:
        with open("num_descargas.txt", "r") as archivo:
            num_descargas = int(archivo.read())
    except FileNotFoundError:
        num_descargas = 0
    return num_descargas

def actualizar_num_descargas():
    num_descargas = obtener_num_descargas() + 1
    with open("num_descargas.txt", "w") as archivo:
        archivo.write(str(num_descargas))

principal()
