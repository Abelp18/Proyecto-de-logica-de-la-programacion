import random

opciones = ["piedra", "papel", "tijera"]
print("¡¡BIENVENIDO AL JUEGO DE PIEDRA PAPEL Y TIJERA!!😎")
while True:
    jugador = input("Elige piedra, papel o tijera: ").lower()
    computadora = random.choice(opciones)

    print("La computadora eligió:", computadora)

    if jugador != opciones:
        print("ESCOJA UNA OPCIÓN VALIDA: piedra, papel o tijera:")
    if jugador == computadora:
        print("¡¡EMPATARON!!")
    elif (jugador == "piedra" and computadora == "tijera") or \
         (jugador == "papel" and computadora == "piedra") or \
         (jugador == "tijera" and computadora == "papel"):
        print("¡Ganaste!🥳🥳")
    else:
        print("😔  Perdiste  😔")

    respuesta = input("¿Quieres volver a jugar? (si/no): ").lower()

    if respuesta == "no":
        print("¡Gracias por jugar GG!🤗")
        break

