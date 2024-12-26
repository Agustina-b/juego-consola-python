import random
from Clases.enemigo import Enemigo
from Clases.jugador import Jugador


def main():
    nombre_jugador = input(
        "¡Bienvenido a la aventura en el espacio! Por favor, ingresa tu nombre: "
    )
    jugador = Jugador(nombre_jugador)

    enemigos = [
        Enemigo("Alien", 50, 10),
        Enemigo("Robot", 30, 5),
        Enemigo("Monstruo", 70, 15),
    ]

    enemigos_derrotados = []

    print("¡Comienza la aventura!")

    while enemigos:
        enemigo_actual = random.choice(enemigos)
        if enemigo_actual in enemigos_derrotados:
            continue

        print(f"te encuentras con un {enemigo_actual.nombre} en tu camino")

        while enemigo_actual.salud > 0:
            accion = input("¿Qué deseas hacer? (atacar/huir): ").lower()

            if accion == "atacar":
                dano_jugador = jugador.atacar()
                print(
                    f"Has atacado al enemigo {enemigo_actual.nombre} y le has causado {dano_jugador} puntos de daño"
                )
                enemigo_actual.recibir_dano(dano_jugador)

                if enemigo_actual.salud > 0:
                    dano_enemigo = enemigo_actual.atacar()
                    print(
                        f"El {enemigo_actual.nombre} te atacó y causó {dano_enemigo} puntos de daño"
                    )
                    jugador.recibir_dano(dano_enemigo)

            elif accion == "huir":
                print("Has decidido huir del combate ¡Cobarde!")
                break

        if jugador.salud <= 0:
            print("¡Has perdido la partida!")
            break

        if enemigo_actual.salud <= 0:
            enemigos_derrotados.append(enemigo_actual)
            enemigos.remove(enemigo_actual)

        jugador.ganar_experiencia(20)

        continuar = input("¿Quieres seguir explorando? (si/no): ").lower()

        if continuar != "si":
            print("¡Gracias por haber jugado Batallas Galácticas!")

    if not enemigos:
        print("¡Felicidades has derrotado a todos los enemigos!")

if __name__ == "__main__": #nos asegura que sólo podremos ejecutar este script desde el programa principal
    main()