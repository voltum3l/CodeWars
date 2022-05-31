#Rot 13
#Crear un algoritmo para codificar una cadena en rot13.

import string

def rot13(mensaje):
    alfabetoLower= string.ascii_lowercase
    alfabetoHigher= string.ascii_uppercase
    nuevoMensaje=""

    for i in range(len(mensaje)):
        if mensaje[i] in alfabetoLower:
            nuevoMensaje = nuevoMensaje + alfabetoLower[returnPosition(alfabetoLower.index(mensaje[i]))]
        elif mensaje[i] in alfabetoHigher:
            nuevoMensaje = nuevoMensaje + alfabetoHigher[returnPosition(alfabetoHigher.index(mensaje[i]))]
        else:
            nuevoMensaje=nuevoMensaje + mensaje[i]

    return nuevoMensaje

def returnPosition(posicion):
    if posicion < 13:
        posicion = posicion + 13
    else:
        posicion = posicion - 13
    return posicion
