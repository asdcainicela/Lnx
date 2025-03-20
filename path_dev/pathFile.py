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

ruta_base = r"C:\Users\asdCain\Desktop\Lnx"  # Cambia por tu ruta
estructura = listar_archivos(ruta_base)

ruta_salida = r"C:\Users\asdCain\Desktop\Lnx\estructura.txt"  

with open(ruta_salida, "w", encoding="utf-8") as f:
    f.write("\n".join(estructura))

print(f"Archivo guardado en: {ruta_salida}")


def convertir_a_html(estructura):
    html = "<ul>\n"
    for linea in estructura:
        nivel = linea.count("  ") // 2
        nombre = linea.strip("|- ")
        html += "  " * nivel + f"<li>{nombre}</li>\n"
    html += "</ul>"
    return html

html_contenido = convertir_a_html(estructura)
ruta_html = r"C:\Users\asdCain\Desktop\Lnx\index.html"

with open(ruta_html, "w", encoding="utf-8") as f:
    f.write(f"<html><body>{html_contenido}</body></html>")

print(f"Archivo HTML guardado en: {ruta_html}")
