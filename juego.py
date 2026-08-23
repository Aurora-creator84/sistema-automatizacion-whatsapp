import random

numero_secreto = random.randint(1, 10)

print("¡Bienvenido al juego de adivinanzas, Aurora!")
print("Estoy pensando en un número entre el 1 y el 10. ¡Tienes 3 intentos!")

# Este bucle se va a repetir 3 veces
for intento_actual in range(1, 4):
    print("\n--- Intentos realizados: " + str(intento_actual - 1) + " de 3 ---")
    intento = int(input("Introduce tu número: "))
    
    if intento == numero_secreto:
        print("¡Felicidades, Aurora! ¡Adivinaste el número secreto!")
        break # Esto detiene el juego de inmediato porque ya ganaste
    elif intento < numero_secreto:
        print("¡Muy bajo! El número secreto es mayor.")
    else:
        print("¡Muy alto! El número secreto es menor.")

# Si agotas los 3 intentos sin adivinar, se ejecuta esto:
else:
    print("\n¡Te quedaste sin intentos! El número secreto era el " + str(numero_secreto))
