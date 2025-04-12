import os

def listar_archivos(directorio, nivel=0, ignorar={".git"}):
    estructura = []
    for archivo in sorted(os.listdir(directorio)):
        if archivo in ignorar:
            continue
        ruta_completa = os.path.join(directorio, archivo)
        estructura.append("  " * nivel + "|-- " + archivo)
        if os.path.isdir(ruta_completa):
            estructura.extend(listar_archivos(ruta_completa, nivel + 1, ignorar))
    return estructura

# Obtener la ruta de la carpeta "Lnx" automáticamente
ruta_base = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
estructura = listar_archivos(ruta_base)

# Guardar el archivo de texto en la misma carpeta del script
ruta_salida = os.path.join(os.path.dirname(__file__), "estructura.txt")

with open(ruta_salida, "w", encoding="utf-8") as f:
    f.write("\n".join(estructura))

print(f"Archivo de estructura guardado en: {os.path.abspath(ruta_salida)}")

def convertir_a_html(estructura):
    html = "<ul>\n"
    for linea in estructura:
        nivel = linea.count("  ") // 2
        nombre = linea.strip("|- ")
        html += "  " * nivel + f"<li>{nombre}</li>\n"
    html += "</ul>"
    return html

html_contenido = convertir_a_html(estructura)

# Guardar el archivo HTML en la misma carpeta del script
ruta_html = os.path.join(os.path.dirname(__file__), "index.html")

with open(ruta_html, "w", encoding="utf-8") as f:
    f.write(f"<html><body>{html_contenido}</body></html>")

print(f"Archivo HTML guardado en: {os.path.abspath(ruta_html)}")
