"""
El módulo turtle, proporciona lasherramientas necesarias para dibujar gráficos mediante la utilización de 
una tortuga. En este caso se va a utilizar para dibujar una estrella.
"""
import turtle
#Función para dibujar la estrella
def dibujar_estrella():
    """
    Esta es la configuración de la tortuga. En este caso estoy definiendo la velocidad a la que quiero
    que dibuje, el color del dibujo, y el grosor que quiero que tenga el dibujo
    """
    turtle.speed(3)
    turtle.color("black")
    turtle.pensize(2)
    
    """
    Este bucle for, me permite dibujar la estrella. En cada iteración, la tortuga avanza 200 unidades 
    hacia alante y luego gira 160º a la derecha. de esta forma, y con el rango definido como 9, el bucle
    se repite 9 veces formando una estrella de 9 puntas como la pedida en el ejercicio.
    """
    for _ in range(9):
        turtle.forward(200)
        turtle.right(160)
    # Finaliza la ventana de Turtle cuando se completa el dibujo
    turtle.done()

# Llama a la función para dibujar la estrella
dibujar_estrella()
