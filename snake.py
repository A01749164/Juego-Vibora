"""Código modificado por:
Erick Hernández Silva y Jeovanni Bástida
"""
from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)# Donde aparece la comida
snake = [vector(10, 0)]# Lista de la longitud de la serpiente
aim = vector(0, -10)# Dirección inicial hacia donde se mueve la serpiente

def change(x, y):
    "Camia la dirección de la serpiente."
    aim.x = x # Modifica el valor de x del aim
    aim.y = y # Modifia el valor de y del aim

def inside(head):
    """Regresa True cuando la serpiente está
    dentro de los límites de la pantalla.
    """
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    # Copia la cabeza de la lista
    head = snake[-1].copy()
    # Movemos la cabeza hacia donde estemos apuntando
    head.move(aim)
    # Si la viborita ya no tiene cabezas termina el juego
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    # La viborita crece
    snake.append(head)

    # Si la viborita come
    if head == food:
        # Se imprime la longitud de la viborita
        print('Snake:', len(snake))
        # Se mueve de lugar la viborita a 1 casilla de distancia máximo
        food.x = randrange(-1,2) * 10
        food.y = randrange(-1, 2) * 10
    else: # Si no comió
        # Quita la ultima inserción de la viborita
        snake.pop(0)

    clear()

    #  Pinta cada cuadro de la serpiente
    for body in snake:
        square(body.x, body.y, 9, 'black')
    # Pinta la comida del color especificado
    square(food.x, food.y, 9, 'green')
    update()
    # Llama a la funcion move despues de 100ms
    ontimer(move, 100)

# Se genera el canvas
setup(420, 420, 370, 0)
# Esconde a la tortuga
hideturtle()
# Apaga la animación de la tortuga al dibujar
tracer(False)
# Escucha el teclado en busca de inputs
listen()
# Si presiona la <- cambia la dirección
onkey(lambda: change(10, 0), 'Right')
# Si presiona la -> cambia la dirección
onkey(lambda: change(-10, 0), 'Left')
# Si presiona la ^ cambia la dirección
onkey(lambda: change(0, 10), 'Up')
# Si presiona la v cambia la dirección
onkey(lambda: change(0, -10), 'Down')
move()# Mueve por primera vez a la función move
done()