# Ejercicio 1
def signNumber(x):
    if x > 0:
        print("El número es positivo")
    elif x == 0:
        print("El número es 0")
    else:
        print("El número es negativo")

x = float(input("Escribe un número: "))
signNumber(x)

#Ejercicio 2
def between(x):
    if x >= -5 and x <= 5:
        print("El número esta en el rango entre -5 y 5")
    else:
        print("No está entre -5 y 5")

y = float(input("Escribe un número: "))
between(y)


#Ejercicio 3
def cuadrante(arg):
    x, y = arg
    if x > 0 and y > 0:
        print("Las coordenadas están en el primer cuadrante")
    elif x < 0 and y > 0:
        print("Las coordenadas están en el segundo cuadrante")
    elif x < 0 and y < 0:
        print("Las coordenadas están en el tercer cuadrante")
    elif x > 0 and y < 0:
        print("Las coordenadas están en el cuarto cuadrante")
    

cuadrante((4,2))
cuadrante((5,-3))
cuadrante((-4,1))
cuadrante((-3,-3))


# Ejercicio 4
import math
def division(x,y):
    return x//y, math.fmod(x,y)

#(cociente, resto)
division(10,7)


# Ejercicio 5
def sqrt_perfect(x):
    r = math.modf(math.sqrt(x))
    return r[0] == 0

sqrt_perfect(4)
sqrt_perfect(9)
sqrt_perfect(12)
sqrt_perfect(16)


# Ejercicio 6
def bisiesto(x):
    return (x % 4 == 0 and x % 100 != 0) or x % 400 == 0
    
bisiesto(1928)
bisiesto(1700)
bisiesto(2100)
bisiesto(2020)
    

# Ejercicio 7
def chess_cell(let,num):
    if (let in ["a","c","e","g"] and num%2 != 0) or (let in ["b","d","f","h"] and num%2 == 0):
        print("La casilla es negra")
    else:
        print("La casilla es blanca")

chess_cell("a",5)
chess_cell("b",3)
chess_cell("d",8)
chess_cell("h",1)
