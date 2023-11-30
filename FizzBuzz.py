def fizz_buzz_game():
    INSTRUCCIONES = """¡Perfecto!, aquí van las instrucciones:
    Se mostrarán números del 1 al 30 en la pantalla. Si el número es divisible por 3, escriba "fizz";
    si es divisible por 5, escriba "buzz"; y si es divisible por ambos, escriba "fizzbuzz".
    Si no corresponde a ninguno de las anteriores, sólo repita el número.
    Si desea dejar de jugar, escriba "Salir."""

    print("¡Bienvenido!, ¿Estás preparado para jugar FIZZ BUZZ?")
    respuesta = input(": ").lower()

    while respuesta != "salir":
        if respuesta == "si":
            print(INSTRUCCIONES)

            for number in range(1, 31):
                print(number)
                respuesta_usuario = input("Respuesta: ").lower()
                
                if number % 3 == 0 and number % 5 == 0 and respuesta_usuario == "fizzbuzz":
                    print("¡Felicitaciones! Sigamos con el siguiente número")
                elif number % 3 == 0 and respuesta_usuario == "fizz":
                    print("¡Felicitaciones! Sigamos con el siguiente número")
                elif number % 5 == 0 and respuesta_usuario == "buzz":
                    print("¡Felicitaciones! Sigamos con el siguiente número")
                elif int(respuesta_usuario) == number and respuesta_usuario not in ["fizz", "buzz", "fizzbuzz"]:
                    print("¡Felicitaciones! Sigamos con el siguiente número")
                else:
                    print(f"Te has equivocado. La respuesta correcta era: {respuesta_correcta(number)}")

        elif respuesta == "no":
            print("No hay problema. Intenténtalo nuevamente cuando estés preparado. ¡Hasta pronto!")
        else:
            print("Respuesta no válida")

        print("...")
        print("¡Hola nuevamente!, ¿Estás preparado para jugar FIZZ BUZZ?")
        respuesta = input(": ").lower()

    print("Fin del juego")

def respuesta_correcta(number):
    if number % 3 == 0 and number % 5 == 0:
        return "fizzbuzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return str(number)

if __name__ == "__main__":
    fizz_buzz_game()
