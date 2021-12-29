def Verificador(answer):
    """
    Esta funcion tiene el proposito de verificar segun cuatro criterios
    de lo que el usuario ingreso. 
    El primer criterio es que los datos a excepcion del string de 
    estado de animo (bien o mal), deben tener si o si el caracter ":", 
    el segundo criterio al igual que el primero esta enfocado en los 
    que tienen los ":" y verifica si la cantidad de ":" es igual al 
    doble de la cantidad de "-". El tercer criterio es si al eliminar
    los caracteres de ";" en caso de tenerlo, el ":" y el "-",
    si se encuentran solo números enteros positivos (ya que el tiempo
    jamas sera negativo) sera verdadero. El cuarto criterio es si al
    separar el string convirtiendolo a lista mediante split separandolo
    por medio de ";" quedan nombres de día de la semana. El ultimo 
    criterio es si el string de estado de animo (bien o mal) al ponerlo 
    en minusculas es igual a "bien" o "mal".
    Esta funcion tiene como entrada la lista de respuestas en esta
    funcion llamada "answer", siendo de tipo list.
    Teniendo como salida un booleano para el archivo sep_days.py.
    """
    # Se declaran variables, si no se ven modificadas durante el
    # codigo significa que no cumplen con los criterios ya descritos
    primero = False
    segundo = False
    tercero = False
    cuarto = False
    final = False
    # este ciclo tiene el proposito de recorrer la lista
    for j in range(len(answer)):
        # Verifica el 4to criterio
        if answer[j].lower() == "bien" or answer[j].lower() == "mal":
            final = True
        elif answer[j][0].lower() == "l" or answer[j][0].lower() == "m" or \
        answer[j][0].lower() == "j" or answer[j][0].lower() == "v" or \
        answer[j][0].lower() == "s" or answer[j][0].lower() == "d":
            cuarto = dias_independientes(answer,j,cuarto)
        else: 
            i = 0
            while i < len(answer[j]):
                # Verifica si tiene ";" en el string
                if answer[j].count(";") != 0:
                    k = 0
                    while k <= answer[j].count(";"):
                        # Pasa la lista, j, y las variables de los criterios
                        # a la funcion contador.
                        primero, segundo, tercero = contador(answer,j,primero,
                                                            segundo,tercero)
                        k += 1
                elif answer[j].count(";") == 0:
                    primero, segundo, tercero = contador(answer,j,primero,
                                                        segundo,tercero)
                i += 1
            
    # Realiza una operacion "and" para verificar que en su conjunto las
    # respuestas cumplen con los criterios       
    resultado = primero and segundo and tercero and cuarto and final
    # Se devuelve el resultado al archivo sep_day.py
    return resultado


def contador(answer,j,primdef Verificador(answer):
    """
    Esta funcion tiene el proposito de verificar segun cuatro criterios
    de lo que el usuario ingreso. 
    El primer criterio es que los datos a excepcion del string de 
    estado de animo (bien o mal), deben tener si o si el caracter ":", 
    el segundo criterio al igual que el primero esta enfocado en los 
    que tienen los ":" y verifica si la cantidad de ":" es igual al 
    doble de la cantidad de "-". El tercer criterio es si al eliminar
    los caracteres de ";" en caso de tenerlo, el ":" y el "-",
    si se encuentran solo números enteros positivos (ya que el tiempo
    jamas sera negativo) sera verdadero. El cuarto criterio es si al
    separar el string convirtiendolo a lista mediante split separandolo
    por medio de ";" quedan nombres de día de la semana. El ultimo 
    criterio es si el string de estado de animo (bien o mal) al ponerlo 
    en minusculas es igual a "bien" o "mal".
    Esta funcion tiene como entrada la lista de respuestas en esta
    funcion llamada "answer", siendo de tipo list.
    Teniendo como salida un booleano para el archivo sep_days.py.
    """
    # Se declaran variables, si no se ven modificadas durante el
    # codigo significa que no cumplen con los criterios ya descritos
    primero = False
    segundo = False
    tercero = False
    cuarto = False
    final = False
    # este ciclo tiene el proposito de recorrer la lista
    for j in range(len(answer)):
        # Verifica el 4to criterio
        if answer[j].lower() == "bien" or answer[j].lower() == "mal":
            final = True
        elif answer[j][0].lower() == "l" or answer[j][0].lower() == "m" or \
        answer[j][0].lower() == "j" or answer[j][0].lower() == "v" or \
        answer[j][0].lower() == "s" or answer[j][0].lower() == "d":
            cuarto = dias_independientes(answer,j,cuarto)
        else: 
            i = 0
            while i < len(answer[j]):
                # Verifica si tiene ";" en el string
                if answer[j].count(";") != 0:
                    k = 0
                    while k <= answer[j].count(";"):
                        # Pasa la lista, j, y las variables de los criterios
                        # a la funcion contador.
                        primero, segundo, tercero = contador(answer,j,primero,
                                                            segundo,tercero)
                        k += 1
                elif answer[j].count(";") == 0:
                    primero, segundo, tercero = contador(answer,j,primero,
                                                        segundo,tercero)
                i += 1
            
    # Realiza una operacion "and" para verificar que en su conjunto las
    # respuestas cumplen con los criterios       
    resultado = primero and segundo and tercero and cuarto and final
    # Se devuelve el resultado al archivo sep_day.py
    return resultado


def contador(answer,j,primero,segundo,tercero):
    """
    Esta es la función que se encarga de comprobar los datos que
    corresponde al tiempo según los criterios ya mencionados en la
    funcion de verificador.
    Esta funcion tiene como entrada la lista de respuestas "answer"
    siendo esta de tipo list, "j" siendo la variable de iteracion
    encargada de recorrer la lista siendo de tipo entero, "primero" 
    siendo la variable del primer criterio, "segundo" siendo la 
    variable del segundo criterio, "tercero" la variable del tercer 
    criterio, estos tres ultimos siendo de tipo booleano.
    Teniendo como salida "primero", "segundo", y "tercero", siendo
    estos tres de tipo booleano.
    """
    # Se declara la lista cifras para ser usada para el tercer criterio
    cifras = ["0","1","2","3","4","5","6","7","8","9"]
    contador = 0
    if answer[j].count(":") != 0:
        # Comprueba si cumple con el primer criterio, si no es asi
        # automaticamente rechaza los demas criterios
        primero = True
        if 2 * answer[j].count("-") == answer[j].count(":"):
            # Se verfica el segundo criterio
            segundo = True
            # Se usa una lista temporal para poder eliminar 
            # elementos ya que en los string no es posible
            temp = list(answer[j])
            while temp.count(":") != 0:
                temp.pop(temp.index(":"))
            while temp.count("-") != 0:
                temp.pop(temp.index("-"))
            while temp.count(";") != 0:
                temp.pop(temp.index(";"))
            # Verifica el tercer criterio
            for l in range(len(temp)):
                # Se inicia un acumulador asignadose un "False", 
                # representando un cero para poder usar la operacion 
                # "or", siendo muy similar a una suma. Recorriendo
                # la lista temp, temp siendo answer[j]
                acumulador = False
                # Se recorre la lista cifras para verificar si temp[l]
                # es igual a una cifra, si no lo es significa que no es
                # entero. Las veces que coincida con un elemento de la
                # lista cifras se sumará 1.
                for p in cifras:
                    acumulador = temp[l] == p or acumulador    
                    if acumulador:
                        contador += 1
                        # Si las veces que fue verdadero el acumulador
                        # coincide con el largo de la lista temp,
                        # significa que todos los elementos que
                        # quedaron en la lista, son enteros.
                        if contador == len(temp):
                            tercero = True
    return primero, segundo, tercero


def dias_independientes(answer,j,cuarto):
    """
    Esta función se encarga de verificar si se cumple la estructura
    de la pregunta en la que pide los días de estudio.
    Esta función tiene de entrada la lista de respuestas del usuario
    siendo este de tipo de list, tambien el iterador j siendo este de
    tipo int, y por ultimo el cuarto criterio "cuarto" siendo este de
    tipo booleano.
    Esta función tiene como salida el booleano cuarto.
    """
    # Se recorre los string de tiempo siendo estos elementos de
    # la lista
    if answer[j].count(";") != 0:
        temp_0 = answer[j].split(";")
    else:
        answer[j] = answer[j] + ";" + answer[j]
        temp_0 = answer[j].split(";")
    dias = ["lunes","martes","miercoles","jueves","viernes","sabado",
                    "domingo"]
    contador = 0
    for k in range(len(temp_0)):
        acumulador = False    
        for p in dias:
            acumulador = temp_0[k] == p or acumulador    
            if acumulador:
                contador += 1
                # Si las veces que fue verdadero el acumulador
                # coincide con el largo de la lista temp,
                # significa que todos los elementos que
                # quedaron en la lista, son enteros.
                if contador == len(temp_0):
                    cuarto = True
    return cuarto  
