import readchar
key = "hola"
"""
Proyecto integrador parte 2
Tu tarea es

Instalar la librería: https://pypi.org/project/readchar/
Investigrar cómo leer un caracter del teclado
Escribir un programa que corra un bucle infinito leyendo e imprimiento las teclas y sólo terminará cuando se presione la tecla ↑ indicada como UP
"""
while True:
    print("")
    key = readchar.readkey() 
    print(key, end="")
    if key=="\x00H":
        print("\nIngresaste arriba")
        break