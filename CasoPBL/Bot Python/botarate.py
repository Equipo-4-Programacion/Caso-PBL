# Propiedad del Equipo 4 de Programación.
# noinspection PyUnresolvedReferences

# Importamos las librerias necesarias para el caso
import json
import re
import datetime
from reportlab.pdfgen import canvas


# Inicio del bot Simple
def botsimple():
    # Inicio de la conversación con un saludo.
    salirbot = False
    nombre = input(">Hola, soy ")
    print(">Muy buenas {nom}. Soy Botarate.".format(nom=nombre))
    # Inicio de la conversación introduciendo un tema de conversación.
    while not salirbot:
        preg = input("Introduce un tema de conversación: ")
        print(">¿Que sabes de {pregunta}?".format(pregunta=preg))
        # respuestas que el bot conoce
        if preg.upper() == "PROGRAMACIÓN":
            print(">Sé programar en Python y Java.")
        elif preg.upper() == "BASES DE DATOS":
            print(">De bases de datos sé las nociones basicas.")
        elif preg.upper() == "CIBERSEGURIDAD":
            print(">Sé bastante sobre ciberseguridad en temas de hacking.")
        elif preg.upper() == "SISTEMAS INFORMÁTICOS":
            print(">Tengo conocimientos sobre el hardware y el software de un ordenador.")
        elif preg.upper() == "OFIMÁTICA":
            print(">Sé usar Word, Powerpoint y Excel a nivel de usuario.")
        elif preg.upper() == "REDES LOCALES":
            print(">Sé crear redes para el hogar, asignando direcciones IP de manera dinámica.")
        elif preg.upper() == "ENTORNOS DE DESARROLLO":
            print(">Pues tengo conocimientos en GIT y GITHub.")
        # Si no conoce el tema de conversación imprime "Pues la verdad de eso poco"
        else:
            print(">Pues la verdad de eso poco.")
        # Esta linea pregunta si quieres hacer otra pregunta
        resp = input("¿Quieres salir? ")
        if resp.upper() == "SI":
            salirbot = True
    return


# Inicio del Bot REGEX
def botregex():
    # diccionario con las respuestas a ciertas palabras (patrones de respuesta)
    respuestas = {"preg1": "^Hola|^hola|Soy|soy",
                  "resp1": "Muy buenas, (variable). Soy Botarate",
                  "preg2": "programacion|Programacion",
                  "resp2": "Se programar en Python y Java.",
                  "preg3": "base|datos|Base",
                  "resp3": "De bases de datos s\u00e9 las nociones basicas.",
                  "preg4": "sistemas|informaticos",
                  "resp4": "Tengo conocimientos sobre el hardware y el software de un ordenador.",
                  "preg5": "ofimatica|Ofimatica",
                  "resp5": "Se usar Word, Powerpoint y Excel a nivel de usuario.",
                  "preg6": "redes|locales|Redes",
                  "resp6": "Se crear redes para el hogar, asignando direcciones IP de manera din\u00e1mica.",
                  "preg7": "entornos|desarrollo|Entornos",
                  "resp7": "Pues tengo conocimientos en GIT y GITHub.",
                  "preg8": "^Salir|^salir"}
    salir1 = False
    # Este bucle iniciará la conversación con el bot, respondiendo al nombre y a los patrones de preguntas.
    while not salir1:
        pregunta = input("> ")
        if re.search(respuestas["preg1"], pregunta):
            nombre = pregunta.split()
            conjunto = respuestas["resp1"]
            conjunto = conjunto.replace("(variable)", nombre[-1])
            print(">", conjunto)
        elif re.search(respuestas["preg2"], pregunta):
            conjunto = respuestas["resp2"]
            print(">", conjunto)
        elif re.search(respuestas["preg3"], pregunta):
            conjunto = respuestas["resp3"]
            print(">", conjunto)
        elif re.search(respuestas["preg4"], pregunta):
            conjunto = respuestas["resp4"]
            print(">", conjunto)
        elif re.search(respuestas["preg5"], pregunta):
            conjunto = respuestas["resp5"]
            print(">", conjunto)
        elif re.search(respuestas["preg6"], pregunta):
            conjunto = respuestas["resp6"]
            print(">", conjunto)
        elif re.search(respuestas["preg7"], pregunta):
            conjunto = respuestas["resp7"]
            print(">", conjunto)
            guardarlainfo(pregunta, conjunto)
        elif re.search(respuestas["preg8"], pregunta):
            break
        else:
            print("No entiendo su pregunta")
    return


# Esta función sirve para introducir el registro de chat en el archivo "conversacion.txt"
def guardarlainfo(preg1, conjunto):
    with open("conversación.txt", "a") as f:
        conversacion = "> " + str(preg1) + "\n> " + str(conjunto + "\n")
        f.write(conversacion)
    return


# Esta función inicia la conversación con el bot REGEX desde fichero. Donde el archivo diccionario.json contiene el
# diccionario de patrones y respuestas de la función anterior.
def botfichero():
    salir2 = False
    while not salir2:
        with open('diccionario.json', 'r') as f:
            conj_datos = json.load(f)
        with open("conversación.txt", "w") as f:
            f.close()
        while True:
            pregunta = input("> ")
            if re.search(conj_datos["preg1"], pregunta):
                nombre = pregunta.split()
                conjunto = conj_datos["resp1"]
                conjunto = conjunto.replace("(variable)", nombre[-1])
                print(">", conjunto)
                guardarlainfo(pregunta, conjunto)
            elif re.search(conj_datos["preg2"], pregunta):
                conjunto = conj_datos["resp2"]
                print(">", conjunto)
                guardarlainfo(pregunta, conjunto)
            elif re.search(conj_datos["preg3"], pregunta):

                conjunto = conj_datos["resp3"]

                print(">", conjunto)
                guardarlainfo(pregunta, conjunto)
            elif re.search(conj_datos["preg4"], pregunta):

                conjunto = conj_datos["resp4"]

                print(">", conjunto)
                guardarlainfo(pregunta, conjunto)
            elif re.search(conj_datos["preg5"], pregunta):

                conjunto = conj_datos["resp5"]

                print(">", conjunto)
                guardarlainfo(pregunta, conjunto)
            elif re.search(conj_datos["preg6"], pregunta):

                conjunto = conj_datos["resp6"]

                print(">", conjunto)
                guardarlainfo(pregunta, conjunto)
            elif re.search(conj_datos["preg7"], pregunta):

                conjunto = conj_datos["resp7"]

                print(">", conjunto)
                guardarlainfo(pregunta, conjunto)
            elif re.search(conj_datos["preg8"], pregunta):
                salir2 = True
                break
            else:
                guardarlainfo(pregunta, "No entiendo su pregunta")
                print(">No entiendo su pregunta")
    return


# Esta funcion se encarga de contar las palabras repetidas de la función informe.
def cuenta_repetidas(p, palab):
    return {p: palab.count(p)}


# Esta función se encarga de generar el archivo conversacion.pdf. En la primera fase de la función se encarga de
# obtener la fecha del sistema, contar cuantos caractéres y palabras tiene la conversación, ademas encuentra cual es
# la palabra mas repetida.
def informe():
    with open('conversación.txt', 'r') as f:
        caracteres = f.read()

    simbolos = [',', '.', '¡', '!', '¿', '?', '(', ')', '"', "'", ">", "<"]
    numpalabras = 0
    with open('conversación.txt', 'r') as f:
        for linea in f:
            for simbolo in simbolos:
                linea = linea.replace(simbolo, ' ')
            palabras = linea.lower().split()
            for elem in palabras:
                numpalabras += 1

    with open('conversación.txt', 'r') as f:
        texto = f.read()

        for char in simbolos:
            texto = texto.replace(char, '')

        palabras = texto.lower().split()

        dict_list = [cuenta_repetidas(p, palabras) for p in palabras]

        resultados = [i for n, i in enumerate(dict_list) if i not in dict_list[n + 1:]]

        res_ordenados = sorted(resultados, key=lambda d: list(d.values()), reverse=True)

        primer1 = res_ordenados[:1]

        for d in primer1:
            for k, v in d.items():
                print("Generado el informe en PDF")

        today = datetime.date.today()
        # En esta segunda fase de la función se encarga de generar el PDF insertando la imagen y el titulo. Seguidamente
        # inserta el texto como un parrafo ajustando su tamaño automaticamente y añadiendo los datos correspondientes
        # sobre la fecha, numero de palabras, etc.
        c = canvas.Canvas("conversación.pdf")
        c.drawImage("chatbot_python.jpg", 100, 600, width=400, height=200)
        c.drawString(200, 550, 'INFORME DE LA CONVERSACIÓN')
        textobject = c.beginText(100, 500)
        for line in caracteres.splitlines(False):
            textobject.textLine(line.rstrip())
        c.drawText(textobject)
        c.drawString(100, 250, f'La conversacion es del  {today}')
        c.drawString(100, 230, f"Consta de {len(caracteres)} caracteres")
        c.drawString(100, 210, f"Está compuesto por {numpalabras} palabras")
        c.drawString(100, 190, f"La palabra {k} aparece {v} veces.")
        c.save()
    return


# Programa Principal
salir = False
# Menu principal
print("\t\t\t\t\t\033[1m\033[4mAPLICACIÓN BOT-ARATE\033[0m \n")

print("1)  Bot simple (Respuestas planas...)")
print("2)  Bot simple (Respuestas REGEX)")
print("3)  Bot simple mejorado desde fichero")
print("4)  Informe de la conversación (PDF)")
print("5)  Salir")
# Elección de bot para hablar indefinidamente hasta salir.
while not salir:
    opcion = int(input("Opción: "))
    if opcion == 1:
        botsimple()
    elif opcion == 2:
        botregex()
    elif opcion == 3:
        botfichero()
    elif opcion == 4:
        informe()
    elif opcion == 5:
        salir = True
