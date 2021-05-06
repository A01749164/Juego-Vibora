# Código modificado por:
# Autor: Erick Hernández Silva 
# Autor: Jeovani Hernández Bástida

# Se importan las liberias a usar 
from turtle import *
from random import randrange, randint, choice
from freegames import square, vector

# Se crean los vectores de comida, longitud, direccion y colores
food = vector(0, 0)     
snake = [vector(10, 0)]     
aim = vector(0, -10)    
colores = ['orange', 'blue', 'black', 'purple', 'green', 'pink']

# Se crean las variables
colorFood = ""
colorSnake = ""
# Se hace un ciclo para evitar colores repetidos
colorFood = choice(colores)   
colores.remove(colorFood)
colorSnake = choice(colores)   



def change(x, y):
    """Cambia la dirección de la serpiente."""
    aim.x = x # Modifica el valor de x del aim
    aim.y = y # Modifia el valor de y del aim


def inside(head):
    """
    Regresa True cuando la serpiente está
    dentro de los límites de la pantalla.
    """
    return -200 < head.x < 190 and -200 < head.y < 190


def moveFood():
    """
    Mueve la comida a un punto aleatorio en un rando de -2 a 2
    cada segundo.
    """
    global food
    #Si la comida está dentro de la pantalla
    if(inside(food)):
        # Modifica hacia donde se movera la comida
        aimFood = vector(randint(-2,2) * 10,randint(-2,2) * 10)
        food.move(aimFood)  # Mueve la comida
    else:
        #Si no, la regresa al punto (0,0)
        food = vector(0,0)
    ontimer(moveFood, 1000) # Se repite cada 1000ms


def move():
    """Mueve la serpiente hacia adelante un segmento."""
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
        square(body.x, body.y, 9, colorSnake)

    # Pinta la comida del color especificado
    square(food.x, food.y, 9, colorFood)
    update()
    
    # Llama a la funcion move despues de 100ms
    ontimer(move, 100)

setup(420, 420, 370, 0)     # Se genera el canvas
hideturtle()    # Esconde a la tortuga
tracer(False)   # Apaga la animación de la tortuga al dibujar
listen()    # Escucha el teclado en busca de inputs

# Se definen las teclas a presionar para el movimiento de la serpiente 
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')

move()  # Mueve por primera vez la serpiente
moveFood()  # Mueve por primera vez la comida
done() 