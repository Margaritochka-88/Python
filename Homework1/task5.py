import math
# 5- Напишите программу, которая принимает на вход координаты двух
# точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5.09
# - A (7,-5); B (1,-1) -> 7.21

ax = float(input('Введите координату точки a по оси x: \n'))
ay = float(input('Введите координату точки a по оси y: \n'))
bx = float(input('Введите координату точки b по оси x: \n'))
by = float(input('Введите координату точки b по оси y: \n'))

distans = math.sqrt((ax-bx)**2+(ay-by)**2)
print(f'Растояние между координатами = {round(distans, 2)}')