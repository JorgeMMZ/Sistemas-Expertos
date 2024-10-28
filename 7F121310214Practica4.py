import random

# Listas de elementos del juego
personajes = ["Sr blanco", "Sra azul", "Prof ciruela", "Srta amapola", "Coronel mostaza"]
habitaciones = ["Sala", "Cocina", "Comedor", "Biblioteca", "Estudio"]
armas = ["Cuchillo", "Pistola", "Cuerda", "Llave inglesa", "Candelabro"]

# Función para crear combinaciones únicas de persona, habitación y arma
def crear_grupos(personajes, habitaciones, armas):
    elementos = list(zip(personajes, habitaciones, armas))
    random.shuffle(elementos)
    return elementos[:5]  # Retornamos cinco grupos aleatorios

# Crear grupos para la partida
grupos = crear_grupos(personajes, habitaciones, armas)

# Escena del crimen (aleatoria y diferente a los grupos generados)
while True:
    escena_crimen = (
        random.choice(personajes),
        random.choice(habitaciones),
        random.choice(armas)
    )
    # Verificar que la escena del crimen no esté en los grupos
    if escena_crimen not in grupos:
        break

# Función para responder a la consulta del usuario
def responder_consulta(elemento):
    encontrado = False
    for personaje, habitacion, arma in grupos:
        if personaje == elemento or habitacion == elemento or arma == elemento:
            encontrado = True
            #print(f"\nInformación del grupo:")
            a = 1
            b = 1
            c = 1
            if personaje == elemento:
                a = 0
                print(f"{personaje} está en {habitacion} y tiene el {arma}.")
            if habitacion == elemento:
                b = 0
                print(f"En la habitación {habitacion} está {personaje} y tiene el {arma}.")
            if arma == elemento:
                c = 0
                print(f"El {arma} lo tiene {personaje} y está en {habitacion}.")
            d = 0
            for objeto in escena_crimen:
                if elemento == objeto:
                    d = 1
            # Verificar la veracidad de cada parte del grupo comparada con la escena del crimen
            es_persona_correcta = personaje == escena_crimen[0]
            es_habitacion_correcta = habitacion == escena_crimen[1]
            es_arma_correcta = arma == escena_crimen[2]
            # Mensajes de veracidad para cada componente del grupo
            if d: 
                if a: print(f"- {personaje} es {'verdadero' if es_persona_correcta else 'falso'}.")
                if b: print(f"- La ubicación ({habitacion}) es {'verdadera' if es_habitacion_correcta else 'falsa'}.")
                if c: print(f"- El arma ({arma}) es {'verdadera' if es_arma_correcta else 'falsa'}.")
            else:
                if a: print(f"- {personaje} es {'falso' if es_persona_correcta else 'veridico'}.")
                if b: print(f"- La ubicación ({habitacion}) es {'falso' if es_habitacion_correcta else 'veridico'}.")
                if c: print(f"- El arma ({arma}) es {'falso' if es_arma_correcta else 'veridica'}.")
            return True
    
    # Si no se encuentra el elemento en ninguno de los grupos
    if not encontrado:
        print("Elemento desconocido, intenta nuevamente.")
        return False

# Simulación del juego
print("\n--- Bienvenido al juego de Clue ---")
print("Puedes preguntar sobre un personaje, una habitación o un arma para saber dónde están y si la información es verídica.")
print("Tienes un máximo de 5 inspecciones para descubrir pistas.")

# Contador de inspecciones permitidas
inspecciones_restantes = 5

# Bucle para consultas del usuario
while inspecciones_restantes > 0:
    consulta = input("\n¿Qué elemento deseas consultar? (escribe 'salir' para terminar): ").strip().capitalize()
    
    if consulta.lower() == "salir":
        print("Gracias por jugar. ¡Hasta la próxima!")
        break
    
    # Realizar la consulta y disminuir el contador sólo si es válida
    if responder_consulta(consulta):
        inspecciones_restantes -= 1
        print(f"Inspecciones restantes: {inspecciones_restantes}")
    
    if inspecciones_restantes == 0:
        print("\nSe han agotado tus inspecciones. ¡Es hora de adivinar la escena del crimen!")
        
        # Solicitar al usuario que adivine la escena del crimen
        sospechoso = input("¿Quién crees que es el culpable?: ").strip().capitalize()
        lugar = input("¿En qué habitación ocurrió el crimen?: ").strip().capitalize()
        arma = input("¿Con qué arma se cometió el crimen?: ").strip().capitalize()
        
        # Comprobar si el usuario adivinó correctamente
        if (sospechoso, lugar, arma) == escena_crimen:
            print("\n¡Felicidades! Has acertado en todos los elementos de la escena del crimen.")
        else:
            print("\nBuen intento, pero no acertaste en todos los elementos.")
            print(f"La escena correcta era: {escena_crimen[0]}, en {escena_crimen[1]} con {escena_crimen[2]}.")
        break
