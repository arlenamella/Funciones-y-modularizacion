import preguntas as p


def verificar(alternativas, eleccion):
    #devuelve el índice de elección dada
    eleccion = ['a', 'b', 'c','d'].index(eleccion) #index es la función que va a asignar un numero de indice a cada posición de la lista
    correcto = 1 #se coloca 1 porque es el número que se designó para marcar la alternativa correcta, el cero será incorrecto
    # generar lógica para determinar respuestas correctas
    ##########################################################################################
    if (alternativas[eleccion][1] == 1):
        correcto = 1
        print("Respuesta correcta")
    else:
        correcto = 0
        print("Respuesta incorrecta")
        
    ##########################################################################################
    return correcto



if __name__ == '__main__':
    from print_preguntas import print_pregunta
    
    # Siempre que se escoja la alternativa con alt_2 estará correcta, e incorrecta en cualquier otro caso
    pregunta = p.pool_preguntas['basicas']['pregunta_2']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    respuesta = input('Escoja la alternativa correcta:\n> ').lower()
    verificar(pregunta['alternativas'], respuesta)






