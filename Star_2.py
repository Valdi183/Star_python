# El módulo, está explicado en el otro archivo
import turtle
# En este caso, la función depende de unos parámetros para que el usuario elija como quiere dibujar las estrellas
def dibujar_estrella(puntas, color, tamaño, separacion):
    turtle.penup() # Sirve para que la tortuga se desplaze de sitio sin dibujar
    turtle.goto(separacion, 0)
    turtle.pendown()

    turtle.color(color)
    turtle.pensize(2)

    # Convertir tamaño a un número antes de pasarlo a turtle.forward()
    tamaño_numero = int(tamaño)

    for _ in range(puntas):
        turtle.forward(tamaño_numero)
        turtle.right(360 / puntas * 2)

def main():
    # Preguntar al usuario cuántas estrellas quiere dibujar
    num_estrellas = int(input("¿Cuántas estrellas quieres dibujar? "))
    
    # Preguntar al usuario la separación entre estrellas
    separacion = int(input("¿Cuál es la separación entre estrellas?(Introduzca un numero mayor al tamaño que le darás posteriormente a la esrella): "))

    # Dibujar cada estrella con los detalles proporcionados por el usuario
    for i in range(num_estrellas):
        color_usuario = input(f"Ingresa el color de la estrella {i + 1} (en inglés. Ej: black, blue...): ")
        puntas_usuario = int(input(f"Ingresa el número de puntas de la estrella {i + 1} (mínimo 5 y número impar): "))
        tamaño_usuario = input(f"Ingresa el tamaño de la estrella {i + 1} (recomendable 100-300): ")

        # Llamar a la función para dibujar la estrella con los datos proporcionados por el usuario
        dibujar_estrella(puntas_usuario, color_usuario, tamaño_usuario, i * separacion)

    # Mantener la ventana de Turtle abierta hasta que se cierre manualmente
    turtle.done()

# Llamar a la función principal
main()