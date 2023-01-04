def choose_level(n_pregunta, p_level):
    
    # Construir lógica para escoger el nivel
    if p_level == 3:
        if n_pregunta < 4:
            level = 'basicas'
        elif n_pregunta > 6:
           level = 'avanzadas'
        else:
            level = 'intermedias'
    elif p_level == 2:
        if n_pregunta < 3:
            level = 'basicas'
        elif n_pregunta > 4:
            level = 'avanzadas'
        else:
            level = 'intermedias'
    elif p_level == 1:
        if n_pregunta == 1:
            level = 'basicas'
        elif n_pregunta == 3:
            level = 'avanzadas'
        else:
            level = 'intermedias'
    else:
        print("Nivel escogido no existe, prueba con 1,2 o 3")
    
    return level

if __name__ == '__main__':
    # verificar resultados
    print(choose_level(2, 2)) # básicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(7, 2)) # avanzadas
    print(choose_level(4, 3)) # intermedias