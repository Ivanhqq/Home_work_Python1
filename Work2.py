
#2.  Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


x= input("Введите значение x: ")
y= input("Введите значение y: ")
z= input("Введите значение z: ")

if not (x or y or z) == (not(x) and not(y) and not(z)):
    print('утверждение верно')
else:
    print('утверждение ложно')
