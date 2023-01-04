import preguntas as p

def print_pregunta(enunciado, alternativas):
    
    alternativas_elegir = ['A', 'B', 'C', 'D']
    
    print(f'{enunciado[0]}\n') #Primero se imprime el ancabezado por separado
    
    #utilizaré un zip para unir las dos listas, la de las letras de cada alternativa junto con la lista de las alternativas en si
    for alternativas_diponibles in zip(alternativas_elegir, alternativas):
        print(f'{alternativas_diponibles[0]}. {alternativas_diponibles[1][0]}') #Acá el 1 y el 0 representan la posición de los elementos en el zip, donde 0 es la letra de la lista alternativas_elegir y el 1 es la alternativa en si
    
    
    
    ###############################################################
        
if __name__ == '__main__':
    # Las preguntas y alternativas deben mostrarse según lo indicado
    pregunta = p.pool_preguntas['basicas']['pregunta_1']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    
    # Enunciado básico 1

    # A. alt_1
    # B. alt_2
    # C. alt_3
    # D. alt_4