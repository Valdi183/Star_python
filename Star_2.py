# El módulo, está explicado en el otro archivo
import turtle
# En este caso, la función depende de unos parámetros para que el usuario elija como quiere dibujar las estrellas
def dibujar_estrella(puntas, color, tamaño, separacion):
    turtle.penup() # Sirve para que la tortuga se desplaze de sitio sin dibujar
    turtle.goto(separacion, 0) # Mueve la tortuga a unas coordenadas específicas para no sobreescribir si se hacen varios dibujos 
    turtle.pendown() # Sirve para que la toortuga vuelva a dibujar (En este caso cuando este en las coordenadas coorrespondientes)

    turtle.color(color)
    turtle.pensize(2)

    # Convierte el tamaño a un número antes de pasarlo a turtle.forward()
    tamaño_numero = int(tamaño)

    # Dibuja la estrella con el numero de puntas que quiera el usuario, girando en función del numero de puntas para escribir la estrella completa
    for _ in range(puntas):
        turtle.forward(tamaño_numero)
        turtle.right(360 / puntas * 2)
# Esta función es la encargada de manejar los parámetros que ponga el usuario
def main():
    # Pregunta al usuario cuántas estrellas quiere dibujar
    num_estrellas = int(input("¿Cuántas estrellas quieres dibujar? "))
    
    # Pregunta al usuario la separación entre estrellas
    separacion = int(input("¿Cuál es la separación entre estrellas?(Introduzca un numero mayor al tamaño que le darás posteriormente a la esrella): "))

    """
    Este bucle for se encarga de iterar num_estrellas veces. En cada iteración, el código solicita al usuario información sobre una estrella específica, 
    utilizando i para indicar el número de estrella actual. Este bucle permite basicamente al usuario proporcionar información sobre cada estrella que 
    se dibujará, con el número de la estrella mostrado en los mensajes. Cada iteración recopila los datos sobre una estrella específica, permitiendo 
    la creación  de múltiples estrellas con características personalizadas por el usuario.
    """
    for i in range(num_estrellas):
        color_usuario = input(f"Ingresa el color de la estrella {i + 1} (en inglés. Ej: black, blue...): ")
        puntas_usuario = int(input(f"Ingresa el número de puntas de la estrella {i + 1} (mínimo 5 y número impar): "))
        tamaño_usuario = input(f"Ingresa el tamaño de la estrella {i + 1} (recomendable 100-300): ")

        # Llama a la función para dibujar la estrella con los datos proporcionados por el usuario
        dibujar_estrella(puntas_usuario, color_usuario, tamaño_usuario, i * separacion)

    # La ventana de turtle se mantendrá abierta, para que se escriban las estrellas en la misma ventana
    turtle.done()

# Llama a la función principal (la que maneja los parámetros introducidos por el usuario)
main()