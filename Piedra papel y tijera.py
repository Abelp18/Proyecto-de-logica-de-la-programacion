import random 
# Funcion que evalúa las reglas del juego para determinar el ganador de la ronda.
def game_rule(user: str, computer: str) -> str: 
    
    # Diccionario de reglas que define al ganador (Clave vence a Valor)
    rule = {
        "piedra": "tijera",
        "papel":  "piedra",
        "tijera": "papel",
    }
    
    # Caso 1: Ambos eligen lo mismo
    if user == computer:
        return "empate"
    
    # Caso 2: La elección de la computadora es vencida por la del usuario
    if rule[user] == computer:
        print("¡Ganaste!🥳🥳")
        return "jugador"
    
    # Caso 3: Si no es empate ni gana el jugador, gana la computadora
    print("😔  Perdiste  😔")
    return "computadora"


# --- Flujo Principal del Juego ---

wins = 0  # Contador de victorias consecutivas (racha)
options = ["piedra", "papel", "tijera"] # Opciones para la computadora

print("¡¡BIENVENIDO AL JUEGO DE PIEDRA PAPEL Y TIJERA!!😎")

# Bucle principal para mantener el juego activo de forma indefinida
while True:
    
    # Bucle de validación para la entrada del jugador
    while True:
        user = input("Elige piedra, papel o tijera: ").lower().strip() # Ingreso de valor del usuario
        if user not in ["piedra", "papel", "tijera"]: # Validación de entrada de datos
            print("Opcion invalida, elija nuevamente:")
        else:
            break  # Entrada válida, salimos del bucle de validación
            
    # Elección aleatoria de la computadora
    computer = random.choice(options)
    print("La computadora eligió:", computer)
    
    # Evaluar el resultado de la ronda
    result = game_rule(user, computer)
    
    # Gestión del sistema de puntos y rachas dependiendo del resultado
    if result == "empate":
        print("¡Empate! Vuelve a elegir.")
        continue  # Reinicia el bucle principal saltándose las preguntas de abajo
        
    if result == "jugador": # Validación si gana el jugador
        wins += 1 # Suma las victorias 
        print(f"LLevas {wins} Victorias consecutivas")
    else:
        # Si el jugador pierde y tenía racha, se le notifica
        if wins != 0:
            print(f"¡Perdiste la racha de {wins} victorias") 
        wins = 0  # Reseteo de la racha
        
    # Bucle de validación para la continuidad del usuario
    while True:
        user = input("¿Quieres volver a jugar? (si/no): ").lower().strip() # Entrada de datos por el usuario
        if user not in ["si", "no"]: # Validación de entrada de datos
            print("Opcion invalida, elija nuevamente:")
        else:
            break  # Entrada válida, salimos del bucle de validación
            
    # Condición de salida definitiva del juego
    if user == "no":
        print("¡¡Gracias por jugar!!")
        break # Rompe el bucle principal del juego