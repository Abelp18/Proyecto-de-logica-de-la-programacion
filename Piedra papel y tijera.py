import random
def game_rule(user:str, computer:str) -> str: 
    rule = {
        "piedra": "tijera",
        "papel":  "piedra",
        "tijera": "papel",
    }
    if user == computer:
        return "empate"
    if rule[user] == computer:
        print("¡Ganaste!🥳🥳")
        return "jugador"
    print("😔  Perdiste  😔")
    return "computadora"





wins = 0
options = ["piedra", "papel", "tijera"]
print("¡¡BIENVENIDO AL JUEGO DE PIEDRA PAPEL Y TIJERA!!😎")
while True:
    while True:
        user = input("Elige piedra, papel o tijera: ").lower()  
        if user not in ["piedra", "papel", "tijera"]:
            print("Opcion invalida, elija nuevamente:")
        else:
            break
    computer = random.choice(options)
    print("La computadora eligió:", computer)
    result = game_rule(user, computer)
    if result == "empate":
        print("¡Empate! Vuelve a elegir.")
        continue  
    if result == "jugador":
        wins += 1
        print(f"LLevas {wins} Victorias consecutivas")
    else:
        if wins != 0:
            print(f"¡Perdiste la racha de {wins} victorias") 
        wins = 0
    while True:
        user = input("¿Quieres volver a jugar? (si/no): ").lower()
        if user not in ["si", "no"]:
            print("Opcion invalida, elija nuevamente:")
        else:
            break
    if user == "no":
        print("¡¡Gracias por jugar!!")
        break