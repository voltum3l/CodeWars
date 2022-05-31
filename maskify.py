#Credit Card MASK

def maskify(mensaje):
    #resultado=mensaje
    resultado=""
    if len(mensaje) > 4:
        for i in range(len(mensaje)):
            if i < (len(mensaje)-4):
                resultado=resultado+"#"
            else:
                resultado=resultado + mensaje[i]
    else:
        if len(mensaje) == 0:
            resultado=""
        else:
            resultado=mensaje
