# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21


from cmath import sqrt


print('Введите координаты точки А')
a1 = int(input("A1 = "))
a2 = int(input("A2 = "))

print('Введите координаты точки B')
b1 = int(input("B1 = "))
b2 = int(input("B2 = "))
print(
    f'Расттояние между точками = {round((((a1-b1)**2) + ((a2-b2)**2))** (0.5), 2)}')
