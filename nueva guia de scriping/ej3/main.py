import re
import requests
from bs4 import BeautifulSoup

def obtener_urls_paginacion(url_base, n=5):
    urls_paginas = [url_base]
    for i in range(2, n + 1):
        urls_paginas.append(url_base + f'?page={i}')
    return urls_paginas

def obtener_contenido_articulos(urls_paginas):
    contenido_articulos = []
    for url_pagina in urls_paginas:
        response = requests.get(url_pagina)
        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            articulos = soup.find_all('article')
            for articulo in articulos:
                contenido_articulos.append(articulo.get_text())
        else:
            print(f"Error al descargar la página {url_pagina}: {response.status_code}")
    return contenido_articulos

def principal():
    try:
        url_base = input("Ingrese la URL base: ")
        if not es_url_valida(url_base):
            print("La URL no es válida.")
            return
        n = int(input("Ingrese el número de páginas de la paginación (si no se especifica, se utilizarán 5 páginas por defecto): ") or "5")
        urls_paginas = obtener_urls_paginacion(url_base, n)
        contenido_articulos = obtener_contenido_articulos(urls_paginas)
        print("\nContenido de los artículos obtenido:\n")
        for idx, articulo in enumerate(contenido_articulos, start=1):
            print(f"Artículo {idx}:\n{articulo}\n")
    except KeyboardInterrupt:
        print("\nInterrupción de usuario. Saliendo del programa.")

def es_url_valida(url):
    patron_url = re.compile(r'https?://(www\.)?[\w.-]+\.\w+')
    return bool(patron_url.match(url))

principal()
